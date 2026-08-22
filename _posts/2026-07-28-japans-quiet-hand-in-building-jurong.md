---
layout: post
title: "Japan's Quiet Hand in Building Jurong"
date: 2026-07-28 10:00:00 +0800
last_modified_at: 2026-08-22 02:00:00 +0800
categories: [history, economy]
image: https://upload.wikimedia.org/wikipedia/commons/0/04/Signs_pointing_to_Jurong_Industrial_Estate_in_Singapore_June_1964.jpg
---

In 1963, on reclaimed mudflats west of the city, Bridgestone broke ground on its first factory outside Japan — not in a friendly, familiar market, but in Singapore, barely eighteen years after Japanese troops had occupied the island and four years before Tokyo agreed to pay for it.

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
  <a href="https://youtu.be/gQEtVjZiujU" target="_blank" rel="noopener" aria-label="Watch this story as a video on YouTube" style="display: inline-flex; flex-direction: column; align-items: center; gap: 0.2em; text-decoration: none; color: inherit;">
    <span aria-hidden="true" style="display: inline-flex; align-items: center; justify-content: center; width: 2.4em; height: 2.4em; border-radius: 50%; border: 1px solid #888;">
      <svg width="1.4em" height="1.4em" viewBox="0 0 24 24" aria-hidden="true"><rect x="1" y="4" width="22" height="16" rx="5" fill="#FF0000"/><path d="M10 8.5l6 3.5-6 3.5z" fill="#fff"/></svg>
    </span>
    <span style="font-size: 0.7em; text-transform: uppercase; letter-spacing: 0.05em; opacity: 0.75;">YouTube</span>
  </a>
</div>

