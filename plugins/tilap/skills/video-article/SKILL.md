---
name: video-article
description: >-
  Write a blog article from one of the owner's collected videos through this plugin's
  notes MCP, and save it as a draft linked to the video. Use only when the user invokes
  /tilap:video-article.
disable-model-invocation: true
metadata:
  plugin: tilap
---

# Video article

Help the owner turn one collected video into a draft blog article, then stop. The
article is the owner's, written with you from what the video says. It is saved by the
`notes` MCP server this plugin ships. Do not create a file.

## Tools

The server is the OrangeMonkey site (`/api/mcp`). For this skill use only:

- `list_imports`
- `get_import`
- `get_writing_guides`
- `list_posts`
- `create_post`
- `update_post`

If `list_imports` is absent, say the notes server is not connected and stop. If
`create_post` is absent, the token is read-only: you can read and draft in the chat, but
nothing can be saved. Do not fall back to a local file.

## Pick the video

`list_imports` returns the videos, newest first, without their texts. A video with status
`done` has its clean transcript; one with `transcribed` has not been cleaned yet (the
owner cleans it from the back-office). Use the video the user names or points to. If they
named none, show the recent `done` videos with their `shortTitle` and ask which one. Do not
guess.

`get_import` returns `transcript` (raw), `cleanTranscript` (same words, in paragraphs)
and `translation` (French, only when the video is not in French). Work from
`cleanTranscript`. Use `translation` as the source text when the article is in French and
the video is not.

## Write

1. Call `get_writing_guides` before writing and apply what it returns, including its
   `howToApply` checks. Do not mention the guides in the text.
2. Ask the owner for the angle if they gave none: the point they want to make, for whom.
   One question at most.
3. Write from the video only. Add no fact, figure, name or claim that the video does not
   contain, since nothing here can check sources. Rewording and reordering are fine.
   Leave out promotional asides (subscribe, follow, comment, courses, products).
4. Show the draft in the chat and rework it with the owner until they approve it.
5. Check the approved text against the guides once more, silently, and fix what fails.

## Save

Call `create_post` with `title`, `summary`, `content` (Markdown), `lang` (`fr` or `en`,
the language of the text) and `importId` set to the video's `id`. The server records the
video as the post's origin. Leave `status` out: the post is a draft. Publish only when the
owner says so, with `update_post` and `status: "published"`.

If this chat already saved the post, call `update_post` with its `id` instead of creating a
second one. An unknown `importId` or a taken slug comes back as an error: say it, fix the
cause (the slug, with `slug`), and retry once.

## After the call

Reply with the post `id`, its title, its slug, its status, and that it is linked to the
video. Do not paste the tool payload. A draft has no public URL.
