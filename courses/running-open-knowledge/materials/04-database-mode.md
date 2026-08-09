Database mode is Open Knowledge as a living institution rather than a
published artifact. The instance keeps its own state — a SQLite database and
uploaded media on local disk, zero external services — and with state come
the features that need memory:

- **Pseudonymous identities.** Registration asks for no name, no email, no
  phone. You are assigned an identity like `Erudito#4821`, secured with any
  TOTP authenticator app (scan a QR, type the code) and recoverable with a
  one-time recovery code. Open Knowledge never knows who you are — by
  design, there is nothing personal to leak.
- **Progress across devices.** Registered learners continue on their phone
  what they started on their laptop.
- **Server-graded exams** whose results are recorded to the learner's
  identity.
- **Certificates.** Completing a course (all required materials, exams
  passed) earns a beautiful, shareable course-completion certificate with a
  verification URL and a downloadable PDF. Learners can optionally set a
  display name for their certificates — the single optional personal field
  in the entire application, voluntary and removable.
- **A visual admin panel.** The first account registered becomes the
  administrator: course editor with sections and materials, exam builder,
  media uploads, news publishing, auxiliary pages, site settings (name,
  logos, hero), user management, and **one-click full environment backup**
  — a zip that restores your entire library onto any fresh instance.
- **Notifications**, so registered learners hear about new courses and
  earned certificates. Nothing social — no comments, no followers, no feeds.

Content here is managed through the admin panel rather than git: create a
course, add sections and materials in the editor, upload covers, publish
when ready. Everything a static library expresses as files, database mode
expresses as friendly forms.

The learner-facing philosophy does not change one millimeter between modes:
reading requires no account, and the learner is never a product. Accounts
exist purely to *keep learning state*, and hold nothing but a pseudonym,
credentials, progress and results.
