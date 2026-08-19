---
layout: post
title: "The Bunker Under Fort Canning Hill"
date: 2026-07-18 09:00:00 +0800
last_modified_at: 2026-08-20 05:11:00 +0800
categories: [history, world-war-two]
image: https://upload.wikimedia.org/wikipedia/commons/c/ce/Fort_Canning_Park_Tree_Tunnel.jpg
---

Beneath Fort Canning Hill, a quiet green space in the middle of the city, sits a concrete bunker most visitors to the park above never notice. Known as the Battlebox, it was once the underground command centre for the British Malaya Command, and it's roughly the size of three basketball courts, buried entirely out of sight.

[← Back to all posts](/)

<div style="display: flex; gap: 2em; margin: 0.5em 0 1.5em 0;">
  <div id="listen-widget" role="button" tabindex="0" aria-label="Play audio narration of this post" style="display: inline-flex; flex-direction: column; align-items: center; cursor: pointer; gap: 0.2em; user-select: none;">
    <span id="listen-icon" aria-hidden="true" style="display: inline-flex; align-items: center; justify-content: center; width: 2.4em; height: 2.4em; border-radius: 50%; border: 1px solid #888; font-size: 1.3em;">&#127911;</span>
    <span style="font-size: 0.7em; text-transform: uppercase; letter-spacing: 0.05em; opacity: 0.75;">Listen</span>
  </div>
  <div id="watch-widget" role="button" tabindex="0" aria-label="Watch an animated version of this post" style="display: inline-flex; flex-direction: column; align-items: center; cursor: pointer; gap: 0.2em; user-select: none;">
    <span aria-hidden="true" style="display: inline-flex; align-items: center; justify-content: center; width: 2.4em; height: 2.4em; border-radius: 50%; border: 1px solid #888; font-size: 1.3em;">&#127916;</span>
    <span style="font-size: 0.7em; text-transform: uppercase; letter-spacing: 0.05em; opacity: 0.75;">Watch</span>
  </div>
</div>

