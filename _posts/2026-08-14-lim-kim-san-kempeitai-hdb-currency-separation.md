---
layout: post
title: "Tortured by the Kempeitai, He Went On to Build a Nation's Homes"
date: 2026-08-14 09:00:00 +0800
last_modified_at: 2026-08-21 09:30:00 +0800
categories: [history, world-war-two]
image: https://upload.wikimedia.org/wikipedia/commons/b/b8/Lim_Kim_San_in_the_1940s.jpg
---

Sometime during the Japanese Occupation of Singapore, the Kempeitai picked up a young Peranakan businessman named Lim Kim San — not once, but twice — and tortured him on the strength of two accusations that couldn't both be true: that he was a communist, and that he was a British sympathiser. Two decades later, that same man would be the one Singaporeans called "Mr HDB," credited with solving the housing crisis of a newly independent nation. Almost nobody remembers the part in between.

[← Back to all posts](/)

<div style="display: flex; gap: 2em; margin: 0.5em 0 1.5em 0; align-items: flex-end;">
  <div id="listen-widget" role="button" tabindex="0" aria-label="Play audio narration of this post" style="display: inline-flex; flex-direction: column; align-items: center; cursor: pointer; gap: 0.2em; user-select: none;">
    <span id="listen-icon" aria-hidden="true" style="display: inline-flex; align-items: center; justify-content: center; width: 2.1em; height: 2.1em; border-radius: 50%; border: 1px solid #888; font-size: 1.1em;">&#127911;</span>
    <span style="font-size: 0.7em; text-transform: uppercase; letter-spacing: 0.05em; opacity: 0.75;">Listen</span>
  </div>
  <div id="watch-widget" role="button" tabindex="0" aria-label="Watch an animated version of this post" style="display: inline-flex; flex-direction: column; align-items: center; cursor: pointer; gap: 0.2em; user-select: none;">
    <span aria-hidden="true" style="display: inline-flex; align-items: center; justify-content: center; width: 2.1em; height: 2.1em; border-radius: 50%; border: 1px solid #888; font-size: 1.1em;">&#127916;</span>
    <span style="font-size: 0.7em; text-transform: uppercase; letter-spacing: 0.05em; opacity: 0.75;">Watch</span>
  </div>
  <a href="https://youtu.be/iTNZd1Op4fI" target="_blank" rel="noopener" aria-label="Watch this story as a video on YouTube" style="display: inline-flex; flex-direction: column; align-items: center; gap: 0.2em; text-decoration: none; color: inherit;">
    <span aria-hidden="true" style="display: inline-flex; align-items: center; justify-content: center; width: 2.4em; height: 2.4em; border-radius: 50%; border: 1px solid #888;">
      <svg width="1.4em" height="1.4em" viewBox="0 0 24 24" aria-hidden="true"><rect x="1" y="4" width="22" height="16" rx="5" fill="#FF0000"/><path d="M10 8.5l6 3.5-6 3.5z" fill="#fff"/></svg>
    </span>
    <span style="font-size: 0.7em; text-transform: uppercase; letter-spacing: 0.05em; opacity: 0.75;">YouTube</span>
  </a>
</div>

<audio id="listen-audio" preload="none" style="display: none;">
  <source src="/audio/lim-kim-san-kempeitai-hdb-currency-separation-kokoro.mp3" type="audio/mpeg">
</audio>

<div id="watch-viewer" style="position: fixed; inset: 0; background: #000; z-index: 9999; display: none;">
  <div id="watch-stage" style="position: absolute; inset: 0; overflow: hidden;"></div>
  <div style="position: absolute; left: 0; right: 0; bottom: 12%; text-align: center; padding: 0 5%; z-index: 2;">
    <span id="watch-caption" style="display: inline-block; background: rgba(0,0,0,0.55); color: #fff; font-size: 1.3em; font-weight: 600; padding: 0.5em 0.8em; border-radius: 4px; max-width: 700px;"></span>
  </div>
  <button id="watch-close" aria-label="Close" style="position: absolute; top: 1em; right: 1.2em; color: #fff; font-size: 1.6em; cursor: pointer; background: none; border: none; z-index: 2;">&times;</button>
  <div style="position: absolute; bottom: 0; left: 0; right: 0; padding: 1em 1.5em; display: flex; align-items: center; gap: 1em; background: linear-gradient(transparent, rgba(0,0,0,0.6)); z-index: 2;">
    <button id="watch-play" aria-label="Play/Pause" style="background: none; border: none; color: #fff; font-size: 1.4em; cursor: pointer; line-height: 1; padding: 0.2em;">&#10074;&#10074;</button>
    <div id="watch-progress" style="flex: 1; height: 4px; background: rgba(255,255,255,0.25); border-radius: 2px; overflow: hidden; cursor: pointer;">
      <div id="watch-progress-fill" style="height: 100%; width: 0%; background: #fff;"></div>
    </div>
    <span id="watch-time" style="color: #fff; font-size: 0.85em; font-variant-numeric: tabular-nums; opacity: 0.8;">0:00 / 0:00</span>
  </div>
