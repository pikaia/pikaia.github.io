---
layout: post
title: "The Largest Japanese Cemetery in Southeast Asia Began as a Grave for Trafficked Women"
date: 2026-08-05 14:00:00 +0800
last_modified_at: 2026-08-21 22:30:00 +0800
categories: [history, world-war-two]
image: https://upload.wikimedia.org/wikipedia/commons/6/6c/Japanese_Cemetery_Park.jpg
---

Walk into the Japanese Cemetery Park in Hougang today and the oldest graves aren't soldiers or merchants — they belong to Japanese women trafficked into Singapore's brothels a century and a half ago. The cemetery holds 910 tombstones, and by most accounts close to half of them mark the graves of *karayuki-san*: girls sold or lured out of impoverished Japanese fishing villages, shipped to Singapore, and put to work on the same streets — Bugis, Malay, Hylam and Malabar — [covered in an earlier post about Bugis Street](/2026/08/05/bugis-street-before-redevelopment/). The cemetery's own founding is stranger still: it exists because a brothel keeper paid for it.

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
  <a href="https://youtu.be/kgXMXJctYrU" target="_blank" rel="noopener" aria-label="Watch this story as a video on YouTube" style="display: inline-flex; flex-direction: column; align-items: center; gap: 0.2em; text-decoration: none; color: inherit;">
    <span aria-hidden="true" style="display: inline-flex; align-items: center; justify-content: center; width: 2.4em; height: 2.4em; border-radius: 50%; border: 1px solid #888;">
      <svg width="1.4em" height="1.4em" viewBox="0 0 24 24" aria-hidden="true"><rect x="1" y="4" width="22" height="16" rx="5" fill="#FF0000"/><path d="M10 8.5l6 3.5-6 3.5z" fill="#fff"/></svg>
    </span>
    <span style="font-size: 0.7em; text-transform: uppercase; letter-spacing: 0.05em; opacity: 0.75;">YouTube</span>
  </a>
</div>

