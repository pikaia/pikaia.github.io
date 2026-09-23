---
layout: post
title: "How Opium Paid for Colonial Singapore"
date: 2026-09-23 09:00:00 +0800
last_modified_at: 2026-09-23 09:00:00 +0800
categories: [history]
image: https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Chinese_Protectorate%2C_Singapore%2C_KITLV_1404946.tiff/lossy-page1-1280px-Chinese_Protectorate%2C_Singapore%2C_KITLV_1404946.tiff.jpg
---

For most of the nineteenth century, the government that ran Singapore paid its bills with money from opium. Not through smuggling, and not by looking the other way, but openly: the colonial administration auctioned off the exclusive right to prepare and sell the drug to the highest bidder, and for decades the proceeds covered somewhere between 40 and 60 percent of everything the government spent. It was the single largest source of public revenue in a free port that famously charged no import duties, and the arrangement ran for well over a century before Singapore turned around and made the very trade that had funded it a crime.

[← Back to all posts](/)

<div id="listen-widget" role="button" tabindex="0" aria-label="Play audio narration of this post" style="display: inline-flex; flex-direction: column; align-items: center; cursor: pointer; gap: 0.2em; margin: 0.5em 0 1.5em 0; user-select: none;">
  <span id="listen-icon" aria-hidden="true" style="display: inline-flex; align-items: center; justify-content: center; width: 2.4em; height: 2.4em; border-radius: 50%; border: 1px solid #888; font-size: 1.3em;">&#127911;</span>
  <span style="font-size: 0.7em; text-transform: uppercase; letter-spacing: 0.05em; opacity: 0.75;">Listen</span>
  <audio id="listen-audio" preload="none" style="display: none;">
    <source src="/audio/how-opium-paid-for-colonial-singapore.mp3" type="audio/mpeg">
  </audio>
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

![The Chinese Protectorate building at the junction of Havelock Road and New Bridge Road, Singapore, photographed between 1906 and 1930, with rickshaws waiting outside](https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Chinese_Protectorate%2C_Singapore%2C_KITLV_1404946.tiff/lossy-page1-1280px-Chinese_Protectorate%2C_Singapore%2C_KITLV_1404946.tiff.jpg)

*The Chinese Protectorate building, Singapore, photographed sometime between 1906 and 1930. The Protectorate oversaw much of Chinese community life under colonial rule, including the labourers and shopkeepers who made up most of the opium trade's customers. (Photo: unknown photographer, KITLV/Leiden University Library, CC BY 4.0, via Wikimedia Commons)*

## The revenue farm

The system was called the revenue farm, and it began in 1820, a year after Raffles founded the settlement, when Resident William Farquhar introduced it as a quick way to raise money without imposing the kind of taxes that would have undercut Singapore's standing as a free port. Rather than run the opium trade itself, the government auctioned off a monopoly licence: whoever bid the highest sum, payable monthly in advance, won the exclusive right to import raw opium, boil it down into smokable chandu, and sell it retail through a network of licensed shops and dens. Everything the farmer collected above what he had bid was his to keep, and the government never had to touch the drug itself, only bank the cheque. The same auction system covered spirits, gambling and pawnbroking, but opium was by far the richest prize on offer.

## The Great Syndicate

<div style="float: left; max-width: 220px; width: 36%; margin: 0.25em 1.5em 1em 0;">
<img src="https://upload.wikimedia.org/wikipedia/commons/3/3d/Cheang_Hong_Lim.png" alt="Studio portrait of Cheang Hong Lim, seated, in traditional dress" style="width: 100%; display: block; border-radius: 4px;">
<em style="display: block; font-size: 0.8em; margin-top: 0.5em;">Cheang Hong Lim, the Great Syndicate's leading figure, from Song Ong Siang's 1923 book. (Photo: Song Ong Siang, One Hundred Years' History of the Chinese in Singapore, 1923, CC BY-SA 4.0, via Wikimedia Commons)</em>
</div>

By the 1870s, the biggest of these prizes had consolidated into the hands of a small group of Chinese businessmen known to colonial officials as the Great Syndicate. Its leading figure was Cheang Hong Lim, the eldest son of an already prominent merchant family. From 1871 to 1879, Cheang and his partners Tan Seng Poh and Tan Hiok Nee held not just Singapore's opium and spirit farms but Johor's, Melaka's and Riau's as well, running what amounted to a private cartel across the strait. Cheang was also, by the standards of the age, a generous public benefactor: in 1876 he funded the conversion of open ground in front of the police office into Singapore's first public garden, which was renamed Hong Lim Green in his honour and survives today as Hong Lim Park.

<div style="clear: both;"></div>

The syndicate's local farms sat on top of a much longer supply chain that made Singapore's position possible in the first place. Raw opium arrived from British India in two main grades: Bengal opium, grown around Patna and Benares and auctioned at Calcutta under a strict government monopoly, and Malwa opium, grown further west and auctioned at Bombay. With no tariffs of its own and a location roughly between both auction cities and the Chinese coast, Singapore became the key transshipment point where the two supplies merged before moving on to Chinese buyers. The trade could run at real scale: in one week in January 1836, four ships alone landed almost 3,900 chests of opium through the port.

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
  --series-2:       #008300;
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
    --series-2:       #1fa61f;
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
  --series-2:       #1fa61f;
  --border:         rgba(255,255,255,0.10);
}
.om-card { background: var(--surface-1); border: 1px solid var(--border); border-radius: 10px; padding: 20px 20px 12px; margin: 1.5em 0; }
.om-title { font-size: 16px; font-weight: 600; color: var(--text-primary); margin: 0 0 2px; }
.om-subtitle { font-size: 13px; color: var(--text-secondary); margin: 0 0 12px; }
.om-legend { display: flex; gap: 18px; flex-wrap: wrap; font-size: 12.5px; color: var(--text-secondary); margin: 0 0 10px; }
.om-legend-item { display: inline-flex; align-items: center; gap: 6px; }
.om-chart-wrap { position: relative; border-radius: 6px; overflow: hidden; }
.om-tooltip {
  position: absolute; pointer-events: none; background: var(--surface-1); border: 1px solid var(--border);
  border-radius: 8px; padding: 8px 10px; font-size: 12.5px; color: var(--text-primary);
  box-shadow: 0 4px 16px rgba(0,0,0,0.15); opacity: 0; transition: opacity 0.1s ease; max-width: 240px; z-index: 5;
}
.om-tooltip.visible { opacity: 1; }
.om-tooltip-val { font-weight: 600; }
.om-tooltip-label { color: var(--text-secondary); }
.om-foot { font-size: 11.5px; color: var(--text-muted); margin-top: 8px; }
.om-details { margin-top: 10px; }
.om-details summary { font-size: 12.5px; color: var(--text-secondary); cursor: pointer; }
.om-table { width: 100%; border-collapse: collapse; margin-top: 8px; font-size: 12.5px; }
.om-table th, .om-table td { text-align: left; padding: 4px 8px; border-bottom: 1px solid var(--grid); color: var(--text-primary); }
.om-table th { color: var(--text-secondary); font-weight: 600; }
.om-node-label { font-size: 16px; font-weight: 700; paint-order: stroke; stroke: var(--surface-1); stroke-width: 4px; stroke-linejoin: round; fill: var(--text-primary); }
.om-node-sub { font-size: 12.5px; paint-order: stroke; stroke: var(--surface-1); stroke-width: 4px; stroke-linejoin: round; fill: var(--text-secondary); }
</style>

