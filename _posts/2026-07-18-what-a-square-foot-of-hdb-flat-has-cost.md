---
layout: post
title: "What a Square Foot of HDB Flat Has Cost, 1990–2026"
date: 2026-07-18
categories: [economy, present-day]
image: https://upload.wikimedia.org/wikipedia/commons/d/d3/HDB_flats_in_Singapore_2.jpg
---

A four-room HDB resale flat today goes for roughly $662 a square foot — for an 807 sqft unit, that's north of half a million dollars before you've even picked a floor. In 1990, the same square foot cost about $80. Most of the last thirty-five years of Singapore's economic history is hiding somewhere in the distance between those two numbers.

[← Back to all posts](/)

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

Then came the 2021–2026 run-up, the steepest on the chart. Part of it was low interest rates during the pandemic; part of it was 92 Build-To-Order projects — 75,800 flats — running about a year behind schedule because of COVID-era construction stoppages, with the last of them only finishing in early 2025. With new flats delayed, more buyers competed for the same resale supply, and prices rose almost 60% in five years, to where they sit today.

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

[← Back to all posts](/)
