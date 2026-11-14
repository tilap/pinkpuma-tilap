#!/usr/bin/env node
// Repository checks for the rules in AGENTS.md that `claude plugin validate` does not cover.
// No dependency. Run from anywhere: `node scripts/check.mjs`. Exits 1 on any failure.

import { existsSync, readdirSync, readFileSync, statSync } from "node:fs";
import { dirname, join, relative, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const failures = [];
const fail = (check, message) => failures.push(`[${check}] ${message}`);
const readJson = (path) => JSON.parse(readFileSync(path, "utf8"));
const rel = (path) => relative(root, path);

const pluginNames = readdirSync(join(root, "plugins")).filter((name) =>
  statSync(join(root, "plugins", name)).isDirectory(),
);

function walk(dir) {
  return readdirSync(dir, { withFileTypes: true }).flatMap((entry) => {
    const path = join(dir, entry.name);
    if (entry.name === ".git" || entry.name === "node_modules") return [];
    return entry.isDirectory() ? walk(path) : [path];
  });
}

// Rule 1: both manifests agree on the shared fields.
for (const name of pluginNames) {
  const dir = join(root, "plugins", name);
  const claude = readJson(join(dir, ".claude-plugin", "plugin.json"));
  const cursor = readJson(join(dir, ".cursor-plugin", "plugin.json"));
  for (const field of ["name", "version", "description", "author"]) {
    if (JSON.stringify(claude[field]) !== JSON.stringify(cursor[field])) {
      fail("manifests", `${name}: "${field}" differs between .claude-plugin and .cursor-plugin`);
    }
  }
  if (claude.name !== name) fail("manifests", `${name}: manifest name is "${claude.name}"`);
}

// Rule 3: every plugin on disk is registered, and the root README lists it.
const marketplace = readJson(join(root, ".claude-plugin", "marketplace.json"));
const readme = readFileSync(join(root, "README.md"), "utf8");
for (const name of pluginNames) {
  const entry = marketplace.plugins.find((plugin) => plugin.name === name);
  if (!entry) fail("registration", `${name}: not listed in .claude-plugin/marketplace.json`);
  else if (resolve(root, entry.source) !== join(root, "plugins", name)) {
    fail("registration", `${name}: marketplace source "${entry.source}" is not plugins/${name}`);
  }
  if (!readme.includes(`(plugins/${name})`)) {
    fail("registration", `${name}: no row in the README Plugins table`);
  }
}
for (const entry of marketplace.plugins) {
  if (!existsSync(resolve(root, entry.source))) {
    fail("registration", `${entry.name}: marketplace source "${entry.source}" does not exist`);
  }
}

// The manifest version has a heading in the plugin's CHANGELOG.
for (const name of pluginNames) {
  const dir = join(root, "plugins", name);
  const { version } = readJson(join(dir, ".claude-plugin", "plugin.json"));
  const changelog = readFileSync(join(dir, "CHANGELOG.md"), "utf8");
  if (!new RegExp(`^## \\[${version.replaceAll(".", "\\.")}\\]`, "m").test(changelog)) {
    fail("changelog", `${name}: CHANGELOG.md has no "## [${version}]" heading`);
  }
}

// Relative links and ${CLAUDE_PLUGIN_ROOT} paths in Markdown point at files that exist.
const markdownFiles = walk(root).filter((path) => path.endsWith(".md"));
for (const file of markdownFiles) {
  const text = readFileSync(file, "utf8");
  const plugin = rel(file).startsWith("plugins/") ? rel(file).split("/")[1] : null;
  const targets = [];
  for (const match of text.matchAll(/\]\(([^)\s]+)\)/g)) {
    const target = match[1];
    if (/^(https?:|mailto:|#)/.test(target)) continue;
    if (target.startsWith("${CLAUDE_PLUGIN_ROOT}")) {
      if (plugin) targets.push(join(root, "plugins", plugin, target.slice("${CLAUDE_PLUGIN_ROOT}".length)));
      continue;
    }
    targets.push(resolve(dirname(file), target));
  }
  for (const target of targets) {
    const path = target.split("#")[0];
    if (path && !existsSync(path)) fail("links", `${rel(file)}: broken link to ${rel(path)}`);
  }
}

// DEFAULT_USAGE.md is one bullet that names its own skill.
for (const file of walk(join(root, "plugins")).filter((path) => path.endsWith("DEFAULT_USAGE.md"))) {
  const skill = file.split("/").at(-2);
  const lines = readFileSync(file, "utf8").split("\n").filter((line) => line.trim());
  if (lines.length !== 1 || !lines[0].startsWith("- ")) {
    fail("default-usage", `${rel(file)}: must be exactly one bullet`);
  } else if (!lines[0].includes(`If the \`${skill}\` skill is available,`)) {
    fail("default-usage", `${rel(file)}: must contain "If the \`${skill}\` skill is available,"`);
  }
}

if (failures.length) {
  console.error(failures.join("\n"));
  console.error(`\n${failures.length} check(s) failed.`);
  process.exit(1);
}
console.log(`All checks passed (${pluginNames.length} plugins, ${markdownFiles.length} Markdown files).`);
