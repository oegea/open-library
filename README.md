# My Open Knowledge library (static content)

This repository IS the library: an [Open Knowledge](https://github.com/oegea/open-knowledge)
instance in **static content mode** reads everything it serves from here.
Editing these files and pushing is publishing — no build, no deploy, no
database. `AGENTS.md` documents every format in detail, and doubles as
instructions for AI coding assistants (Claude Code, Codex, OpenCode…), so
one can assist you in drafting, structuring and publishing your material
directly in this repository.

## Publish the library in three steps

1. **Push this folder** to a public GitHub repository (the scaffolder
   already ran `git init` and made the first commit):

   ```sh
   git remote add origin git@github.com:<user>/<repo>.git
   git push -u origin main
   ```

2. **Deploy the Open Knowledge app** (once) with the environment variable
   `OK_CONTENT_REPO` pointing at this repository's raw URL:
   `https://raw.githubusercontent.com/<user>/<repo>/main`
3. **Edit, commit, push** to publish content from now on. Changes appear
   within a minute.

### Deploy option A — Vercel (no server at all)

The app is stateless in this mode, so a serverless platform works. Click:

> https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Foegea%2Fopen-knowledge&env=OK_CONTENT_REPO&envDescription=Raw%20base%20URL%20of%20your%20content%20repository

…and when asked, set `OK_CONTENT_REPO` to your raw URL from step 2.

### Deploy option B — any machine with Docker

```sh
git clone https://github.com/oegea/open-knowledge.git && cd open-knowledge
docker build -t open-knowledge .
docker run -d --name open-knowledge --restart unless-stopped -p 3000:3000 \
  -e OK_CONTENT_REPO=https://raw.githubusercontent.com/<user>/<repo>/main \
  open-knowledge
```

### Deploy option C — container platforms

The same image runs on Railway, Render, Fly.io and friends. No volume is
needed — the container is stateless and disposable.

## Structure

One file per thing; long-form text lives in Markdown, never inside JSON:

| Path | What it is |
|------|------------|
| `settings.json` | Library name, hero texts, logos, news toggle |
| `courses/index.json` | Course directory names, in catalog order |
| `courses/<name>/course.json` | One course: metadata, sections, materials, exams |
| `courses/<name>/materials/*.md` | One Markdown file per text lesson |
| `news/<name>.json` + `.md` | One news post each, listed in `news/index.json` |
| `pages/<name>.json` + `.md` | One auxiliary page each, listed in `pages/index.json` |
| `media/` | Images and files, referenced as `media/<file>` |

In this mode there are no accounts: visitors study anonymously and their
progress lives in their own browser.
