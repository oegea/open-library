#!/usr/bin/env python3
"""Generate timed transcripts for narrated chapters with ElevenLabs forced alignment.

Usage:
  ELEVENLABS_API_KEY=... python3 scripts/align.py --course <dir> [--only mat-01-01] [--force] [--dry-run]

For every audio/video material whose title starts with "Historia" and that has
a `mediaPath` under media/, sends the mp3 plus the narration text (the same
cleaned Markdown narrate.py synthesized) to POST /v1/forced-alignment and
writes `media/audio/<file>.transcript.json` in the Open Knowledge timed
transcript format ({"words": [{"text","start","end"}]}). Then sets the
material's `transcriptPath`. Forced alignment does not consume TTS credits;
the script prints the credit counter before and after anyway.
Materials that already have a transcript are skipped unless --force.
"""
import argparse, datetime, json, os, pathlib, re, sys, urllib.request, uuid

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from narrate import clean_markdown  # noqa: E402

API = "https://api.elevenlabs.io/v1"
ROOT = pathlib.Path(__file__).resolve().parent.parent

def credits(key):
    req = urllib.request.Request(f"{API}/user/subscription", headers={"xi-api-key": key})
    with urllib.request.urlopen(req, timeout=60) as r:
        d = json.load(r)
    return d["character_count"], d["character_limit"]

def narration_text(markdown: str) -> str:
    text = clean_markdown(markdown)
    return re.sub(r"<break[^>]*/>", "", text)

def forced_alignment(key, audio_path: pathlib.Path, text: str) -> dict:
    boundary = uuid.uuid4().hex
    body = b""
    body += (f"--{boundary}\r\nContent-Disposition: form-data; name=\"text\"\r\n\r\n").encode() + text.encode() + b"\r\n"
    body += (f"--{boundary}\r\nContent-Disposition: form-data; name=\"file\"; filename=\"{audio_path.name}\"\r\n"
             f"Content-Type: audio/mpeg\r\n\r\n").encode() + audio_path.read_bytes() + b"\r\n"
    body += f"--{boundary}--\r\n".encode()
    req = urllib.request.Request(
        f"{API}/forced-alignment", data=body, method="POST",
        headers={"xi-api-key": key, "Content-Type": f"multipart/form-data; boundary={boundary}"})
    with urllib.request.urlopen(req, timeout=900) as r:
        return json.load(r)

def to_transcript(alignment: dict) -> dict:
    words = []
    for w in alignment["words"]:
        text = w["text"].strip()
        if not text:
            continue
        words.append({"text": text, "start": round(float(w["start"]), 3), "end": round(float(w["end"]), 3)})
    return {"words": words}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--course", required=True)
    ap.add_argument("--only"); ap.add_argument("--force", action="store_true"); ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    key = os.environ.get("ELEVENLABS_API_KEY")
    if not key and not a.dry_run: sys.exit("ELEVENLABS_API_KEY not set")

    course = ROOT / "courses" / a.course
    cj = course / "course.json"
    data = json.loads(cj.read_text())
    if not a.dry_run:
        used, limit = credits(key); print(f"credits before: {used}/{limit}")
    changed = False
    for s in data["sections"]:
        for m in s["materials"]:
            if m.get("type") not in ("audio", "video") or not m.get("markdownFile") or not m.get("mediaPath"):
                continue
            if not m["title"].startswith("Historia"): continue
            if a.only and m["id"] != a.only: continue
            audio = ROOT / m["mediaPath"]
            out_rel = re.sub(r"\.(mp3|m4a|ogg|wav|mp4|webm)$", "", m["mediaPath"]) + ".transcript.json"
            out = ROOT / out_rel
            text = narration_text((course / m["markdownFile"]).read_text())
            print(f"{m['id']}  {len(text):6d} chars  {audio.name} -> {out_rel}")
            if a.dry_run: continue
            if out.exists() and m.get("transcriptPath") == out_rel and not a.force:
                print("    already aligned, skipping"); continue
            alignment = forced_alignment(key, audio, text)
            transcript = to_transcript(alignment)
            out.write_text(json.dumps(transcript, ensure_ascii=False, separators=(",", ":")) + "\n")
            print(f"    {len(transcript['words'])} words, loss {alignment.get('loss'):.3f}, "
                  f"last word ends at {transcript['words'][-1]['end']:.1f}s")
            if m.get("transcriptPath") != out_rel:
                m["transcriptPath"] = out_rel; changed = True
            used, limit = credits(key); print(f"    credits now: {used}/{limit}")
    if changed and not a.dry_run:
        data["updatedAt"] = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        cj.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
        print("course.json updated")

if __name__ == "__main__":
    main()