<div class="om-card">
  <p class="om-title">Singapore, the hub of two opium networks</p>
  <p class="om-subtitle">Routes are approximate and not to scale; the map beneath them is a real OpenStreetMap extract</p>
  <div class="om-legend">
    <span class="om-legend-item"><svg width="22" height="10" aria-hidden="true"><line x1="0" y1="5" x2="22" y2="5" stroke="var(--series-1)" stroke-width="3"/></svg>Long-haul supply route, India to China</span>
    <span class="om-legend-item"><svg width="22" height="10" aria-hidden="true"><line x1="0" y1="5" x2="22" y2="5" stroke="var(--series-2)" stroke-width="3" stroke-dasharray="6,4"/></svg>The Great Syndicate's regional farm territories, 1871&ndash;79</span>
  </div>

  <div class="om-chart-wrap">
    <svg viewBox="0 0 1140 550" width="100%" height="auto" role="img" aria-label="A real map of South and Southeast Asia, with two opium networks drawn over it, centred on Singapore. Blue arrows show the long-haul supply route: raw opium travelled from Bombay, where Malwa opium was auctioned, and from Calcutta, where Bengal opium was auctioned, both in British India, converging on Singapore, then onward to the south China coast, the main market. Green dashed lines radiate from Singapore to Melaka, Johor and Riau, the three neighbouring territories where the Singapore-based Great Syndicate held the opium and spirit farm rights at the same time, from 1871 to 1879.">
      <image href="/assets/images/osm-opium-network-asia.jpg" x="0" y="0" width="1140" height="550" preserveAspectRatio="xMidYMid slice"/>
      <rect x="0" y="0" width="1140" height="550" fill="var(--surface-1)" opacity="0.08"/>

      <g fill="none" stroke="var(--series-1)" stroke-width="3.5" stroke-linecap="round" opacity="0.9">
        <path d="M 490,165 C 613.5,242.0 675.25,275.0 737,385"/>
        <path d="M 370,210 C 553.5,271.25 645.25,297.5 737,385"/>
        <path d="M 737,385 C 816.0,303.1 855.5,268.0 895,151"/>
      </g>
      <g fill="var(--series-1)" stroke="var(--surface-1)" stroke-width="1.5">
        <circle cx="370" cy="210" r="6"/>
        <circle cx="490" cy="165" r="6"/>
        <circle cx="895" cy="151" r="6"/>
      </g>

      <text class="om-node-label" x="370" y="210" dx="10" dy="-8" text-anchor="start">Bombay</text>
      <text class="om-node-sub" x="370" y="210" dx="10" dy="10" text-anchor="start">Malwa opium auctions</text>
      <text class="om-node-label" x="490" y="165" dx="10" dy="-8" text-anchor="start">Calcutta</text>
      <text class="om-node-sub" x="490" y="165" dx="10" dy="10" text-anchor="start">Bengal opium auctions</text>
      <text class="om-node-label" x="895" y="151" dx="10" dy="4" text-anchor="start">South China coast</text>

      <g fill="none" stroke="var(--series-2)" stroke-width="3" stroke-dasharray="7,5" stroke-linecap="round">
        <path d="M 737,385 L 650,340"/>
        <path d="M 737,385 L 733,345"/>
        <path d="M 737,385 L 765,435"/>
      </g>
      <g fill="var(--series-2)" stroke="var(--surface-1)" stroke-width="1.5">
        <circle cx="650" cy="340" r="5"/>
        <circle cx="733" cy="345" r="5"/>
        <circle cx="765" cy="435" r="5"/>
      </g>
      <text class="om-node-label" x="650" y="340" dx="-10" dy="-8" text-anchor="end">Melaka</text>
      <text class="om-node-label" x="733" y="345" dx="0" dy="-14" text-anchor="middle">Johor</text>
      <text class="om-node-label" x="765" y="435" dx="10" dy="16" text-anchor="start">Riau</text>

      <circle cx="737" cy="385" r="7" fill="var(--text-primary)" stroke="var(--surface-1)" stroke-width="2"/>
      <text class="om-node-label" x="737" y="385" dx="14" dy="5" text-anchor="start" font-size="18">Singapore</text>

      <g class="om-hits">
        <path d="M 490,165 C 613.5,242.0 675.25,275.0 737,385" fill="none" stroke="transparent" stroke-width="20" class="om-hit" tabindex="0" data-label="Calcutta &rarr; Singapore" data-val="Bengal opium, grown around Patna and Benares, was auctioned at Calcutta before shipment to Singapore."/>
        <path d="M 370,210 C 553.5,271.25 645.25,297.5 737,385" fill="none" stroke="transparent" stroke-width="20" class="om-hit" tabindex="0" data-label="Bombay &rarr; Singapore" data-val="Malwa opium, grown further west in India, was auctioned at Bombay before shipment to Singapore."/>
        <path d="M 737,385 C 816.0,303.1 855.5,268.0 895,151" fill="none" stroke="transparent" stroke-width="20" class="om-hit" tabindex="0" data-label="Singapore &rarr; South China coast" data-val="Singapore was the key transshipment point between India and China on this route. In one week in January 1836, four ships alone moved almost 3,900 chests of opium through the port."/>
        <path d="M 737,385 L 650,340" fill="none" stroke="transparent" stroke-width="16" class="om-hit" tabindex="0" data-label="Singapore &ndash; Melaka" data-val="One of the four territories where the Singapore-based Great Syndicate (Cheang Hong Lim, Tan Seng Poh, Tan Hiok Nee) held the opium and spirit farm rights, 1871&ndash;79."/>
        <path d="M 737,385 L 733,345" fill="none" stroke="transparent" stroke-width="16" class="om-hit" tabindex="0" data-label="Singapore &ndash; Johor" data-val="One of the four territories where the Singapore-based Great Syndicate (Cheang Hong Lim, Tan Seng Poh, Tan Hiok Nee) held the opium and spirit farm rights, 1871&ndash;79."/>
        <path d="M 737,385 L 765,435" fill="none" stroke="transparent" stroke-width="16" class="om-hit" tabindex="0" data-label="Singapore &ndash; Riau" data-val="One of the four territories where the Singapore-based Great Syndicate (Cheang Hong Lim, Tan Seng Poh, Tan Hiok Nee) held the opium and spirit farm rights, 1871&ndash;79."/>
      </g>
    </svg>
    <div class="om-tooltip"></div>
  </div>

  <p class="om-foot">Map data &copy; OpenStreetMap contributors. Routes and farm territories are schematic and drawn from the sources cited below the post.</p>

  <details class="om-details">
    <summary>View as table</summary>
    <table class="om-table">
      <thead><tr><th>Connection</th><th>Detail</th></tr></thead>
      <tbody>
        <tr><td>Calcutta &rarr; Singapore</td><td>Bengal opium, auctioned at Calcutta</td></tr>
        <tr><td>Bombay &rarr; Singapore</td><td>Malwa opium, auctioned at Bombay</td></tr>
        <tr><td>Singapore &rarr; South China coast</td><td>Singapore as transshipment point; almost 3,900 chests moved through the port in one week in January 1836</td></tr>
        <tr><td>Singapore &ndash; Melaka</td><td>Great Syndicate farm territory, 1871&ndash;79</td></tr>
        <tr><td>Singapore &ndash; Johor</td><td>Great Syndicate farm territory, 1871&ndash;79</td></tr>
        <tr><td>Singapore &ndash; Riau</td><td>Great Syndicate farm territory, 1871&ndash;79</td></tr>
      </tbody>
    </table>
  </details>
