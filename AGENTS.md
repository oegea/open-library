# This repository IS a knowledge library

This is a **content repository** for [Open Knowledge](https://github.com/oegea/open-knowledge),
an open-source, self-hostable application that publishes course libraries. An
Open Knowledge instance in *static content mode* reads everything it serves
straight from this repository over HTTP. There is no build step and no
database: **editing these files and pushing IS publishing**. Changes go live
within about a minute (the instance caches content for 60 seconds).

When in doubt about any format detail, the application source is open —
consult it at https://github.com/oegea/open-knowledge. The JSON shapes used
here are exactly the domain primitives under `src/modules/*/domain/*.ts`
(the `XPrimitive` interfaces and their `fromPrimitive` validation), and the
loaders live in `src/modules/*/infrastructure/Static*Repository.ts`.

## Layout: one file per thing

```
settings.json                        site identity and configuration
courses/index.json                   course directory names, catalog order
courses/<name>/course.json           one course (metadata + structure)
courses/<name>/materials/<file>.md   one Markdown file per text lesson
news/index.json                      news entry names, newest first
news/<name>.json  +  news/<name>.md  one news post each
pages/index.json                     page entry names
pages/<name>.json + pages/<name>.md  one auxiliary page each
media/                               images and files
```

Long-form text NEVER lives inside JSON: descriptors reference a Markdown
file through the `markdownFile` field (a path relative to the descriptor's
directory). That keeps JSON small and structural, and prose editable as
plain Markdown.

## Ground rules

- Every `.json` file must stay **valid JSON** (double quotes, no trailing
  commas, no comments). A malformed file makes that content disappear from
  the site until fixed.
- `id` values must be unique within their content type and **must never
  change** once published: visitor progress is keyed by course and material
  ids, and changing them resets everyone's progress.
- `slug` values are the public URLs (`/courses/<slug>`, `/news/<slug>`,
  `/p/<slug>`): lowercase, hyphen-separated, unique per content type. Keep
  them stable; renaming one breaks old links (static mode has no redirects).
- An item not listed in its `index.json` does not exist, no matter what
  files are on disk. Index order is display order (courses: catalog order;
  news: newest first).
- Dates are ISO 8601 UTC strings, e.g. `"2026-08-09T12:00:00Z"`.
- Markdown supports headings, lists, links, images, code blocks and tables.
- Images live in `media/` and are referenced with repo-relative paths like
  `"media/my-image.jpg"`. Absolute `https://` URLs also work.

## Adding a course

1. Create the directory `courses/<name>/` with a `course.json` and a
   `materials/` folder for its text lessons.
2. Append `"<name>"` to `courses/index.json`.

`course.json` shape:

```json
{
  "id": "course-unique-id",
  "title": "Course title",
  "slug": "course-title",
  "description": "One or two sentences shown in the catalog card and detail page.",
  "language": "en",
  "category": "Science",
  "coverImage": "media/my-cover.jpg",
  "authors": ["Author Name"],
  "sources": [
    { "title": "A book or reference", "url": null },
    { "title": "A website", "url": "https://example.org" }
  ],
  "license": "CC BY-SA 4.0",
  "aiAssisted": false,
  "published": true,
  "createdAt": "2026-08-09T12:00:00Z",
  "updatedAt": "2026-08-09T12:00:00Z",
  "sections": [
    {
      "id": "section-1",
      "title": "First section",
      "materials": []
    }
  ]
}
```

Field notes:

- `language`: one of `es en fr de it zh ru uk ca gl eu pt ja`. The catalog
  filters by it.
- `category`: free text or `null`. Courses sharing a category get a filter chip.
- `coverImage`: required in practice — the catalog is visual. 16:9 works best.
- `sources`: the bibliography shown on the course page. `url` may be `null`
  for offline references (books).
- `license`: free text shown on the course page (e.g. `"CC BY-SA 4.0"`), or
  `null` to omit.
- `aiAssisted`: set `true` if AI helped produce the materials — the course
  will show a clear notice. Open Knowledge is deliberately transparent about
  this; do not hide it.
- `published`: `false` keeps the course out of the catalog entirely (static
  mode has no admin preview, so unpublished courses are simply invisible).

### Materials

`sections` is an ordered array; each section contains ordered `materials` —
the order is the pedagogical path visitors follow. Every material shares
this envelope:

```json
{
  "id": "material-unique-id",
  "title": "Material title",
  "type": "markdown",
  "markdownFile": "materials/my-lesson.md",
  "mediaPath": null,
  "exam": null,
  "required": true,
  "sources": []
}
```

- `required`: required materials count towards course completion.
- `sources`: optional per-material bibliography, same shape as the course's.

The four material types:

1. **`"type": "markdown"`** — a text lesson. Write the content in a file
   under `materials/` and point `markdownFile` at it (path relative to the
   course directory). Don't repeat the title as a heading — the app renders
   it. `mediaPath` and `exam` stay `null`.
2. **`"type": "video"`** — set `mediaPath` to a video file
   (`media/lesson.mp4` or an absolute URL). `markdownFile` may point to
   optional notes rendered below the player.
3. **`"type": "audio"`** — same as video with an audio file
   (`media/talk.mp3`). The player shows the course artwork.
4. **`"type": "exam"`** — keep the questions inline in `course.json` (they
   are structure, not prose). Set `exam` to:

```json
{
  "passingScore": 0.7,
  "questionsPerAttempt": 5,
  "questions": [
    {
      "id": "q1",
      "text": "The question?",
      "choices": [
        { "id": "a", "text": "First choice" },
        { "id": "b", "text": "Second choice" }
      ],
      "correctChoiceId": "b",
      "explanation": "Shown after answering — explain WHY, don't just grade."
    }
  ]
}
```

- `passingScore` is a ratio (0.7 = 70%).
- `questionsPerAttempt`: how many questions each attempt draws randomly from
  the pool — a bank of 50 questions with `questionsPerAttempt: 10` gives
  every visitor a different exam.
- Write real `explanation`s: the product's exam philosophy is feedback, not
  scores.

## Adding a news post

1. Create `news/<name>.json` and `news/<name>.md` (the body).
2. **Prepend** `"<name>"` to `news/index.json` — the list is newest first,
   and the first entry renders as the large featured story.

```json
{
  "id": "news-unique-id",
  "title": "Post title",
  "slug": "post-title",
  "markdownFile": "post-title.md",
  "imagePath": "media/featured.jpg",
  "author": "Editor Name",
  "published": true,
  "createdAt": "2026-08-09T12:00:00Z",
  "updatedAt": "2026-08-09T12:00:00Z"
}
```

`imagePath` (featured image) and `author` (byline next to the date) are
optional — use `null` / `""`. News can be disabled site-wide via
`newsEnabled` in `settings.json`.

## Adding an auxiliary page

1. Create `pages/<name>.json` and `pages/<name>.md`.
2. Add `"<name>"` to `pages/index.json`.

```json
{
  "id": "page-unique-id",
  "title": "Page title",
  "slug": "page-title",
  "markdownFile": "page-title.md",
  "placement": "menu",
  "position": 1,
  "createdAt": "2026-08-09T12:00:00Z",
  "updatedAt": "2026-08-09T12:00:00Z"
}
```

`placement` decides where the page is linked: `"menu"` (header navigation),
`"footer"` (footer links) or `"hidden"` (reachable only by URL). `position`
orders pages within their placement.

## Site identity: name, texts, logos

Everything lives in `settings.json`:

- `libraryName` — the site name, browser-tab title and header brand.
- `ownerName` — shown in the footer as "This library belongs to X…". Empty
  string hides the ownership part.
- `heroTitle` / `heroText` — the home headline and subtitle. Empty strings
  fall back to localized defaults.
- `heroImagePath` — optional home hero background image (e.g.
  `"media/hero.jpg"`); `null` shows an animated brand gradient instead.
- `logoPath` — header logo image; `null` shows the library name as text.
- `documentLogoPath` — logo used inside exported EPUB/PDF documents; falls
  back to `logoPath`.
- `certificateLogoPath` — irrelevant in static mode (no certificates).
- `newsEnabled` — `false` removes the news section entirely.
- `registrationOpen` — ignored in static mode; there are no accounts.

To change a logo: drop the image into `media/` and set the path. SVG, PNG,
JPEG and WebP all work in the UI; PNG/JPEG reproduce best inside exported
PDFs.

## What does NOT exist in static mode

No accounts, no registration, no login, no notifications, no certificates,
no admin panel. Visitors study anonymously; their progress stays in their own
browser. If you need those features, run Open Knowledge in its default
database mode instead (see the application README).
