Deploying a static library takes three steps and a few minutes. This
lesson is deliberately concrete — commands you can paste — because the
promise of the previous lesson only matters if the path is actually this
short.

## Step 1 — Scaffold your content repository

One command, with no dependency beyond a shell:

```sh
curl -fsSL https://raw.githubusercontent.com/oegea/open-knowledge/main/scripts/init-content-repo.sh | sh -s my-library
```

The script creates a `my-library/` folder containing a complete working
example — a course with a text lesson and an exam, a news post, an about
page, a cover image — already initialized as a git repository with its
first commit made. It also writes two documentation files: a `README.md`
with deploy instructions (essentially this lesson), and the `AGENTS.md`
format reference for you and for AI assistants.

Nothing about the example is sacred: it exists to be edited, copied and
deleted as you replace it with your own material.

## Step 2 — Publish it on GitHub

Create a new **public** repository on GitHub (the content must be publicly
readable — that is what the instance will fetch, and given the tradition,
it is also the point). Then connect and push:

```sh
cd my-library
git remote add origin git@github.com:<user>/my-library.git
git push -u origin main
```

Your content now has a raw URL of the form
`https://raw.githubusercontent.com/<user>/my-library/main` — note it, it is
the only configuration the app needs.

## Step 3 — Deploy the app, once

Two easy paths; both take minutes.

**Serverless (e.g. Vercel).** Because static mode keeps no server state, a
serverless platform works — the filesystem being wiped between invocations
costs nothing when there is nothing to keep. Use the platform's "deploy
from repository" flow pointed at `github.com/oegea/open-knowledge`, and set
one environment variable:

```
OK_CONTENT_REPO = https://raw.githubusercontent.com/<user>/my-library/main
```

**Docker, on any machine you control:**

```sh
git clone https://github.com/oegea/open-knowledge.git && cd open-knowledge
docker build -t open-knowledge .
docker run -d -p 3000:3000 \
  -e OK_CONTENT_REPO=https://raw.githubusercontent.com/<user>/my-library/main \
  open-knowledge
```

That is the entire operation, and here is the part worth internalizing:
**you never redeploy for content again.** Edit, commit, push — live within
a minute. The application only needs redeploying when you want a newer
version of Open Knowledge itself.

## The habits that keep a static library healthy

- **The index is the truth.** An item must be listed in its `index.json`
  to exist, no matter what files sit on disk; index order is display
  order (courses: catalog order; news: newest first).
- **Ids are forever.** Visitors' progress is keyed to course and material
  ids in their own browsers. Renaming an id silently resets the progress
  of every person who ever read that course. Choose ids once, keep them.
- **Slugs are URLs.** Changing one breaks inbound links — static mode has
  no redirect memory. Same rule: choose well, keep them.
- **Images go in `media/`** and are referenced by relative paths; the
  instance resolves them against your repository automatically.
- **Validate your JSON** after hand-editing (any editor or `python3 -m
  json.tool` will do): a malformed file makes that content vanish from the
  site until fixed — the failure is silent by design, never a broken page
  for your readers.