</div>

<script>
(function() {
  var card = document.currentScript.previousElementSibling;
  var svg = card.querySelector('svg');
  var wrap = svg.parentElement;
  var tooltip = wrap.querySelector('.om-tooltip');
  var hits = svg.querySelectorAll('.om-hit');

  hits.forEach(function(hit) {
    hit.addEventListener('pointerenter', show);
    hit.addEventListener('focus', show);
    hit.addEventListener('pointerleave', hide);
    hit.addEventListener('blur', hide);

    function show() {
      tooltip.innerHTML = '<div class="om-tooltip-label">' + hit.getAttribute('data-label') + '</div>' +
        '<div class="om-tooltip-val">' + hit.getAttribute('data-val') + '</div>';
      var rectBox = hit.getBoundingClientRect();
      var wrapRect = wrap.getBoundingClientRect();
      var left = rectBox.left - wrapRect.left + rectBox.width / 2;
      tooltip.style.left = Math.min(Math.max(left - 100, 0), wrapRect.width - 240) + 'px';
      tooltip.style.top = Math.max(rectBox.top - wrapRect.top - 60, 0) + 'px';
      tooltip.classList.add('visible');
    }
    function hide() {
      tooltip.classList.remove('visible');
    }
  });
})();
</script>
</div>

## Money from a drug

All of this made opium a fiscal engine unlike anything else in the colony's budget. Across the nineteenth century and into the twentieth, opium revenue is estimated to have covered somewhere between 40 and 60 percent of the Straits Settlements government's entire income, not a niche source of funds but the backbone of it. The dependence went beyond ordinary domestic spending: in 1914, the Straits Settlements contributed the largest share of military funding of any Crown Colony to the Imperial Exchequer in London, and more than half of that contribution was drawn from opium revenue alone. A free port that prided itself on charging no duties was, in practice, running on a single drug.