<audio id="listen-audio" preload="none" style="display: none;">
  <source src="/audio/the-bunker-under-fort-canning.mp3" type="audio/mpeg">
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
  var slides = [
    { src: "https://upload.wikimedia.org/wikipedia/commons/c/ce/Fort_Canning_Park_Tree_Tunnel.jpg", type: "cover", zoom: [1, 1.1, 1.16], pan: ["50% 60%", "55% 40%", "45% 30%"], ease: "ease-in-out" },
    { src: "https://upload.wikimedia.org/wikipedia/commons/8/8a/BattleBoxEntrance.JPG", type: "cover", zoom: [1, 1.12, 1.2], pan: ["60% 30%", "50% 50%", "40% 70%"], ease: "ease-in" },
    { src: "https://upload.wikimedia.org/wikipedia/commons/6/6e/Door_of_The_Battle_Box%2C_Singapore_-_20100306.jpg", type: "cover", zoom: [1, 1.1, 1.18], pan: ["40% 70%", "50% 45%", "60% 25%"], ease: "ease-in-out" },
    { src: "https://upload.wikimedia.org/wikipedia/commons/4/4e/In_the_Battle_Box%2C_Singapore_-_panoramio.jpg", type: "cover", zoom: [1.18, 1.08, 1], pan: ["30% 60%", "50% 45%", "65% 35%"], ease: "ease-out" },
    { src: "https://upload.wikimedia.org/wikipedia/commons/9/91/Fort_Canning_Hill-1902.jpg", type: "cover", zoom: [1, 1.04, 1.08], pan: ["50% 50%", "55% 45%", "60% 40%"], ease: "linear" },
    { src: "https://upload.wikimedia.org/wikipedia/commons/e/eb/Interior_of_the_Battle_Box%2C_Singapore_-_20110506-01.jpg", type: "cover", zoom: [1, 1.1, 1.16], pan: ["35% 65%", "50% 45%", "65% 30%"], ease: "ease-in" },
    { src: "https://upload.wikimedia.org/wikipedia/commons/c/cf/Interior_of_the_Battle_Box%2C_Singapore_-_20120722-01.jpg", type: "cover", zoom: [1, 1.12, 1.18], pan: ["65% 35%", "50% 55%", "35% 65%"], ease: "ease-in-out" },
    { src: "https://upload.wikimedia.org/wikipedia/commons/3/39/Lieutenant_General_Arthur_Percival.jpg", type: "cover", zoom: [1, 1.1, 1.18], pan: ["55% 65%", "45% 45%", "35% 30%"], ease: "ease-in" },
    { src: "https://upload.wikimedia.org/wikipedia/commons/2/21/Yamashita_e_Suzuki.jpg", type: "cover", zoom: [1.16, 1.06, 1], pan: ["30% 40%", "50% 50%", "70% 60%"], ease: "ease-out" },
    { src: "https://upload.wikimedia.org/wikipedia/commons/c/ce/Fort_Canning_Park_Tree_Tunnel.jpg", type: "cover", zoom: [1.15, 1.05, 1], pan: ["45% 40%", "55% 55%", "65% 70%"], ease: "ease-out" }
  ];

  // Real per-sentence timestamps captured for free from edge-tts's
  // SentenceBoundary events (see scripts/generate_narration.py) - drives
  // captions independently of image switching, in exact sync with speech.
  var sentences = [{"text":"The Bunker Under Fort Canning Hill","offset_s":0.05,"duration_s":2.3125},{"text":"Beneath Fort Canning Hill, a quiet green space in the middle of the city, sits a concrete bunker most visitors to the park above never notice.","offset_s":2.3625,"duration_s":8.9},{"text":"Known as the Battlebox, it was once the underground command centre for the British Malaya Command, and it's roughly the size of three basketball courts, buried entirely out of sight.","offset_s":11.2625,"duration_s":11.15},{"text":"It was here, in this windowless maze of rooms, that British commanders spent the final days before Singapore fell to Japanese forces in February 1942.","offset_s":22.4125,"duration_s":10.3125},{"text":"The decision to surrender — one of the most consequential moments in the island's history — was made in this bunker, not in a grand hall or government building, but underground, out of view.","offset_s":32.725,"duration_s":11.8375},{"text":"After the war the bunker was sealed up and largely forgotten for decades.","offset_s":44.5625,"duration_s":4.2125},{"text":"It's since been restored and reopened to the public, filled with reconstructed rooms, wartime documents, and life-sized figures recreating those final tense days.","offset_s":48.775,"duration_s":10.2375},{"text":"Walking through it today, lined with old telephones and map tables, gives a strange, quiet sense of just how much history can happen in a space nobody thinks to look for.","offset_s":59.0125,"duration_s":10.7375},{"text":"Fort Canning Hill's part in the story didn't start or end with the bunker itself — it runs from the hill's pre-war role as the seat of British Malaya Command through to the commanders on both sides of the surrender table.","offset_s":69.75,"duration_s":12.45},{"text":"Where it fits in the bigger story: the Battlebox sits alongside other lesser-known wartime sites across Singapore — a reminder that much of the island's most pivotal history happened in unremarkable, easy-to-miss places.","offset_s":82.2,"duration_s":13.9125}];

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
    { t: 0, slide: 0 },        // tree tunnel - intro
    { t: 11.26, slide: 1 },    // Battlebox entrance - "Known as the Battlebox..."
    { t: 22.41, slide: 2 },    // blast door - "windowless maze of rooms..."
    { t: 32.73, slide: 3 },    // war council reconstruction - "the decision to surrender..."
    { t: 44.56, slide: 4 },    // 1902 photo - "sealed up and largely forgotten"
    { t: 48.78, slide: 5 },    // interior (figures/telephone/maps) - "restored... reconstructed rooms..."
    { t: 59.01, slide: 6 },    // interior (comms booths) - "old telephones and map tables"
    { t: 69.75, slide: 7 },    // Percival arrives - "pre-war role..."
    { t: 76.0, slide: 8 },     // Yamashita - "...commanders on both sides"
    { t: 82.2, slide: 9 }      // tree tunnel again - closing line
  ];
  var TOTAL_DURATION = 96.168;
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

