---
layout: post
title: "The Concert Hall That Was Once a Courtroom for Hanging Men"
date: 2026-08-15 23:55:00 +0800
last_modified_at: 2026-08-21 16:00:00 +0800
categories: [history, world-war-two]
image: https://upload.wikimedia.org/wikipedia/commons/e/e6/Victoria_Theatre_and_Victoria_Memorial_Hall_-_c_1930.jpg
---

Every week, concertgoers file into Victoria Concert Hall to hear the Singapore Symphony Orchestra, mostly unaware that the same room once served as a stage for Japanese wartime propaganda, and then, within two years, as the courtroom where Japanese officers were sentenced to hang. It has been rebuilt, renamed, and rebranded more times than almost any other building in Singapore — and every time, it has gone back to being a place for culture, as if nothing else had ever happened inside it.

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
  <a href="https://youtu.be/7qLCW-xv4MY" target="_blank" rel="noopener" aria-label="Watch this story as a video on YouTube" style="display: inline-flex; flex-direction: column; align-items: center; gap: 0.2em; text-decoration: none; color: inherit;">
    <span aria-hidden="true" style="display: inline-flex; align-items: center; justify-content: center; width: 2.4em; height: 2.4em; border-radius: 50%; border: 1px solid #888;">
      <svg width="1.4em" height="1.4em" viewBox="0 0 24 24" aria-hidden="true"><rect x="1" y="4" width="22" height="16" rx="5" fill="#FF0000"/><path d="M10 8.5l6 3.5-6 3.5z" fill="#fff"/></svg>
    </span>
    <span style="font-size: 0.7em; text-transform: uppercase; letter-spacing: 0.05em; opacity: 0.75;">YouTube</span>
  </a>
</div>

