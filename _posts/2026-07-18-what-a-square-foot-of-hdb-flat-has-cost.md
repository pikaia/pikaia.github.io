---
layout: post
title: "What a Square Foot of HDB Flat Has Cost, 1990–2026"
date: 2026-07-18 11:00:00 +0800
last_modified_at: 2026-07-18 11:00:00 +0800
categories: [economy, present-day]
image: https://upload.wikimedia.org/wikipedia/commons/d/d3/HDB_flats_in_Singapore_2.jpg
---

A four-room HDB resale flat today goes for roughly $662 a square foot — for an 807 sqft unit, that's north of half a million dollars before you've even picked a floor. In 1990, the same square foot cost about $80. Most of the last thirty-five years of Singapore's economic history is hiding somewhere in the distance between those two numbers.

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
  <a href="https://youtu.be/bmIkTfx99kQ" target="_blank" rel="noopener" aria-label="Watch this story as a video on YouTube" style="display: inline-flex; flex-direction: column; align-items: center; gap: 0.2em; text-decoration: none; color: inherit;">
    <span aria-hidden="true" style="display: inline-flex; align-items: center; justify-content: center; width: 2.4em; height: 2.4em; border-radius: 50%; border: 1px solid #888;">
      <svg width="1.4em" height="1.4em" viewBox="0 0 24 24" aria-hidden="true"><rect x="1" y="4" width="22" height="16" rx="5" fill="#FF0000"/><path d="M10 8.5l6 3.5-6 3.5z" fill="#fff"/></svg>
    </span>
    <span style="font-size: 0.7em; text-transform: uppercase; letter-spacing: 0.05em; opacity: 0.75;">YouTube</span>
  </a>
</div>