<audio id="listen-audio" preload="none" style="display: none;">
  <source src="/audio/japanese-cemetery-park-karayuki-san.mp3" type="audio/mpeg">
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
  var HERO = "https://upload.wikimedia.org/wikipedia/commons/6/6c/Japanese_Cemetery_Park.jpg";
  var CEM1 = "https://upload.wikimedia.org/wikipedia/commons/1/12/Japanese_Cemetery_Park_1.jpg";
  var LOCATOR = "/assets/images/osm-japanese-cemetery-park-location.png";
  var KARAYUKI = "https://upload.wikimedia.org/wikipedia/commons/9/9e/Karayukisan_in_Saigon.JPG";
  var OTOKICHI_PORTRAIT = "https://upload.wikimedia.org/wikipedia/commons/7/74/Otokichi.jpg";
  var OTOKICHI_GRAVE = "https://upload.wikimedia.org/wikipedia/commons/4/4f/Yamamoto_Otokichi_memorial%2C_Japanese_Cemetery_Park%2C_Singapore_-_20070526.jpg";
  var WARMEM = "https://upload.wikimedia.org/wikipedia/commons/e/ea/Japanese_war_memorial%2C_Japanese_Cemetery_Park%2C_Singapore_-_20070526.jpg";
  var TERAUCHI_PORTRAIT = "https://upload.wikimedia.org/wikipedia/commons/8/83/General_Hisaichi_Terauchi%2C_Djawa_Baroe%2C_Vol._1%2C_Iss._13_%281943-07-01%29%2C_p11.jpg";
  var TERAUCHI_GRAVE = "https://upload.wikimedia.org/wikipedia/commons/5/59/Hisaichi_Terauchi_memorial%2C_Japanese_Cemetery_Park%2C_Singapore_-_20070526.jpg";
  var PRAYERHALL = "https://upload.wikimedia.org/wikipedia/commons/b/bf/Prayer_hall%2C_Japanese_Cemetery_Park%2C_Singapore_-_20070526.jpg";
  var CARETAKER = "https://upload.wikimedia.org/wikipedia/commons/a/a4/Caretaker%27s_quarters%2C_Japanese_Cemetery_Park%2C_Singapore.jpg";

  var slides = [
    { src: HERO, type: "cover", zoom: [1, 1.08, 1.15], pan: ["50% 45%", "50% 50%", "50% 55%"], ease: "ease-in-out" },
    { src: CEM1, type: "cover", zoom: [1, 1.09, 1.16], pan: ["35% 50%", "50% 50%", "65% 50%"], ease: "ease-out" },
    { src: LOCATOR, type: "cover", zoom: [1, 1.06, 1.12], pan: ["50% 50%", "48% 50%", "46% 50%"], ease: "linear" },
    { src: KARAYUKI, type: "letterbox", zoom: [1, 1.06, 1.12], pan: ["45% 50%", "50% 50%", "55% 50%"], ease: "ease-in-out" },
    { src: KARAYUKI, type: "letterbox", zoom: [1.12, 1.06, 1], pan: ["55% 50%", "50% 50%", "45% 50%"], ease: "ease-in" },
    { src: CEM1, type: "cover", zoom: [1.16, 1.06, 1], pan: ["65% 55%", "50% 50%", "35% 45%"], ease: "ease-in" },
    { src: CEM1, type: "cover", zoom: [1, 1.1, 1.18], pan: ["50% 35%", "50% 50%", "50% 65%"], ease: "ease-out" },
    { src: HERO, type: "cover", zoom: [1.15, 1.06, 1], pan: ["45% 55%", "50% 50%", "55% 45%"], ease: "ease-in" },
    { src: KARAYUKI, type: "letterbox", zoom: [1, 1.08, 1.15], pan: ["50% 50%", "50% 50%", "50% 50%"], ease: "linear" },
    { src: PRAYERHALL, type: "cover", zoom: [1, 1.08, 1.15], pan: ["50% 45%", "50% 50%", "50% 55%"], ease: "ease-in-out" },
    { src: OTOKICHI_PORTRAIT, type: "letterbox", zoom: [1, 1.06, 1.12], pan: ["50% 50%", "50% 50%", "50% 50%"], ease: "linear" },
    { src: OTOKICHI_GRAVE, type: "cover", zoom: [1, 1.09, 1.16], pan: ["40% 50%", "50% 50%", "60% 50%"], ease: "ease-out" },
    { src: WARMEM, type: "cover", zoom: [1, 1.1, 1.18], pan: ["50% 40%", "50% 50%", "50% 60%"], ease: "ease-out" },
    { src: WARMEM, type: "cover", zoom: [1.18, 1.09, 1], pan: ["60% 45%", "50% 50%", "40% 55%"], ease: "ease-in" },
    { src: TERAUCHI_PORTRAIT, type: "letterbox", zoom: [1, 1.06, 1.12], pan: ["50% 50%", "50% 50%", "50% 50%"], ease: "linear" },
    { src: CARETAKER, type: "cover", zoom: [1, 1.08, 1.15], pan: ["45% 50%", "50% 50%", "55% 50%"], ease: "ease-in-out" },
    { src: TERAUCHI_GRAVE, type: "letterbox", zoom: [1, 1.06, 1.12], pan: ["50% 50%", "50% 50%", "50% 50%"], ease: "linear" },
    { src: HERO, type: "cover", zoom: [1, 1.09, 1.16], pan: ["50% 60%", "50% 50%", "50% 40%"], ease: "ease-in-out" }
  ];

  // Real per-sentence timestamps captured for free from Kokoro TTS's own
  // per-sentence synthesis (see scripts/generate_narration.py) - drives
  // captions independently of image switching, in exact sync with speech.
  var sentences = [{"text":"The Largest Japanese Cemetery in Southeast Asia Began as a Grave for Trafficked Women","offset_s":0.0,"duration_s":6.3},{"text":"Walk into the Japanese Cemetery Park in Hougang today and the oldest graves aren't soldiers or merchants — they belong to Japanese women trafficked into Singapore's brothels a century and a half ago.","offset_s":6.3,"duration_s":13.725},{"text":"The cemetery holds 910 tombstones, and by most accounts close to half of them mark the graves of *karayuki-san*: girls sold or lured out of impoverished Japanese fishing villages, shipped to Singapore, and put to work on the same streets — Bugis, Malay, Hylam and Malabar — covered in an earlier post about Bugis Street.","offset_s":20.025,"duration_s":22.125},{"text":"The cemetery's own founding is stranger still: it exists because a brothel keeper paid for it.","offset_s":42.15,"duration_s":7.05},{"text":"Karayuki-san — literally \"one who has gone abroad\" — were mostly girls from Amakusa and Shimabara, two of the poorest, most volcanic corners of Kyushu, sold by their own families or lured by brokers known as *zegen* who promised factory work overseas and delivered them instead to brothels.","offset_s":49.2,"duration_s":20.15},{"text":"Some were smuggled out hidden in ships' holds; contemporary accounts describe girls suffocating or starving during the crossing.","offset_s":69.35,"duration_s":8.6},{"text":"Singapore's Japanese-run brothel district — concentrated along Malay, Malabar, Hylam and Bugis Streets — grew from about 14 women in two brothels in 1877 to an officially recorded 633 women in 109 brothels by 1905, peaking at roughly 2,086 Japanese sex workers in 1906.","offset_s":77.95,"duration_s":23.4},{"text":"The real total, including unlicensed workers, was almost certainly higher.","offset_s":101.35,"duration_s":5.7},{"text":"The cemetery exists because of that trade, not despite it.","offset_s":107.05,"duration_s":4.525},{"text":"In 1891, three Japanese brothel keepers — Futaki Takajiro, Shibuya Ginji and Nakagawa Kikuzo — petitioned Singapore's colonial government for land to bury destitute karayuki-san, who until then had been buried informally or not at all.","offset_s":111.575,"duration_s":18.15},{"text":"Futaki donated six acres from his own rubber plantation; the government added roughly another acre of public land.","offset_s":129.725,"duration_s":9.05},{"text":"Most of the karayuki-san graves are modest granite pillars, plainer than the elaborate monuments built later for wealthier community members — and many were left deliberately unmarked, to spare families back in Japan the shame of a daughter's profession.","offset_s":138.775,"duration_s":16.65},{"text":"The trade didn't end because Singapore or Britain moved against it.","offset_s":155.425,"duration_s":5.025},{"text":"It ended because Japan did.","offset_s":160.45,"duration_s":3.05},{"text":"As Meiji Japan's international standing rose — victory over China in 1895, over Russia in 1905, an alliance with Britain by 1914 — the karayuki-san went from a useful source of remittances to a national embarrassment.","offset_s":163.5,"duration_s":17.75},{"text":"Japan's own consulate in Singapore banned Japanese-run brothels in 1920.","offset_s":181.25,"duration_s":6.85},{"text":"Roughly half the women were repatriated; the rest stayed on and found other work.","offset_s":188.1,"duration_s":6.2},{"text":"The cemetery outlived the trade that founded it by decades, and it didn't stay a memorial to trafficked women for long.","offset_s":194.3,"duration_s":8.1},{"text":"Once the brothel era ended, it became the resting place for Singapore's wider Japanese community — merchants, diplomats, and Yamamoto Otokichi, a shipwrecked sailor regarded as the first Japanese person to settle in Singapore, reinterred here after his original grave in a Christian cemetery was cleared.","offset_s":202.4,"duration_s":20.7},{"text":"Then came the war.","offset_s":223.1,"duration_s":2.075},{"text":"When Japan's occupation government fell in 1945, retreating soldiers destroyed their own war memorial at Bukit Batok before British forces finished the job; the ashes of roughly 10,000 Japanese war dead were later moved here and sealed beneath a new memorial.","offset_s":225.175,"duration_s":18.55},{"text":"Japanese prisoners of war added two more markers in April 1947: one listing 135 men executed at Changi Prison as war criminals, another for 79 executed elsewhere in Malaya.","offset_s":243.725,"duration_s":16.3},{"text":"Field Marshal Hisaichi Terauchi, who commanded Japan's entire Southern Expeditionary Army, died in nearby detention in 1946 and is buried in the cemetery's eastern corner.","offset_s":260.025,"duration_s":13.9},{"text":"The Japanese Association, Singapore has managed the cemetery since 1969; it was restored and reopened as a public heritage park in 1987.","offset_s":273.925,"duration_s":12.325},{"text":"Guided tours today walk visitors past both kinds of history side by side — the trafficked women who are the reason the cemetery exists, and the war dead and executed war criminals who arrived four decades later under entirely different circumstances.","offset_s":286.25,"duration_s":17.025},{"text":"Where it fits in the bigger story: A cemetery a brothel keeper paid for so trafficked women wouldn't go unburied ended up, within two lifetimes, holding the graves of the general who commanded Japan's wartime forces across Southeast Asia and the men executed for war crimes committed under him — two very different kinds of Japanese history sharing one plot of land in Hougang, with the women who came first still the least remembered of anyone buried there.","offset_s":303.275,"duration_s":26.4}];

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
    { t: 0, slide: 0 }, { t: 20.025, slide: 1 }, { t: 42.15, slide: 2 }, { t: 49.2, slide: 3 },
    { t: 77.95, slide: 4 }, { t: 107.05, slide: 5 }, { t: 129.725, slide: 6 }, { t: 155.425, slide: 7 },
    { t: 181.25, slide: 8 }, { t: 194.3, slide: 9 }, { t: 202.4, slide: 10 }, { t: 213.0, slide: 11 },
    { t: 223.1, slide: 12 }, { t: 243.725, slide: 13 }, { t: 260.025, slide: 14 }, { t: 273.925, slide: 15 },
    { t: 286.25, slide: 16 }, { t: 303.275, slide: 17 }
  ];
  var TOTAL_DURATION = 329.675;
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

