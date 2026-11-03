"""Check every image a post depends on can actually be fetched from THIS machine.

Born of the Force Z step-5 failure (2026-11-02): the build died 30 minutes in
because one image URL (ibiblio.org) fails TLS verification from the PC --
CERTIFICATE_VERIFY_FAILED, self-signed certificate in certificate chain --
while the same URL fetched fine elsewhere. The failure is environment-specific,
so this check must run on the machine that will run the build, using the same
fetch path as watch_video_lib (urllib + the same User-Agent).

Usage:
    python scripts/check_image_urls.py <slug>
    python scripts/check_image_urls.py --urls URL [URL ...]

Collects image references from the post, its gallery, and both video configs.
Remote URLs are fetched (first bytes only); local /assets/... paths are checked
for existence. Hosts are tracked in scripts/image_hosts_known.txt: a host on
its first appearance is reported as NEW; once a host passes it is recorded.
Exits nonzero if anything fails, so it can gate a pipeline block.
"""
import re
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path
from urllib.parse import urlparse

USER_AGENT = "pikaia-blog-tool/1.0 (https://pikaia.github.io; chriskslee@gmail.com)"
ROOT = Path(__file__).resolve().parent.parent
KNOWN_HOSTS_FILE = Path(__file__).resolve().parent / "image_hosts_known.txt"
PAUSE_S = 0.7          # be gentle: upload.wikimedia.org answers 429 to bursts
RETRY_429_PAUSE_S = 6


def collect_from_slug(slug: str):
    refs = []  # (origin-label, ref)
    post = next((ROOT / "_posts").glob(f"*-{slug}.md"), None)
    gallery = ROOT / "_gallery" / f"{slug}.md"
    configs = [
        ROOT / "scripts" / "video-configs" / f"{slug}.py",
        ROOT / "scripts" / "video-configs" / f"{slug}-short.py",
    ]
    md_img = re.compile(r"!\[[^\]]*\]\(([^)\s]+)")
    front_img = re.compile(r"^image:\s*(\S+)", re.M)
    cfg_img = re.compile(r'"[A-Z0-9_]+":\s*"((?:https?://|/assets/)[^"]+)"')
    for path, kind in [(post, "post"), (gallery, "gallery")]:
        if path and path.exists():
            text = path.read_text(encoding="utf-8")
            for m in md_img.findall(text):
                refs.append((kind, m))
            for m in front_img.findall(text):
                refs.append((kind, m))
    for path in configs:
        if path.exists():
            text = path.read_text(encoding="utf-8")
            for m in cfg_img.findall(text):
                refs.append((path.name, m))
    return refs


def fetch_verdict(url: str):
    """Return (ok, detail). Mirrors watch_video_lib.load_source's fetch."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            resp.read(128)
            return True, f"HTTP {resp.status}"
    except urllib.error.HTTPError as e:
        if e.code == 429:
            time.sleep(RETRY_429_PAUSE_S)
            return fetch_verdict_retry(url)
        return False, f"HTTP {e.code}"
    except urllib.error.URLError as e:
        return False, f"{e.reason}"
    except Exception as e:  # ssl errors surface as URLError, belt and braces
        return False, f"{type(e).__name__}: {e}"


def fetch_verdict_retry(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            resp.read(128)
            return True, f"HTTP {resp.status} (after 429 retry)"
    except Exception as e:
        return False, f"after 429 retry: {e}"


def main():
    argv = sys.argv[1:]
    if not argv:
        print(__doc__)
        return 2
    if argv[0] == "--urls":
        refs = [("arg", u) for u in argv[1:]]
    else:
        refs = collect_from_slug(argv[0])
    if not refs:
        print("No image references found.")
        return 2

    seen = {}
    for origin, ref in refs:
        seen.setdefault(ref, []).append(origin)
    remote = sorted(r for r in seen if r.startswith("http"))
    local = sorted(r for r in seen if r.startswith("/"))

    known = set()
    if KNOWN_HOSTS_FILE.exists():
        known = {ln.strip() for ln in KNOWN_HOSTS_FILE.read_text().splitlines() if ln.strip()}

    failures = 0
    new_hosts = set()
    print(f"Checking {len(remote)} remote image URL(s), {len(local)} local...")
    for ref in local:
        path = ROOT / ref.lstrip("/")
        ok = path.exists()
        print(f"  {'OK  ' if ok else 'FAIL'} local {ref}" + ("" if ok else " -- file missing"))
        failures += 0 if ok else 1
    for url in remote:
        host = urlparse(url).netloc
        tag = "NEW HOST" if host not in known else "        "
        ok, detail = fetch_verdict(url)
        print(f"  {'OK  ' if ok else 'FAIL'} {tag} {host} -- {detail} -- {url[:100]}")
        if ok and host not in known:
            new_hosts.add(host)
        failures += 0 if ok else 1
        time.sleep(PAUSE_S)

    if new_hosts:
        with KNOWN_HOSTS_FILE.open("a", encoding="utf-8") as f:
            for h in sorted(new_hosts):
                f.write(h + "\n")
        print(f"Recorded new host(s) as known-good: {', '.join(sorted(new_hosts))}")
    print("RESULT:", "ALL PASS" if failures == 0 else f"{failures} FAILURE(S)")
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