## On the ground

<div style="float: left; max-width: 300px; width: 42%; margin: 0.25em 1.5em 1em 0;">
<img src="https://upload.wikimedia.org/wikipedia/commons/c/cf/Photographic_Views_of_Singapore_Plate_02_South_Bridge_Road.jpg" alt="South Bridge Road, Singapore, around 1900, showing the Sri Mariamman Temple gopuram, Masjid Jamae's minarets, rickshaws and horse-drawn carriages" style="width: 100%; display: block; border-radius: 4px;">
<em style="display: block; font-size: 0.8em; margin-top: 0.5em;">South Bridge Road, Singapore, around 1900. Licensed opium shops and dens did business along streets like this one throughout the farm era. (Photo: G.R. Lambert &amp; Co., c.1900, public domain, via Wikimedia Commons)</em>
</div>

That revenue was collected one pipe at a time. Licensed opium shops and dens lined South Bridge Road, Boat Quay, Amoy Street, Carpenter Street, Bugis Street and Malay Street, doing business openly under whichever syndicate held the current farm. The map below marks where the story played out on the ground: not just that den row through Chinatown, but Hong Lim Park a few streets over, and Havelock Road, where the Chinese Protectorate, the colonial body that oversaw much of Chinese community life, from newly arrived labourers to secret societies, moved into a new building in 1886, among the same population most exposed to the trade.

<div style="clear: both;"></div>

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
.om-card { background: var(--surface-1); border: 1px solid var(--border); border-radius: 10px; padding: 20px 20px 12px; margin: 1.5em 0; }
.om-title { font-size: 16px; font-weight: 600; color: var(--text-primary); margin: 0 0 2px; }
.om-subtitle { font-size: 13px; color: var(--text-secondary); margin: 0 0 12px; }
.om-chart-wrap { position: relative; border-radius: 6px; overflow: hidden; }
.om-tooltip {
  position: absolute; pointer-events: none; background: var(--surface-1); border: 1px solid var(--border);
  border-radius: 8px; padding: 8px 10px; font-size: 12.5px; color: var(--text-primary);
  box-shadow: 0 4px 16px rgba(0,0,0,0.15); opacity: 0; transition: opacity 0.1s ease; max-width: 260px; z-index: 5;
}
.om-tooltip.visible { opacity: 1; }
.om-tooltip-val { font-weight: 600; margin-bottom: 2px; }
.om-tooltip-label { color: var(--text-secondary); }
.om-foot { font-size: 11.5px; color: var(--text-muted); margin-top: 8px; }
.om-details { margin-top: 10px; }
.om-details summary { font-size: 12.5px; color: var(--text-secondary); cursor: pointer; }
.om-table { width: 100%; border-collapse: collapse; margin-top: 8px; font-size: 12.5px; }
.om-table th, .om-table td { text-align: left; padding: 4px 8px; border-bottom: 1px solid var(--grid); color: var(--text-primary); }
.om-table th { color: var(--text-secondary); font-weight: 600; }
.om-node-label { font-size: 14.5px; font-weight: 700; paint-order: stroke; stroke: var(--surface-1); stroke-width: 4px; stroke-linejoin: round; fill: var(--text-primary); }
.om-node-sub { font-size: 12px; paint-order: stroke; stroke: var(--surface-1); stroke-width: 4px; stroke-linejoin: round; fill: var(--text-secondary); }
</style>