<audio id="listen-audio" preload="none" style="display: none;">
  <source src="/audio/japans-quiet-hand-in-building-jurong.mp3" type="audio/mpeg">
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
  var HERO = "https://upload.wikimedia.org/wikipedia/commons/0/04/Signs_pointing_to_Jurong_Industrial_Estate_in_Singapore_June_1964.jpg";
  var GOH = "https://upload.wikimedia.org/wikipedia/commons/f/f5/Goh_Keng_Swee_in_Australia%2C_1967.jpg";
  var WINSEMIUS = "https://upload.wikimedia.org/wikipedia/commons/2/2e/Albert_Winsemius_%281971%29.jpg";
  var SURRENDER1945 = "https://upload.wikimedia.org/wikipedia/commons/a/a9/Signing_of_the_Japanese_Surrender_at_Singapore%2C_1945_CF720.jpg";
  var ROADSTEAD1963 = "https://upload.wikimedia.org/wikipedia/commons/4/4e/Singapore_roadstead_1963_01.jpg";
  var TENGAH1964 = "https://upload.wikimedia.org/wikipedia/commons/c/ca/Malay_village_near_Tengah_Singapore_October_1964.jpg";
  var STPAGE = "/assets/images/straits-times-19640220-jurong-shipyard-foundation-stone.jpg";
  var STAFFQUARTERS1967 = "https://upload.wikimedia.org/wikipedia/commons/4/47/Jurong_Staff_Quarters.jpg";
  var WINDINGROAD1967 = "https://upload.wikimedia.org/wikipedia/commons/0/06/1967_-_Winding_Road_to_Jurong_Staff_Quarters.jpg";

  var slides = [
    { src: HERO, type: "cover", zoom: [1, 1.08, 1.15], pan: ["50% 45%", "50% 50%", "50% 55%"], ease: "ease-in-out" },
    { src: SURRENDER1945, type: "cover", zoom: [1, 1.09, 1.16], pan: ["35% 50%", "50% 50%", "65% 50%"], ease: "ease-out" },
    { src: ROADSTEAD1963, type: "cover", zoom: [1, 1.08, 1.15], pan: ["50% 40%", "50% 50%", "50% 60%"], ease: "ease-in-out" },
    { src: WINSEMIUS, type: "letterbox", zoom: [1, 1.06, 1.12], pan: ["50% 50%", "50% 50%", "50% 50%"], ease: "linear" },
    { src: GOH, type: "cover", zoom: [1, 1.08, 1.15], pan: ["45% 50%", "50% 50%", "55% 50%"], ease: "ease-in-out" },
    { src: TENGAH1964, type: "cover", zoom: [1.15, 1.06, 1], pan: ["55% 55%", "50% 50%", "45% 45%"], ease: "ease-in" },
    { src: HERO, type: "cover", zoom: [1.15, 1.06, 1], pan: ["55% 45%", "50% 50%", "45% 55%"], ease: "ease-in" },
    { src: STPAGE, type: "letterbox", zoom: [1, 1.06, 1.12], pan: ["50% 50%", "50% 50%", "50% 50%"], ease: "linear" },
    { src: STAFFQUARTERS1967, type: "cover", zoom: [1, 1.08, 1.15], pan: ["45% 50%", "50% 50%", "55% 50%"], ease: "ease-in-out" },
    { src: ROADSTEAD1963, type: "cover", zoom: [1.16, 1.06, 1], pan: ["65% 55%", "50% 50%", "35% 45%"], ease: "ease-in" },
    { src: SURRENDER1945, type: "cover", zoom: [1.16, 1.06, 1], pan: ["65% 45%", "50% 50%", "35% 55%"], ease: "ease-in" },
    { src: WINDINGROAD1967, type: "cover", zoom: [1, 1.08, 1.15], pan: ["50% 45%", "50% 50%", "50% 55%"], ease: "ease-in-out" },
    { src: HERO, type: "cover", zoom: [1, 1.09, 1.16], pan: ["40% 50%", "50% 50%", "60% 50%"], ease: "ease-out" },
    { src: STAFFQUARTERS1967, type: "cover", zoom: [1.15, 1.06, 1], pan: ["55% 55%", "50% 50%", "45% 45%"], ease: "ease-in" },
    { src: WINSEMIUS, type: "letterbox", zoom: [1.12, 1.06, 1], pan: ["50% 50%", "50% 50%", "50% 50%"], ease: "linear" },
    { src: HERO, type: "cover", zoom: [1, 1.09, 1.16], pan: ["50% 60%", "50% 50%", "50% 40%"], ease: "ease-in-out" }
  ];

  // Real per-sentence timestamps captured for free from Kokoro TTS's own
  // per-sentence synthesis (see scripts/generate_narration.py) - drives
  // captions independently of image switching, in exact sync with speech.
  var sentences = [{"text":"Japan's Quiet Hand in Building Jurong","offset_s":0.0,"duration_s":3.6},{"text":"In 1963, on reclaimed mudflats west of the city, Bridgestone broke ground on its first factory outside Japan — not in a friendly, familiar market, but in Singapore, barely eighteen years after Japanese troops had occupied the island and four years before Tokyo agreed to pay for it.","offset_s":3.6,"duration_s":20.1},{"text":"The louder story of Singapore's postwar relationship with Japan is the one this blog has already told: the \"blood debt\" — decades of wrangling over wartime compensation, settled in 1966-67 with a payment Tokyo insisted on calling \"economic cooperation,\" not reparations.","offset_s":23.7,"duration_s":20.3},{"text":"That fight played out in public, in parliament and in the press.","offset_s":44.0,"duration_s":4.65},{"text":"The quieter story ran underneath it, on the ground in Jurong, and it started before the loud one was even finished.","offset_s":48.65,"duration_s":8.1},{"text":"When the Economic Development Board was set up in 1961, newly self-governing Singapore had almost no industrial base.","offset_s":56.75,"duration_s":9.45},{"text":"Its economy still ran on entrepot trade.","offset_s":66.2,"duration_s":3.925},{"text":"On the advice of Albert Winsemius, a Dutch UN economist brought in to draw up a development plan, the EDB's strategy was blunt: take whatever foreign capital and technical know-how would actually come, and don't be choosy about the source.","offset_s":70.125,"duration_s":16.1},{"text":"EDB officers courted American firms like Texas Instruments and Fairchild — and Japanese manufacturers barely a generation removed from being the occupying power.","offset_s":86.225,"duration_s":12.8},{"text":"Finance minister Goh Keng Swee, who did much of the deal-making, called it pragmatism, not forgiveness: Singapore needed jobs and factories, and Japan had capital sitting idle for a market willing to take it.","offset_s":99.025,"duration_s":14.3},{"text":"Jurong — a swampy stretch of reclaimed land designated as the country's first industrial estate — is where that pragmatism took physical shape.","offset_s":113.325,"duration_s":10.45},{"text":"Jurong Shipyard, Singapore's first commercial shipyard, was incorporated in April 1963 as a joint venture between Ishikawajima-Harima Heavy Industries of Japan and the Singapore government.","offset_s":123.775,"duration_s":14.625},{"text":"Goh laid its foundation stone himself on 20 February 1964, at a ceremony The Straits Times covered across a full page the same day — EDB chairman Hon Sui Sen used the occasion to argue that \"the shipbuilding and ship repairing industry in Singapore must be expanded to meet the needs of the ever-increasing number and tonnage of ships passing through\" the port, while the yard's own board already mixed Japanese directors (Messrs Takata, Hashimoto, Sakirai, and Shinto) with Singaporean ones (Hon Sui Sen, Tan Teck Chwee, J.Y.","offset_s":138.4,"duration_s":33.1},{"text":"Pillay) from day one.","offset_s":171.5,"duration_s":2.25},{"text":"Early Singaporean shipwrights were sent to Japan for apprenticeships; Japanese engineers ran the yard floor.","offset_s":173.75,"duration_s":7.825},{"text":"The model was simple: Singapore supplied the land, the labour, and the state backing, while Japan supplied the machines and the know-how.","offset_s":181.575,"duration_s":8.8},{"text":"Bridgestone's tyre plant, which broke ground that same year, followed the same playbook on the consumer side — Singapore's first taste of large-scale Japanese industrial capital.","offset_s":190.375,"duration_s":12.325},{"text":"It ran for seventeen years, closing in 1980 once the government judged the local tyre industry strong enough to survive without tariff protection.","offset_s":202.7,"duration_s":11.0},{"text":"None of this waited for Tokyo and Singapore to resolve the blood debt.","offset_s":213.7,"duration_s":5.25},{"text":"If anything, it made the political settlement easier: by the time the two governments sat down to negotiate compensation in the mid-1960s, Japanese firms were already Singapore's business partners, not just its former occupiers.","offset_s":218.95,"duration_s":15.775},{"text":"Japan's insistence on calling the 1967 settlement \"economic cooperation\" — a label Singapore's negotiators resented — reads differently against that backdrop.","offset_s":234.725,"duration_s":12.85},{"text":"It wasn't just face-saving.","offset_s":247.575,"duration_s":2.675},{"text":"The two countries were already knee-deep in exactly that kind of cooperation, and had been for years.","offset_s":250.25,"duration_s":7.125},{"text":"Jurong Shipyard is a Sembcorp Marine yard today, its Japanese joint-venture origins reduced to a line in corporate histories.","offset_s":257.375,"duration_s":9.725},{"text":"The Bridgestone plant is long gone.","offset_s":267.1,"duration_s":3.175},{"text":"But the Jurong template — court whoever has the capital and expertise, let the politics catch up later — became the EDB's playbook for decades, applied just as readily to American, European, and later Chinese investment.","offset_s":270.275,"duration_s":15.425},{"text":"Japan was just the test case that proved it could work, even under the worst possible historical conditions.","offset_s":285.7,"duration_s":7.925},{"text":"Why it matters today: Singapore's economic development is usually told as a story of Lee Kuan Yew's vision and Winsemius's advice.","offset_s":293.625,"duration_s":10.15},{"text":"The fact that some of the earliest capital came from wartime Japan — years before the two countries formally made peace — is a reminder that Singapore's \"pragmatism over sentiment\" reputation started paying off almost immediately, on the most sensitive relationship it could have chosen.","offset_s":303.775,"duration_s":18.85}];;

  var MAX_CHARS = 100;
  function splitLongSentence(text, offset, duration) {
    if (text.length <= MAX_CHARS) return [{ text: text, offset_s: offset, duration_s: duration }];
    var parts = text.split(/(?<=[:;])\s+/);
    var chunks = [];
    parts.forEach(function (p) {
      if (p.length <= MAX_CHARS) { chunks.push(p); return; }
      var words = p.split(' ');
      var cur = '';
      words.forEach(function (w) {
        if ((cur + ' ' + w).trim().length > MAX_CHARS) {
          chunks.push(cur.trim());
          cur = w;
        } else {
          cur = (cur + ' ' + w).trim();
        }
      });
      if (cur) chunks.push(cur.trim());
    });
    var totalChars = chunks.reduce(function (a, c) { return a + c.length; }, 0);
    var t = offset;
    return chunks.map(function (c) {
      var share = duration * (c.length / totalChars);
      var entry = { text: c, offset_s: t, duration_s: share };
      t += share;
      return entry;
    });
  }

  var captionChunks = [];
  sentences.forEach(function (s) {
    captionChunks = captionChunks.concat(splitLongSentence(s.text, s.offset_s, s.duration_s));
  });

  var imageSchedule = [
    { t: 0, slide: 0 }, { t: 23.7, slide: 1 }, { t: 48.65, slide: 2 }, { t: 70.125, slide: 3 },
    { t: 86.225, slide: 4 }, { t: 113.325, slide: 5 }, { t: 123.775, slide: 6 }, { t: 138.4, slide: 7 },
    { t: 173.75, slide: 8 }, { t: 190.375, slide: 9 }, { t: 213.7, slide: 10 }, { t: 247.575, slide: 11 },
    { t: 257.375, slide: 12 }, { t: 270.275, slide: 13 }, { t: 293.625, slide: 14 }, { t: 303.775, slide: 15 }
  ];
  var TOTAL_DURATION = 322.625;
  var slideDurations = imageSchedule.map(function (entry, i) {
    var next = imageSchedule[i + 1];
    return (next ? next.t : TOTAL_DURATION) - entry.t;
  });

  var viewer = document.getElementById('watch-viewer');
  var stage = document.getElementById('watch-stage');
  var captionEl = document.getElementById('watch-caption');
  var closeBtn = document.getElementById('watch-close');
  var playBtn = document.getElementById('watch-play');
  var progress = document.getElementById('watch-progress');
  var progressFill = document.getElementById('watch-progress-fill');
  var timeEl = document.getElementById('watch-time');
  var watchWidget = document.getElementById('watch-widget');
  var listenAudio = document.getElementById('listen-audio');
  var watchAudio = new Audio(listenAudio.querySelector('source').src);
  watchAudio.preload = 'none';

  var styleEl = document.createElement('style');
  document.head.appendChild(styleEl);

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

  function slideIndexForTime(t) {
    var idx = 0;
    for (var i = 0; i < imageSchedule.length; i++) {
      if (imageSchedule[i].t <= t) idx = imageSchedule[i].slide; else break;
    }
    return idx;
  }

  function sentenceIndexForTime(t) {
    var idx = 0;
    for (var i = 0; i < captionChunks.length; i++) {
      if (captionChunks[i].offset_s <= t) idx = i; else break;
    }
    return idx;
  }

  function updateForTime(t) {
    var sIdx = slideIndexForTime(t);
    if (sIdx !== currentIndex) {
      if (currentIndex >= 0) slideEls[currentIndex].style.opacity = '0';
      slideEls[sIdx].style.opacity = '1';
      currentIndex = sIdx;
    }
    var cIdx = sentenceIndexForTime(t);
    if (cIdx !== currentSentenceIndex) {
      captionEl.textContent = captionChunks[cIdx].text;
      currentSentenceIndex = cIdx;
    }
    var pct = Math.min(100, (t / TOTAL_DURATION) * 100);
    progressFill.style.width = pct + '%';
    timeEl.textContent = fmtTime(t) + ' / ' + fmtTime(TOTAL_DURATION);
  }

  function openViewer() {
    viewer.style.display = 'block';
    currentIndex = -1;
    currentSentenceIndex = -1;
    slideEls.forEach(function (el) { el.style.opacity = '0'; });
    watchAudio.currentTime = 0;
    updateForTime(0);
    watchAudio.play();
  }

  function closeViewer() {
    viewer.style.display = 'none';
    watchAudio.pause();
  }

  watchWidget.addEventListener('click', openViewer);
  watchWidget.addEventListener('keydown', function (e) {
    if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); openViewer(); }
  });
  closeBtn.addEventListener('click', closeViewer);
  playBtn.addEventListener('click', function () {
    if (watchAudio.paused) watchAudio.play(); else watchAudio.pause();
  });
  watchAudio.addEventListener('play', function () { playBtn.innerHTML = '&#10074;&#10074;'; });
  watchAudio.addEventListener('pause', function () { playBtn.innerHTML = '&#9654;'; });
  watchAudio.addEventListener('timeupdate', function () { updateForTime(watchAudio.currentTime); });
  watchAudio.addEventListener('ended', closeViewer);
  progress.addEventListener('click', function (e) {
    var rect = progress.getBoundingClientRect();
    var pct = (e.clientX - rect.left) / rect.width;
    watchAudio.currentTime = pct * TOTAL_DURATION;
  });
})();
</script>