<audio id="listen-audio" preload="none" style="display: none;">
  <source src="/audio/victoria-memorial-hall-culture-war-crimes-trials.mp3" type="audio/mpeg">
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
  var HERO = "https://upload.wikimedia.org/wikipedia/commons/e/e6/Victoria_Theatre_and_Victoria_Memorial_Hall_-_c_1930.jpg";
  var CIRCA1900 = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/KITLV_-_33196_-_Victoria_Theatre_and_Memorial_Hall_in_Singapore_-_circa_1900.tif/lossy-page1-1280px-KITLV_-_33196_-_Victoria_Theatre_and_Memorial_Hall_in_Singapore_-_circa_1900.tif.jpg";
  var STADHUIS1915 = "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/KITLV_A740_-_Stadhuis_te_Singapore%2C_KITLV_90268.tiff/lossy-page1-1280px-KITLV_A740_-_Stadhuis_te_Singapore%2C_KITLV_90268.tiff.jpg";
  var LOCATOR = "/assets/images/osm-victoria-theatre-concert-hall-location.png";
  var RAFFLES2004 = "https://upload.wikimedia.org/wikipedia/commons/5/5a/Victoria_Theatre_and_Concert_Hall_-_Stamford_Raffles_Statue_2004.jpg";
  var PHOTO1973 = "https://upload.wikimedia.org/wikipedia/commons/7/78/Singapore-Victoria_Theatre_and_Concert_Hall-1973-74-WUS08256.jpg";
  var PHOTO1960 = "https://upload.wikimedia.org/wikipedia/commons/3/3d/Victoria_Theatre_Singapore_May_1960.jpg";
  var PHOTO1965 = "https://upload.wikimedia.org/wikipedia/commons/2/29/VictoriaTheatreandMemorialHall-Singapore-1965.jpg";
  var FRONT2014 = "https://upload.wikimedia.org/wikipedia/commons/5/54/Front_of_Victoria_Theatre%2C_Singapore_-_20141101-01.JPG";
  var ATRIUM2014 = "https://upload.wikimedia.org/wikipedia/commons/8/80/Entrance_to_the_atrium_of_Victoria_Theatre_and_Concert_Hall%2C_Singapore_-_20141101-01.JPG";
  var PHOTO2023 = "https://upload.wikimedia.org/wikipedia/commons/c/c9/Victoria_Memorial_Hall%2C_Singapore%2C_August_2023.jpg";

  var slides = [
    { src: HERO, type: "cover", zoom: [1, 1.08, 1.15], pan: ["50% 40%", "45% 45%", "40% 50%"], ease: "ease-in-out" },
    { src: CIRCA1900, type: "cover", zoom: [1, 1.09, 1.16], pan: ["45% 50%", "50% 50%", "55% 50%"], ease: "ease-out" },
    { src: STADHUIS1915, type: "cover", zoom: [1.15, 1.06, 1], pan: ["55% 45%", "50% 50%", "45% 55%"], ease: "ease-in" },
    { src: LOCATOR, type: "cover", zoom: [1, 1.06, 1.12], pan: ["50% 50%", "48% 50%", "46% 50%"], ease: "linear" },
    { src: HERO, type: "cover", zoom: [1.15, 1.06, 1], pan: ["55% 55%", "50% 50%", "45% 45%"], ease: "ease-out" },
    { src: RAFFLES2004, type: "cover", zoom: [1, 1.08, 1.15], pan: ["50% 35%", "50% 45%", "50% 55%"], ease: "ease-in-out" },
    { src: PHOTO1973, type: "cover", zoom: [1, 1.09, 1.16], pan: ["40% 50%", "50% 50%", "60% 50%"], ease: "linear" },
    { src: PHOTO1973, type: "cover", zoom: [1.16, 1.06, 1], pan: ["60% 45%", "50% 50%", "40% 55%"], ease: "ease-in-out" },
    { src: PHOTO1960, type: "cover", zoom: [1, 1.1, 1.18], pan: ["45% 50%", "50% 45%", "55% 40%"], ease: "ease-out" },
    { src: PHOTO1965, type: "cover", zoom: [1.15, 1.06, 1], pan: ["55% 40%", "50% 50%", "45% 60%"], ease: "ease-in" },
    { src: FRONT2014, type: "cover", zoom: [1, 1.08, 1.15], pan: ["50% 55%", "50% 50%", "50% 40%"], ease: "linear" },
    { src: ATRIUM2014, type: "cover", zoom: [1, 1.09, 1.16], pan: ["45% 45%", "50% 50%", "55% 55%"], ease: "ease-in-out" },
    { src: PHOTO2023, type: "cover", zoom: [1, 1.1, 1.18], pan: ["50% 50%", "48% 45%", "46% 40%"], ease: "ease-out" }
  ];

  // Real per-sentence timestamps captured for free from Kokoro TTS's own
  // per-sentence synthesis (see scripts/generate_narration.py) - drives
  // captions independently of image switching, in exact sync with speech.
  var sentences = [{"text":"The Concert Hall That Was Once a Courtroom for Hanging Men","offset_s":0.0,"duration_s":4.2},{"text":"Every week, concertgoers file into Victoria Concert Hall to hear the Singapore Symphony Orchestra, mostly unaware that the same room once served as a stage for Japanese wartime propaganda, and then, within two years, as the courtroom where Japanese officers were sentenced to hang.","offset_s":4.2,"duration_s":19.6},{"text":"It has been rebuilt, renamed, and rebranded more times than almost any other building in Singapore — and every time, it has gone back to being a place for culture, as if nothing else had ever happened inside it.","offset_s":23.8,"duration_s":13.95},{"text":"The complex began as two separate civic projects joined almost by accident.","offset_s":37.75,"duration_s":6.0},{"text":"The older half, the Town Hall, had its foundation stone laid in 1855 after the colony's previous theatre fell into disrepair; designed by municipal engineer John Bennett, it opened in 1862 with a theatre downstairs and government offices upstairs, and housed Singapore's public library until 1876.","offset_s":43.75,"duration_s":22.6},{"text":"After Queen Victoria died in 1901, a public meeting held inside that same Town Hall resolved to build her a memorial hall next door — designed by colonial engineer Alexander Murray and completed by R.A.J.","offset_s":66.35,"duration_s":15.525},{"text":"Bidwell of Swan & Maclaren in Palladian style, opened in October 1905, and joined to the older building by a 54-metre clock tower finished the following year.","offset_s":81.875,"duration_s":12.35},{"text":"The extra construction funds went toward renovating the old Town Hall to match, and it reopened in 1909, renamed Victoria Theatre, with a staging of *The Pirates of Penzance*.","offset_s":94.225,"duration_s":13.8},{"text":"For over three decades it stayed exactly what it looked like: a civic hall for concerts, meetings and public events.","offset_s":108.025,"duration_s":7.9},{"text":"That changed in December 1941, when a Japanese bomb struck the colonnade before Singapore had even surrendered.","offset_s":115.925,"duration_s":8.775},{"text":"Early in the occupation the buildings served as a makeshift hospital for the wounded; once the fighting ended, the new administration moved the Raffles statue out to erase the most visible symbol of colonial rule, renamed the complex Syonan Kokkaido — \"Public Hall of the Light of the South\" — and turned it into a stage for Japanese culture, hosting noh and kabuki performances and concerts as part of the propaganda for Japan's \"Greater East Asia Co-Prosperity Sphere.\"","offset_s":124.7,"duration_s":27.4},{"text":"Within two years, the same hall was staging something entirely different.","offset_s":152.1,"duration_s":5.225},{"text":"From 1946 to 1947, it hosted British military tribunals trying Japanese officers for war crimes — including, in a case tied directly to the Sook Ching massacre and Blood Debt settlement already covered on this blog, the trial of seven officers between 10 March and 2 April 1947.","offset_s":157.325,"duration_s":21.9},{"text":"Lieutenant-General Kawamura Saburo, the garrison commander, and Lieutenant-Colonel Oishi Masayuki, the Kempeitai commander who had overseen the killings, were both sentenced to death; the other five received life imprisonment.","offset_s":179.225,"duration_s":15.0},{"text":"Kawamura and Oishi were hanged on 26 June 1947, with only six family members of their victims permitted to witness it.","offset_s":194.225,"duration_s":10.025},{"text":"The room that had staged Japanese cultural propaganda in 1943 was, by 1947, the room where the men responsible for the killings were sentenced to die for it.","offset_s":204.25,"duration_s":12.75},{"text":"After the trials, the hall went straight back to ordinary civic life — briefing election officials and counting ballots from 1948, hosting two public hearings of the constitutional Rendel Commission in the 1950s, and, on 21 November 1954, hosting the newly formed People's Action Party's first-ever meeting.","offset_s":217.0,"duration_s":22.4},{"text":"A 1952–58 renovation added air-conditioning and soundproofing; Singapore's first television broadcasts launched from the hall in 1963; and a further 1979 renovation, which enlarged its seating and renamed the Memorial Hall the Victoria Concert Hall, made it the permanent home of the Singapore Symphony Orchestra — a role it still holds.","offset_s":239.4,"duration_s":24.6},{"text":"The building was gazetted a national monument in 1992, then closed again in 2010 for a four-year, S$158 million restoration that kept its original facade while rebuilding much of the interior, reopening in July 2014 with a performance by the very orchestra it now houses.","offset_s":264.0,"duration_s":21.8},{"text":"Nothing about a night at the concert hall today points back to 1943, or to 1947 — the building simply absorbed both and moved on, the way it had absorbed every previous identity before them.","offset_s":285.8,"duration_s":14.1},{"text":"Why it matters today: Most of Singapore's war memory sits in places built specifically to hold it — a memorial, a cemetery, a museum.","offset_s":299.9,"duration_s":9.775},{"text":"Victoria Theatre and Concert Hall never asked to be one of those places; it just kept being repurposed, by whoever held power at the time, for whatever that moment required — hospital, propaganda stage, courtroom, ballot-counting hall, party headquarters, concert venue — and each time, the building itself gave no sign of what had happened there before.","offset_s":309.675,"duration_s":21.95}];

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
    { t: 0, slide: 0 }, { t: 37.75, slide: 1 }, { t: 43.75, slide: 2 }, { t: 66.35, slide: 3 },
    { t: 94.225, slide: 4 }, { t: 124.7, slide: 5 }, { t: 152.1, slide: 6 }, { t: 194.225, slide: 7 },
    { t: 217.0, slide: 8 }, { t: 239.4, slide: 9 }, { t: 264.0, slide: 10 }, { t: 285.8, slide: 11 },
    { t: 299.9, slide: 12 }
  ];
  var TOTAL_DURATION = 331.625;
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