</div>

<script>
(function () {
  var widget = document.getElementById('listen-widget');
  var icon = document.getElementById('listen-icon');
  var audio = document.getElementById('listen-audio');

  function setIcon(playing) {
    icon.innerHTML = playing ? '&#10074;&#10074;' : '&#127911;';
  }

  function toggle() {
    if (audio.paused) {
      audio.play();
    } else {
      audio.pause();
    }
  }

  widget.addEventListener('click', toggle);
  widget.addEventListener('keydown', function (e) {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      toggle();
    }
  });
  audio.addEventListener('play', function () { setIcon(true); });
  audio.addEventListener('pause', function () { setIcon(false); });
  audio.addEventListener('ended', function () { setIcon(false); });
})();
</script>

<script>
(function () {
  var LIM = "https://upload.wikimedia.org/wikipedia/commons/b/b8/Lim_Kim_San_in_the_1940s.jpg";
  var SHONAN = "https://upload.wikimedia.org/wikipedia/commons/f/fc/Street_in_Shonan.JPG";
  var FIRE = "https://upload.wikimedia.org/wikipedia/commons/3/39/ST27May1961.jpg";
  var BLOCK45 = "https://upload.wikimedia.org/wikipedia/commons/d/dd/Block_45_Stirling_Road%2C_Singapore.jpg";
  var GOH = "https://upload.wikimedia.org/wikipedia/commons/4/49/Goh_Keng_Swee%2C_1967_%283x4_crop%29.jpg";
  var WEDDING = "https://upload.wikimedia.org/wikipedia/commons/b/b4/Lim_Kim_San%2C_1940.jpg";
  var RAFFLES = "https://upload.wikimedia.org/wikipedia/commons/2/28/Raffles_College_graduates_1934.webp";
  var QUEENSTOWN = "https://upload.wikimedia.org/wikipedia/commons/5/5c/Queenstown_hdb.jpg";
  var MEMORIAL = "https://upload.wikimedia.org/wikipedia/commons/2/27/Civilian_War_Memorial%2C_Singapore-3276.jpg";

  var slides = [
    { src: LIM, type: "letterbox", zoom: [1, 1.08, 1.15], pan: ["50% 40%", "55% 50%", "60% 60%"], ease: "ease-in-out" },
    { src: RAFFLES, type: "cover", zoom: [1, 1.1, 1.18], pan: ["40% 50%", "50% 45%", "60% 40%"], ease: "ease-out" },
    { src: WEDDING, type: "letterbox", zoom: [1, 1.1, 1.2], pan: ["50% 30%", "50% 50%", "50% 70%"], ease: "ease-in" },
    { src: SHONAN, type: "cover", zoom: [1, 1.12, 1.2], pan: ["30% 50%", "50% 50%", "70% 50%"], ease: "linear" },
    { src: MEMORIAL, type: "letterbox", zoom: [1.15, 1.06, 1], pan: ["60% 30%", "50% 50%", "40% 70%"], ease: "ease-in-out" },
    { src: LIM, type: "letterbox", zoom: [1, 1.1, 1.16], pan: ["45% 60%", "50% 50%", "55% 40%"], ease: "ease-out" },
    { src: BLOCK45, type: "cover", zoom: [1, 1.08, 1.15], pan: ["35% 40%", "50% 50%", "65% 60%"], ease: "ease-in" },
    { src: BLOCK45, type: "cover", zoom: [1.15, 1.06, 1], pan: ["65% 60%", "50% 50%", "35% 40%"], ease: "ease-in-out" },
    { src: FIRE, type: "letterbox", zoom: [1, 1.04, 1.08], pan: ["50% 30%", "50% 50%", "50% 70%"], ease: "linear" },
    { src: QUEENSTOWN, type: "cover", zoom: [1, 1.1, 1.18], pan: ["40% 60%", "50% 45%", "60% 30%"], ease: "ease-out" },
    { src: BLOCK45, type: "cover", zoom: [1, 1.1, 1.17], pan: ["50% 50%", "55% 45%", "60% 40%"], ease: "ease-in-out" },
    { src: LIM, type: "letterbox", zoom: [1, 1.09, 1.16], pan: ["55% 45%", "50% 50%", "45% 55%"], ease: "ease-in" },
    { src: LIM, type: "letterbox", zoom: [1.14, 1.06, 1], pan: ["40% 55%", "50% 50%", "60% 45%"], ease: "ease-out" },
    { src: GOH, type: "letterbox", zoom: [1, 1.1, 1.18], pan: ["50% 35%", "50% 50%", "50% 65%"], ease: "ease-in-out" },
    { src: GOH, type: "letterbox", zoom: [1.16, 1.06, 1], pan: ["60% 60%", "50% 50%", "40% 40%"], ease: "ease-in" },
    { src: GOH, type: "letterbox", zoom: [1, 1.08, 1.15], pan: ["45% 40%", "50% 50%", "55% 60%"], ease: "ease-out" },
    { src: GOH, type: "letterbox", zoom: [1, 1.12, 1.2], pan: ["50% 50%", "55% 45%", "60% 40%"], ease: "linear" },
    { src: LIM, type: "letterbox", zoom: [1, 1.1, 1.17], pan: ["60% 40%", "50% 50%", "40% 60%"], ease: "ease-in-out" },
    { src: QUEENSTOWN, type: "cover", zoom: [1.15, 1.06, 1], pan: ["35% 55%", "50% 50%", "65% 45%"], ease: "ease-out" },
    { src: LIM, type: "letterbox", zoom: [1, 1.09, 1.16], pan: ["50% 60%", "50% 50%", "50% 40%"], ease: "ease-in" },
    { src: BLOCK45, type: "cover", zoom: [1, 1.1, 1.18], pan: ["45% 50%", "50% 50%", "55% 50%"], ease: "ease-out" },
    { src: MEMORIAL, type: "letterbox", zoom: [1, 1.12, 1.2], pan: ["40% 65%", "50% 50%", "60% 35%"], ease: "ease-in-out" }
  ];

  // Real per-sentence timestamps captured for free from Kokoro TTS's own
  // per-sentence synthesis (see scripts/generate_narration.py) - drives
  // captions independently of image switching, in exact sync with speech.
  var sentences = [{"text":"Tortured by the Kempeitai, He Went On to Build a Nation's Homes","offset_s":0.0,"duration_s":4.1},{"text":"Sometime during the Japanese Occupation of Singapore, the Kempeitai picked up a young Peranakan businessman named Lim Kim San — not once, but twice — and tortured him on the strength of two accusations that couldn't both be true: that he was a communist, and that he was a British sympathiser.","offset_s":4.1,"duration_s":18.4},{"text":"Two decades later, that same man would be the one Singaporeans called \"Mr HDB,\" credited with solving the housing crisis of a newly independent nation.","offset_s":22.5,"duration_s":10.7},{"text":"Almost nobody remembers the part in between.","offset_s":33.2,"duration_s":3.225},{"text":"Lim was born in Singapore in 1916, the eldest of six children in a Peranakan Chinese family; his father, Lim Choon Huat, was a businessman in shipping and commodities.","offset_s":36.425,"duration_s":12.375},{"text":"He was educated at Oldham Hall School and the Anglo-Chinese School before going on to Raffles College to study economics, graduating in 1939.","offset_s":48.8,"duration_s":10.2},{"text":"It was there that he struck up a friendship with a fellow student named Goh Keng Swee — a connection that would matter far more to Singapore's history than either of them could have guessed at the time.","offset_s":59.0,"duration_s":11.425},{"text":"In February 1940 Lim married Pang Gek Kim in a traditional Peranakan wedding, and afterward went to work managing his father-in-law's businesses: a sago factory, along with interests in diamonds, jewellery, pawnshops and banking.","offset_s":70.425,"duration_s":15.65},{"text":"Then came the war.","offset_s":86.075,"duration_s":1.725},{"text":"When the Japanese occupied Singapore in 1942, the secret military police detained and tortured Lim on suspicion of being both pro-communist and pro-British — contradictory labels that reflected how broadly the Kempeitai's suspicion could fall on Chinese businessmen with the wrong connections, real or imagined.","offset_s":87.8,"duration_s":21.15},{"text":"Decades later, Lim reflected that those who survived the \"horror and the brutality\" of the occupation would never forget it, and that the experience had politicised his entire generation, leaving them determined to \"never let our fate be decided by others.\"","offset_s":108.95,"duration_s":16.05},{"text":"After the war, though, he didn't go anywhere near politics.","offset_s":125.0,"duration_s":3.675},{"text":"He went back to business, working to make up for years lost to the occupation, and by 36 he'd made his first million using a machine that produced sago pearls more cheaply than anyone else in the trade.","offset_s":128.675,"duration_s":12.725},{"text":"He stayed on the sidelines of the People's Action Party even as it rose — friendly with its leaders, quietly supportive, but unwilling to stand as a candidate in the pivotal 1959 election that first brought the PAP to power.","offset_s":141.4,"duration_s":14.575},{"text":"What he offered instead was administrative help, and in 1960 the new government took him up on it in the biggest way possible: chairman of the newly created Housing & Development Board, tasked with clearing a backlog that had left more than 400,000 people crammed into slum shophouses and squatter settlements.","offset_s":155.975,"duration_s":20.05},{"text":"Lim took the job unpaid and stayed unpaid for three years, dispensing with the Singapore Improvement Trust's careful planning process in favour of rough estimates and speed, standardising designs, and supervising private contractors instead of building directly.","offset_s":176.025,"duration_s":17.25},{"text":"When the Bukit Ho Swee fire tore through a squatter settlement in May 1961 and left roughly 16,000 people homeless overnight, it was Lim's HDB that rebuilt and rehoused them, delivering 1,200 replacement flats within four years.","offset_s":193.275,"duration_s":17.0},{"text":"By the time his three-year tenure was up, the Board had built around 26,000 flats — more than the SIT had managed in its entire 32-year history — with the satellite town of Queenstown, over 17,500 flats built as a self-contained new town with its own shops and amenities, as the flagship achievement that later HDB towns would all copy.","offset_s":210.275,"duration_s":23.35},{"text":"Singapore awarded him the Order of Temasek, its highest civilian honour, in 1962; the Philippines gave him the Ramon Magsaysay Award in 1965.","offset_s":233.625,"duration_s":11.45},{"text":"By 1963, Lee Kuan Yew had persuaded Lim to do what he'd refused in 1959: stand for office.","offset_s":245.075,"duration_s":8.025},{"text":"He won the Cairnhill seat and was made Minister for National Development, overseeing the housing programme he'd just spent three years building from scratch.","offset_s":253.1,"duration_s":9.15},{"text":"Two years later, after Singapore's abrupt 1965 separation from Malaysia, Lee moved him to Finance — and it's here that Lim's least-remembered achievement played out.","offset_s":262.25,"duration_s":11.3},{"text":"Singapore had kept sharing a common currency with Malaysia and Brunei after separation, but by mid-1966 the arrangement was falling apart: Malaysia's finance minister, Tan Siew Sin, wanted Bank Negara Malaysia to hold title over the reserves backing Singapore's share of that currency, a condition Lim refused to accept.","offset_s":273.55,"duration_s":22.125},{"text":"He flew to Kuala Lumpur in August 1966 with a formal proposal — either an independent trustee for the reserves, or a separately incorporated Singapore currency board — and when Tan rejected both, Lim held his ground: Singapore, he wrote back, \"could not be placed in a position where its reserves might be jeopardised.\"","offset_s":295.675,"duration_s":20.65},{"text":"Fittingly, it was his old Raffles College friend Goh Keng Swee, by then Defence Minister, who worked the negotiations alongside him.","offset_s":316.325,"duration_s":8.55},{"text":"On 17 August 1966 both governments announced they would issue separate currencies, effective 12 June 1967 — Singapore's second, far quieter separation from Malaysia, and one that gave the republic direct control over its own reserves for the first time. (The following year, Lim and Goh swapped portfolios again, trading Finance for Interior and Defence.)","offset_s":324.875,"duration_s":24.775},{"text":"Lim went on to hold half the seats in Cabinet over the following decade and a half — Education, Environment twice over, Communications, National Development a second time — before retiring from elected politics in 1980.","offset_s":349.65,"duration_s":14.975},{"text":"He wasn't done, though: he chaired the Port of Singapore Authority through the 1980s, ran the Monetary Authority of Singapore, later took over Singapore Press Holdings as executive chairman, and spent over a decade chairing the Council of Presidential Advisers.","offset_s":364.625,"duration_s":16.075},{"text":"He died in Singapore in July 2006, at 89, having spent six decades in public service, from the HDB's earliest years to some of the government's highest advisory posts.","offset_s":380.7,"duration_s":12.85},{"text":"Why it matters today: Every account of Lim Kim San leads with the HDB, and it's not wrong to — a fifth of Singapore's population now lives in the system he built the template for.","offset_s":393.55,"duration_s":12.05},{"text":"But the housing crisis wasn't the first emergency he'd lived through, and the currency board wasn't the last one he'd help build from nothing; both were downstream of a war that convinced an entire generation of Singaporeans that competence, not just survival, was the only insurance against ever again having their fate decided by someone else.","offset_s":405.6,"duration_s":21.025}];

  // Long sentences (some run 400+ characters / 25+ seconds) overwhelm a
  // caption card if shown whole, so split them into shorter chunks that
  // share the real sentence's timing proportionally by character count.
  function splitLongSentence(text, offset, duration) {
    var MAX = 100;
    if (text.length <= MAX) return [{ text: text, offset_s: offset, duration_s: duration }];
    var parts = text.split(/(?<=[:;])\s+/);
    var chunks = [];
    parts.forEach(function (p) {
      if (p.length <= MAX) { chunks.push(p); return; }
      var words = p.split(' ');
      var cur = '';
      words.forEach(function (w) {
        if ((cur + ' ' + w).trim().length > MAX) { chunks.push(cur.trim()); cur = w; }
        else { cur = (cur + ' ' + w).trim(); }
      });
      if (cur) chunks.push(cur.trim());
    });
    var totalChars = chunks.reduce(function (a, c) { return a + c.length; }, 0);
    var result = [];
    var t = offset;
    chunks.forEach(function (c) {
      var share = duration * (c.length / totalChars);
      result.push({ text: c, offset_s: t, duration_s: share });
      t += share;
    });
    return result;
  }
  var captionChunks = [];
  sentences.forEach(function (s) {
    captionChunks = captionChunks.concat(splitLongSentence(s.text, s.offset_s, s.duration_s));
  });

  var watchWidget = document.getElementById('watch-widget');
  var viewer = document.getElementById('watch-viewer');
  var stage = document.getElementById('watch-stage');
  var captionEl = document.getElementById('watch-caption');
  var listenAudio = document.getElementById('listen-audio');
  var watchAudio = new Audio(listenAudio.querySelector('source').src);
  watchAudio.preload = 'none';
  var playBtn = document.getElementById('watch-play');
  var progressFill = document.getElementById('watch-progress-fill');
  var progressBar = document.getElementById('watch-progress');
  var timeLabel = document.getElementById('watch-time');

  var styleEl = document.createElement('style');
  document.head.appendChild(styleEl);

  // Which slide is on screen at any given time, aligned to what the
  // narration is actually saying at that moment (real sentence offsets
  // above) rather than an even split of total duration.
  var imageSchedule = [
    { t: 0, slide: 0 },
    { t: 36.425, slide: 1 },
    { t: 70.425, slide: 2 },
    { t: 86.075, slide: 3 },
    { t: 108.95, slide: 4 },
    { t: 125.0, slide: 5 },
    { t: 155.975, slide: 6 },
    { t: 176.025, slide: 7 },
    { t: 193.275, slide: 8 },
    { t: 210.275, slide: 9 },
    { t: 233.625, slide: 10 },
    { t: 245.075, slide: 11 },
    { t: 262.25, slide: 12 },
    { t: 273.55, slide: 13 },
    { t: 295.675, slide: 14 },
    { t: 316.325, slide: 15 },
    { t: 324.875, slide: 16 },
    { t: 349.65, slide: 17 },
    { t: 364.625, slide: 18 },
    { t: 380.7, slide: 19 },
    { t: 393.55, slide: 20 },
    { t: 405.6, slide: 21 }
  ];
  var TOTAL_DURATION = 426.625;
  var slideDurations = imageSchedule.map(function (entry, i) {
    var next = i + 1 < imageSchedule.length ? imageSchedule[i + 1].t : TOTAL_DURATION;
    return next - entry.t;
  });

  var slideEls = slides.map(function (s, i) {
    var el = document.createElement('div');
    el.style.cssText = 'position:absolute;inset:0;opacity:0;transition:opacity 0.8s ease;';

    var ease = s.ease || 'linear';
    var dur = slideDurations[imageSchedule.findIndex(function (e) { return e.slide === i; })];

    if (s.type === 'letterbox') {
      var bg = document.createElement('div');
      bg.style.cssText = 'position:absolute;inset:-8%;background-size:cover;background-position:center;filter:blur(30px) brightness(0.55);background-image:url(\'' + s.src + '\');';
      bg.style.animation = 'kb' + i + ' ' + dur + 's ' + ease + ' forwards';
      var fg = document.createElement('div');
      fg.style.cssText = 'position:absolute;inset:6%;background-size:contain;background-position:center;background-repeat:no-repeat;background-image:url(\'' + s.src + '\');';
      el.appendChild(bg);
      el.appendChild(fg);
      el._animTargets = [bg];
    } else {
      var layer = document.createElement('div');
      layer.style.cssText = 'position:absolute;inset:-8%;background-size:cover;background-image:url(\'' + s.src + '\');';
      layer.style.animation = 'kb' + i + ' ' + dur + 's ' + ease + ' forwards';
      el.appendChild(layer);
      el._animTargets = [layer];
    }

    styleEl.textContent += '@keyframes kb' + i + ' { 0% { transform: scale(' + s.zoom[0] + '); background-position: ' + s.pan[0] + '; } 50% { transform: scale(' + s.zoom[1] + '); background-position: ' + s.pan[1] + '; } 100% { transform: scale(' + s.zoom[2] + '); background-position: ' + s.pan[2] + '; } }\n';
    stage.appendChild(el);
    return el;
  });

  slides.forEach(function (s) { var img = new Image(); img.src = s.src; });

  var currentIndex = -1;
  var currentSentenceIndex = -1;

  function fmtTime(t) {
    if (!isFinite(t)) return '0:00';
    var m = Math.floor(t / 60), s = Math.floor(t % 60);
    return m + ':' + (s < 10 ? '0' : '') + s;
  }

  function sentenceIndexForTime(t) {
    var idx = 0;
    for (var i = 0; i < captionChunks.length; i++) {
      if (captionChunks[i].offset_s <= t) idx = i; else break;
    }
    return idx;
  }

  function slideIndexForTime(t) {
    var idx = imageSchedule[0].slide;
    for (var i = 0; i < imageSchedule.length; i++) {
      if (imageSchedule[i].t <= t) idx = imageSchedule[i].slide; else break;
    }
    return idx;
  }

  function updateForTime(t) {
    var idx = slideIndexForTime(t);
    if (idx !== currentIndex) {
      currentIndex = idx;
      var dur = slideDurations[imageSchedule.findIndex(function (e) { return e.slide === idx; })];
      slideEls.forEach(function (el, i) {
        el.style.opacity = (i === idx) ? '1' : '0';
        if (i === idx) {
          var ease = slides[i].ease || 'linear';
          el._animTargets.forEach(function (target) {
            target.style.animation = 'none';
            void target.offsetWidth;
            target.style.animation = 'kb' + i + ' ' + dur + 's ' + ease + ' forwards';
          });
        }
      });
    }

    var sIdx = sentenceIndexForTime(t);
    if (sIdx !== currentSentenceIndex) {
      currentSentenceIndex = sIdx;
      captionEl.textContent = captionChunks[sIdx].text;
    }
  }

  function openViewer() {
    viewer.style.display = 'block';
    watchAudio.currentTime = 0;
    watchAudio.play();
  }
  function closeViewer() {
    viewer.style.display = 'none';
    watchAudio.pause();
    currentIndex = -1;
    currentSentenceIndex = -1;
    slideEls.forEach(function (el) { el.style.opacity = '0'; });
  }

  watchWidget.addEventListener('click', openViewer);
  watchWidget.addEventListener('keydown', function (e) {
    if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); openViewer(); }
  });
  document.getElementById('watch-close').addEventListener('click', closeViewer);

  watchAudio.addEventListener('loadedmetadata', function () {
    timeLabel.textContent = '0:00 / ' + fmtTime(watchAudio.duration);
  });
  watchAudio.addEventListener('timeupdate', function () {
    updateForTime(watchAudio.currentTime);
    var pct = (watchAudio.currentTime / watchAudio.duration) * 100;
    progressFill.style.width = pct + '%';
    timeLabel.textContent = fmtTime(watchAudio.currentTime) + ' / ' + fmtTime(watchAudio.duration);
  });
  watchAudio.addEventListener('ended', closeViewer);
  watchAudio.addEventListener('play', function () { playBtn.innerHTML = '&#10074;&#10074;'; });
  watchAudio.addEventListener('pause', function () { playBtn.innerHTML = '&#9654;'; });

  playBtn.addEventListener('click', function () {
    if (watchAudio.paused) watchAudio.play(); else watchAudio.pause();
  });
  progressBar.addEventListener('click', function (e) {
    var rect = progressBar.getBoundingClientRect();
    var pct = (e.clientX - rect.left) / rect.width;
    watchAudio.currentTime = pct * watchAudio.duration;
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && viewer.style.display === 'block') closeViewer();
  });
})();
</script>

