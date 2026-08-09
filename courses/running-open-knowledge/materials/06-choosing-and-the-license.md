**Which mode should you run?** The question that decides it: *do your
learners need the library to remember them?*

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
| Maintenance | None | Backups, upgrades (both easy) |

Start static if in doubt: it is the five-minute path, and a static library
can always migrate later — recreate the content through the admin panel of a
database instance, or keep both: many libraries never need accounts at all.

**On the license, and on the spirit.** Open Knowledge is released under the
**MIT license**. Legally, MIT permits virtually everything: use, copy,
modify, redistribute, even sell, with attribution. That permissiveness is
deliberate — it is how open tools spread, and your library never depends on
anyone's permission.

But the project asks you to understand the difference between what the
license *allows* and what the project *is for*. **Open Knowledge was not
built to power paywalled course platforms, knowledge-as-product businesses,
or libraries that treat learners as customers to convert.** It was built so
that knowledge someone cared enough to curate could be given away well — in
the tradition of the public library, of free software, of Wikipedia. The
license is a floor. The tradition is the compass.

If you have knowledge worth sharing, you now know everything needed to
share it. Scaffold a repository, push it, deploy — and leave the door open
behind you.