![Victoria Theatre and Victoria Memorial Hall, photographed as a postcard in the 1930s](https://upload.wikimedia.org/wikipedia/commons/e/e6/Victoria_Theatre_and_Victoria_Memorial_Hall_-_c_1930.jpg)

*Victoria Theatre and Victoria Memorial Hall, photographed for a postcard in the 1930s. (Photo: National Archives of Singapore / Wikimedia Commons, public domain)*

![Map showing the location of Victoria Theatre and Concert Hall within Singapore's Civic District](/assets/images/osm-victoria-theatre-concert-hall-location.png)

*Victoria Theatre and Concert Hall sits on the Singapore River, between the Padang and Boat Quay, in the heart of the Civic District. (Map data: © OpenStreetMap contributors)*

The complex began as two separate civic projects joined almost by accident. The older half, the Town Hall, had its foundation stone laid in 1855 after the colony's previous theatre fell into disrepair; designed by municipal engineer John Bennett, it opened in 1862 with a theatre downstairs and government offices upstairs, and housed Singapore's public library until 1876. After Queen Victoria died in 1901, a public meeting held inside that same Town Hall resolved to build her a memorial hall next door — designed by colonial engineer Alexander Murray and completed by R.A.J. Bidwell of Swan & Maclaren in Palladian style, opened in October 1905, and joined to the older building by a 54-metre clock tower finished the following year. The extra construction funds went toward renovating the old Town Hall to match, and it reopened in 1909, renamed Victoria Theatre, with a staging of *The Pirates of Penzance*.

![Victoria Theatre and Memorial Hall, Singapore, photographed circa 1900](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/KITLV_-_33196_-_Victoria_Theatre_and_Memorial_Hall_in_Singapore_-_circa_1900.tif/lossy-page1-1280px-KITLV_-_33196_-_Victoria_Theatre_and_Memorial_Hall_in_Singapore_-_circa_1900.tif.jpg)

*Victoria Theatre and Memorial Hall on an early postcard. Commons dates this to circa 1900, though the completed clock tower — finished in 1906 — suggests it's from somewhat later. (Photo: Leiden University Libraries / KITLV, via Wikimedia Commons, public domain)*

For over three decades it stayed exactly what it looked like: a civic hall for concerts, meetings and public events. That changed in December 1941, when a Japanese bomb struck the colonnade before Singapore had even surrendered. Early in the occupation the buildings served as a makeshift hospital for the wounded; once the fighting ended, the new administration moved the Raffles statue out to erase the most visible symbol of colonial rule, renamed the complex Syonan Kokkaido — "Public Hall of the Light of the South" — and turned it into a stage for Japanese culture, hosting noh and kabuki performances and concerts as part of the propaganda for Japan's "Greater East Asia Co-Prosperity Sphere."

![The Stamford Raffles statue outside Victoria Theatre and Concert Hall, photographed in 2004](https://upload.wikimedia.org/wikipedia/commons/5/5a/Victoria_Theatre_and_Concert_Hall_-_Stamford_Raffles_Statue_2004.jpg)

*The Stamford Raffles statue outside Victoria Theatre and Concert Hall, photographed in 2004 — long since restored to its plinth after the occupation-era administration moved it out. (Photo: Orderinchaos / Wikimedia Commons, CC BY-SA 4.0)*

Within two years, the same hall was staging something entirely different. From 1946 to 1947, it hosted British military tribunals trying Japanese officers for war crimes — including, in a case tied directly to [the Sook Ching massacre and Blood Debt settlement already covered on this blog](/2026/07/18/four-chopsticks-blood-debt-singapore-japan/), the trial of seven officers between 10 March and 2 April 1947. Lieutenant-General Kawamura Saburo, the garrison commander, and Lieutenant-Colonel Oishi Masayuki, the Kempeitai commander who had overseen the killings, were both sentenced to death; the other five received life imprisonment. Kawamura and Oishi were hanged on 26 June 1947, with only six family members of their victims permitted to witness it. The room that had staged Japanese cultural propaganda in 1943 was, by 1947, the room where the men responsible for the killings were sentenced to die for it.

![Victoria Theatre and Concert Hall, photographed in 1973 or 1974](https://upload.wikimedia.org/wikipedia/commons/7/78/Singapore-Victoria_Theatre_and_Concert_Hall-1973-74-WUS08256.jpg)

*Victoria Theatre and Concert Hall, photographed in 1973 or 1974, by then long restored to civic and cultural use. (Photo: Rainer Halama / Wikimedia Commons, CC BY-SA 4.0)*

After the trials, the hall went straight back to ordinary civic life — briefing election officials and counting ballots from 1948, hosting two public hearings of the constitutional Rendel Commission in the 1950s, and, on 21 November 1954, hosting the newly formed People's Action Party's first-ever meeting. A 1952–58 renovation added air-conditioning and soundproofing; Singapore's first television broadcasts launched from the hall in 1963; and a further 1979 renovation, which enlarged its seating and renamed the Memorial Hall the Victoria Concert Hall, made it the permanent home of the Singapore Symphony Orchestra — a role it still holds. [See six more historical photos related to this post →](/gallery/victoria-memorial-hall-culture-war-crimes-trials/)

![The reopened atrium entrance of Victoria Theatre and Concert Hall, photographed in 2014](https://upload.wikimedia.org/wikipedia/commons/8/80/Entrance_to_the_atrium_of_Victoria_Theatre_and_Concert_Hall%2C_Singapore_-_20141101-01.JPG)

*The reopened atrium entrance of Victoria Theatre and Concert Hall, photographed in November 2014, months after its S$158 million restoration. (Photo: Jacklee / Wikimedia Commons, CC BY-SA 4.0)*

The building was gazetted a national monument in 1992, then closed again in 2010 for a four-year, S$158 million restoration that kept its original facade while rebuilding much of the interior, reopening in July 2014 with a performance by the very orchestra it now houses. Nothing about a night at the concert hall today points back to 1943, or to 1947 — the building simply absorbed both and moved on, the way it had absorbed every previous identity before them.

**Why it matters today:** Most of Singapore's war memory sits in places built specifically to hold it — a memorial, a cemetery, a museum. Victoria Theatre and Concert Hall never asked to be one of those places; it just kept being repurposed, by whoever held power at the time, for whatever that moment required — hospital, propaganda stage, courtroom, ballot-counting hall, party headquarters, concert venue — and each time, the building itself gave no sign of what had happened there before.

---

**Sources:**
- [Victoria Theatre and Concert Hall — Singapore Infopedia, National Library Board](https://www.nlb.gov.sg/main/article-detail?cmsuuid=8472b2d8-5549-4858-912b-f6150b4bcae6)
- [Victoria Theatre and Concert Hall — Roots.gov.sg, National Heritage Board](https://www.roots.gov.sg/places/places-landing/Places/national-monuments/victoria-theatre-and-concert-hall)
- [Iconic architecture as vessel for political and cultural expression: Victoria Theatre and Concert Hall changing with Singapore cultural icon — Journal of Asian Architecture and Building Engineering](https://www.tandfonline.com/doi/full/10.1080/13467581.2024.2397123)
- [The Singapore War Crimes Trials: A Web Portal for All — Roots.gov.sg](https://www.roots.gov.sg/stories-landing/stories/the-singapore-war-crimes-trials-a-web-portal-for-all/story)
- [War Crimes Trials in Singapore — BiblioAsia, National Library Board](https://biblioasia.nlb.gov.sg/files/pdf/vol-11/issue-4/v11-issue4_WarCrimes.pdf)
- [Victoria Theatre and Concert Hall — Wikipedia](https://en.wikipedia.org/wiki/Victoria_Theatre_and_Concert_Hall)
- [File:Victoria Theatre and Victoria Memorial Hall - c 1930.jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Victoria_Theatre_and_Victoria_Memorial_Hall_-_c_1930.jpg)
- [File:Singapore-Victoria Theatre and Concert Hall-1973-74-WUS08256.jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Singapore-Victoria_Theatre_and_Concert_Hall-1973-74-WUS08256.jpg)
- [File:Entrance to the atrium of Victoria Theatre and Concert Hall, Singapore - 20141101-01.JPG — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Entrance_to_the_atrium_of_Victoria_Theatre_and_Concert_Hall,_Singapore_-_20141101-01.JPG)
- [File:Victoria Theatre Singapore May 1960.jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Victoria_Theatre_Singapore_May_1960.jpg)
- [File:VictoriaTheatreandMemorialHall-Singapore-1965.jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:VictoriaTheatreandMemorialHall-Singapore-1965.jpg)
- [File:Rear entrance of Victoria Theatre and Concert Hall, Singapore - 20141101.JPG — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Rear_entrance_of_Victoria_Theatre_and_Concert_Hall,_Singapore_-_20141101.JPG)
- [File:Front of Victoria Theatre, Singapore - 20141101-01.JPG — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Front_of_Victoria_Theatre,_Singapore_-_20141101-01.JPG)
- [File:Victoria Memorial Hall, Singapore, August 2023.jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Victoria_Memorial_Hall,_Singapore,_August_2023.jpg)
- [File:KITLV - 33196 - Victoria Theatre and Memorial Hall in Singapore - circa 1900.tif — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:KITLV_-_33196_-_Victoria_Theatre_and_Memorial_Hall_in_Singapore_-_circa_1900.tif)
- [File:KITLV A740 - Stadhuis te Singapore, KITLV 90268.tiff — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:KITLV_A740_-_Stadhuis_te_Singapore,_KITLV_90268.tiff)
- [File:Victoria Theatre and Concert Hall - Stamford Raffles Statue 2004.jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Victoria_Theatre_and_Concert_Hall_-_Stamford_Raffles_Statue_2004.jpg)
- [Victoria Theatre and Concert Hall (relation) — OpenStreetMap](https://www.openstreetmap.org/relation/3899820)

[← Back to all posts](/)
