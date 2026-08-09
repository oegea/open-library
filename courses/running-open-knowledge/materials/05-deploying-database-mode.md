Because database mode keeps state on disk, it wants the opposite of
serverless: **one machine, one disk, one instance**. The natural home is a
small VPS at a fixed monthly price — which also means **no variable
costs**: no per-request billing, no bandwidth surprises, no bill that an
attacker or a traffic spike can inflate. A few euros a month, flat.

## The recipe

On any small VPS (1 vCPU and 512 MB of RAM are genuinely enough to start),
a Raspberry Pi on a shelf, or a home server with Docker:

```sh
git clone https://github.com/oegea/open-knowledge.git && cd open-knowledge
docker build -t open-knowledge .
docker run -d --name open-knowledge --restart unless-stopped \
  -p 3000:3000 -v ok_data:/data open-knowledge
```

Put a reverse proxy in front for HTTPS. With Caddy it is genuinely one
line — certificates included, renewed automatically:

```sh
caddy reverse-proxy --from your-domain.example --to :3000
```

Now open your domain and **register the first account: it becomes the
administrator.** Do this immediately — on a fresh instance the first
registration is the keys to the building. Save the recovery code somewhere
safe and offline; with no email on file, that code is your way back in if
you lose your authenticator.

## The one rule: the volume

Everything that matters lives in `/data`: the SQLite database, every
uploaded image and audio file, and the encryption key that protects TOTP
secrets at rest. Two consequences follow:

1. **Always mount a persistent volume at `/data`.** A container without
   one forgets everything when it is recreated.
2. **Never run two instances against the same data.** SQLite is built
   around a single writer; one instance is not a limitation to work
   around but the design. It will take you much further than you expect —
   this is a course library, not a social network.

## Operations, honestly small

- **Upgrades:** `git pull`, rebuild the image, recreate the container with
  the same volume. Database migrations run automatically on startup and
  are strictly additive — an upgrade never rewrites or drops your data.
- **Backups:** copy the volume, or click "Download backup" in the admin
  panel for the full-environment zip. Do the thing seasoned operators do:
  **test one restore** onto a scratch instance, once. A backup you have
  restored is an insurance policy; one you have not is a hope.
- **Container platforms** (Fly.io, Railway, Render…) also work: mount a
  persistent volume at `/data` and keep exactly one instance. Be aware
  that usage-based platforms rarely offer hard spending caps — a
  fixed-price VPS cannot surprise you, which is why this course recommends
  one.
- **Without Docker** it is just `pnpm install && pnpm build && pnpm start`
  (Node 20+); state lives in `./data`, relocatable with the `OK_DATA_DIR`
  environment variable.
