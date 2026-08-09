**Which mode should you run?** One question decides it: *do your learners
need the library to remember them?*

| | Static mode | Database mode |
|---|---|---|
| Content lives in | A public git repository | SQLite + admin panel |
| Publishing | `git push` | Visual editor |
| Accounts | None exist | Pseudonymous TOTP identities |
| Progress | Visitor's own browser | Across devices, server-side |
| Exams | Graded in the browser | Graded and recorded server-side |
| Certificates | — | Yes, with PDF and verification URL |
| Server state | None — disposable instance | `/data` volume — one instance |
| Hosting | Anywhere, serverless included | A machine with a disk (VPS) |
| Maintenance | None | Backups and upgrades (both easy) |

Three sketches, to make it concrete:

- *A teacher publishing a course for anyone who finds it* — static. No
  accounts to manage, no server to maintain, content versioned in git,
  hosting effectively free.
- *A community school that wants learners to keep progress across devices
  and earn certificates* — database mode on a small VPS. A few euros a
  month, one backup habit.
- *Not sure yet* — start static. It is the five-minute path, and a static
  library can migrate later by recreating its content through a database
  instance's admin panel. Many libraries never need accounts at all; you
  will know you need them when learners start asking to be remembered.

## The license, and what it is for

Open Knowledge is released under the **MIT license**, one of the most
permissive in existence. In plain terms it says: use this, copy it, modify
it, redistribute it, even sell things built on it — just keep the
copyright notice, and accept that it comes with no warranty. That
permissiveness is deliberate. It is how open tools spread, and it
guarantees something this course has cared about from the first lesson:
**your library depends on nobody's permission** — not a vendor's, not a
platform's, not even this project's.

But the project asks you to understand the difference between what the
license *allows* and what the project *is for*. A license is law; a
project also has a tradition. **Open Knowledge was not built to power
paywalled course platforms, knowledge-as-product businesses, or libraries
that treat learners as customers to convert.** It was built so that
knowledge someone cared enough to curate could be given away well — in the
tradition of the public library, of free software, of Wikipedia: the
tradition its companion course traces across twenty-seven centuries. The
license is a floor. The tradition is the compass.

If you have knowledge worth sharing, you now know everything needed to
share it. Scaffold a repository, push it, deploy — and leave the door open
behind you.
