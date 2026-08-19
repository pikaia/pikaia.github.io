---
layout: post
title: "The Two Men Behind Singapore's Most Photographed Statue"
date: 2026-08-19 17:00:00 +0800
last_modified_at: 2026-08-20 02:04:00 +0800
categories: [history]
image: https://upload.wikimedia.org/wikipedia/commons/c/c0/Merlion%2C_Singapore.JPG
---

Millions of people photograph the Merlion every year, and almost none of them could name the men who made it. That is not a knock on the tourists. Singapore itself has done a poor job remembering: the lion-headed, fish-tailed statue at Marina Bay is arguably the single most recognisable image the country has ever produced, more instantly "Singapore" in a photo than the flag or the skyline, and yet the two people responsible for it, a British fish expert and a self-taught local sculptor, both died within a year of each other in the late 1980s without much public notice.

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
  <source src="/audio/two-men-behind-singapore-merlion-statue.mp3" type="audio/mpeg">
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
    { src: "https://upload.wikimedia.org/wikipedia/commons/c/c0/Merlion%2C_Singapore.JPG", type: "cover", zoom: [1, 1.12, 1.18], pan: ["45% 35%", "62% 55%", "72% 45%"], ease: "ease-in-out" },
    { src: "https://upload.wikimedia.org/wikipedia/commons/a/ae/Merlion_Closeup_Large.JPG", type: "cover", zoom: [1, 1.1, 1.22], pan: ["55% 60%", "40% 45%", "28% 40%"], ease: "ease-in" },
    { src: "https://upload.wikimedia.org/wikipedia/commons/8/81/Lim_Nang_Seng.jpg", type: "letterbox", zoom: [1, 1.02, 1.05], pan: ["50% 50%", "54% 46%", "58% 42%"], ease: "linear" },
    { src: "https://upload.wikimedia.org/wikipedia/commons/f/f2/Merlion_and_the_Singapore_Skyline.JPG", type: "cover", zoom: [1.18, 1.08, 1], pan: ["60% 25%", "50% 50%", "40% 75%"], ease: "ease-out" },
    { src: "https://upload.wikimedia.org/wikipedia/commons/2/20/Rear_view_of_the_Merlion_statue_at_Merlion_Park%2C_Singapore%2C_with_Marina_Bay_Sands_in_the_distance_-_20140307.jpg", type: "cover", zoom: [1, 1.1, 1.16], pan: ["35% 72%", "55% 50%", "65% 28%"], ease: "ease-in-out" },
    { src: "https://upload.wikimedia.org/wikipedia/commons/b/bb/Singapore_Mini_Merlion.JPG", type: "cover", zoom: [1, 1.12, 1.2], pan: ["75% 60%", "50% 45%", "25% 35%"], ease: "ease-in" },
    { src: "https://upload.wikimedia.org/wikipedia/commons/2/24/Merlion_statue_at_Tourism_Court%2C_Singapore_-_20150329.jpg", type: "cover", zoom: [1, 1.08, 1.15], pan: ["40% 30%", "55% 50%", "45% 65%"], ease: "ease-in" },
    { src: "https://upload.wikimedia.org/wikipedia/commons/8/80/2005_%E6%96%B0%E5%8A%A0%E5%9D%A1_-_panoramio_%282%29.jpg", type: "cover", zoom: [1.16, 1.06, 1], pan: ["30% 65%", "50% 45%", "72% 30%"], ease: "ease-out" },
    { src: "https://upload.wikimedia.org/wikipedia/commons/5/51/Singapore_Merlion_in_1978.jpg", type: "cover", zoom: [1.14, 1.06, 1], pan: ["55% 60%", "48% 45%", "35% 35%"], ease: "ease-out" },
    { src: "https://upload.wikimedia.org/wikipedia/commons/8/8e/Former_Merlion_Park.JPG", type: "cover", zoom: [1, 1.08, 1.14], pan: ["45% 30%", "55% 55%", "65% 75%"], ease: "linear" }
  ];

  // Real per-sentence timestamps captured for free from edge-tts's
  // SentenceBoundary events (see scripts/generate_narration.py) - drives
  // captions independently of image switching, in exact sync with speech.
  var sentences = [{"text":"The Two Men Behind Singapore's Most Photographed Statue","offset_s":0.05,"duration_s":3.75},{"text":"Millions of people photograph the Merlion every year, and almost none of them could name the men who made it.","offset_s":3.8,"duration_s":6.25},{"text":"That is not a knock on the tourists.","offset_s":10.05,"duration_s":2.0875},{"text":"Singapore itself has done a poor job remembering: the lion-headed, fish-tailed statue at Marina Bay is arguably the single most recognisable image the country has ever produced, more instantly \"Singapore\" in a photo than the flag or the skyline, and yet the two people responsible for it, a British fish expert and a self-taught local sculptor, both died within a year of each other in the late 1980s without much public notice.","offset_s":12.1375,"duration_s":25.95},{"text":"The creature itself was never supposed to become a monument.","offset_s":38.0875,"duration_s":3.5},{"text":"It began in 1964 as a piece of graphic design, drawn by Alec Fraser-Brunner, an Englishman who had spent the previous decade as curator of the Van Kleef Aquarium at the foot of Fort Canning Hill.","offset_s":41.5875,"duration_s":12.375},{"text":"Fraser-Brunner was a career ichthyologist, not an artist by trade, a man who had catalogued fish for Britain's Colonial Office and would later curate the aquarium at Edinburgh Zoo.","offset_s":53.9625,"duration_s":10.9625},{"text":"Sitting on a committee tasked with giving Singapore's fledgling tourism board a logo, he sketched a creature with a lion's head grafted onto a fish's body: the lion for the founding legend of Sang Nila Utama, the Sumatran prince said to have spotted the beast that gave the island its name, Singapura, \"Lion City\"; the fish for Temasek, the older name for the settlement, meaning \"sea town.\"","offset_s":64.925,"duration_s":23.0125},{"text":"The trademark was registered in 1966 and used quietly as a tourism board emblem for the rest of the decade, a flat piece of branding with no statue attached to it and, outside of ichthyology circles, no name attached to Fraser-Brunner either.","offset_s":87.9375,"duration_s":15.05},{"text":"He died in 1986, and today the clearest public record of his authorship is a Wikipedia article.","offset_s":102.9875,"duration_s":6.525},{"text":"Turning that emblem into a monument fell to Lim Nang Seng, a sculptor with no formal art training who had started out as a schoolteacher and picked up sculpture as a hobby.","offset_s":109.5125,"duration_s":10.4},{"text":"Lim had built a modest local reputation by the early 1970s, winning design prizes and completing a public sculpture in Tiong Bahru that some critics found too abstract for their taste, when he was selected in 1971, working from a blueprint prepared by the artist Kwan Sai Kheong, to build a statue based on Fraser-Brunner's decade-old logo.","offset_s":119.9125,"duration_s":22.0375},{"text":"The job took him from November 1971 to August 1972: an 8.6-metre, 70-tonne cement structure, built with the help of all eight of his children, then aged 11 to 23.","offset_s":141.95,"duration_s":13.775},{"text":"The older ones climbed the wooden scaffolding to work on the eyes; the younger ones carved the fish scales and fins into the tail.","offset_s":155.725,"duration_s":7.6875},{"text":"Prime Minister Lee Kuan Yew unveiled the finished statue at the mouth of the Singapore River on 15 September 1972.","offset_s":163.4125,"duration_s":8.0625},{"text":"Lim earned a modest income from the commission and, by his family's account, actively discouraged his own children from following him into sculpture as a career.","offset_s":171.475,"duration_s":9.65},{"text":"The statue outgrew both of them almost immediately.","offset_s":181.125,"duration_s":3.2375},{"text":"It was relocated a short distance to its current spot at Merlion Park in 2002, after the newly built Esplanade Bridge blocked the original view, and it has since been joined by a two-metre \"cub\" and by unrelated Merlion statues elsewhere in the country, none of which changes the fact that the entire image, lion head, fish tail and all, traces back to one aquarium curator's sketch and one sculptor's cement.","offset_s":184.3625,"duration_s":25.6625},{"text":"Lim never got to see how far the statue's fame would travel.","offset_s":210.025,"duration_s":3.7},{"text":"On 17 November 1987, during Merlion Week, a set of annual celebrations built around the very statue he had built fifteen years earlier, he collapsed while working on a set of clay figurines and died shortly afterward at Singapore General Hospital.","offset_s":213.725,"duration_s":16.6875},{"text":"Why it matters today: the Merlion is reproduced on more souvenirs, postcards and Instagram grids than any other image associated with Singapore, and almost nobody buying or posting one could tell you that a British fish taxonomist drew it as a logo, or that a former schoolteacher and his eight children built it out of cement over nine months.","offset_s":230.522,"duration_s":19.825},{"text":"The most famous thing to come out of Singapore's tourism board turned out to be the perfect case study in how completely a creation can eclipse its creators.","offset_s":250.347,"duration_s":8.8}];

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
  // above) rather than an even split of total duration - e.g. slide 2
  // (Lim Nang Seng) doesn't start until 109.51s, right as the narration
  // actually turns to him, so it never shows up mid-Fraser-Brunner story.
  // This is hand-mapped to this post's specific narration/image set and
  // will need re-deriving if the sentences or slide order ever change.
  var imageSchedule = [
    { t: 0, slide: 0 },       // hero - intro
    { t: 38.09, slide: 1 },   // closeup - Fraser-Brunner's design story
    { t: 109.51, slide: 2 },  // Lim Nang Seng portrait - his bio + building it
    { t: 181.13, slide: 3 },  // skyline - statue outgrew both of them
    { t: 190.0, slide: 4 },   // rear view - relocated 2002, Esplanade Bridge
    { t: 198.0, slide: 5 },   // mini merlion - "joined by a two-metre cub"
    { t: 204.0, slide: 6 },   // tourism court - "unrelated Merlion statues elsewhere"
    { t: 210.03, slide: 9 },  // former merlion park - Lim never saw its fame, died 1987
    { t: 230.52, slide: 7 },  // sentosa - "why it matters today"
    { t: 250.35, slide: 8 }   // 1978 photo - closing line
  ];
  var slideDurations = imageSchedule.map(function (entry, i) {
    var next = i + 1 < imageSchedule.length ? imageSchedule[i + 1].t : 259.2;
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
    // Chunks are in ascending offset order; find the last one that has started.
    var idx = 0;
    for (var i = 0; i < captionChunks.length; i++) {
      if (captionChunks[i].offset_s <= t) idx = i; else break;
    }
    return idx;
  }

  function slideIndexForTime(t) {
    // Schedule entries are in ascending time order; find the last one that has started.
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

![The Merlion statue at Merlion Park, Singapore](https://upload.wikimedia.org/wikipedia/commons/c/c0/Merlion%2C_Singapore.JPG)

*The Merlion at Merlion Park, Marina Bay. (Photo: PookieFugglestein / Wikimedia Commons, CC0)*

The creature itself was never supposed to become a monument. It began in 1964 as a piece of graphic design, drawn by Alec Fraser-Brunner, an Englishman who had spent the previous decade as curator of the Van Kleef Aquarium at the foot of Fort Canning Hill. Fraser-Brunner was a career ichthyologist, not an artist by trade, a man who had catalogued fish for Britain's Colonial Office and would later curate the aquarium at Edinburgh Zoo. Sitting on a committee tasked with giving Singapore's fledgling tourism board a logo, he sketched a creature with a lion's head grafted onto a fish's body: the lion for the founding legend of Sang Nila Utama, the Sumatran prince said to have spotted the beast that gave the island its name, Singapura, "Lion City"; the fish for Temasek, the older name for the settlement, meaning "sea town." The trademark was registered in 1966 and used quietly as a tourism board emblem for the rest of the decade, a flat piece of branding with no statue attached to it and, outside of ichthyology circles, no name attached to Fraser-Brunner either. He died in 1986, and today the clearest public record of his authorship is a Wikipedia article.

<div style="float: left; max-width: 280px; width: 45%; margin: 0.25em 1.5em 1em 0;">
<img src="https://upload.wikimedia.org/wikipedia/commons/a/ae/Merlion_Closeup_Large.JPG" alt="Close-up of the Merlion statue's head" style="width: 100%; display: block; border-radius: 4px;">
<em style="display: block; font-size: 0.8em; margin-top: 0.5em;">The lion head and fish scales Fraser-Brunner sketched as a flat 1964 emblem, later given three-dimensional form. (Photo: Jpatokal / Wikimedia Commons, CC BY-SA)</em>
</div>

Turning that emblem into a monument fell to Lim Nang Seng, a sculptor with no formal art training who had started out as a schoolteacher and picked up sculpture as a hobby. Lim had built a modest local reputation by the early 1970s, winning design prizes and completing a public sculpture in Tiong Bahru that some critics found too abstract for their taste, when he was selected in 1971, working from a blueprint prepared by the artist Kwan Sai Kheong, to build a statue based on Fraser-Brunner's decade-old logo. The job took him from November 1971 to August 1972: an 8.6-metre, 70-tonne cement structure, built with the help of all eight of his children, then aged 11 to 23. The older ones climbed the wooden scaffolding to work on the eyes; the younger ones carved the fish scales and fins into the tail. Prime Minister Lee Kuan Yew unveiled the finished statue at the mouth of the Singapore River on 15 September 1972. Lim earned a modest income from the commission and, by his family's account, actively discouraged his own children from following him into sculpture as a career.

<div style="float: left; max-width: 260px; width: 42%; margin: 0.25em 1.5em 1em 0;">
<img src="https://upload.wikimedia.org/wikipedia/commons/8/81/Lim_Nang_Seng.jpg" alt="Lim Nang Seng and his wife at Tiger Balm Gardens, 1950" style="width: 100%; display: block; border-radius: 4px;">
<em style="display: block; font-size: 0.8em; margin-top: 0.5em;">Lim Nang Seng and his wife at Tiger Balm Gardens, 1950, two decades before the Merlion commission. (Photo: National Archives of Singapore / Wikimedia Commons, public domain)</em>
</div>

The statue outgrew both of them almost immediately. It was relocated a short distance to its current spot at Merlion Park in 2002, after the newly built Esplanade Bridge blocked the original view, and it has since been joined by a two-metre "cub" and by unrelated Merlion statues elsewhere in the country, none of which changes the fact that the entire image, lion head, fish tail and all, traces back to one aquarium curator's sketch and one sculptor's cement. [See more historical photos related to this post →](/gallery/two-men-behind-singapore-merlion-statue/) Lim never got to see how far the statue's fame would travel. On 17 November 1987, during Merlion Week, a set of annual celebrations built around the very statue he had built fifteen years earlier, he collapsed while working on a set of clay figurines and died shortly afterward at Singapore General Hospital.

**Why it matters today:** the Merlion is reproduced on more souvenirs, postcards and Instagram grids than any other image associated with Singapore, and almost nobody buying or posting one could tell you that a British fish taxonomist drew it as a logo, or that a former schoolteacher and his eight children built it out of cement over nine months. The most famous thing to come out of Singapore's tourism board turned out to be the perfect case study in how completely a creation can eclipse its creators.

---

**Sources:**
- [Alec Fraser-Brunner — Wikipedia](https://en.wikipedia.org/wiki/Alec_Fraser-Brunner)
- [Van Kleef Aquarium — Wikipedia](https://en.wikipedia.org/wiki/Van_Kleef_Aquarium)
- [Lim Nang Seng — Wikipedia](https://en.wikipedia.org/wiki/Lim_Nang_Seng)
- [Celebrating 50 Years of the Merlion: Stories Behind the National Icon — Roots.gov.sg, National Heritage Board](https://www.roots.gov.sg/stories-landing/stories/celebrating-50-years-of-the-merlion-stories-behind-the-national-icon/story)
- [Unveiling of The Merlion Statue — SG101](https://www.sg101.gov.sg/resources/archives/identity-unveiling-of-the-merlion-statue/)
- [MR LIM NANG SENG SCULPTING A MINIATURE MERLION STATUE, 1972 — National Archives of Singapore](http://www.nas.gov.sg/blogs/archivistpick/mr-lim-nang-seng-sculpting-a-miniature-merlion-statue-1972/)
- [Waterboat House Garden — Wikipedia](https://en.wikipedia.org/wiki/Waterboat_House_Garden)
- [File:Merlion, Singapore.JPG — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Merlion,_Singapore.JPG)
- [File:Merlion Closeup Large.JPG — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Merlion_Closeup_Large.JPG)
- [File:Lim Nang Seng.jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Lim_Nang_Seng.jpg)
- [File:Merlion and the Singapore Skyline.JPG — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Merlion_and_the_Singapore_Skyline.JPG)
- [File:Rear view of the Merlion statue at Merlion Park, Singapore, with Marina Bay Sands in the distance - 20140307.jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Rear_view_of_the_Merlion_statue_at_Merlion_Park,_Singapore,_with_Marina_Bay_Sands_in_the_distance_-_20140307.jpg)
- [File:Singapore Mini Merlion.JPG — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Singapore_Mini_Merlion.JPG)
- [File:Merlion statue at Tourism Court, Singapore - 20150329.jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Merlion_statue_at_Tourism_Court,_Singapore_-_20150329.jpg)
- [File:2005 新加坡 - panoramio (2).jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:2005_%E6%96%B0%E5%8A%A0%E5%9D%A1_-_panoramio_(2).jpg)
- [File:Singapore Merlion in 1978.jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Singapore_Merlion_in_1978.jpg)
- [File:Former Merlion Park.JPG — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Former_Merlion_Park.JPG)

[← Back to all posts](/)