<div class="om-card">
  <p class="om-title">Places in the story, on the ground</p>
  <p class="om-subtitle">Locations are approximate; the map beneath them is a real OpenStreetMap extract of Singapore</p>

  <div class="om-chart-wrap">
    <svg viewBox="0 0 1221 571" width="100%" height="auto" role="img" aria-label="A real map of central and western Singapore marking five places from the opium trade's history: Chinatown and South Bridge Road, the retail row of opium dens and shops; Hong Lim Park, donated in 1876 by the opium farmer Cheang Hong Lim; Havelock Road, site of the Chinese Protectorate building; Queen Street, where an authorised opium shop operated during the Japanese Occupation; and Pasir Panjang, further west, site of the government's opium packing factory from 1930.">
      <image href="/assets/images/osm-opium-network-singapore.jpg" x="0" y="0" width="1221" height="571" preserveAspectRatio="xMidYMid slice"/>
      <rect x="0" y="0" width="1221" height="571" fill="var(--surface-1)" opacity="0.05"/>

      <line x1="418" y1="350" x2="762" y2="305" stroke="var(--series-1)" stroke-width="1.5" stroke-dasharray="3,5" opacity="0.35"/>

      <g fill="var(--series-1)" stroke="var(--surface-1)" stroke-width="1.5">
        <circle cx="762" cy="305" r="6"/>
        <circle cx="728" cy="258" r="6"/>
        <circle cx="652" cy="243" r="6"/>
        <circle cx="792" cy="198" r="6"/>
        <circle cx="418" cy="350" r="6"/>
      </g>

      <text class="om-node-label" x="762" y="305" dx="10" dy="4" text-anchor="start">Chinatown / South Bridge Rd</text>
      <text class="om-node-label" x="728" y="258" dx="10" dy="-8" text-anchor="start">Hong Lim Park</text>
      <text class="om-node-label" x="652" y="243" dx="-10" dy="4" text-anchor="end">Havelock Road</text>
      <text class="om-node-label" x="792" y="198" dx="0" dy="-14" text-anchor="middle">Queen Street</text>
      <text class="om-node-label" x="418" y="350" dx="0" dy="24" text-anchor="middle">Pasir Panjang</text>

      <g class="om-hits">
        <circle cx="762" cy="305" r="16" fill="transparent" class="om-hit" tabindex="0" data-label="Chinatown / South Bridge Road" data-val="Opium dens and shops lined South Bridge Road, Boat Quay, Amoy Street, Carpenter Street, Bugis Street and Malay Street &ndash; the retail end of a trade run under licence from whoever held the farm."/>
        <circle cx="728" cy="258" r="16" fill="transparent" class="om-hit" tabindex="0" data-label="Hong Lim Park" data-val="Singapore's first public garden, opened in 1876 after Cheang Hong Lim &ndash; the Great Syndicate's leading opium and spirit farmer &ndash; funded its creation."/>
        <circle cx="652" cy="243" r="16" fill="transparent" class="om-hit" tabindex="0" data-label="Havelock Road" data-val="Site of the Chinese Protectorate, the colonial body overseeing Chinese community affairs &ndash; labour, secret societies, welfare &ndash; among the same population most exposed to the opium trade."/>
        <circle cx="792" cy="198" r="16" fill="transparent" class="om-hit" tabindex="0" data-label="Queen Street" data-val="During the Japanese Occupation, an authorised chandu (prepared opium) shop operated here &ndash; the wartime administration, like the British before it, kept selling opium for revenue."/>
        <circle cx="418" cy="350" r="16" fill="transparent" class="om-hit" tabindex="0" data-label="Pasir Panjang" data-val="From 1930, the government's own packing factory here sealed measured doses of opium into small tins stamped with date and place of issue, tightening its grip on the retail supply."/>
      </g>
    </svg>
    <div class="om-tooltip"></div>
  </div>

  <p class="om-foot">Map data &copy; OpenStreetMap contributors.</p>

  <details class="om-details">
    <summary>View as table</summary>
    <table class="om-table">
      <thead><tr><th>Place</th><th>Connection to the opium trade</th></tr></thead>
      <tbody>
        <tr><td>Chinatown / South Bridge Road</td><td>Opium dens and shops along South Bridge Road, Boat Quay, Amoy Street, Carpenter Street, Bugis Street and Malay Street</td></tr>
        <tr><td>Hong Lim Park</td><td>Opened 1876, funded by opium farmer Cheang Hong Lim</td></tr>
        <tr><td>Havelock Road</td><td>Site of the Chinese Protectorate building</td></tr>
        <tr><td>Queen Street</td><td>Authorised wartime chandu shop, Japanese Occupation, 1942</td></tr>
        <tr><td>Pasir Panjang</td><td>Government opium packing factory, from 1930</td></tr>
      </tbody>
    </table>
  </details>
</div>

<script>
(function() {
  var card = document.currentScript.previousElementSibling;
  var svg = card.querySelector('svg');
  var wrap = svg.parentElement;
  var tooltip = wrap.querySelector('.om-tooltip');
  var hits = svg.querySelectorAll('.om-hit');

  hits.forEach(function(hit) {
    hit.addEventListener('pointerenter', show);
    hit.addEventListener('focus', show);
    hit.addEventListener('pointerleave', hide);
    hit.addEventListener('blur', hide);

    function show() {
      tooltip.innerHTML = '<div class="om-tooltip-val">' + hit.getAttribute('data-label') + '</div>' +
        '<div class="om-tooltip-label">' + hit.getAttribute('data-val') + '</div>';
      var rectBox = hit.getBoundingClientRect();
      var wrapRect = wrap.getBoundingClientRect();
      var left = rectBox.left - wrapRect.left + rectBox.width / 2;
      tooltip.style.left = Math.min(Math.max(left - 110, 0), wrapRect.width - 260) + 'px';
      tooltip.style.top = Math.max(rectBox.top - wrapRect.top - 70, 0) + 'px';
      tooltip.classList.add('visible');
    }
    function hide() {
      tooltip.classList.remove('visible');
    }
  });
})();
</script>
</div>

## Ending the farm

Organised opposition to the trade had been building for years before the government acted. Dr Lim Boon Keng, a physician and Legislative Council member, co-founded an Anti-Opium Society in 1906, the same year his associate S.C. Yin opened a refuge in Singapore to help addicts break the habit. The Singapore Anti-Opium Society was formally inaugurated in 1907, the same year a colonial Opium Commission was appointed to investigate the scale of the problem. Its 1909 findings led directly to the Chandu Revenue Ordinance, which abolished the private farm system outright: from then on, the government would prepare and sell opium itself, through a Monopolies Department formed the following year, rather than auction the privilege away.

