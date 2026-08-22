---
layout: post
title: "The World-Famous Nightlife Strip Singapore Bulldozed for an MRT Station"
date: 2026-08-05 09:00:00 +0800
last_modified_at: 2026-08-22 01:00:00 +0800
categories: [history, present-day]
image: https://upload.wikimedia.org/wikipedia/commons/e/ec/New_Bugis_Street%2C_Singapore%2C_2014_%2801%29.JPG
---

On a good night in the 1970s, Bugis Street didn't quiet down until sunrise. Hawker stalls served fried noodles and cheap beer at rickety open-air tables, American sailors on leave from Vietnam mixed with British servicemen who'd nicknamed the place "Boogie Street," and after 11pm the crowd waited for the real spectacle: thirty or forty transgender women who gathered nightly to perform, pose for photos with tourists, and outshine everyone else on the strip. Newsweek wrote it up. Guidebooks called it unmissable. In October 1985, with little fanfare, Singapore bulldozed the whole street.

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
  <a href="https://youtu.be/Plpob2vL5fI" target="_blank" rel="noopener" aria-label="Watch this story as a video on YouTube" style="display: inline-flex; flex-direction: column; align-items: center; gap: 0.2em; text-decoration: none; color: inherit;">
    <span aria-hidden="true" style="display: inline-flex; align-items: center; justify-content: center; width: 2.4em; height: 2.4em; border-radius: 50%; border: 1px solid #888;">
      <svg width="1.4em" height="1.4em" viewBox="0 0 24 24" aria-hidden="true"><rect x="1" y="4" width="22" height="16" rx="5" fill="#FF0000"/><path d="M10 8.5l6 3.5-6 3.5z" fill="#fff"/></svg>
    </span>
    <span style="font-size: 0.7em; text-transform: uppercase; letter-spacing: 0.05em; opacity: 0.75;">YouTube</span>
  </a>
</div>

