Database mode is Open Knowledge as a **living institution** rather than a
published artifact. The instance keeps its own state — a SQLite database
and uploaded media on local disk, zero external services — and with memory
come the features that need it. What does not change is the philosophy:
reading still requires no account, and the learner is still not a product.

## Identity without personal data

Registration in Open Knowledge asks for no name, no email, no phone
number. Instead, the instance offers you a generated pseudonym — something
like `Erudito#4821` — and a QR code. You scan it with any TOTP
authenticator app (the same kind you may already use for two-factor
authentication), and from then on you sign in with your pseudonym plus the
six-digit code your app generates. A one-time **recovery code**, shown once
at registration, is your fallback if you lose the device.

It is worth appreciating what this design refuses to do. There is no email
to leak, no password to reuse, no profile to build, no way for the library
to know who you are — and therefore nothing personal to breach. The
learner's identity is exactly as real as their learning, and no realer.
The single, deliberate exception: you may optionally set a display name to
appear on your certificates, and remove it whenever you wish.

## What memory buys

- **Progress across devices.** Continue on your phone what you started on
  your laptop; the library remembers your page the way your browser did in
  static mode, but everywhere.
- **Exams graded and recorded server-side**, attached to your pseudonym —
  the basis for completion.
- **Certificates.** Completing a course — every required material, exams
  passed — earns a shareable certificate with its own verification URL and
  a downloadable PDF. Not an academic credential; a beautiful, durable way
  of recognizing that a learning path was walked to its end.
- **Notifications** for new courses and earned certificates. Nothing
  social: no comments, no followers, no feeds. The list of things database
  mode deliberately does *not* add is as important as the list it does.

## The admin panel

The first account registered on a fresh instance becomes the
administrator — so registering immediately after deploying is part of the
deploy. From the panel, the administrator manages:

- **Courses**, in a visual editor: sections, materials in the four types,
  an exam builder with question pools, cover and media uploads,
  publish/unpublish.
- **News and auxiliary pages** (about, legal…), with menu or footer
  placement.
- **Site settings**: library name, hero texts and image, up to three
  logos (header, certificates, exported documents), registration toggle,
  news toggle.
- **Users**: list identities, open a user's detail, adjust their
  certificate display name, revoke certificates, promote a trusted person
  to admin, or delete an account.
- **Backups**: one click downloads a zip of the entire environment —
  database, media, settings, everything. Restoring that zip onto a fresh
  instance reproduces the library exactly. It is disaster recovery,
  migration tool and peace of mind in one button.

Everything a static library expresses as files in a repository, database
mode expresses as forms. Which interface is better is not a matter of
sophistication but of temperament — some people think in git, some in
buttons — and of whether your learners need the library to remember them.