Ending the private farm did not end the government's dependence on opium money overnight. It took until 1925 for the colony to formally commit to weaning itself off the revenue, when it set up the Opium Revenue Replacement Reserve Fund to absorb the coming shortfall, and 1930 before a purpose-built factory at Pasir Panjang began sealing measured doses into small, tamper-evident tins, stamped with date and place of issue, tightening the government's own grip on a retail trade it now ran directly.

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
  --series-2:       #008300;
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
    --series-2:       #1fa61f;
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
  --series-2:       #1fa61f;
  --border:         rgba(255,255,255,0.10);
}
.om-card { background: var(--surface-1); border: 1px solid var(--border); border-radius: 10px; padding: 20px 20px 12px; margin: 1.5em 0; }
.om-title { font-size: 16px; font-weight: 600; color: var(--text-primary); margin: 0 0 2px; }
.om-subtitle { font-size: 13px; color: var(--text-secondary); margin: 0 0 12px; }
.om-legend { display: flex; gap: 18px; flex-wrap: wrap; font-size: 12.5px; color: var(--text-secondary); margin: 0 0 4px; }
.om-legend-item { display: inline-flex; align-items: center; gap: 6px; }
.om-chart-wrap { position: relative; }
.om-tooltip {
  position: absolute; pointer-events: none; background: var(--surface-1); border: 1px solid var(--border);
  border-radius: 8px; padding: 8px 10px; font-size: 12.5px; color: var(--text-primary);
  box-shadow: 0 4px 16px rgba(0,0,0,0.15); opacity: 0; transition: opacity 0.1s ease; max-width: 260px; z-index: 5;
}
.om-tooltip.visible { opacity: 1; }
.om-tooltip-val { font-weight: 600; margin-bottom: 2px; }
.om-tooltip-label { color: var(--text-secondary); }
.om-foot { font-size: 11.5px; color: var(--text-muted); margin-top: 6px; }
.om-details { margin-top: 10px; }
.om-details summary { font-size: 12.5px; color: var(--text-secondary); cursor: pointer; }
.om-table { width: 100%; border-collapse: collapse; margin-top: 8px; font-size: 12.5px; }
.om-table th, .om-table td { text-align: left; padding: 4px 8px; border-bottom: 1px solid var(--grid); color: var(--text-primary); }
.om-table th { color: var(--text-secondary); font-weight: 600; }
.om-event-year { font-size: 13px; font-weight: 700; fill: var(--text-primary); }
.om-event-label { font-size: 12px; fill: var(--text-secondary); }
.om-axis-year { font-size: 11.5px; fill: var(--text-muted); }
</style>