<audio id="listen-audio" preload="none" style="display: none;">
  <source src="/audio/bugis-street-before-redevelopment.mp3" type="audio/mpeg">
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
  var MARKET2014A = "https://upload.wikimedia.org/wikipedia/commons/e/ec/New_Bugis_Street%2C_Singapore%2C_2014_%2801%29.JPG";
  var MAP1890 = "https://upload.wikimedia.org/wikipedia/commons/c/cf/Guide_map_of_Singapore_Town_from_The_Stranger%27s_Guide_to_Singapore_%281890%29.jpg";
  var FOUNTAIN = "https://upload.wikimedia.org/wikipedia/commons/e/ea/BugisJunction_Fountain.JPG";
  var MARKET2014B = "https://upload.wikimedia.org/wikipedia/commons/4/4a/New_Bugis_Street%2C_Singapore%2C_2014_%2803%29.JPG";
  var MARKET2006 = "https://upload.wikimedia.org/wikipedia/commons/e/e7/Bugis_Street%2C_Aug_06.JPG";
  var JUNCTION2016 = "https://upload.wikimedia.org/wikipedia/commons/0/0a/2016-04-05_Bugis_Junction_01.jpg";
  var MARKETINSIDE2020 = "https://upload.wikimedia.org/wikipedia/commons/f/f3/Bugis_Street_Market.jpg";

  var slides = [
    { src: MARKET2014A, type: "cover", zoom: [1, 1.08, 1.15], pan: ["50% 45%", "50% 50%", "50% 55%"], ease: "ease-in-out" },
    { src: MAP1890, type: "cover", zoom: [1, 1.1, 1.2], pan: ["30% 40%", "50% 50%", "70% 60%"], ease: "linear" },
    { src: MAP1890, type: "cover", zoom: [1.2, 1.1, 1], pan: ["65% 60%", "50% 50%", "35% 40%"], ease: "linear" },
    { src: MARKET2006, type: "cover", zoom: [1, 1.09, 1.16], pan: ["35% 50%", "50% 50%", "65% 50%"], ease: "ease-out" },
    { src: MARKET2006, type: "cover", zoom: [1.16, 1.06, 1], pan: ["65% 55%", "50% 50%", "35% 45%"], ease: "ease-in" },
    { src: MARKETINSIDE2020, type: "cover", zoom: [1, 1.08, 1.15], pan: ["50% 40%", "50% 50%", "50% 60%"], ease: "ease-in-out" },
    { src: MARKETINSIDE2020, type: "cover", zoom: [1.15, 1.06, 1], pan: ["45% 55%", "50% 50%", "55% 45%"], ease: "ease-in" },
    { src: MARKET2014B, type: "cover", zoom: [1, 1.1, 1.18], pan: ["40% 50%", "50% 45%", "60% 40%"], ease: "ease-out" },
    { src: FOUNTAIN, type: "cover", zoom: [1, 1.08, 1.15], pan: ["50% 45%", "50% 50%", "50% 55%"], ease: "ease-in-out" },
    { src: JUNCTION2016, type: "cover", zoom: [1, 1.09, 1.16], pan: ["35% 50%", "50% 50%", "65% 50%"], ease: "ease-out" },
    { src: JUNCTION2016, type: "cover", zoom: [1.16, 1.06, 1], pan: ["65% 55%", "50% 50%", "35% 45%"], ease: "ease-in" },
    { src: MARKET2014A, type: "cover", zoom: [1.15, 1.06, 1], pan: ["55% 55%", "50% 50%", "45% 45%"], ease: "ease-in" },
    { src: MARKET2014B, type: "cover", zoom: [1, 1.08, 1.15], pan: ["45% 50%", "50% 55%", "55% 60%"], ease: "ease-in-out" },
    { src: MARKETINSIDE2020, type: "cover", zoom: [1, 1.06, 1.12], pan: ["50% 50%", "48% 50%", "46% 50%"], ease: "linear" },
    { src: FOUNTAIN, type: "cover", zoom: [1, 1.09, 1.16], pan: ["50% 60%", "50% 50%", "50% 40%"], ease: "ease-in-out" }
  ];

  // Real per-sentence timestamps captured for free from Kokoro TTS's own
  // per-sentence synthesis (see scripts/generate_narration.py) - drives
  // captions independently of image switching, in exact sync with speech.
  var sentences = [{"text":"The World-Famous Nightlife Strip Singapore Bulldozed for an MRT Station","offset_s":0.0,"duration_s":5.5},{"text":"On a good night in the 1970s, Bugis Street didn't quiet down until sunrise.","offset_s":5.5,"duration_s":6.225},{"text":"Hawker stalls served fried noodles and cheap beer at rickety open-air tables, American sailors on leave from Vietnam mixed with British servicemen who'd nicknamed the place \"Boogie Street,\" and after 11pm the crowd waited for the real spectacle: thirty or forty transgender women who gathered nightly to perform, pose for photos with tourists, and outshine everyone else on the strip.","offset_s":11.725,"duration_s":24.1},{"text":"Newsweek wrote it up.","offset_s":35.825,"duration_s":2.15},{"text":"Guidebooks called it unmissable.","offset_s":37.975,"duration_s":2.8},{"text":"In October 1985, with little fanfare, Singapore bulldozed the whole street.","offset_s":40.775,"duration_s":6.225},{"text":"The name is far older than any of that.","offset_s":47.0,"duration_s":3.5},{"text":"The street took its name from the Bugis, seafaring traders from South Sulawesi who settled nearby at Kampong Bugis from around 1820.","offset_s":50.5,"duration_s":10.325},{"text":"It shows up on an 1857 map as \"Charles Street,\" renamed \"Buggis Street\" by 1878.","offset_s":60.825,"duration_s":7.725},{"text":"For decades before that, the surrounding blocks — Bugis, Malay, Hylam and Malabar Streets — made up Singapore's licensed vice district: European sex workers operated there from the 1860s, followed from the 1870s by brothels staffed by *karayuki-san*, Japanese women trafficked into sex work, whose numbers peaked at around 130 brothels in 1904–05.","offset_s":68.55,"duration_s":26.3},{"text":"Licensed prostitution was abolished in 1920.","offset_s":94.85,"duration_s":4.65},{"text":"It was the hawkers who moved in after the Second World War who gave the street its second identity — an open-air run of food stalls between Victoria and Queen Streets that a 1957 *Singapore Free Press* article nicknamed \"the Montmartre of Singapore.\"","offset_s":99.5,"duration_s":18.4},{"text":"By the 1950s, Bugis Street's hawker stalls had become the stage for one of Singapore's most improbable subcultures.","offset_s":117.9,"duration_s":8.775},{"text":"Every night, dozens of transgender women — by most accounts 30 to 40 on a busy evening — gathered along the street to socialise, perform, and meet clients and tourists.","offset_s":126.675,"duration_s":11.95},{"text":"Contemporary newspapers called them \"transvestites\"; the common local term was \"ah kua\" (Hokkien), now considered dated and often derogatory, while several oral-history accounts have the women referring to each other simply as \"sisters.\"","offset_s":138.625,"duration_s":15.975},{"text":"They were disproportionately Malay relative to Singapore's population at the time, alongside Chinese and Indian women, and they built an entire informal economy around the street: sex work, paid photographs with curious tourists (who were charged roughly triple what locals paid), and nightly drag performances staged from around 11pm.","offset_s":154.6,"duration_s":21.975},{"text":"One of the best-documented figures, a woman named Shonna, worked her way from department-store sales girl to cabaret performer under the stage name \"Mama Chan,\" and in July 1971 underwent Singapore's — and one of Asia's — first sex-reassignment surgeries, at Kandang Kerbau Hospital.","offset_s":176.575,"duration_s":19.75},{"text":"The surgery hadn't come from nowhere: a Gender Identity Clinic had opened that same year, and for roughly three decades afterward Singapore was, unexpectedly, a regional leader in gender-reassignment medicine, drawing patients from Malaysia and Thailand.","offset_s":196.325,"duration_s":17.175},{"text":"Their legal footing was never secure.","offset_s":213.5,"duration_s":3.35},{"text":"Section 377A, enacted in 1938, criminalised sex between men but didn't target the community directly — it did, however, exclude them from the colony's licensed brothel system, which is part of why the trade around Bugis Street stayed informal and street-based to begin with.","offset_s":216.85,"duration_s":20.35},{"text":"Policing swung between tolerance and crackdown: in April 1977, police rounded up and registered more than 40 trans women in a single sweep, and in August 1980 the Vice Squad gave Bugis Street's trans sex workers a choice — move to Lorong 6 in Geylang, or face arrest — five years before the street itself came down.","offset_s":237.2,"duration_s":22.625},{"text":"The street had its own rituals, too.","offset_s":259.825,"duration_s":3.2},{"text":"Sailors on shore leave developed a signature stunt — climbing onto the roof of a public toilet near the street and performing what oral histories still call, half-affectionately, \"the Dance of the Flaming Arseholes,\" a lit-paper initiation passed down through service postings.","offset_s":263.025,"duration_s":17.75},{"text":"The toilet is long gone; the spot it stood on is now roughly where the fountain at Bugis Junction mall sits.","offset_s":280.775,"duration_s":7.7},{"text":"None of the street's fame saved it.","offset_s":288.475,"duration_s":2.7},{"text":"The Urban Redevelopment Authority's rezoning studies in the early 1980s concluded the area wouldn't be preserved, and the decisive push came from underground: Singapore's first MRT line needed a station at Victoria Street, and construction — which broke ground in December 1985 and opened Bugis MRT station in 1989 — meant clearing the old shophouses outright.","offset_s":291.175,"duration_s":25.15},{"text":"Bulldozers moved in that October.","offset_s":316.325,"duration_s":3.425},{"text":"The Straits Times captured the moment on 9 October 1985, reporting under the headline \"Bugis St to get new lease of life — on another site\" that \"Bugis Street as the world knows it dies tonight\" — even as the same piece broke the surprise news that the street would be reborn on another site rather than vanish for good.","offset_s":319.75,"duration_s":21.425},{"text":"Hawkers appealed to their member of parliament to save the street; the appeal failed, and stallholders were relocated elsewhere in Singapore.","offset_s":341.175,"duration_s":9.375},{"text":"The trans sex workers who'd defined the street's nightlife for three decades scattered too, mostly toward Geylang, where police had already been steering them for years.","offset_s":350.55,"duration_s":10.95},{"text":"Within weeks, press accounts noted only five or six trans women still working the old site after midnight, down from crowds that had once run to forty.","offset_s":361.5,"duration_s":11.025},{"text":"What eventually reopened bore the old name and little else.","offset_s":372.525,"duration_s":4.5},{"text":"By the early-to-mid 1990s, a pedestrianised shopping street had gone up near the original site, selling clothes and souvenirs under the Bugis Street name; Bugis Junction, the glass-roofed mall built over the old vice-district blocks a few streets over, opened in September 1995.","offset_s":377.025,"duration_s":20.05},{"text":"Today's Bugis Street market — expanded again in the 2000s — is one of the area's busiest tourist shopping stops.","offset_s":397.075,"duration_s":8.525},{"text":"What it isn't is the place a 2019 oral history recalled as somewhere \"Hollywood, Bollywood actors and actresses wanted to come see\" — and the trans women who made it that are largely missing from how the area explains its own history today; heritage signage nearby has been criticised for barely mentioning them at all.","offset_s":405.6,"duration_s":20.925},{"text":"Where it fits in the bigger story: Bugis Street's fame was real — Newsweek covered it, guidebooks recommended it, sailors mythologised it — and none of that fame was enough to save it, or to guarantee the community at its centre a place in how Singapore now tells the area's own history.","offset_s":426.525,"duration_s":18.2}];;

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
    { t: 0, slide: 0 }, { t: 35.825, slide: 1 }, { t: 68.55, slide: 2 }, { t: 94.85, slide: 3 },
    { t: 126.675, slide: 4 }, { t: 154.6, slide: 5 }, { t: 176.575, slide: 6 }, { t: 213.5, slide: 7 },
    { t: 259.825, slide: 8 }, { t: 288.475, slide: 9 }, { t: 319.75, slide: 10 }, { t: 341.175, slide: 11 },
    { t: 372.525, slide: 12 }, { t: 397.075, slide: 13 }, { t: 405.6, slide: 14 }
  ];
  var TOTAL_DURATION = 444.725;
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

