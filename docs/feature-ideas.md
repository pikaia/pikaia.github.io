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