![Lim Kim San, photographed in the 1940s](https://upload.wikimedia.org/wikipedia/commons/b/b8/Lim_Kim_San_in_the_1940s.jpg)

*Lim Kim San, photographed in the 1940s. (Photo: National Archives of Singapore, via Wikimedia Commons, public domain)*

Lim was born in Singapore in 1916, the eldest of six children in a Peranakan Chinese family; his father, Lim Choon Huat, was a businessman in shipping and commodities. He was educated at Oldham Hall School and the Anglo-Chinese School before going on to Raffles College to study economics, graduating in 1939. It was there that he struck up a friendship with a fellow student named Goh Keng Swee — a connection that would matter far more to Singapore's history than either of them could have guessed at the time. In February 1940 Lim married Pang Gek Kim in a traditional Peranakan wedding, and afterward went to work managing his father-in-law's businesses: a sago factory, along with interests in diamonds, jewellery, pawnshops and banking.

![A street in Shonan-to, the wartime Japanese name for Singapore, February 1943](https://upload.wikimedia.org/wikipedia/commons/f/fc/Street_in_Shonan.JPG)

*A street in Shonan-to, the wartime Japanese name for occupied Singapore, photographed in February 1943. (Photo: Mainichi Newspapers Co., from* Hakyoku e no michi */ Wikimedia Commons, public domain)*

Then came the war. When the Japanese occupied Singapore in 1942, the secret military police detained and tortured Lim on suspicion of being both pro-communist and pro-British — contradictory labels that reflected how broadly the Kempeitai's suspicion could fall on Chinese businessmen with the wrong connections, real or imagined. Decades later, Lim reflected that those who survived the "horror and the brutality" of the occupation would never forget it, and that the experience had politicised his entire generation, leaving them determined to "never let our fate be decided by others." After the war, though, he didn't go anywhere near politics. He went back to business, working to make up for years lost to the occupation, and by 36 he'd made his first million using a machine that produced sago pearls more cheaply than anyone else in the trade.

He stayed on the sidelines of the People's Action Party even as it rose — friendly with its leaders, quietly supportive, but unwilling to stand as a candidate in the pivotal 1959 election that first brought the PAP to power. What he offered instead was administrative help, and in 1960 the new government took him up on it in the biggest way possible: chairman of the newly created Housing & Development Board, tasked with clearing a backlog that had left more than 400,000 people crammed into slum shophouses and squatter settlements. Lim took the job unpaid and stayed unpaid for three years, dispensing with the Singapore Improvement Trust's careful planning process in favour of rough estimates and speed, standardising designs, and supervising private contractors instead of building directly. When the Bukit Ho Swee fire tore through a squatter settlement in May 1961 and left roughly 16,000 people homeless overnight, it was Lim's HDB that rebuilt and rehoused them, delivering 1,200 replacement flats within four years.

![The Straits Times front page, 27 May 1961, reporting on relief efforts after the Bukit Ho Swee fire](https://upload.wikimedia.org/wikipedia/commons/3/39/ST27May1961.jpg)

*The Straits Times, 27 May 1961 — "AID for FIRE VICTIMS" — two days after the Bukit Ho Swee fire, reporting the government's plan to build 12,000 low-cost flats on the razed land. (Source: The Straits Times, via NLB NewspaperSG / Wikimedia Commons. Public domain in Singapore: under the Copyright Act (Cap. 63) §96, a published edition's copyright expires if first published before 10 April 1987 — this issue is from 1961, well before that cutoff.)*

By the time his three-year tenure was up, the Board had built around 26,000 flats — more than the SIT had managed in its entire 32-year history — with the satellite town of Queenstown, over 17,500 flats built as a self-contained new town with its own shops and amenities, as the flagship achievement that later HDB towns would all copy. Singapore awarded him the Order of Temasek, its highest civilian honour, in 1962; the Philippines gave him the Ramon Magsaysay Award in 1965.

![Block 45 Stirling Road, Singapore, one of the first flats built by the HDB, photographed in 2021](https://upload.wikimedia.org/wikipedia/commons/d/dd/Block_45_Stirling_Road%2C_Singapore.jpg)

*Block 45 Stirling Road, one of the first three blocks completed by the HDB in October 1960, still standing in Queenstown as photographed in 2021. (Photo: Seloloving / Wikimedia Commons, CC BY-SA 4.0)*

<div style="float: left; max-width: 220px; margin: 0.25em 1.5em 1em 0;">
<img src="https://upload.wikimedia.org/wikipedia/commons/4/49/Goh_Keng_Swee%2C_1967_%283x4_crop%29.jpg" alt="Goh Keng Swee, photographed in 1967" style="width: 100%; display: block; border-radius: 4px;">
<em style="display: block; font-size: 0.8em; margin-top: 0.5em;">Goh Keng Swee, photographed in 1967 — the same year Singapore's separate currency took effect. Lim's Raffles College friend and negotiating partner, by then Defence Minister. (Photo: Australian News and Information Bureau / Wikimedia Commons, public domain — Australian Crown Copyright, expired)</em>
</div>

By 1963, Lee Kuan Yew had persuaded Lim to do what he'd refused in 1959: stand for office. He won the Cairnhill seat and was made Minister for National Development, overseeing the housing programme he'd just spent three years building from scratch. Two years later, after Singapore's abrupt 1965 separation from Malaysia, Lee moved him to Finance — and it's here that Lim's least-remembered achievement played out. Singapore had kept sharing a common currency with Malaysia and Brunei after separation, but by mid-1966 the arrangement was falling apart: Malaysia's finance minister, Tan Siew Sin, wanted Bank Negara Malaysia to hold title over the reserves backing Singapore's share of that currency, a condition Lim refused to accept. He flew to Kuala Lumpur in August 1966 with a formal proposal — either an independent trustee for the reserves, or a separately incorporated Singapore currency board — and when Tan rejected both, Lim held his ground: Singapore, he wrote back, "could not be placed in a position where its reserves might be jeopardised." Fittingly, it was his old Raffles College friend Goh Keng Swee, by then Defence Minister, who worked the negotiations alongside him. On 17 August 1966 both governments announced they would issue separate currencies, effective 12 June 1967 — Singapore's second, far quieter separation from Malaysia, and one that gave the republic direct control over its own reserves for the first time. (The following year, Lim and Goh swapped portfolios again, trading Finance for Interior and Defence.)

<div style="clear: both;"></div>

Lim went on to hold half the seats in Cabinet over the following decade and a half — Education, Environment twice over, Communications, National Development a second time — before retiring from elected politics in 1980. He wasn't done, though: he chaired the Port of Singapore Authority through the 1980s, ran the Monetary Authority of Singapore, later took over Singapore Press Holdings as executive chairman, and spent over a decade chairing the Council of Presidential Advisers. He died in Singapore in July 2006, at 89, having spent six decades in public service, from the HDB's earliest years to some of the government's highest advisory posts. [See four more historical photos related to this post →](/gallery/lim-kim-san-kempeitai-hdb-currency-separation/)

**Why it matters today:** Every account of Lim Kim San leads with the HDB, and it's not wrong to — a fifth of Singapore's population now lives in the system he built the template for. But the housing crisis wasn't the first emergency he'd lived through, and the currency board wasn't the last one he'd help build from nothing; both were downstream of a war that convinced an entire generation of Singaporeans that competence, not just survival, was the only insurance against ever again having their fate decided by someone else.

---

**Sources:**
- [Lim Kim San — Wikipedia](https://en.wikipedia.org/wiki/Lim_Kim_San)
- [Lim Kim San — Biographical Notes, ISEAS Library](https://www.iseas.edu.sg/wp-content/uploads/2021/12/Lim-Kim-San-Biographical-Notes.pdf)
- [Lim Kim San — Roots.gov.sg](https://www.roots.gov.sg/stories-landing/stories/lim-kim-san/story)
- [Lim Kim San — NLB Infopedia](https://eresources.nlb.gov.sg/infopedia/articles/SIP_645_2005-01-11.html)
- [Why Singapore rejected a common currency with Malaysia — CashChanger Stories](https://stories.cashchanger.co/why-singapore-rejected-a-common-currency-with-malaysia/)
- [Bukit Ho Swee fire — Wikipedia](https://en.wikipedia.org/wiki/Bukit_Ho_Swee_fire)
- [File:Lim Kim San in the 1940s.jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Lim_Kim_San_in_the_1940s.jpg)
- [File:ST27May1961.jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:ST27May1961.jpg)
- [File:Goh Keng Swee, 1967 (3x4 crop).jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Goh_Keng_Swee,_1967_(3x4_crop).jpg)
- [File:Street in Shonan.JPG — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Street_in_Shonan.JPG)
- [File:Block 45 Stirling Road, Singapore.jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Block_45_Stirling_Road,_Singapore.jpg)
- [File:Lim Kim San, 1940.jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Lim_Kim_San,_1940.jpg)
- [File:Raffles College graduates 1934.webp — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Raffles_College_graduates_1934.webp)
- [File:Queenstown hdb.jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Queenstown_hdb.jpg)
- [File:Civilian War Memorial, Singapore-3276.jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Civilian_War_Memorial,_Singapore-3276.jpg)

[← Back to all posts](/)
