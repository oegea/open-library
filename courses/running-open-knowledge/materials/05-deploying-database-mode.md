Because database mode keeps state on disk, it wants the opposite of
serverless: **one machine, one disk, one instance**. The natural home is a
small VPS at a fixed monthly price — which also means **no variable costs**:
nobody can inflate your bill with traffic.

**The recipe.** On any small VPS (1 vCPU / 512 MB is plenty to start), a
Raspberry Pi, or a home server with Docker:

```sh
git clone https://github.com/oegea/open-knowledge.git && cd open-knowledge
docker build -t open-knowledge .
docker run -d --name open-knowledge --restart unless-stopped \
  -p 3000:3000 -v ok_data:/data open-knowledge
```

Put a reverse proxy in front for HTTPS — Caddy makes it one line:

```sh
caddy reverse-proxy --from your-domain.example --to :3000
```

Open your domain and **register the first account: it becomes the
administrator**. Save its recovery code somewhere safe — with no email on
file, that code is your way back in.

**The one rule: the volume.** Everything that matters — database, uploaded
media, the encryption key protecting TOTP secrets — lives in `/data`. Mount
a persistent volume there, always, and never run two instances against the
same data (SQLite wants a single writer).

**Operations, honestly small:**

- *Upgrades:* `git pull`, rebuild the image, recreate the container with the
  same volume. Database migrations run automatically and are additive.
- *Backups:* copy the volume — or click "Download backup" in the admin
  panel, which produces a zip that restores your entire environment onto
  any fresh instance. Test a restore once; future-you says thanks.
- *Container platforms* (Fly.io, Railway, Render…) also work if you mount a
  persistent volume at `/data` and keep exactly one instance. Mind that
  usage-based platforms rarely offer hard spending caps; a fixed-price VPS
  cannot surprise you.