![The tree tunnel staircase in Fort Canning Park](https://upload.wikimedia.org/wikipedia/commons/c/ce/Fort_Canning_Park_Tree_Tunnel.jpg)

*Fort Canning Park today — the quiet green space with a wartime command bunker hidden beneath it. (Photo: DianaAndassova / Wikimedia Commons, CC BY-SA 4.0)*

![Entrance to the Battlebox at Fort Canning Hill](https://upload.wikimedia.org/wikipedia/commons/8/8a/BattleBoxEntrance.JPG)

*The entrance to the Battlebox, tucked into the hillside below Fort Canning Park. (Photo: Zawed / Wikimedia Commons, public domain)*

It was here, in this windowless maze of rooms, that British commanders spent the final days before Singapore fell to Japanese forces in February 1942. The decision to surrender — one of the most consequential moments in the island's history — was made in this bunker, not in a grand hall or government building, but underground, out of view.

After the war the bunker was sealed up and largely forgotten for decades. It's since been restored and reopened to the public, filled with reconstructed rooms, wartime documents, and life-sized figures recreating those final tense days. Walking through it today, lined with old telephones and map tables, gives a strange, quiet sense of just how much history can happen in a space nobody thinks to look for.

![Blast door leading into the Battlebox tunnels](https://upload.wikimedia.org/wikipedia/commons/6/6e/Door_of_The_Battle_Box%2C_Singapore_-_20100306.jpg)

*The heavy blast door guarding the entrance to the bunker's tunnels. (Photo: Roberto Arias / Wikimedia Commons, CC BY 2.0)*

Fort Canning Hill's part in the story didn't start or end with the bunker itself — it runs from the hill's pre-war role as the seat of British Malaya Command through to the commanders on both sides of the surrender table. [See more historical photos related to this post →](/gallery/the-bunker-under-fort-canning/)

**Where it fits in the bigger story:** the Battlebox sits alongside other lesser-known wartime sites across Singapore — a reminder that much of the island's most pivotal history happened in unremarkable, easy-to-miss places.

---

**Sources:**
- [Battlebox — Wikipedia](https://en.wikipedia.org/wiki/Battlebox)
- [File:Fort Canning Park Tree Tunnel.jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Fort_Canning_Park_Tree_Tunnel.jpg)
- [File:BattleBoxEntrance.JPG — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:BattleBoxEntrance.JPG)
- [File:Door of The Battle Box, Singapore - 20100306.jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Door_of_The_Battle_Box,_Singapore_-_20100306.jpg)
- [File:Fort Canning Hill-1902.jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Fort_Canning_Hill-1902.jpg)
- [File:Lieutenant General Arthur Percival.jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Lieutenant_General_Arthur_Percival.jpg)
- [File:Yamashita e Suzuki.jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Yamashita_e_Suzuki.jpg)
- [File:British troops surrender in Singapore.png — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:British_troops_surrender_in_Singapore.png)
- [File:Singaporesurrender.jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Singaporesurrender.jpg)
- [File:Sang nila utama garden.jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Sang_nila_utama_garden.jpg)
- [File:Singapore from the Sea June 1823 - Lt. Phillip Jackson.jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Singapore_from_the_Sea_June_1823_-_Lt._Phillip_Jackson.jpg)
- [File:Part of Singapore Island (British Library India Office Records, 1825, detail).jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Part_of_Singapore_Island_(British_Library_India_Office_Records,_1825,_detail).jpg)
- [File:Fort Canning from the Singapore River - 1860–1900.jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Fort_Canning_from_the_Singapore_River_-_1860%E2%80%931900.jpg)
- [File:20250628 oldchristiancemetery.jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:20250628_oldchristiancemetery.jpg)
- [File:Dispositions of the Garrison February-1942.png — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Dispositions_of_the_Garrison_February-1942.png)
- [File:Percival with war correspondents.jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Percival_with_war_correspondents.jpg)
- [File:Terauchi Hisaichi in Singapore 1942.png — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Terauchi_Hisaichi_in_Singapore_1942.png)
- [File:Liberated British Prisoners of War in the Far East, 1945, HU 69968.jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Liberated_British_Prisoners_of_War_in_the_Far_East,_1945,_HU_69968.jpg)
- [File:In the Battle Box, Singapore - panoramio.jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:In_the_Battle_Box,_Singapore_-_panoramio.jpg)
- [File:Interior of the Battle Box, Singapore - 20110506-01.jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Interior_of_the_Battle_Box,_Singapore_-_20110506-01.jpg)
- [File:Interior of the Battle Box, Singapore - 20120722-01.jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Interior_of_the_Battle_Box,_Singapore_-_20120722-01.jpg)

[← Back to all posts](/)
