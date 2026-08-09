In static content mode your library has **no database and no server
state**. Everything it serves lives as plain files in a **public git
repository**:

```
settings.json                          the library's name and configuration
courses/index.json                     which courses exist, in catalog order
courses/<name>/course.json             one course: metadata, sections, exams
courses/<name>/materials/*.md          one Markdown file per text lesson
news/<name>.json + news/<name>.md      one news post each
pages/<name>.json + pages/<name>.md    one auxiliary page each
media/                                 images and files
```

The Open Knowledge instance is told where that repository lives — a single
environment variable, `OK_CONTENT_REPO`, pointing at the repository's raw
URL — and simply renders it, refreshing its cache about once a minute.

## Why git, of all things?

Because a git repository is quietly the best content-management system ever
built, and you already know how to use it. Consider what you get without
installing anything:

- **Publishing is a push.** Edit a Markdown file, commit, push — your
  library updates within a minute. No deploy, no build step, no admin
  session.
- **History is automatic.** Every version of every lesson, forever, with
  authorship and dates. Made a mess? Revert the commit. Want to know what
  changed in a course since spring? `git diff`.
- **Review comes free.** A colleague can propose a fix to your course as a
  pull request. You read the diff, you merge. That workflow took software
  engineering decades to refine, and your library inherits it whole.
- **The server is disposable.** No state means nothing to back up, nothing
  to migrate, nothing that can be lost. If the container dies, you start
  another; if the platform disappoints you, you point a different one at
  the same repository. Your library cannot be held hostage.
- **Radical openness, structurally.** Your content is not *in* a platform;
  it IS a public repository. Anyone can read its history, learn from how it
  is built, or start their own library from a copy — which, given the
  tradition this project belongs to, is exactly the point.

## The shape of the content

One design rule keeps the format pleasant: **long-form text never lives
inside JSON**. The JSON descriptors stay small and structural — titles,
ordering, metadata, exam definitions — while every lesson is an ordinary
Markdown file, referenced by name. Prose stays diffable, reviewable and
comfortable to write. The one deliberate exception is exam questions, which
stay inline in `course.json`: they are structure (choices, correct answers,
explanations), not prose.

Every scaffolded content repository also includes an `AGENTS.md` that
documents this whole format in detail. It doubles as instructions for AI
coding assistants (Claude Code, Codex, OpenCode…), so one can help you
draft, structure and publish your material — with you supplying the
knowledge and the judgment, and the assistant handling the format.

## What does not exist here

There are no accounts of any kind in static mode. Visitors study
anonymously; their progress lives in their own browsers; exams are graded
on the spot without being recorded anywhere. Registration, notifications,
certificates and the admin panel simply do not exist — not disabled:
absent. For many libraries that is not a limitation but a feature: nothing
to secure, nothing to leak, nothing to maintain.

This very library runs in static mode. The page you are reading is a
Markdown file in a public repository, and if you check that repository's
history you can watch this exact paragraph being written.
