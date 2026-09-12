# Feature idea backlog

Candidate site features, not yet built. Remove an entry once it's implemented.

## Comments

- **Reader comments, without requiring commenters to log in anywhere** — the site is fully static (GitHub Pages, no server), so anonymous commenting unavoidably needs *some* small backend to catch the submission; the question is just where that piece lives. Options considered, in order of fit:
  1. **Git-based via Staticman** — a form posts to a small serverless relay (free tier, e.g. Vercel/Netlify function) that commits the comment as a data file in this repo, optionally gated behind a PR for approval before it renders in the next Jekyll build. No ads, no commenter login, comments live in git like everything else here.
  2. **Small serverless relay + GitHub Discussions** — a free-tier function (e.g. Cloudflare Worker) takes the anonymous submission and posts it into a GitHub Discussion using the site owner's own token; comments render by reading the Discussion back. Similar effort to Staticman, one more moving part.
  3. **Paid ad-free host (e.g. Hyvor Talk)** — a small recurring subscription buys a fully-managed, no-ads, no-tracking widget with guest (name-only) commenting, at the cost of ongoing money and being on someone else's service.
  - Explicitly ruled out: giscus/utterances (require commenters to have a GitHub account) and Disqus (ads/tracking on the free tier).
  - Not yet decided which option to build — revisit when ready to implement.

## Narration voice

- **Contribute a Singaporean-accented voice to Kokoro TTS** (long-term
  goal, not started). The site's narration currently uses `bm_george`,
  a British voice — serviceable, but not actually the accent of the
  place the blog is about. Kokoro (`hexgrad/Kokoro-82M`) is open-source
  (Apache 2.0), so a new voice is at least theoretically something
  that could be trained and contributed upstream, rather than waiting
  for one to show up.
  - Would need a real recorded-speech dataset in Singaporean English
    (a specific voice actor/speaker, enough clean audio to train
    against) — the actual bottleneck, not the code.
  - Unclear yet whether Kokoro's training pipeline realistically
    supports a community-contributed voice this way, or what the
    practical effort/cost looks like — this needs real research before
    it's more than an idea.
  - Payoff if it works: narration that actually sounds like it's
    telling a Singapore story, not just narrating one in a borrowed
    accent.
  - Not yet researched in detail — revisit when there's a real chance
    to invest the time.

## Reader voting on what to post next

- **Let readers vote on candidate topics from the post-ideas backlog** — a signal to inform what gets written next, not a binding commitment to always follow the vote.
  - Anonymous, no login required to vote (favored over GitHub-issue reactions, which would require a GitHub account, same barrier as the comments idea above). Since it's just a signal, occasional spam/multi-voting is an acceptable tradeoff for staying login-free.
  - Same underlying constraint as comments: a fully static site can't tally anonymous votes without *some* backend to hold the counts — likely a small free-tier counter service (e.g. a Cloudflare Worker + KV, or a third-party anonymous-counter API), not yet decided.
  - Natural integration point: the existing `docs/post-ideas.md` backlog — would need a reader-facing page listing candidate topics (that file is currently excluded from the built site via `_config.yml`'s `exclude:`, so it'd need a public-facing counterpart or to be un-excluded/reformatted).
  - Not yet designed in detail — revisit when ready to implement.

## Chunked/checkpointed video rendering

- **Split `watch_video_lib.py`'s `render()` into segments, encoding each to its own file as it finishes and concatenating at the end**, instead of one continuous ffmpeg pipe for the whole video.
  - Motivated by the render-step "low memory" kills Claude's Bash tool hit repeatedly across the nutmeg and Elizabeth Choy posts (2026-09-11) — confirmed a false positive of Claude's own tool/sandbox (real system RAM stayed healthy every time, and the identical command completed clean in Chris's own terminal), so this wouldn't fix that specific root cause. The standing fix for that is procedural: Part C renders run in Chris's terminal, not Claude's Bash tool ([[feedback_live_pipeline_walkthrough_style]]).
  - Worth doing anyway as a resilience/usability improvement: `render()` already streams individual frames straight into ffmpeg (never buffers the whole video), so the actual memory cost is each worker's own prepared-image cache, not accumulated output — but a kill from any cause (crash, power loss, a future real OOM) currently loses the entire render, since the mp4 muxer only finalizes at the end. Chunking would let a restart pick up from the last completed segment instead of frame 0.
  - Tradeoff: added complexity (segment boundaries, concat step, matching audio offsets per chunk) and a little encode overhead from stitching multiple GOPs, for a problem that hasn't actually caused lost work yet (Chris's terminal has never hit it).
  - Not yet designed in detail — revisit when there's time to invest, per Chris (2026-09-12): "anything that improves stability and usability is worth pursuing."

## Video audio loudness normalization

- **Bake a fixed loudness target into `watch_video_lib.py`'s render step** (e.g. an `-af loudnorm` pass targeting -16 or -14 LUFS, matching YouTube's own stated normalization target for regular video) instead of the current straight AAC passthrough encode.
  - Motivated by a real discrepancy found on the four-chopsticks-blood-debt-singapore-japan post: the main video and Short sounded different in loudness when viewed on YouTube, even though direct `ffmpeg loudnorm` measurement of both rendered mp4 files showed near-identical loudness (-25.08 vs -25.07 LUFS integrated) — confirming the divergence isn't in our files, it's YouTube normalizing regular videos and Shorts differently at playback.
  - Pre-normalizing to a fixed target wouldn't necessarily fully close that gap (YouTube's own processing still runs on top regardless), but starting both files from the same normalized baseline should narrow it, since there'd be less room for YouTube's per-format processing to diverge.
  - Not yet implemented or tested — revisit if the discrepancy recurs on future posts, or proactively before it does.