<div class="om-card">
  <p class="om-title">Singapore's opium trade, start to end</p>
  <p class="om-subtitle">1820 to 1951 &ndash; from a private tax farm to a state monopoly to a crime</p>
  <div class="om-legend">
    <span class="om-legend-item"><svg width="16" height="12" aria-hidden="true"><rect x="0" y="2" width="16" height="8" rx="2" fill="var(--series-1)"/></svg>Privately farmed (auctioned to the highest bidder)</span>
    <span class="om-legend-item"><svg width="16" height="12" aria-hidden="true"><rect x="0" y="2" width="16" height="8" rx="2" fill="var(--series-2)"/></svg>Government monopoly</span>
    <span class="om-legend-item"><svg width="16" height="12" aria-hidden="true"><rect x="0" y="2" width="16" height="8" rx="2" fill="url(#om-hatch)"/></svg>Banned / criminalised</span>
  </div>

  <div class="om-chart-wrap">
    <svg viewBox="0 0 1160 340" width="100%" height="auto" role="img" aria-label="A timeline from 1820 to 1951 showing Singapore's opium trade moving through three phases. From 1820 to 1909 it was privately farmed: the right to sell opium was auctioned to the highest bidder, with the Great Syndicate of Cheang Hong Lim, Tan Seng Poh and Tan Hiok Nee holding the Singapore, Johor, Melaka and Riau farms from 1871 to 1879. In 1907 to 1909 an Opium Commission investigated the trade and the Chandu Revenue Ordinance ended the private farm system. From 1909 to 1946 the government ran opium as a state monopoly: the Monopolies Department took over production and retail in 1910, the Opium Revenue Replacement Reserve Fund was established in 1925 to wind down the colony's dependence on opium revenue, and a government packing factory opened at Pasir Panjang in 1930. From 1943 the trade was progressively banned: opium smoking was prohibited under the Japanese Occupation in 1943, the British banned consumption and possession in 1946, and the 1951 Dangerous Drugs Ordinance made consumption a criminal offence punishable by imprisonment.">
      <defs>
        <pattern id="om-hatch" width="7" height="7" patternTransform="rotate(45)" patternUnits="userSpaceOnUse">
          <rect width="7" height="7" fill="var(--grid)"/>
          <line x1="0" y1="0" x2="0" y2="7" stroke="var(--text-muted)" stroke-width="2"/>
        </pattern>
      </defs>

      <line x1="60" y1="163" x2="1100" y2="163" stroke="var(--axis)" stroke-width="1"/>
      <line x1="60" y1="177" x2="1100" y2="177" stroke="var(--axis)" stroke-width="1"/>
      <g class="om-axis-year" text-anchor="middle">
        <text x="97" y="200">1820</text>
        <text x="320" y="200">1860</text>
        <text x="617" y="200">1900</text>
        <text x="915" y="200">1940</text>
        <text x="1071" y="200">1951</text>
      </g>

      <rect x="97" y="163" width="662" height="14" fill="var(--series-1)"/>
      <rect x="759" y="163" width="275" height="14" fill="var(--series-2)"/>
      <rect x="1034" y="163" width="66" height="14" fill="url(#om-hatch)"/>

      <path d="M 476,177 L 476,206 L 536,206 L 536,177" fill="none" stroke="var(--text-secondary)" stroke-width="1.5"/>
      <text class="om-event-year" x="506" y="222" text-anchor="middle">1871&ndash;79</text>
      <text class="om-event-label" x="506" y="237" text-anchor="middle">The Great Syndicate holds the</text>
      <text class="om-event-label" x="506" y="251" text-anchor="middle">Singapore, Johor, Melaka &amp; Riau farms</text>

      <g class="om-hit" tabindex="0" data-label="1820" data-val="William Farquhar introduces the revenue farm system: the right to sell opium is auctioned to the highest bidder.">
        <line x1="97" y1="163" x2="97" y2="140" stroke="var(--text-secondary)" stroke-width="1.5"/>
        <circle cx="97" cy="140" r="4" fill="var(--series-1)"/>
        <text class="om-event-year" x="97" y="130" text-anchor="middle">1820</text>
        <text class="om-event-label" x="97" y="116" text-anchor="middle">introduced</text>
        <text class="om-event-label" x="97" y="102" text-anchor="middle">Farm system</text>
      </g>

      <g class="om-hit" tabindex="0" data-label="1907&ndash;09" data-val="An Opium Commission investigates the trade; the Chandu Revenue Ordinance ends the private farm system.">
        <line x1="751" y1="163" x2="751" y2="140" stroke="var(--text-secondary)" stroke-width="1.5"/>
        <circle cx="751" cy="140" r="4" fill="var(--series-1)"/>
        <text class="om-event-year" x="751" y="130" text-anchor="middle">1907&ndash;09</text>
        <text class="om-event-label" x="751" y="116" text-anchor="middle">system ends</text>
        <text class="om-event-label" x="751" y="102" text-anchor="middle">Commission; farm</text>
      </g>

      <g class="om-hit" tabindex="0" data-label="1910" data-val="The Monopolies Department takes over the production and retail sale of opium directly.">
        <line x1="766" y1="177" x2="766" y2="255" stroke="var(--text-secondary)" stroke-width="1.5"/>
        <circle cx="766" cy="255" r="4" fill="var(--series-2)"/>
        <text class="om-event-year" x="766" y="271" text-anchor="middle">1910</text>
        <text class="om-event-label" x="766" y="286" text-anchor="middle">Monopolies</text>
        <text class="om-event-label" x="766" y="300" text-anchor="middle">Dept formed</text>
      </g>

      <g class="om-hit" tabindex="0" data-label="1925" data-val="The Opium Revenue Replacement Reserve Fund is established, beginning a deliberate wind-down of the colony's dependence on opium revenue.">
        <line x1="877" y1="163" x2="877" y2="140" stroke="var(--text-secondary)" stroke-width="1.5"/>
        <circle cx="877" cy="140" r="4" fill="var(--series-2)"/>
        <text class="om-event-year" x="877" y="130" text-anchor="middle">1925</text>
        <text class="om-event-label" x="877" y="116" text-anchor="middle">begins wind-down</text>
        <text class="om-event-label" x="877" y="102" text-anchor="middle">Reserve Fund</text>
      </g>

      <g class="om-hit" tabindex="0" data-label="1930" data-val="A government packing factory at Pasir Panjang seals measured doses of opium into tins stamped with date and place of issue.">
        <line x1="915" y1="177" x2="915" y2="255" stroke="var(--text-secondary)" stroke-width="1.5"/>
        <circle cx="915" cy="255" r="4" fill="var(--series-2)"/>
        <text class="om-event-year" x="915" y="271" text-anchor="middle">1930</text>
        <text class="om-event-label" x="915" y="286" text-anchor="middle">Pasir Panjang</text>
        <text class="om-event-label" x="915" y="300" text-anchor="middle">packing factory</text>
      </g>

      <g class="om-hit" tabindex="0" data-label="1943&ndash;46" data-val="Opium smoking is prohibited under the Japanese Occupation in November 1943; the British ban consumption and possession outright in 1946.">
        <line x1="1023" y1="163" x2="1023" y2="140" stroke="var(--text-secondary)" stroke-width="1.5"/>
        <circle cx="1023" cy="140" r="4" fill="var(--text-secondary)"/>
        <text class="om-event-year" x="1023" y="130" text-anchor="middle">1943&ndash;46</text>
        <text class="om-event-label" x="1023" y="116" text-anchor="middle">occupier then coloniser</text>
        <text class="om-event-label" x="1023" y="102" text-anchor="middle">Banned, first by</text>
      </g>

      <g class="om-hit" tabindex="0" data-label="1951" data-val="The Dangerous Drugs Ordinance makes opium consumption a criminal offence punishable by imprisonment.">
        <line x1="1071" y1="177" x2="1071" y2="255" stroke="var(--text-secondary)" stroke-width="1.5"/>
        <circle cx="1071" cy="255" r="4" fill="var(--text-secondary)"/>
        <text class="om-event-year" x="1071" y="271" text-anchor="middle">1951</text>
        <text class="om-event-label" x="1071" y="286" text-anchor="middle">Consumption made</text>
        <text class="om-event-label" x="1071" y="300" text-anchor="middle">a criminal offence</text>
      </g>
    </svg>
    <div class="om-tooltip"></div>
  </div>

  <p class="om-foot">Dates from the sources cited below the post.</p>

  <details class="om-details">
    <summary>View as table</summary>
    <table class="om-table">
      <thead><tr><th>Date</th><th>Event</th></tr></thead>
      <tbody>
        <tr><td>1820</td><td>Revenue farm system introduced by William Farquhar</td></tr>
        <tr><td>1871&ndash;79</td><td>The Great Syndicate holds the Singapore, Johor, Melaka &amp; Riau opium and spirit farms</td></tr>
        <tr><td>1907&ndash;09</td><td>Opium Commission investigates; Chandu Revenue Ordinance ends the private farm system</td></tr>
        <tr><td>1910</td><td>Monopolies Department takes over production and retail</td></tr>
        <tr><td>1925</td><td>Opium Revenue Replacement Reserve Fund established</td></tr>
        <tr><td>1930</td><td>Government packing factory opens at Pasir Panjang</td></tr>
        <tr><td>1943&ndash;46</td><td>Opium smoking banned, first under the Japanese Occupation, then by the British</td></tr>
        <tr><td>1951</td><td>Dangerous Drugs Ordinance makes consumption a criminal offence</td></tr>
      </tbody>
    </table>
  </details>