![Bugis Street shopping market today](https://upload.wikimedia.org/wikipedia/commons/e/ec/New_Bugis_Street%2C_Singapore%2C_2014_%2801%29.JPG)

*The Queen Street entrance to today's Bugis Street market, photographed in 2014 — a pedestrianised shopping strip that reopened near the original site, selling clothes and souvenirs where the nightly drag spectacle used to be. (Photo: Bahnfrend / Wikimedia Commons, CC BY-SA 4.0)*

The name is far older than any of that. The street took its name from the Bugis, seafaring traders from South Sulawesi who settled nearby at Kampong Bugis from around 1820. It shows up on an 1857 map as "Charles Street," renamed "Buggis Street" by 1878. For decades before that, the surrounding blocks — Bugis, Malay, Hylam and Malabar Streets — made up Singapore's licensed vice district: European sex workers operated there from the 1860s, followed from the 1870s by brothels staffed by *karayuki-san*, Japanese women trafficked into sex work, whose numbers peaked at around 130 brothels in 1904–05. Licensed prostitution was abolished in 1920. It was the hawkers who moved in after the Second World War who gave the street its second identity — an open-air run of food stalls between Victoria and Queen Streets that a 1957 *Singapore Free Press* article nicknamed "the Montmartre of Singapore."

![Guide map of Singapore Town, 1890](https://upload.wikimedia.org/wikipedia/commons/c/cf/Guide_map_of_Singapore_Town_from_The_Stranger%27s_Guide_to_Singapore_%281890%29.jpg)

*A "Guide Map of Singapore Town" from 1890, showing Rochor and the streets around it — the district Bugis Street sat in — a little over a decade after the street's name was fixed on colonial maps. (Source: British Library, Flickr Commons / Wikimedia Commons, public domain)*

By the 1950s, Bugis Street's hawker stalls had become the stage for one of Singapore's most improbable subcultures. Every night, dozens of transgender women — by most accounts 30 to 40 on a busy evening — gathered along the street to socialise, perform, and meet clients and tourists. Contemporary newspapers called them "transvestites"; the common local term was "ah kua" (Hokkien), now considered dated and often derogatory, while several oral-history accounts have the women referring to each other simply as "sisters." They were disproportionately Malay relative to Singapore's population at the time, alongside Chinese and Indian women, and they built an entire informal economy around the street: sex work, paid photographs with curious tourists (who were charged roughly triple what locals paid), and nightly drag performances staged from around 11pm. One of the best-documented figures, a woman named Shonna, worked her way from department-store sales girl to cabaret performer under the stage name "Mama Chan," and in July 1971 underwent Singapore's — and one of Asia's — first sex-reassignment surgeries, at Kandang Kerbau Hospital. The surgery hadn't come from nowhere: a Gender Identity Clinic had opened that same year, and for roughly three decades afterward Singapore was, unexpectedly, a regional leader in gender-reassignment medicine, drawing patients from Malaysia and Thailand.

Their legal footing was never secure. Section 377A, enacted in 1938, criminalised sex between men but didn't target the community directly — it did, however, exclude them from the colony's licensed brothel system, which is part of why the trade around Bugis Street stayed informal and street-based to begin with. Policing swung between tolerance and crackdown: in April 1977, police rounded up and registered more than 40 trans women in a single sweep, and in August 1980 the Vice Squad gave Bugis Street's trans sex workers a choice — move to Lorong 6 in Geylang, or face arrest — five years before the street itself came down.

The street had its own rituals, too. Sailors on shore leave developed a signature stunt — climbing onto the roof of a public toilet near the street and performing what oral histories still call, half-affectionately, "the Dance of the Flaming Arseholes," a lit-paper initiation passed down through service postings. The toilet is long gone; the spot it stood on is now roughly where the fountain at Bugis Junction mall sits.

![Fountain at Bugis Junction](https://upload.wikimedia.org/wikipedia/commons/e/ea/BugisJunction_Fountain.JPG)

*The fountain at Bugis Junction mall, near the spot where sailors once staged Bugis Street's most notorious ritual. (Photo: Jpatokal / Wikimedia Commons, CC BY-SA 3.0)*

None of the street's fame saved it. The Urban Redevelopment Authority's rezoning studies in the early 1980s concluded the area wouldn't be preserved, and the decisive push came from underground: Singapore's first MRT line needed a station at Victoria Street, and construction — which broke ground in December 1985 and opened Bugis MRT station in 1989 — meant clearing the old shophouses outright. Bulldozers moved in that October. The Straits Times captured the moment on 9 October 1985, reporting under the headline "Bugis St to get new lease of life — on another site" that "Bugis Street as the world knows it dies tonight" — even as the same piece broke the surprise news that the street would be reborn on another site rather than vanish for good. Hawkers appealed to their member of parliament to save the street; the appeal failed, and stallholders were relocated elsewhere in Singapore. The trans sex workers who'd defined the street's nightlife for three decades scattered too, mostly toward Geylang, where police had already been steering them for years. Within weeks, press accounts noted only five or six trans women still working the old site after midnight, down from crowds that had once run to forty.

What eventually reopened bore the old name and little else. By the early-to-mid 1990s, a pedestrianised shopping street had gone up near the original site, selling clothes and souvenirs under the Bugis Street name; Bugis Junction, the glass-roofed mall built over the old vice-district blocks a few streets over, opened in September 1995. Today's Bugis Street market — expanded again in the 2000s — is one of the area's busiest tourist shopping stops. What it isn't is the place a 2019 oral history recalled as somewhere "Hollywood, Bollywood actors and actresses wanted to come see" — and the trans women who made it that are largely missing from how the area explains its own history today; heritage signage nearby has been criticised for barely mentioning them at all. [See more photos of the street today, and what replaced it →](/gallery/bugis-street-before-redevelopment/)

**Where it fits in the bigger story:** Bugis Street's fame was real — Newsweek covered it, guidebooks recommended it, sailors mythologised it — and none of that fame was enough to save it, or to guarantee the community at its centre a place in how Singapore now tells the area's own history.

---

**Sources:**
- [Bugis Street: From Sleazy to Sanitised — BiblioAsia, National Library Board](https://biblioasia.nlb.gov.sg/vol-11/issue-3/oct-dec-2015/bugis)
- [Bugis Street — Wikipedia](https://en.wikipedia.org/wiki/Bugis_Street)
- [Bugis Street: transgender aspects — Singapore LGBT Encyclopaedia](https://the-singapore-lgbt-encyclopaedia.fandom.com/wiki/Bugis_Street:_transgender_aspects)
- [Redevelopment of Bugis Street — Singapore LGBT Encyclopaedia](https://the-singapore-lgbt-encyclopaedia.fandom.com/wiki/Redevelopment_of_Bugis_Street)
- [A Gender Variance Who's Who: Trans Singapore Part 1 — Zagria](https://zagria.blogspot.com/2023/11/trans-singapore-part-1-to-first-sex.html)
- [Trans Woman Tells Us Stories of a Wilder Bugis Street — Kopi](https://thekopi.co/2019/02/16/bugis-street-history/)
- [Bugis Street was once the place to catch "The Dance of the Flaming Arseholes" — Mothership](https://mothership.sg/2017/10/bugis-street-was-once-the-place-to-catch-the-dance-of-the-flaming-arseholes/)
- [Bugis MRT station — Wikipedia](https://en.wikipedia.org/wiki/Bugis_MRT_station)
- [Bugis St to get new lease of life — on another site, The Straits Times, 9 October 1985 — NewspaperSG, National Library Board](https://eresources.nlb.gov.sg/newspapers/digitised/issue/straitstimes19851009-1)
- [Bugis Street to be cleared of transvestites, The Straits Times, 23 August 1980 — NewspaperSG, National Library Board](https://eresources.nlb.gov.sg/newspapers/digitised/issue/straitstimes19800823-1)
- [File:New Bugis Street, Singapore, 2014 (01).JPG — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:New_Bugis_Street,_Singapore,_2014_(01).JPG)
- [File:Guide map of Singapore Town from The Stranger's Guide to Singapore (1890).jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Guide_map_of_Singapore_Town_from_The_Stranger%27s_Guide_to_Singapore_(1890).jpg)
- [File:BugisJunction Fountain.JPG — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:BugisJunction_Fountain.JPG)
- [File:New Bugis Street, Singapore, 2014 (03).JPG — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:New_Bugis_Street,_Singapore,_2014_(03).JPG)
- [File:Bugis Street, Aug 06.JPG — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Bugis_Street,_Aug_06.JPG)
- [File:2016-04-05 Bugis Junction 01.jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:2016-04-05_Bugis_Junction_01.jpg)
- [File:Bugis Street Market.jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Bugis_Street_Market.jpg)

[← Back to all posts](/)
