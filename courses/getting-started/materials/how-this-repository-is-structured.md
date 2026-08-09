Everything your library serves lives in this repository, one file per thing:

- `settings.json` — the library name and site configuration.
- `courses/index.json` — which courses exist and their catalog order.
- `courses/<name>/course.json` — one course: metadata, sections, materials.
- `courses/<name>/materials/*.md` — each text lesson is its own Markdown file.
- `news/<name>.json` + `news/<name>.md` — one news post each.
- `pages/<name>.json` + `pages/<name>.md` — one auxiliary page each.
- `media/` — images referenced with relative paths like `media/cover.svg`.

Edit a file, push, and the library updates within a minute. **No accounts
exist in this mode** — visitors study anonymously and their progress stays in
their own browser.