</div>

<script>
(function() {
  var card = document.currentScript.previousElementSibling;
  var svg = card.querySelector('svg');
  var wrap = svg.parentElement;
  var tooltip = wrap.querySelector('.om-tooltip');
  var hits = svg.querySelectorAll('.om-hit');

  hits.forEach(function(hit) {
    hit.addEventListener('pointerenter', show);
    hit.addEventListener('focus', show);
    hit.addEventListener('pointerleave', hide);
    hit.addEventListener('blur', hide);

    function show() {
      tooltip.innerHTML = '<div class="om-tooltip-val">' + hit.getAttribute('data-label') + '</div>' +
        '<div class="om-tooltip-label">' + hit.getAttribute('data-val') + '</div>';
      var rectBox = hit.getBoundingClientRect();
      var wrapRect = wrap.getBoundingClientRect();
      var left = rectBox.left - wrapRect.left + rectBox.width / 2;
      tooltip.style.left = Math.min(Math.max(left - 110, 0), wrapRect.width - 260) + 'px';
      tooltip.style.top = Math.max(rectBox.top - wrapRect.top - 20, 0) + 'px';
      tooltip.classList.add('visible');
    }
    function hide() {
      tooltip.classList.remove('visible');
    }
  });
})();
</script>
</div>

## What it cost

What the trade cost the people who actually used it is harder to pin down than what it earned the government, which mostly counted money rather than lives. The 1907 Opium Commission itself found that the worst of the harm fell on the poor, who were often reduced to scraping and re-smoking the dregs of opium already used by others. Anti-opium campaigners like Lim Boon Keng had been making that same argument for years before the Commission sat.

It took a world war to finally end things. Opium smoking was banned outright under the Japanese Occupation in November 1943, and when the British returned they kept the wartime ban rather than reopen the old monopoly. By 1951, the Dangerous Drugs Ordinance had turned what was once a major line item in the government's own budget into a criminal offence punishable by imprisonment. The physician and social reformer Chen Su Lan, who was elected president of the Singapore Anti-Opium Society in 1930 and campaigned against the trade for decades afterward, lived to see it finally outlawed.

<div style="float: left; max-width: 260px; width: 40%; margin: 0.25em 1.5em 1em 0;">
<img src="https://upload.wikimedia.org/wikipedia/commons/6/6e/Tomb_of_Cheang_Hong_Lim.jpg" alt="The ornate tomb of Cheang Hong Lim, with carved stone panels and Chinese inscriptions, set against a hillside" style="width: 100%; display: block; border-radius: 4px;">
<em style="display: block; font-size: 0.8em; margin-top: 0.5em;">The tomb of Cheang Hong Lim, photographed in 2021. (Photo: Gavin Kia Wee Koh, CC BY-SA 4.0, via Wikimedia Commons)</em>
</div>

Cheang Hong Lim himself did not live to see any of this. He died in 1893, sixteen years before the farm system that had made his fortune was abolished. His tomb still stands today, and Hong Lim Park, the garden he funded, remains one of the few places in Singapore where the name of a nineteenth-century opium farmer is written plainly into the landscape rather than quietly left out of it.

<div style="clear: both;"></div>

**Where it fits in the bigger story:** Singapore's free port famously charged no import duties, and for most of its colonial history it did not need to. It had opium instead. The drug that other colonial governments fought to keep out of their own populations was, for Singapore, the single most reliable source of government income there was, until public pressure and a foreign occupation did what decades of reform commissions alone could not.

---

**Sources**

- [The Sticky Problem of Opium Revenue, BiblioAsia](https://biblioasia.nlb.gov.sg/vol-16/issue-3/oct-dec-2020/opium-revenue/)
- [Chasing the Dragon: The Scourge of Opium, BiblioAsia](https://biblioasia.nlb.gov.sg/vol-11/issue-3/oct-dec-2015/dragon/)
- [Of Towchangs and the "Republic Beard": Dr Lim Boon Keng's Life and Achievements, BiblioAsia](https://biblioasia.nlb.gov.sg/all-sections/vol-2-issue4-jan-2007-lim-boon-keng-towchang-beard/)
- [The Chinese Protectorate, National Library Board Singapore](https://www.nlb.gov.sg/main/article-detail?cmsuuid=04d3f708-c117-457a-9ea0-9717f9f03971)
- [History of Hong Lim Park, National Parks Board](https://www.nparks.gov.sg/visit/parks/hong-lim-park/special-features/history)
- [Cheang Hong Lim, Wikipedia](https://en.wikipedia.org/wiki/Cheang_Hong_Lim)
- [File:Chinese Protectorate, Singapore, KITLV 1404946.tiff, Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Chinese_Protectorate,_Singapore,_KITLV_1404946.tiff)
- [File:Cheang Hong Lim.png, Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Cheang_Hong_Lim.png)
- [File:Tomb of Cheang Hong Lim.jpg, Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Tomb_of_Cheang_Hong_Lim.jpg)
- [File:Photographic Views of Singapore Plate 02 South Bridge Road.jpg, Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Photographic_Views_of_Singapore_Plate_02_South_Bridge_Road.jpg)
- [OpenStreetMap contributors](https://www.openstreetmap.org/copyright)

[← Back to all posts](/)
