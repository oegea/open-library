In static content mode, your library has **no database and no server
state**. Everything it serves lives as plain files in a **public git
repository**:

```
settings.json                        the library's name and configuration
courses/index.json                   which courses exist, in catalog order
courses/<name>/course.json           one course: metadata, sections, exams
courses/<name>/materials/*.md        one Markdown file per text lesson
news/<name>.json + news/<name>.md    one news post each
pages/<name>.json + pages/<name>.md  one auxiliary page each
media/                               images and files
```

The Open Knowledge instance is told where that repository lives (an
environment variable, `OK_CONTENT_REPO`, pointing at the repository's raw
URL) and simply renders it, refreshing its cache about once a minute.

The consequences are worth savoring:

- **Publishing is a git push.** Edit a Markdown file, commit, push — your
  library updates within a minute. Git is your admin panel, and you get
  version history, review, and rollback for free.
- **The server is disposable.** No state means nothing to back up, nothing
  to migrate, nothing to break. The instance can run on serverless
  platforms, free tiers, or a container anywhere.
- **Your content is radically open.** It is not *in* a platform; it IS a
  public repository. Anyone can read its history or start their own
  library from a copy of yours — which is exactly the spirit.
- **There are no accounts of any kind.** Visitors study anonymously and
  their progress lives in their own browsers. Registration, notifications,
  certificates and the admin panel simply do not exist in this mode.

Long-form text never lives inside JSON: descriptors are small and
structural, and each lesson is an ordinary Markdown file — pleasant to write
by hand, and equally pleasant to work on with an AI coding assistant. Every
scaffolded content repository includes an `AGENTS.md` that teaches
assistants (Claude Code, Codex, OpenCode…) the full format, so they can help
you draft, structure and publish your material.

This very library runs in static mode. The page you are reading is a
Markdown file in a public repository.