<audio id="listen-audio" preload="none" style="display: none;">
  <source src="/audio/what-a-square-foot-of-hdb-flat-has-cost.mp3" type="audio/mpeg">
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
  var HERO = "https://upload.wikimedia.org/wikipedia/commons/d/d3/HDB_flats_in_Singapore_2.jpg";
  var KAMPONG1964 = "https://upload.wikimedia.org/wikipedia/commons/8/81/Kampong_in_Braddell_Hill_Singapore_about_1964.jpg";
  var STPAGE = "https://upload.wikimedia.org/wikipedia/commons/3/39/ST27May1961.jpg";
  var HOUSING1973A = "https://upload.wikimedia.org/wikipedia/commons/8/87/Singapore-Public_Housing-1973-74-WUS08215.jpg";
  var HOUSING1973B = "https://upload.wikimedia.org/wikipedia/commons/b/b9/Singapore-Public_Housing-1973-74-WUS08216.jpg";

  // Same data the post's own static chart uses (see the .hdb-psf-chart
  // script above) - duplicated here by design, same pattern as every
  // other Watch-widget data source on this site.
  var HDB_DATA = [[1990,80],[1991,81],[1992,90],[1993,132],[1994,170],[1995,209],[1996,285],[1997,293],[1998,243],[1999,231],[2000,242],[2001,221],[2002,212],[2003,218],[2004,226],[2005,224],[2006,227],[2007,246],[2008,298],[2009,320],[2010,359],[2011,408],[2012,440],[2013,464],[2014,431],[2015,419],[2016,420],[2017,424],[2018,420],[2019,419],[2020,440],[2021,496],[2022,538],[2023,571],[2024,615],[2025,658],[2026,662]];

  var slides = [
    { src: HERO, type: "cover", zoom: [1, 1.08, 1.15], pan: ["50% 45%", "50% 50%", "50% 55%"], ease: "ease-in-out" },
    { src: KAMPONG1964, type: "cover", zoom: [1, 1.09, 1.16], pan: ["40% 50%", "50% 50%", "60% 50%"], ease: "ease-out" },
    { src: HOUSING1973A, type: "cover", zoom: [1, 1.08, 1.15], pan: ["50% 40%", "50% 50%", "50% 60%"], ease: "ease-in-out" },
    { src: STPAGE, type: "letterbox", zoom: [1, 1.06, 1.12], pan: ["50% 50%", "50% 50%", "50% 50%"], ease: "linear" },
    {
      type: "chart",
      data: HDB_DATA,
      xRange: [1990, 2026],
      yRange: [0, 700],
      title: "Average resale price per square foot, 4-room HDB flats, Singapore-wide (1990–2026 YTD)",
      annotations: [[1990, 80, "$80 (1990)", "below"], [1997, 293, "$293 (1997)", "above"]],
      // Maps absolute post time -> current year at a pace matching what
      // each sentence actually says, not a uniform year-per-second rate -
      // mirrors year_checkpoints in scripts/video-configs/what-a-square-
      // foot-of-hdb-flat-has-cost.py exactly, so the live widget and the
      // exported video pace the same way. See that file for the reasoning
      // behind each checkpoint.
      yearCheckpoints: [
        [44.75, 1990], [61.45, 1997], [73.75, 2009], [77.675, 2009],
        [93.75, 2013], [110.45, 2013], [124.45, 2019], [131.75, 2021],
        [151.0, 2025], [161.425, 2026]
      ]
    },
    { src: HOUSING1973B, type: "cover", zoom: [1, 1.09, 1.16], pan: ["50% 55%", "50% 50%", "50% 45%"], ease: "ease-out" }
  ];

  // Real per-sentence timestamps captured for free from Kokoro TTS's own
  // per-sentence synthesis (see scripts/generate_narration.py) - drives
  // captions independently of image switching, in exact sync with speech.
  var sentences = [{"text":"What a Square Foot of HDB Flat Has Cost, 1990–2026","offset_s":0.0,"duration_s":7.5},{"text":"A four-room HDB resale flat today goes for roughly $662 a square foot — for an 807 sqft unit, that's north of half a million dollars before you've even picked a floor.","offset_s":7.5,"duration_s":14.9},{"text":"In 1990, the same square foot cost about $80.","offset_s":22.4,"duration_s":4.95},{"text":"Most of the last thirty-five years of Singapore's economic history is hiding somewhere in the distance between those two numbers.","offset_s":27.35,"duration_s":8.9},{"text":"Plotted out, the price isn't a straight line up — it moves in distinct eras, each one a response to something specific.","offset_s":36.25,"duration_s":8.5},{"text":"The first stretch, from 1990 to 1997, is a boom: prices more than tripled as the economy grew and the resale market matured, peaking at $293 a square foot right before the Asian Financial Crisis hit.","offset_s":44.75,"duration_s":16.7},{"text":"What follows is a decade of going nowhere — prices fell after the crisis and then just sat in the low $200s through SARS, the dot-com bust, and a generally cautious 2000s.","offset_s":61.45,"duration_s":12.3},{"text":"The next big move starts around 2009.","offset_s":73.75,"duration_s":3.925},{"text":"Interest rates fell sharply after the global financial crisis, and new supply hadn't kept pace with a fast-growing population — prices climbed almost every year, hitting $464 a square foot by 2013.","offset_s":77.675,"duration_s":16.075},{"text":"That run is also why the government's stamp-duty and loan curbs exist in their current form: the Additional Buyer's Stamp Duty arrived in December 2011, followed by the Total Debt Servicing Ratio framework in June 2013.","offset_s":93.75,"duration_s":16.7},{"text":"Prices flattened almost immediately after, sitting in a narrow $419–$440 band for the next six years — a rare stretch where policy visibly did what it was built to do.","offset_s":110.45,"duration_s":14.0},{"text":"Then came the 2021–2026 run-up, the steepest on the chart.","offset_s":124.45,"duration_s":7.3},{"text":"Part of it was low interest rates during the pandemic; part of it was 92 Build-To-Order projects — 75,800 flats — running about a year behind schedule because of COVID-era construction stoppages, with the last of them only finishing in early 2025.","offset_s":131.75,"duration_s":19.25},{"text":"With new flats delayed, more buyers competed for the same resale supply, and prices rose almost 60% in five years, to where they sit today.","offset_s":151.0,"duration_s":10.425},{"text":"Why it matters today: the shape of that line isn't just a market history — every kink in it marks a specific shock or policy response, most of which the people paying today's prices have never had reason to trace back to a chart.","offset_s":161.425,"duration_s":15.4}];;

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
    { t: 0, slide: 0 }, { t: 22.4, slide: 1 }, { t: 27.35, slide: 2 }, { t: 36.25, slide: 3 },
    { t: 44.75, slide: 4 }, { t: 161.425, slide: 5 }
  ];
  var TOTAL_DURATION = 176.825;
  var slideDurations = imageSchedule.map(function (entry, i) {
    var next = imageSchedule[i + 1];
    return (next ? next.t : TOTAL_DURATION) - entry.t;
  });

  var CHART_W = 1280, CHART_H = 720;
  var SVGNS = 'http://www.w3.org/2000/svg';
  function svgEl(tag, attrs) {
    var e = document.createElementNS(SVGNS, tag);
    for (var k in attrs) { e.setAttribute(k, attrs[k]); }
    return e;
  }

  // Builds the chart slide's SVG once (static axes/gridlines/title, the
  // price line itself hidden via a pathLength-normalized stroke-dashoffset
  // - same technique as the route-walk slide type's animated line) and
  // returns an update(progress) function that reveals more of the line,
  // moves the live end-dot/value readout, and reveals annotation dots as
  // the drawn line reaches them - mirrors compose_chart_frame() in
  // scripts/watch_video_lib.py exactly, so the live widget and the
  // exported video show the same animation. Added 2026-08-22 at Chris's
  // request, so the chart draws itself instead of appearing pre-finished.
  function buildChartSlide(s) {
    var svg = svgEl('svg', { viewBox: '0 0 ' + CHART_W + ' ' + CHART_H, width: '100%', height: '100%', preserveAspectRatio: 'xMidYMid slice' });
    svg.style.cssText = 'position:absolute;inset:0;background:#1a1a19;';

    var left = CHART_W * 0.09, right = CHART_W * 0.95, top = CHART_H * 0.16, bottom = CHART_H * 0.82;
    var xMin = s.xRange[0], xMax = s.xRange[1], yMin = s.yRange[0], yMax = s.yRange[1];
    function sx(yr) { return left + (yr - xMin) / (xMax - xMin) * (right - left); }
    function sy(v) { return top + (yMax - v) / (yMax - yMin) * (bottom - top); }
    var FONT = 'system-ui,-apple-system,"Segoe UI",sans-serif';

    if (s.title) {
      var titleEl = svgEl('text', { x: left, y: CHART_H * 0.08, fill: '#fff', 'font-size': CHART_H * 0.032, 'font-weight': '600', 'font-family': FONT });
      titleEl.textContent = s.title;
      svg.appendChild(titleEl);
    }

    var step = (yMax <= 800) ? 100 : 200;
    for (var v = 0; v <= yMax; v += step) {
      var y = sy(v);
      svg.appendChild(svgEl('line', { x1: left, x2: right, y1: y, y2: y, stroke: v === 0 ? '#383835' : '#2c2c2a', 'stroke-width': 1 }));
      var lt = svgEl('text', { x: left - 10, y: y + 4, fill: '#898781', 'font-size': CHART_H * 0.022, 'text-anchor': 'end', 'font-family': FONT });
      lt.textContent = '$' + v;
      svg.appendChild(lt);
    }
    for (var yr = xMin; yr <= xMax; yr += 5) {
      var x = sx(yr);
      var xt = svgEl('text', { x: x, y: bottom + CHART_H * 0.045, fill: '#898781', 'font-size': CHART_H * 0.022, 'text-anchor': 'middle', 'font-family': FONT });
      xt.textContent = String(yr);
      svg.appendChild(xt);
    }

    var d = s.data.map(function (p, i) { return (i === 0 ? 'M' : 'L') + sx(p[0]) + ',' + sy(p[1]); }).join(' ');
    var path = svgEl('path', {
      d: d, fill: 'none', stroke: '#3987e5', 'stroke-width': Math.max(2, CHART_H * 0.0035),
      'stroke-linejoin': 'round', 'stroke-linecap': 'round', 'pathLength': '1',
      'stroke-dasharray': '1', 'stroke-dashoffset': '1'
    });
    svg.appendChild(path);

    var annEls = (s.annotations || []).map(function (a) {
      var ax = sx(a[0]), ay = sy(a[1]);
      var r = Math.max(3, CHART_H * 0.006);
      var g = svgEl('g', { opacity: 0 });
      g.appendChild(svgEl('circle', { cx: ax, cy: ay, r: r, fill: '#3987e5', stroke: '#1a1a19', 'stroke-width': 2 }));
      var ly = a[3] === 'below' ? ay + r + 14 : ay - r - 6;
      var lbl = svgEl('text', { x: ax, y: ly, fill: '#c3c2b7', 'font-size': CHART_H * 0.02, 'text-anchor': 'middle', 'font-family': FONT });
      lbl.textContent = a[2];
      g.appendChild(lbl);
      svg.appendChild(g);
      return { year: a[0], el: g };
    });

    var dot = svgEl('circle', { r: Math.max(4, CHART_H * 0.007), fill: '#3987e5', stroke: '#1a1a19', 'stroke-width': 2, opacity: 0 });
    svg.appendChild(dot);
    var valText = svgEl('text', { fill: '#fff', 'font-size': CHART_H * 0.026, 'font-weight': '600', 'font-family': FONT, opacity: 0 });
    svg.appendChild(valText);
    var yearText = svgEl('text', { fill: '#c3c2b7', 'font-size': CHART_H * 0.02, 'font-family': FONT, opacity: 0 });
    svg.appendChild(yearText);

    function interpAt(year) {
      var data = s.data;
      if (year <= data[0][0]) return data[0][1];
      if (year >= data[data.length - 1][0]) return data[data.length - 1][1];
      for (var i = 0; i < data.length - 1; i++) {
        var y0 = data[i][0], v0 = data[i][1], y1 = data[i + 1][0], v1 = data[i + 1][1];
        if (y0 <= year && year <= y1) { var f = (y1 !== y0) ? (year - y0) / (y1 - y0) : 0; return v0 + (v1 - v0) * f; }
      }
      return data[data.length - 1][1];
    }

    // Generic piecewise-linear lookup - used to map absolute post time to
    // the chart's current year at whatever pace s.yearCheckpoints defines,
    // instead of a uniform progress*year rate. Mirrors piecewise_interp()
    // in scripts/watch_video_lib.py.
    function piecewiseInterp(checkpoints, x) {
      if (x <= checkpoints[0][0]) return checkpoints[0][1];
      if (x >= checkpoints[checkpoints.length - 1][0]) return checkpoints[checkpoints.length - 1][1];
      for (var i = 0; i < checkpoints.length - 1; i++) {
        var x0 = checkpoints[i][0], y0 = checkpoints[i][1], x1 = checkpoints[i + 1][0], y1 = checkpoints[i + 1][1];
        if (x0 <= x && x <= x1) { var f = (x1 !== x0) ? (x - x0) / (x1 - x0) : 0; return y0 + (y1 - y0) * f; }
      }
      return checkpoints[checkpoints.length - 1][1];
    }

    function update(t, progress) {
      path.setAttribute('stroke-dashoffset', String(1 - progress));
      var curYear = s.yearCheckpoints ? piecewiseInterp(s.yearCheckpoints, t) : xMin + (xMax - xMin) * progress;
      var curVal = interpAt(curYear);
      var ex = sx(curYear), ey = sy(curVal);
      dot.setAttribute('cx', ex); dot.setAttribute('cy', ey); dot.setAttribute('opacity', 1);
      var labelX = Math.min(ex + 14, right - CHART_W * 0.16);
      valText.setAttribute('x', labelX); valText.setAttribute('y', ey - CHART_H * 0.03);
      valText.textContent = '$' + Math.round(curVal) + ' / sqft'; valText.setAttribute('opacity', 1);
      yearText.setAttribute('x', labelX); yearText.setAttribute('y', ey - CHART_H * 0.005);
      yearText.textContent = String(Math.round(curYear)); yearText.setAttribute('opacity', 1);
      annEls.forEach(function (a) { a.el.setAttribute('opacity', curYear >= a.year - 0.01 ? 1 : 0); });
    }

    return { svg: svg, update: update };
  }

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

    if (s.type === 'chart') {
      var chart = buildChartSlide(s);
      el.appendChild(chart.svg);
      el._chartUpdate = chart.update;
    } else if (s.type === 'letterbox') {
      var bg = document.createElement('div');
      bg.style.cssText = 'position:absolute;inset:-8%;background-size:cover;background-position:center;filter:blur(30px) brightness(0.55);background-image:url(\'' + s.src + '\');';
      bg.style.animation = 'kb' + i + ' ' + dur + 's ' + ease + ' forwards';
      var fg = document.createElement('div');
      fg.style.cssText = 'position:absolute;inset:6%;background-size:contain;background-position:center;background-repeat:no-repeat;background-image:url(\'' + s.src + '\');';
      el.appendChild(bg);
      el.appendChild(fg);
      el._animTargets = [bg];
      styleEl.textContent += '@keyframes kb' + i + ' { 0% { transform: scale(' + s.zoom[0] + '); background-position: ' + s.pan[0] + '; } 50% { transform: scale(' + s.zoom[1] + '); background-position: ' + s.pan[1] + '; } 100% { transform: scale(' + s.zoom[2] + '); background-position: ' + s.pan[2] + '; } }\n';
    } else {
      var layer = document.createElement('div');
      layer.style.cssText = 'position:absolute;inset:-8%;background-size:cover;background-image:url(\'' + s.src + '\');';
      layer.style.animation = 'kb' + i + ' ' + dur + 's ' + ease + ' forwards';
      el.appendChild(layer);
      el._animTargets = [layer];
      styleEl.textContent += '@keyframes kb' + i + ' { 0% { transform: scale(' + s.zoom[0] + '); background-position: ' + s.pan[0] + '; } 50% { transform: scale(' + s.zoom[1] + '); background-position: ' + s.pan[1] + '; } 100% { transform: scale(' + s.zoom[2] + '); background-position: ' + s.pan[2] + '; } }\n';
    }

    stage.appendChild(el);
    return el;
  });

  slides.forEach(function (s) { if (s.src) { var img = new Image(); img.src = s.src; } });

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
    if (slideEls[sIdx]._chartUpdate) {
      var schedIdx = imageSchedule.findIndex(function (e) { return e.slide === sIdx; });
      var segStart = imageSchedule[schedIdx].t;
      var nextEntry = imageSchedule[schedIdx + 1];
      var segEnd = nextEntry ? nextEntry.t : TOTAL_DURATION;
      var chartProgress = Math.min(1, Math.max(0, (t - segStart) / Math.max(0.001, segEnd - segStart)));
      slideEls[sIdx]._chartUpdate(t, chartProgress);
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

![HDB flats in Singapore](https://upload.wikimedia.org/wikipedia/commons/d/d3/HDB_flats_in_Singapore_2.jpg)

*Public housing blocks in Singapore — home to about eight in ten residents, and the market this chart tracks. (Photo: ProjectManhattan / Wikimedia Commons, CC BY-SA 3.0)*

Plotted out, the price isn't a straight line up — it moves in distinct eras, each one a response to something specific.

<div class="hdb-psf-chart">
<style>
.hdb-psf-chart {
  --surface-1: #1a1a19;
  --text-primary: #ffffff;
  --text-secondary: #c3c2b7;
  --text-muted: #898781;
  --grid-line: #2c2c2a;
  --baseline: #383835;
  --series-1: #3987e5;
  --tooltip-bg: #0d0d0d;
  color-scheme: dark;
  background: var(--surface-1);
  border-radius: 8px;
  padding: 1.25em 1.25em 0.75em;
  margin: 1.5em 0;
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}
.hdb-psf-chart .hdb-psf-title {
  color: var(--text-primary);
  font-size: 0.95em;
  font-weight: 600;
  margin: 0 0 0.9em;
}
.hdb-psf-chart svg { display: block; width: 100%; height: auto; }
.hdb-psf-chart .hdb-grid { stroke: var(--grid-line); stroke-width: 1; }
.hdb-psf-chart .hdb-baseline { stroke: var(--baseline); stroke-width: 1; }
.hdb-psf-chart .hdb-tick { fill: var(--text-muted); font-size: 11px; }
.hdb-psf-chart .hdb-line { fill: none; stroke: var(--series-1); stroke-width: 2; stroke-linejoin: round; stroke-linecap: round; }
.hdb-psf-chart .hdb-endlabel { fill: var(--text-primary); font-size: 12px; font-weight: 600; }
.hdb-psf-chart .hdb-endlabel-sub { fill: var(--text-secondary); font-size: 10px; }
.hdb-psf-chart .hdb-peaklabel { fill: var(--text-secondary); font-size: 10px; }
.hdb-psf-chart .hdb-dot { fill: var(--series-1); stroke: var(--surface-1); stroke-width: 2; }
.hdb-psf-chart .hdb-crosshair { stroke: var(--text-muted); stroke-width: 1; stroke-dasharray: 2 2; opacity: 0; }
.hdb-psf-chart .hdb-hoverdot { fill: var(--series-1); stroke: var(--surface-1); stroke-width: 2; opacity: 0; }
.hdb-psf-chart .hdb-tooltip-bg { fill: var(--tooltip-bg); opacity: 0; }
.hdb-psf-chart .hdb-tooltip-year { fill: var(--text-secondary); font-size: 10px; opacity: 0; }
.hdb-psf-chart .hdb-tooltip-val { fill: var(--text-primary); font-size: 12px; font-weight: 600; opacity: 0; }
.hdb-psf-chart .hdb-hitrect { fill: transparent; cursor: crosshair; }
.hdb-psf-chart details { margin-top: 0.75em; }
.hdb-psf-chart summary { color: var(--text-secondary); font-size: 0.85em; cursor: pointer; }
.hdb-psf-chart table { width: 100%; border-collapse: collapse; margin-top: 0.6em; font-size: 0.85em; color: var(--text-secondary); }
.hdb-psf-chart th, .hdb-psf-chart td { text-align: right; padding: 2px 8px; border-bottom: 1px solid var(--grid-line); font-variant-numeric: tabular-nums; }
.hdb-psf-chart th:first-child, .hdb-psf-chart td:first-child { text-align: left; }
</style>

<p class="hdb-psf-title">Average resale price per square foot, 4-room HDB flats, Singapore-wide (1990&ndash;2026 YTD)</p>

<svg viewBox="0 0 720 380" role="img" aria-label="Line chart showing average HDB 4-room resale price per square foot rising from about $80 in 1990 to about $662 in 2026, with a peak of $293 in 1997 before the Asian Financial Crisis, a dip through the early 2000s, a run-up to $464 in 2013, a flat period through the late 2010s, and a sharp rise from 2021 to 2026.">
  <g id="hdb-gridlines"></g>
  <g id="hdb-xticks"></g>
  <path id="hdb-line" class="hdb-line"></path>
  <g id="hdb-annotations"></g>
  <line id="hdb-crosshair" class="hdb-crosshair" y1="24" y2="326"></line>
  <circle id="hdb-hoverdot" class="hdb-hoverdot" r="4"></circle>
  <g id="hdb-tooltip">
    <rect id="hdb-tooltip-bg" class="hdb-tooltip-bg" rx="4" width="86" height="34"></rect>
    <text id="hdb-tooltip-year" class="hdb-tooltip-year"></text>
    <text id="hdb-tooltip-val" class="hdb-tooltip-val"></text>
  </g>
  <rect id="hdb-hitrect" class="hdb-hitrect" x="46" y="24" width="610" height="302"></rect>
</svg>

<details>
<summary>View data as a table</summary>
<table>
<thead><tr><th>Year</th><th>$ / sqft</th></tr></thead>
<tbody>
<tr><td>1990</td><td>80</td></tr>
<tr><td>1991</td><td>81</td></tr>
<tr><td>1992</td><td>90</td></tr>
<tr><td>1993</td><td>132</td></tr>
<tr><td>1994</td><td>170</td></tr>
<tr><td>1995</td><td>209</td></tr>
<tr><td>1996</td><td>285</td></tr>
<tr><td>1997</td><td>293</td></tr>
<tr><td>1998</td><td>243</td></tr>
<tr><td>1999</td><td>231</td></tr>
<tr><td>2000</td><td>242</td></tr>
<tr><td>2001</td><td>221</td></tr>
<tr><td>2002</td><td>212</td></tr>
<tr><td>2003</td><td>218</td></tr>
<tr><td>2004</td><td>226</td></tr>
<tr><td>2005</td><td>224</td></tr>
<tr><td>2006</td><td>227</td></tr>
<tr><td>2007</td><td>246</td></tr>
<tr><td>2008</td><td>298</td></tr>
<tr><td>2009</td><td>320</td></tr>
<tr><td>2010</td><td>359</td></tr>
<tr><td>2011</td><td>408</td></tr>
<tr><td>2012</td><td>440</td></tr>
<tr><td>2013</td><td>464</td></tr>
<tr><td>2014</td><td>431</td></tr>
<tr><td>2015</td><td>419</td></tr>
<tr><td>2016</td><td>420</td></tr>
<tr><td>2017</td><td>424</td></tr>
<tr><td>2018</td><td>420</td></tr>
<tr><td>2019</td><td>419</td></tr>
<tr><td>2020</td><td>440</td></tr>
<tr><td>2021</td><td>496</td></tr>
<tr><td>2022</td><td>538</td></tr>
<tr><td>2023</td><td>571</td></tr>
<tr><td>2024</td><td>615</td></tr>
<tr><td>2025</td><td>658</td></tr>
<tr><td>2026 (YTD)</td><td>662</td></tr>
</tbody>
</table>
</details>

<p style="color: var(--text-muted); font-size: 0.8em; margin-top: 0.6em;">Computed from HDB's official resale transaction records (data.gov.sg), weighted average across all towns. 2026 figure is year-to-date.</p>
</div>

<script>
(function () {
  var data = [[1990,80],[1991,81],[1992,90],[1993,132],[1994,170],[1995,209],[1996,285],[1997,293],[1998,243],[1999,231],[2000,242],[2001,221],[2002,212],[2003,218],[2004,226],[2005,224],[2006,227],[2007,246],[2008,298],[2009,320],[2010,359],[2011,408],[2012,440],[2013,464],[2014,431],[2015,419],[2016,420],[2017,424],[2018,420],[2019,419],[2020,440],[2021,496],[2022,538],[2023,571],[2024,615],[2025,658],[2026,662]];

  var scope = document.currentScript.parentElement.querySelector('.hdb-psf-chart');
  if (!scope) { return; }

  var svgEl = scope.querySelector('svg');
  var left = 46, right = 656, top = 24, bottom = 326;
  var yMin = 0, yMax = 700;
  var xMin = 1990, xMax = 2026;

  function sx(year) { return left + (year - xMin) / (xMax - xMin) * (right - left); }
  function sy(val) { return top + (yMax - val) / (yMax - yMin) * (bottom - top); }

  var NS = 'http://www.w3.org/2000/svg';
  function el(tag, attrs) {
    var e = document.createElementNS(NS, tag);
    for (var k in attrs) { e.setAttribute(k, attrs[k]); }
    return e;
  }

  var gridG = scope.querySelector('#hdb-gridlines');
  for (var v = 0; v <= 700; v += 100) {
    var y = sy(v);
    gridG.appendChild(el('line', { class: v === 0 ? 'hdb-baseline' : 'hdb-grid', x1: left, x2: right, y1: y, y2: y }));
    var t = el('text', { class: 'hdb-tick', x: left - 8, y: y + 3, 'text-anchor': 'end' });
    t.textContent = '$' + v;
    gridG.appendChild(t);
  }

  var xG = scope.querySelector('#hdb-xticks');
  for (var yr = 1990; yr <= 2025; yr += 5) {
    var x = sx(yr);
    var t2 = el('text', { class: 'hdb-tick', x: x, y: bottom + 18, 'text-anchor': 'middle' });
    t2.textContent = String(yr);
    xG.appendChild(t2);
  }

  var d = data.map(function (p, i) { return (i === 0 ? 'M' : 'L') + sx(p[0]) + ',' + sy(p[1]); }).join(' ');
  scope.querySelector('#hdb-line').setAttribute('d', d);

  var annoG = scope.querySelector('#hdb-annotations');
  var peak = data.filter(function (p) { return p[0] === 1997; })[0];
  var px = sx(peak[0]), py = sy(peak[1]);
  annoG.appendChild(el('circle', { class: 'hdb-dot', cx: px, cy: py, r: 3 }));
  var peakLabel = el('text', { class: 'hdb-peaklabel', x: px, y: py - 10, 'text-anchor': 'middle' });
  peakLabel.textContent = '$293 (1997)';
  annoG.appendChild(peakLabel);

  var end = data[data.length - 1];
  var ex = sx(end[0]), ey = sy(end[1]);
  annoG.appendChild(el('circle', { class: 'hdb-dot', cx: ex, cy: ey, r: 4 }));
  var endLabel = el('text', { class: 'hdb-endlabel', x: ex - 4, y: ey - 12, 'text-anchor': 'end' });
  endLabel.textContent = '$662';
  annoG.appendChild(endLabel);
  var endSub = el('text', { class: 'hdb-endlabel-sub', x: ex - 4, y: ey - 24, 'text-anchor': 'end' });
  endSub.textContent = '2026 YTD';
  annoG.appendChild(endSub);

  var start = data[0];
  var stx = sx(start[0]), sty = sy(start[1]);
  annoG.appendChild(el('circle', { class: 'hdb-dot', cx: stx, cy: sty, r: 3 }));
  var startLabel = el('text', { class: 'hdb-peaklabel', x: stx + 6, y: sty + 14, 'text-anchor': 'start' });
  startLabel.textContent = '$80 (1990)';
  annoG.appendChild(startLabel);

  var hit = scope.querySelector('#hdb-hitrect');
  var crosshair = scope.querySelector('#hdb-crosshair');
  var hoverDot = scope.querySelector('#hdb-hoverdot');
  var tipBg = scope.querySelector('#hdb-tooltip-bg');
  var tipYear = scope.querySelector('#hdb-tooltip-year');
  var tipVal = scope.querySelector('#hdb-tooltip-val');

  function nearest(year) {
    var best = data[0], bestDist = Infinity;
    for (var i = 0; i < data.length; i++) {
      var dist = Math.abs(data[i][0] - year);
      if (dist < bestDist) { bestDist = dist; best = data[i]; }
    }
    return best;
  }

  function handleMove(clientX) {
    var rect = svgEl.getBoundingClientRect();
    var scale = 720 / rect.width;
    var svgX = (clientX - rect.left) * scale;
    var year = xMin + (svgX - left) / (right - left) * (xMax - xMin);
    year = Math.max(xMin, Math.min(xMax, year));
    var pt = nearest(year);
    var px2 = sx(pt[0]), py2 = sy(pt[1]);

    crosshair.setAttribute('x1', px2);
    crosshair.setAttribute('x2', px2);
    crosshair.style.opacity = 1;
    hoverDot.setAttribute('cx', px2);
    hoverDot.setAttribute('cy', py2);
    hoverDot.style.opacity = 1;

    var flip = px2 > (left + right) / 2;
    var boxW = 86, boxH = 34;
    var boxX = flip ? px2 - boxW - 10 : px2 + 10;
    var boxY = Math.max(top, py2 - boxH - 8);
    tipBg.setAttribute('x', boxX);
    tipBg.setAttribute('y', boxY);
    tipBg.setAttribute('width', boxW);
    tipBg.setAttribute('height', boxH);
    tipBg.style.opacity = 0.95;
    tipYear.setAttribute('x', boxX + 10);
    tipYear.setAttribute('y', boxY + 14);
    tipYear.textContent = String(pt[0]);
    tipYear.style.opacity = 1;
    tipVal.setAttribute('x', boxX + 10);
    tipVal.setAttribute('y', boxY + 27);
    tipVal.textContent = '$' + pt[1] + ' / sqft';
    tipVal.style.opacity = 1;
  }

  function handleLeave() {
    crosshair.style.opacity = 0;
    hoverDot.style.opacity = 0;
    tipBg.style.opacity = 0;
    tipYear.style.opacity = 0;
    tipVal.style.opacity = 0;
  }

  hit.addEventListener('pointermove', function (e) { handleMove(e.clientX); });
  hit.addEventListener('pointerleave', handleLeave);
  hit.addEventListener('touchmove', function (e) { if (e.touches[0]) { handleMove(e.touches[0].clientX); } }, { passive: true });
})();
</script>

The first stretch, from 1990 to 1997, is a boom: prices more than tripled as the economy grew and the resale market matured, peaking at $293 a square foot right before the Asian Financial Crisis hit. What follows is a decade of going nowhere — prices fell after the crisis and then just sat in the low $200s through SARS, the dot-com bust, and a generally cautious 2000s.

The next big move starts around 2009. Interest rates fell sharply after the global financial crisis, and new supply hadn't kept pace with a fast-growing population — prices climbed almost every year, hitting $464 a square foot by 2013. That run is also why the government's stamp-duty and loan curbs exist in their current form: the Additional Buyer's Stamp Duty arrived in December 2011, followed by the Total Debt Servicing Ratio framework in June 2013. Prices flattened almost immediately after, sitting in a narrow $419–$440 band for the next six years — a rare stretch where policy visibly did what it was built to do.

Then came the 2021–2026 run-up, the steepest on the chart. Part of it was low interest rates during the pandemic; part of it was 92 Build-To-Order projects — 75,800 flats — running about a year behind schedule because of COVID-era construction stoppages, with the last of them only finishing in early 2025. With new flats delayed, more buyers competed for the same resale supply, and prices rose almost 60% in five years, to where they sit today. [See four more historical photos related to this post →](/gallery/what-a-square-foot-of-hdb-flat-has-cost/)

**Why it matters today:** the shape of that line isn't just a market history — every kink in it marks a specific shock or policy response, most of which the people paying today's prices have never had reason to trace back to a chart.

---

**Sources:**
- [Resale Flat Prices (Based on Approval Date), 1990-1999 — data.gov.sg](https://data.gov.sg/datasets/d_ebc5ab87086db484f88045b47411ebc5/view)
- [Resale Flat Prices (Based on Approval Date), 2000-Feb 2012 — data.gov.sg](https://data.gov.sg/datasets/d_43f493c6c50d54243cc1eab0df142d6a/view)
- [Resale Flat Prices (Based on Registration Date), Mar 2012-Dec 2014 — data.gov.sg](https://data.gov.sg/datasets/d_2d5ff9ea31397b66239f245f57751537/view)
- [Resale Flat Prices (Based on Registration Date), Jan 2015-Dec 2016 — data.gov.sg](https://data.gov.sg/datasets/d_ea9ed51da2787afaf8e51f827c304208/view)
- [Resale Flat Prices (Based on Registration Date), Jan 2017 onwards — data.gov.sg](https://data.gov.sg/datasets/d_8b84c4ee58e3cfc0ece0d773c8ca6abc/view)
- [Property Cooling Measures In SG: Complete Timeline — DollarBack Mortgage](https://dollarbackmortgage.com/blog/property-cooling-measures-timeline/)
- [Singapore Cooling Measures — History since 2009 — StackedHomes](https://stackedhomes.com/editorial/singapore-cooling-measures-history/)
- [All Buyers of Last Two Pandemic-Delayed BTO Projects Have Been Scheduled to Collect Their Keys — HDB](https://www.hdb.gov.sg/about-us/news-and-publications/press-releases/All-Buyers-of-Last-Two-Pandemic-Delayed-BTO-Projects-Have-Been-Scheduled-to-Collect-Their-Keys)
- [All pandemic-delayed BTO projects are now completed. What's next? — 99.co](https://www.99.co/singapore/insider/pandemic-delayed-bto-projects/)
- [File:HDB flats in Singapore 2.jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:HDB_flats_in_Singapore_2.jpg)
- [File:Kampong in Braddell Hill Singapore about 1964.jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Kampong_in_Braddell_Hill_Singapore_about_1964.jpg)
- [File:ST27May1961.jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:ST27May1961.jpg)
- [File:Singapore-Public Housing-1973-74-WUS08215.jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Singapore-Public_Housing-1973-74-WUS08215.jpg)
- [File:Singapore-Public Housing-1973-74-WUS08216.jpg — Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Singapore-Public_Housing-1973-74-WUS08216.jpg)

[← Back to all posts](/)