<img src="https://upload.wikimedia.org/wikipedia/commons/0/04/Signs_pointing_to_Jurong_Industrial_Estate_in_Singapore_June_1964.jpg" alt="Directional signs pointing to Jurong Industrial Estate, Singapore, June 1964" style="width:100%; max-width:700px; display:block; margin:0 auto;">

*Signs pointing to Jurong Industrial Estate, Singapore, June 1964. Photo by [Don Christie](https://commons.wikimedia.org/wiki/File:Signs_pointing_to_Jurong_Industrial_Estate_in_Singapore_June_1964.jpg), licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.en).*

The louder story of Singapore's postwar relationship with Japan is the one this blog has already told: the "[blood debt](/2026/07/18/four-chopsticks-blood-debt-singapore-japan/)" — decades of wrangling over wartime compensation, settled in 1966-67 with a payment Tokyo insisted on calling "economic cooperation," not reparations. That fight played out in public, in parliament and in the press.

The quieter story ran underneath it, on the ground in Jurong, and it started before the loud one was even finished.

<div style="float: left; max-width: 280px; width: 45%; margin: 0.25em 1.5em 1em 0;">
<img src="https://upload.wikimedia.org/wikipedia/commons/f/f5/Goh_Keng_Swee_in_Australia%2C_1967.jpg" alt="Goh Keng Swee in 1967" style="width: 100%; display: block; border-radius: 4px;">
<em style="display: block; font-size: 0.8em; margin-top: 0.5em;">Goh Keng Swee, Singapore's finance minister and chief architect of its industrialisation drive, pictured on a visit to Australia in 1967. (Photo: J. Crowther, Australian News and Information Bureau / Wikimedia Commons, public domain)</em>
</div>

<div style="float: right; max-width: 220px; margin: 0.25em 0 1em 1.5em;">
<img src="https://upload.wikimedia.org/wikipedia/commons/2/2e/Albert_Winsemius_%281971%29.jpg" alt="Albert Winsemius, photographed in 1971" style="width: 100%; display: block; border-radius: 4px;">
<em style="display: block; font-size: 0.8em; margin-top: 0.5em;">Albert Winsemius, the Dutch economist whose 1961 development plan set the EDB's original "take whatever capital and know-how will come" strategy — photographed in 1971 at an unrelated press conference in the Netherlands. (Photo: Bert Verhoeff / Anefo, Wikimedia Commons, CC BY-SA 3.0 NL)</em>
</div>

When the Economic Development Board was set up in 1961, newly self-governing Singapore had almost no industrial base. Its economy still ran on entrepot trade. On the advice of Albert Winsemius, a Dutch UN economist brought in to draw up a development plan, the EDB's strategy was blunt: take whatever foreign capital and technical know-how would actually come, and don't be choosy about the source. EDB officers courted American firms like Texas Instruments and Fairchild — and Japanese manufacturers barely a generation removed from being the occupying power. Finance minister Goh Keng Swee, who did much of the deal-making, called it pragmatism, not forgiveness: Singapore needed jobs and factories, and Japan had capital sitting idle for a market willing to take it.

<div style="clear: both;"></div>

Jurong — a swampy stretch of reclaimed land designated as the country's first industrial estate — is where that pragmatism took physical shape. Jurong Shipyard, Singapore's first commercial shipyard, was incorporated in April 1963 as a joint venture between Ishikawajima-Harima Heavy Industries of Japan and the Singapore government. Goh laid its foundation stone himself on 20 February 1964, at a ceremony The Straits Times covered across a full page the same day — EDB chairman Hon Sui Sen used the occasion to argue that "the shipbuilding and ship repairing industry in Singapore must be expanded to meet the needs of the ever-increasing number and tonnage of ships passing through" the port, while the yard's own board already mixed Japanese directors (Messrs Takata, Hashimoto, Sakirai, and Shinto) with Singaporean ones (Hon Sui Sen, Tan Teck Chwee, J.Y. Pillay) from day one. Early Singaporean shipwrights were sent to Japan for apprenticeships; Japanese engineers ran the yard floor. The model was simple: Singapore supplied the land, the labour, and the state backing, while Japan supplied the machines and the know-how.

<img src="/assets/images/straits-times-19640220-jurong-shipyard-foundation-stone.jpg" alt="The Straits Times, 20 February 1964, page 8, covering the Jurong Shipyard foundation-stone ceremony" style="width:100%; max-width:500px; display:block; margin:0 auto;">

*The Straits Times, 20 February 1964, page 8 — full coverage of the Jurong Shipyard foundation-stone ceremony, including a "bird's eye view" rendering of the planned yard and a photo of its floating dock, towed in from Japan. Pre-1987 Singapore newspaper editions are public domain in their page layout under the Copyright Act (Cap. 63 §96); this scan is reproduced from NLB's NewspaperSG archive while awaiting a clean copy from SPH Media. (The Straits Times / SPH Media, via NewspaperSG, National Library Board)*

Bridgestone's tyre plant, which broke ground that same year, followed the same playbook on the consumer side — Singapore's first taste of large-scale Japanese industrial capital. It ran for seventeen years, closing in 1980 once the government judged the local tyre industry strong enough to survive without tariff protection.

None of this waited for Tokyo and Singapore to resolve the blood debt. If anything, it made the political settlement easier: by the time the two governments sat down to negotiate compensation in the mid-1960s, Japanese firms were already Singapore's business partners, not just its former occupiers. Japan's insistence on calling the 1967 settlement "economic cooperation" — a label Singapore's negotiators resented — reads differently against that backdrop. It wasn't just face-saving. The two countries were already knee-deep in exactly that kind of cooperation, and had been for years.

Jurong Shipyard is a Sembcorp Marine yard today, its Japanese joint-venture origins reduced to a line in corporate histories. The Bridgestone plant is long gone. But the Jurong template — court whoever has the capital and expertise, let the politics catch up later — became the EDB's playbook for decades, applied just as readily to American, European, and later Chinese investment. Japan was just the test case that proved it could work, even under the worst possible historical conditions. [See five more historical photos related to this post →](/gallery/japans-quiet-hand-in-building-jurong/)

**Why it matters today:** Singapore's economic development is usually told as a story of Lee Kuan Yew's vision and Winsemius's advice. The fact that some of the earliest capital came from wartime Japan — years before the two countries formally made peace — is a reminder that Singapore's "pragmatism over sentiment" reputation started paying off almost immediately, on the most sensitive relationship it could have chosen.

---

**Sources**

- [Made in Singapore: 60 years of manufacturing — Singapore EDB](https://www.edb.gov.sg/en/business-insights/insights/made-in-singapore-60-years-of-manufacturing.html)
- [Jurong Industrial Estate — Roots.gov.sg](https://www.roots.gov.sg/stories-landing/stories/jurong-industrial-estate/story)
- [What is the Singapore Economic Development Board? — JC History Tuition](https://www.jchistorytuition.com.sg/what-is-the-singapore-economic-development-board/)
- [History of Bridgestone Corporation — FundingUniverse](https://www.fundinguniverse.com/company-histories/bridgestone-corporation-history/)
- [Bridgestone History — Bridgestone Singapore](https://www.bridgestone.com.sg/en/about/who-we-are)
- [Speech by DPM Lee Hsien Loong at the Jurong Shipyard National Day Observance Ceremony, 2002 — National Archives of Singapore](https://www.nas.gov.sg/archivesonline/data/pdfdoc/2002081002.htm)
- [Tokyo kept war redress out of '67 Singapore accord title — The Japan Times](https://www.japantimes.co.jp/news/2003/12/25/national/tokyo-kept-war-redress-out-of-67-singapore-accord-title/)
- [Albert Winsemius — Wikipedia](https://en.wikipedia.org/wiki/Albert_Winsemius)
- [File: Albert Winsemius (1971).jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Albert_Winsemius_(1971).jpg)
- [File: Signs pointing to Jurong Industrial Estate in Singapore June 1964.jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Signs_pointing_to_Jurong_Industrial_Estate_in_Singapore_June_1964.jpg)
- [File: Goh Keng Swee in Australia, 1967.jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Goh_Keng_Swee_in_Australia,_1967.jpg)
- [File: Signing of the Japanese Surrender at Singapore, 1945 CF720.jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Signing_of_the_Japanese_Surrender_at_Singapore,_1945_CF720.jpg)
- [File: Singapore roadstead 1963 01.jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Singapore_roadstead_1963_01.jpg)
- [File: Malay village near Tengah Singapore October 1964.jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Malay_village_near_Tengah_Singapore_October_1964.jpg)
- [File: 1967 - Winding Road to Jurong Staff Quarters.jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:1967_-_Winding_Road_to_Jurong_Staff_Quarters.jpg)
- [File: Jurong Staff Quarters.jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Jurong_Staff_Quarters.jpg)
- [The Straits Times, 20 February 1964 — NewspaperSG, National Library Board](https://eresources.nlb.gov.sg/newspapers/digitised/issue/straitstimes19640220-1)

[← Back to all posts](/)
