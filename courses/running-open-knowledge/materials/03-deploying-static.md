Deploying a static library takes three steps and a few minutes.

**Step 1 — Scaffold your content repository.** One command, no
dependencies beyond a shell:

```sh
curl -fsSL https://raw.githubusercontent.com/oegea/open-knowledge/main/scripts/init-content-repo.sh | sh -s my-library
```

You get a working example — a course, an exam, a news post, an about page —
already committed to a fresh git repository, plus a README with these same
instructions and an `AGENTS.md` for AI assistants.

**Step 2 — Push it to GitHub, public:**

```sh
cd my-library
git remote add origin git@github.com:<user>/my-library.git
git push -u origin main
```

**Step 3 — Deploy the app once, pointing at your content.** Two easy paths:

*Serverless (e.g. Vercel).* Because static mode is stateless, serverless
hosting works. Use Vercel's "deploy from repository" flow against
`github.com/oegea/open-knowledge` and set one environment variable:

```
OK_CONTENT_REPO = https://raw.githubusercontent.com/<user>/my-library/main
```

*Docker, on any machine:*

```sh
git clone https://github.com/oegea/open-knowledge.git && cd open-knowledge
docker build -t open-knowledge .
docker run -d -p 3000:3000 \
  -e OK_CONTENT_REPO=https://raw.githubusercontent.com/<user>/my-library/main \
  open-knowledge
```

That is the entire operation. From now on you never redeploy for content:
edit, commit, push, and the site updates within a minute. You redeploy the
app only to pick up new versions of Open Knowledge itself.

A few practical notes:

- The content repository **must be publicly readable** — that is what makes
  the mode work, and it is also the point.
- Images go in `media/` and are referenced by relative paths.
- An item must be listed in its `index.json` to exist; index order is
  display order.
- Never change an `id` once published: visitors' local progress is keyed to
  course and material ids.