![Entrance to the Japanese Cemetery Park, Singapore](https://upload.wikimedia.org/wikipedia/commons/6/6c/Japanese_Cemetery_Park.jpg)

*The entrance to the Japanese Cemetery Park on Chuan Hoe Avenue, Hougang — the largest Japanese cemetery in Southeast Asia. (Photo: ProjectManhattan / Wikimedia Commons, CC BY-SA 3.0)*

![Map showing the location of the Japanese Cemetery Park within Singapore](/assets/images/osm-japanese-cemetery-park-location.png)

*The Japanese Cemetery Park sits on an ordinary residential street in Hougang, boxed in by condominiums — easy to pass without ever noticing it's there. (Map data: © OpenStreetMap contributors)*

<div style="float: left; max-width: 220px; margin: 0.25em 1.5em 1em 0;">
<img src="https://upload.wikimedia.org/wikipedia/commons/9/9e/Karayukisan_in_Saigon.JPG" alt="A karayuki-san photographed in Saigon, circa 1910" style="width: 100%; display: block; border-radius: 4px;">
<em style="display: block; font-size: 0.8em; margin-top: 0.5em;">A karayuki-san photographed in Saigon, circa 1910 — the same trade that populated brothels across Southeast Asia, including Singapore's. (Photo: from "Japan of 100 Years Ago," Life Information Center / Wikimedia Commons, public domain)</em>
</div>

Karayuki-san — literally "one who has gone abroad" — were mostly girls from Amakusa and Shimabara, two of the poorest, most volcanic corners of Kyushu, sold by their own families or lured by brokers known as *zegen* who promised factory work overseas and delivered them instead to brothels. Some were smuggled out hidden in ships' holds; contemporary accounts describe girls suffocating or starving during the crossing. Singapore's Japanese-run brothel district — concentrated along Malay, Malabar, Hylam and Bugis Streets — grew from about 14 women in two brothels in 1877 to an officially recorded 633 women in 109 brothels by 1905, peaking at roughly 2,086 Japanese sex workers in 1906. The real total, including unlicensed workers, was almost certainly higher.

<div style="clear: both;"></div>

The cemetery exists because of that trade, not despite it. In 1891, three Japanese brothel keepers — Futaki Takajiro, Shibuya Ginji and Nakagawa Kikuzo — petitioned Singapore's colonial government for land to bury destitute karayuki-san, who until then had been buried informally or not at all. Futaki donated six acres from his own rubber plantation; the government added roughly another acre of public land. Most of the karayuki-san graves are modest granite pillars, plainer than the elaborate monuments built later for wealthier community members — and many were left deliberately unmarked, to spare families back in Japan the shame of a daughter's profession.

![Grave markers at the Japanese Cemetery Park](https://upload.wikimedia.org/wikipedia/commons/1/12/Japanese_Cemetery_Park_1.jpg)

*Rows of granite grave markers at the Japanese Cemetery Park — many of the oldest and plainest belong to karayuki-san. (Photo: ProjectManhattan / Wikimedia Commons, CC BY-SA 3.0)*

The trade didn't end because Singapore or Britain moved against it. It ended because Japan did. As Meiji Japan's international standing rose — victory over China in 1895, over Russia in 1905, an alliance with Britain by 1914 — the karayuki-san went from a useful source of remittances to a national embarrassment. Japan's own consulate in Singapore banned Japanese-run brothels in 1920. Roughly half the women were repatriated; the rest stayed on and found other work.

The cemetery outlived the trade that founded it by decades, and it didn't stay a memorial to trafficked women for long. Once the brothel era ended, it became the resting place for Singapore's wider Japanese community — merchants, diplomats, and Yamamoto Otokichi, a shipwrecked sailor regarded as the first Japanese person to settle in Singapore, reinterred here after his original grave in a Christian cemetery was cleared. Then came the war. When Japan's occupation government fell in 1945, retreating soldiers destroyed their own war memorial at Bukit Batok before British forces finished the job; the ashes of roughly 10,000 Japanese war dead were later moved here and sealed beneath a new memorial. Japanese prisoners of war added two more markers in April 1947: one listing 135 men executed at Changi Prison as war criminals, another for 79 executed elsewhere in Malaya. Field Marshal Hisaichi Terauchi, who commanded Japan's entire Southern Expeditionary Army, died in nearby detention in 1946 and is buried in the cemetery's eastern corner.

![War memorial stones at the Japanese Cemetery Park](https://upload.wikimedia.org/wikipedia/commons/e/ea/Japanese_war_memorial%2C_Japanese_Cemetery_Park%2C_Singapore_-_20070526.jpg)

*War memorial stones at the Japanese Cemetery Park, added by Japanese prisoners of war in April 1947. (Photo: Aldwin Teo / Wikimedia Commons, CC BY-SA 3.0)*

<div class="viz-root" style="clear: both;">
<style>
.viz-root {
  color-scheme: light;
  --surface-1:      #fcfcfb;
  --text-primary:   #0b0b0b;
  --text-secondary: #52514e;
  --text-muted:     #898781;
  --grid:           #e1e0d9;
  --axis:           #c3c2b7;
  --series-1:       #2a78d6;
  --border:         rgba(11,11,11,0.10);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}
@media (prefers-color-scheme: dark) {
  :root:where(:not([data-theme="light"])) .viz-root {
    color-scheme: dark;
    --surface-1:      #1a1a19;
    --text-primary:   #ffffff;
    --text-secondary: #c3c2b7;
    --text-muted:     #898781;
    --grid:           #2c2c2a;
    --axis:           #383835;
    --series-1:       #3987e5;
    --border:         rgba(255,255,255,0.10);
  }
}
:root[data-theme="dark"] .viz-root {
  color-scheme: dark;
  --surface-1:      #1a1a19;
  --text-primary:   #ffffff;
  --text-secondary: #c3c2b7;
  --text-muted:     #898781;
  --grid:           #2c2c2a;
  --axis:           #383835;
  --series-1:       #3987e5;
  --border:         rgba(255,255,255,0.10);
}
.tl-card { background: var(--surface-1); border: 1px solid var(--border); border-radius: 10px; padding: 20px 20px 12px; margin: 1.5em 0; }
.tl-title { font-size: 16px; font-weight: 600; color: var(--text-primary); margin: 0 0 2px; }
.tl-subtitle { font-size: 13px; color: var(--text-secondary); margin: 0 0 14px; }
.tl-chart-wrap { position: relative; }
.tl-tooltip {
  position: absolute; pointer-events: none; background: var(--surface-1); border: 1px solid var(--border);
  border-radius: 8px; padding: 8px 10px; font-size: 12.5px; color: var(--text-primary);
  box-shadow: 0 4px 16px rgba(0,0,0,0.15); opacity: 0; transition: opacity 0.1s ease; max-width: 240px; z-index: 5;
}
.tl-tooltip.visible { opacity: 1; }
.tl-tooltip-val { font-weight: 600; }
.tl-tooltip-label { color: var(--text-secondary); }
.tl-foot { font-size: 11.5px; color: var(--text-muted); margin-top: 8px; }
.tl-details { margin-top: 10px; }
.tl-details summary { font-size: 12.5px; color: var(--text-secondary); cursor: pointer; }
.tl-table { width: 100%; border-collapse: collapse; margin-top: 8px; font-size: 12.5px; }
.tl-table th, .tl-table td { text-align: left; padding: 4px 8px; border-bottom: 1px solid var(--grid); color: var(--text-primary); }
.tl-table th { color: var(--text-secondary); font-weight: 600; }
</style>

<div class="tl-card">
  <p class="tl-title">One cemetery, three eras</p>
  <p class="tl-subtitle">The Japanese Cemetery Park, Singapore, 1891–1987</p>

  <div class="tl-chart-wrap">
    <svg viewBox="0 0 640 220" width="100%" height="auto" role="img" aria-label="Timeline of the Japanese Cemetery Park. Founded 1891 by three Japanese brothel keepers to bury karayuki-san. Saiyuji prayer hall built 1911. Japan's own consulate bans Japanese brothels in 1920, ending the trade the cemetery was founded to serve. Ashes of roughly 10,000 Japanese war dead and memorials to 214 executed war criminals added 1947. Japanese Association Singapore takes over management in 1969. Restored and reopened as a public heritage park in 1987, still standing today.">
      <line x1="70" y1="110" x2="524.4" y2="110" stroke="var(--axis)" stroke-width="2"/>
      <line x1="524.4" y1="110" x2="600" y2="110" stroke="var(--axis)" stroke-width="2" stroke-dasharray="3,4"/>

      <line x1="70" y1="98" x2="70" y2="122" stroke="var(--series-1)" stroke-width="2"/>
      <line x1="164.7" y1="98" x2="164.7" y2="122" stroke="var(--series-1)" stroke-width="2"/>
      <line x1="207.3" y1="98" x2="207.3" y2="122" stroke="var(--series-1)" stroke-width="2"/>
      <line x1="335.1" y1="98" x2="335.1" y2="122" stroke="var(--series-1)" stroke-width="2"/>
      <line x1="439.2" y1="98" x2="439.2" y2="122" stroke="var(--series-1)" stroke-width="2"/>
      <line x1="524.4" y1="98" x2="524.4" y2="122" stroke="var(--series-1)" stroke-width="2"/>

      <text x="70" y="70" text-anchor="middle" font-size="12" font-weight="600" fill="var(--text-primary)">1891</text>
      <text x="70" y="86" text-anchor="middle" font-size="10.5" fill="var(--text-secondary)">Founded</text>

      <text x="164.7" y="150" text-anchor="middle" font-size="12" font-weight="600" fill="var(--text-primary)">1911</text>
      <text x="164.7" y="166" text-anchor="middle" font-size="10.5" fill="var(--text-secondary)">Saiyuji temple</text>
      <text x="164.7" y="180" text-anchor="middle" font-size="10.5" fill="var(--text-secondary)">built</text>

      <text x="207.3" y="70" text-anchor="middle" font-size="12" font-weight="600" fill="var(--text-primary)">1920</text>
      <text x="207.3" y="86" text-anchor="middle" font-size="10.5" fill="var(--text-secondary)">Brothel era ends</text>

      <text x="335.1" y="150" text-anchor="middle" font-size="12" font-weight="600" fill="var(--text-primary)">1947</text>
      <text x="335.1" y="166" text-anchor="middle" font-size="10.5" fill="var(--text-secondary)">War memorials</text>
      <text x="335.1" y="180" text-anchor="middle" font-size="10.5" fill="var(--text-secondary)">added</text>

      <text x="439.2" y="70" text-anchor="middle" font-size="12" font-weight="600" fill="var(--text-primary)">1969</text>
      <text x="439.2" y="86" text-anchor="middle" font-size="10.5" fill="var(--text-secondary)">JAS takeover</text>

      <text x="524.4" y="150" text-anchor="middle" font-size="12" font-weight="600" fill="var(--text-primary)">1987</text>
      <text x="524.4" y="166" text-anchor="middle" font-size="10.5" fill="var(--text-secondary)">Heritage park</text>

      <text x="600" y="150" text-anchor="middle" font-size="10.5" fill="var(--text-muted)">Today</text>

      <g fill="var(--series-1)" stroke="var(--surface-1)" stroke-width="1.5">
        <circle cx="70" cy="110" r="6"/>
        <circle cx="164.7" cy="110" r="6"/>
        <circle cx="207.3" cy="110" r="6"/>
        <circle cx="335.1" cy="110" r="6"/>
        <circle cx="439.2" cy="110" r="6"/>
        <circle cx="524.4" cy="110" r="6"/>
      </g>

      <rect data-year="1891 — Founded" data-val="Three Japanese brothel keepers donate land to bury karayuki-san who died in Singapore" x="45" y="20" width="45" height="180" fill="transparent" class="tl-hit" tabindex="0"/>
      <rect data-year="1911 — Saiyuji temple built" data-val="Buddhist prayer hall added on the grounds" x="142" y="20" width="45" height="180" fill="transparent" class="tl-hit" tabindex="0"/>
      <rect data-year="1920 — Brothel era ends" data-val="Japan's own consulate bans Japanese-run brothels in Singapore" x="185" y="20" width="45" height="180" fill="transparent" class="tl-hit" tabindex="0"/>
      <rect data-year="1947 — War memorials added" data-val="Japanese POWs add markers for ~10,000 war dead and 214 executed war criminals" x="313" y="20" width="45" height="180" fill="transparent" class="tl-hit" tabindex="0"/>
      <rect data-year="1969 — JAS takeover" data-val="Japanese Association, Singapore takes over management, still runs it today" x="417" y="20" width="45" height="180" fill="transparent" class="tl-hit" tabindex="0"/>
      <rect data-year="1987 — Heritage park" data-val="Restored and gazetted as a public heritage park" x="502" y="20" width="98" height="180" fill="transparent" class="tl-hit" tabindex="0"/>
    </svg>
    <div class="tl-tooltip" id="tl-tooltip"></div>
  </div>

  <p class="tl-foot">The trade that founded the cemetery ended within 30 years. The cemetery has stood for over 130.</p>

  <details class="tl-details">
    <summary>View data as table</summary>
    <table class="tl-table">
      <thead><tr><th>Year</th><th>Event</th><th>Note</th></tr></thead>
      <tbody>
        <tr><td>1891</td><td>Founded</td><td>Three brothel keepers donate land to bury karayuki-san</td></tr>
        <tr><td>1911</td><td>Saiyuji temple built</td><td>Buddhist prayer hall added on the grounds</td></tr>
        <tr><td>1920</td><td>Brothel era ends</td><td>Japan's consulate bans Japanese-run brothels in Singapore</td></tr>
        <tr><td>1947</td><td>War memorials added</td><td>POWs add markers for ~10,000 war dead and 214 executed war criminals</td></tr>
        <tr><td>1969</td><td>JAS takeover</td><td>Japanese Association, Singapore takes over management</td></tr>
        <tr><td>1987</td><td>Heritage park</td><td>Restored and gazetted as a public heritage park</td></tr>
      </tbody>
    </table>
  </details>
</div>

<script>
(function() {
  var card = document.currentScript.previousElementSibling;
  var svg = card.querySelector('svg');
  var wrap = svg.parentElement;
  var tooltip = wrap.querySelector('.tl-tooltip');
  var hits = svg.querySelectorAll('.tl-hit');

  hits.forEach(function(hit) {
    hit.addEventListener('pointerenter', show);
    hit.addEventListener('focus', show);
    hit.addEventListener('pointerleave', hide);
    hit.addEventListener('blur', hide);

    function show() {
      var year = hit.getAttribute('data-year');
      var val = hit.getAttribute('data-val');
      tooltip.innerHTML = '<div class="tl-tooltip-label">' + year + '</div><div class="tl-tooltip-val">' + val + '</div>';
      var rectBox = hit.getBoundingClientRect();
      var wrapRect = wrap.getBoundingClientRect();
      var left = rectBox.left - wrapRect.left;
      tooltip.style.left = Math.min(Math.max(left - 40, 0), wrapRect.width - 250) + 'px';
      tooltip.style.top = '4px';
      tooltip.classList.add('visible');
    }
    function hide() {
      tooltip.classList.remove('visible');
    }
  });
})();
</script>
</div>

The Japanese Association, Singapore has managed the cemetery since 1969; it was restored and reopened as a public heritage park in 1987. Guided tours today walk visitors past both kinds of history side by side — the trafficked women who are the reason the cemetery exists, and the war dead and executed war criminals who arrived four decades later under entirely different circumstances. [See six more historical photos related to this post →](/gallery/japanese-cemetery-park-karayuki-san/)

**Where it fits in the bigger story:** A cemetery a brothel keeper paid for so trafficked women wouldn't go unburied ended up, within two lifetimes, holding the graves of the general who commanded Japan's wartime forces across Southeast Asia and the men executed for war crimes committed under him — two very different kinds of Japanese history sharing one plot of land in Hougang, with the women who came first still the least remembered of anyone buried there.

---

**Sources:**
- [Japanese Cemetery Park — NLB Infopedia](https://eresources.nlb.gov.sg/infopedia/articles/SIP_1879_2012-04-19.html)
- [When Women Were Commodities — BiblioAsia, National Library Board](https://biblioasia.nlb.gov.sg/all-sections/vol-15-issue-4-jan-mar-2020-when-women-were-commodities/)
- [Singapore's Early Japanese Community on a Rare Map — BiblioAsia, National Library Board](https://biblioasia.nlb.gov.sg/all-sections/vol-22-issue-1-apr-jun-2026-singapore-s-early-japanese-community-on-a-rare-map/)
- [Mapping the Prewar Japanese Community in Singapore — Roots.gov.sg, National Heritage Board](https://www.roots.gov.sg/MUSE/articles/Mapping-the-Prewar-Japanese-Community-in-Singapore)
- [Bukit Batok Memorials — Roots.gov.sg, National Heritage Board](https://www.roots.gov.sg/places/places-landing/Places/historic-sites/bukit-batok-memorials)
- [Japanese Cemetery Park — Wikipedia](https://en.wikipedia.org/wiki/Japanese_Cemetery_Park)
- [Karayuki-san — Wikipedia](https://en.wikipedia.org/wiki/Karayuki-san)
- [Japanese Cemetery Park — Remember Singapore](https://remembersingapore.org/japanese-cemetery-park/)
- James Francis Warren, *Ah Ku and Karayuki-san: Prostitution in Singapore, 1870–1940* (NUS Press)
- [File:Japanese Cemetery Park.jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Japanese_Cemetery_Park.jpg)
- [File:Japanese Cemetery Park 1.jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Japanese_Cemetery_Park_1.jpg)
- [File:Japanese war memorial, Japanese Cemetery Park, Singapore - 20070526.jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Japanese_war_memorial,_Japanese_Cemetery_Park,_Singapore_-_20070526.jpg)
- [File:Yamamoto Otokichi memorial, Japanese Cemetery Park, Singapore - 20070526.jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Yamamoto_Otokichi_memorial,_Japanese_Cemetery_Park,_Singapore_-_20070526.jpg)
- [File:Hisaichi Terauchi memorial, Japanese Cemetery Park, Singapore - 20070526.jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Hisaichi_Terauchi_memorial,_Japanese_Cemetery_Park,_Singapore_-_20070526.jpg)
- [File:Prayer hall, Japanese Cemetery Park, Singapore - 20070526.jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Prayer_hall,_Japanese_Cemetery_Park,_Singapore_-_20070526.jpg)
- [File:Caretaker's quarters, Japanese Cemetery Park, Singapore.jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Caretaker%27s_quarters,_Japanese_Cemetery_Park,_Singapore.jpg)
- [File:Karayukisan in Saigon.JPG — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Karayukisan_in_Saigon.JPG)
- [File:Otokichi.jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Otokichi.jpg)
- [File:General Hisaichi Terauchi, Djawa Baroe, Vol. 1, Iss. 13 (1943-07-01), p11.jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:General_Hisaichi_Terauchi,_Djawa_Baroe,_Vol._1,_Iss._13_(1943-07-01),_p11.jpg)
- [Japanese Cemetery Park (way) — OpenStreetMap](https://www.openstreetmap.org/way/159148707)
- [The Straits Times, 13 June 1946 — NewspaperSG, National Library Board](https://eresources.nlb.gov.sg/newspapers/digitised/issue/straitstimes19460613-1)

[← Back to all posts](/)
