---
layout: post
title: "Barings, 1995: The Singapore Trading Desk That Broke a 233-Year-Old Bank"
date: 2026-10-02 03:02:24 +0800
last_modified_at: 2026-10-02 03:02:24 +0800
categories: [history]
image: https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Fire_of_Great_Hanshin_earthquake_Seen_from_Portisland.jpg/1280px-Fire_of_Great_Hanshin_earthquake_Seen_from_Portisland.jpg
---

On the afternoon of Thursday 23 February 1995, Nick Leeson told a colleague at Barings' office in Singapore that he had to visit his wife in hospital, and left. He did not come back. Leeson ran the bank's futures business on the Singapore International Monetary Exchange, known as SIMEX, and over two and a half years he had hidden mounting losses in an account numbered 88888. Three days later Barings, a London bank founded in 1762, was insolvent.

[← Back to all posts](/)

<div id="listen-widget" role="button" tabindex="0" aria-label="Play audio narration of this post" style="display: inline-flex; flex-direction: column; align-items: center; cursor: pointer; gap: 0.2em; margin: 0.5em 0 1.5em 0; user-select: none;">
  <span id="listen-icon" aria-hidden="true" style="display: inline-flex; align-items: center; justify-content: center; width: 2.4em; height: 2.4em; border-radius: 50%; border: 1px solid #888; font-size: 1.3em;">&#127911;</span>
  <span style="font-size: 0.7em; text-transform: uppercase; letter-spacing: 0.05em; opacity: 0.75;">Listen</span>
  <audio id="listen-audio" preload="none" style="display: none;">
    <source src="/audio/barings-1995-the-singapore-trading-desk-that-broke-a-233-year-old-bank.mp3" type="audio/mpeg">
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

![Smoke and flames rising over the port of Kobe at dawn, with cranes silhouetted against the sky](<https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Fire_of_Great_Hanshin_earthquake_Seen_from_Portisland.jpg/1280px-Fire_of_Great_Hanshin_earthquake_Seen_from_Portisland.jpg>)

*Fires burning in Kobe, seen from Port Island, after the earthquake of 17 January 1995. The earthquake set off the market fall that turned Leeson's hidden losses into the collapse of Barings. (Photo: City of Kobe, CC BY 2.1 JP, via Wikimedia Commons)*

## Britain's oldest merchant bank

<div style="float: left; max-width: 230px; width: 42%; margin: 0.25em 1.5em 1em 0;">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Sir_Francis_Baring%2C_1st_Baronet.jpg/1280px-Sir_Francis_Baring%2C_1st_Baronet.jpg" alt="A portrait of Sir Francis Baring, an elderly man in a dark coat seated with his hand raised to his ear" style="width: 100%; display: block; border-radius: 4px;">
<em style="display: block; font-size: 0.8em; margin-top: 0.5em;">Sir Francis Baring, who founded the bank in 1762, in an 1823 portrait by Charles Muss. (Image: Charles Muss, public domain, via Wikimedia Commons)</em>
</div>

Barings was founded in 1762 by Francis Baring, and by 1995 it was the oldest merchant bank in Britain. It had come close to failing once before. In 1890, heavy losses on Argentine debt threatened its solvency, and a consortium of banks was put together to rescue it. A century later it was a respected but old-fashioned house, still run from its head office on Bishopsgate in the City of London.

Barings' futures arm in Singapore, Baring Futures (Singapore), had been incorporated in 1986. It was a small unit, and for most of its life it attracted little attention in London.

<div style="clear: both;"></div>

## The star on the SIMEX floor

<div style="float: left; max-width: 240px; width: 42%; margin: 0.25em 1.5em 1em 0;">
<img src="https://upload.wikimedia.org/wikipedia/commons/5/53/OUB_Centre_3.JPG" alt="OUB Centre, a tall grey triangular office tower, seen from below against a blue sky" style="width: 100%; display: block; border-radius: 4px;">
<em style="display: block; font-size: 0.8em; margin-top: 0.5em;">OUB Centre at Raffles Place, where SIMEX had its trading floor from 1989. (Photo: Terence Ong, CC BY 2.5, via Wikimedia Commons)</em>
</div>

Leeson had joined Barings in London in 1989 as a clerk in its settlements department, the office that processes and records trades after they are made. He arrived in Singapore in April 1992 to manage the futures operation's paperwork, and after passing the Institute of Banking and Finance's futures trading test in June he began trading as well. In July 1992 Baring Futures (Singapore) started trading on SIMEX, whose trading floor was in OUB Centre at Raffles Place, with Leeson as one of its two traders.

On 3 July 1992 he opened an error account, numbered 88888. Error accounts are a normal part of a trading business, used to park small mistakes, such as a trade done at the wrong price, until they are sorted out. Leeson used this one to hide the losses on his own unauthorised trading. By the end of September 1992, according to the inspectors later appointed by Singapore's Minister for Finance, the account held losses of S$8.8 million.

In June 1993 Leeson was made general manager of Baring Futures (Singapore). He was in charge of the front office, which did the trading, and also of the back office, which processed and recorded it. The person placing the trades was therefore the same person checking them. An internal audit in July and August 1994 warned that this was a serious risk, but the bank kept Leeson in both roles because of his experience and the profits he appeared to be making. Those reported profits had made him a star in London. By the end of December 1994, the losses hidden in account 88888 had reached S$373.9 million.

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
.om-panel { font-size: 15px; font-weight: 700; fill: var(--text-primary); }
.om-panel-sub { font-size: 12px; fill: var(--text-muted); }
.om-event-year { font-size: 13px; font-weight: 700; fill: var(--text-primary); }
.om-event-label { font-size: 12px; fill: var(--text-secondary); }
.om-axis-year { font-size: 11.5px; fill: var(--text-muted); }
</style>

<div class="om-card">
  <p class="om-title">The losses hidden in account 88888, 1992&ndash;1995</p>
  <p class="om-subtitle">Singapore dollars; linear scale. Hover or tap a bar for details.</p>

  <div class="om-chart-wrap">
    <svg viewBox="0 0 900 286" width="100%" height="auto" role="img" aria-label="Bar chart of the losses hidden in Barings Futures Singapore's account 88888: S$8.8 million at the end of September 1992, S$373.9 million at the end of December 1994, S$1.4 billion on 23 February 1995 when Leeson left Singapore, and total losses of S$2.2 billion when Barings collapsed on 26 February 1995.">
      <g class="om-hit" tabindex="0" data-label="Sep 1992" data-val="End of September 1992: losses hidden in account 88888 had reached S$8.8 million, three months after Leeson opened it.">
      <text class="om-event-year" style="font-size:17px" x="286" y="29" text-anchor="end">Sep 1992</text>
      <text class="om-event-label" style="font-size:14px" x="286" y="47" text-anchor="end">three months after it opened</text>
      <rect x="300" y="14" width="3" height="32" rx="4" fill="var(--series-1)"/>
      <text class="om-event-year" style="font-size:17px" x="312" y="36">S$8.8 million</text>
      </g>
      <g class="om-hit" tabindex="0" data-label="Dec 1994" data-val="End of December 1994: S$373.9 million, a few months after an internal audit warned that Leeson ran both trading and settlement.">
      <text class="om-event-year" style="font-size:17px" x="286" y="91" text-anchor="end">Dec 1994</text>
      <text class="om-event-label" style="font-size:14px" x="286" y="109" text-anchor="end">after the internal audit</text>
      <rect x="300" y="76" width="69" height="32" rx="4" fill="var(--series-1)"/>
      <text class="om-event-year" style="font-size:17px" x="379" y="98">S$373.9 million</text>
      </g>
      <g class="om-hit" tabindex="0" data-label="23 Feb 1995" data-val="23 February 1995: with the Nikkei at 17,580, the losses had reached S$1.4 billion, and Leeson left Singapore that night.">
      <text class="om-event-year" style="font-size:17px" x="286" y="153" text-anchor="end">23 Feb 1995</text>
      <text class="om-event-label" style="font-size:14px" x="286" y="171" text-anchor="end">the day Leeson left</text>
      <rect x="300" y="138" width="258" height="32" rx="4" fill="var(--series-1)"/>
      <text class="om-event-year" style="font-size:17px" x="568" y="160">S$1.4 billion</text>
      </g>
      <g class="om-hit" tabindex="0" data-label="26 Feb 1995" data-val="26 February 1995: Barings' total losses came to S$2.2 billion when it was placed in administration.">
      <text class="om-event-year" style="font-size:17px" x="286" y="215" text-anchor="end">26 Feb 1995</text>
      <text class="om-event-label" style="font-size:14px" x="286" y="233" text-anchor="end">Barings' total losses</text>
      <rect x="300" y="200" width="405" height="32" rx="4" fill="var(--series-2)"/>
      <text class="om-event-year" style="font-size:17px" x="715" y="222">S$2.2 billion</text>
      </g>
      <line x1="300" y1="8" x2="300" y2="252" stroke="var(--axis)" stroke-width="1"/>
      <text class="om-axis-year" style="font-size:14px" x="300" y="274" text-anchor="middle">S$0</text>
      <text class="om-axis-year" style="font-size:14px" x="484" y="274" text-anchor="middle">S$1 billion</text>
      <text class="om-axis-year" style="font-size:14px" x="668" y="274" text-anchor="middle">S$2 billion</text>
    </svg>
    <div class="om-tooltip"></div>
  </div>

  <p class="om-foot">Source: &ldquo;Collapse of Barings&rdquo;, Infopedia (National Library Board), citing the report of the inspectors appointed by the Minister for Finance (1995).</p>

  <details class="om-details">
    <summary>View as table</summary>
    <table class="om-table">
      <thead><tr><th>When</th><th>Note</th><th>Losses</th></tr></thead>
      <tbody>
        <tr><td>Sep 1992</td><td>three months after it opened</td><td>S$8.8 million</td></tr>
        <tr><td>Dec 1994</td><td>after the internal audit</td><td>S$373.9 million</td></tr>
        <tr><td>23 Feb 1995</td><td>the day Leeson left</td><td>S$1.4 billion</td></tr>
        <tr><td>26 Feb 1995</td><td>Barings' total losses</td><td>S$2.2 billion</td></tr>
      </tbody>
    </table>
  </details>
</div>

<script>
(function() {
  var card = document.currentScript.previousElementSibling;
  var svg = card.querySelector('.om-chart-wrap svg') || card.querySelector('svg');
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

## Kobe

In January 1995 a senior auditor found a discrepancy in the Singapore accounts. Leeson explained it with a story about a trade with an American firm, Spear, Leeds & Kellogg, and produced a doctored payment statement to support it. In the same month, SIMEX alerted Barings to the size of its positions in Nikkei futures and options, the contracts that track Japan's main stock index. Barings' senior management told SIMEX that the bank had enough assets to back the trades.

<div style="float: left; max-width: 230px; width: 42%; margin: 0.25em 1.5em 1em 0;">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Hanshin-Awaji_earthquake_1995_Chuo-ku_Kobe_city_Hyogo_prefecture_350.jpg/1280px-Hanshin-Awaji_earthquake_1995_Chuo-ku_Kobe_city_Hyogo_prefecture_350.jpg" alt="A tall narrow building in Kobe leaning badly after the 1995 earthquake, with its lower floors crushed" style="width: 100%; display: block; border-radius: 4px;">
<em style="display: block; font-size: 0.8em; margin-top: 0.5em;">A building in Kobe's Chuo ward on the day of the earthquake, 17 January 1995. (Photo: Akiyoshi's Room, public domain, via Wikimedia Commons)</em>
</div>

Leeson's positions in early 1995 depended on the Nikkei 225 index not falling below about 19,000 points. At 5.46 in the morning on 17 January 1995, a powerful earthquake struck Kobe, killing more than 6,400 people. Japanese shares fell, and by 23 January the Nikkei was down to 17,785. Instead of cutting his losses, Leeson bought more, hoping the market would bounce back. It kept sliding, and on 23 February, when the index touched 17,580, his losses reached S$1.4 billion.

<div style="clear: both;"></div>

## Four days in February

That afternoon, a senior settlements clerk on secondment from London noticed the discrepancy in Leeson's account and asked him about it. Leeson said he had to go to the hospital, and that night he and his wife flew to Kuala Lumpur. At first his colleagues feared he had stolen money and disappeared. On 24 February they found account 88888.

Barings did not have the money to cover the losses. The Bank of England tried to arrange a rescue and failed, and on Sunday 26 February 1995 Barings was placed in administration, with total losses of S$2.2 billion. The next day SIMEX placed Baring Futures (Singapore) under interim judicial management. On 6 March the Dutch group ING completed its takeover of Barings, paying a nominal £1 and putting in £540 million to pay creditors.

![A street junction in the City of London in 1993, with stone office buildings, a red traffic light and a motorcycle courier](<https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Junction_of_Bishopsgate_and_Threadneedle_Street%2C_London%2C_July_1993.jpg/1280px-Junction_of_Bishopsgate_and_Threadneedle_Street%2C_London%2C_July_1993.jpg>)

*The junction of Bishopsgate and Threadneedle Street in the City of London in July 1993. Barings' head office stood on Bishopsgate. (Photo: Martin Wheatley, CC BY-SA 4.0, via Wikimedia Commons)*

Leeson and his wife went on from Kuala Lumpur to Sabah, and on 1 March they took a flight to Frankfurt by way of Brunei, Bangkok and Abu Dhabi. They were detained on arrival at Frankfurt airport on 2 March. Leeson first fought Singapore's request to extradite him, asking instead to be sent to Britain, but in October he decided to return to Singapore for trial. He was extradited on 23 November 1995. On 1 December he pleaded guilty to two charges of fraud and forgery, and was sentenced to six and a half years in prison. He was released on 3 July 1999 with remission for good behaviour.

## Singapore's side of the story

<div style="float: left; max-width: 230px; width: 42%; margin: 0.25em 1.5em 1em 0;">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/SGX_Centre%2C_Singapore_-_20121015.jpg/960px-SGX_Centre%2C_Singapore_-_20121015.jpg" alt="SGX Centre, a glass and steel office tower on Shenton Way, with trees in front" style="width: 100%; display: block; border-radius: 4px;">
<em style="display: block; font-size: 0.8em; margin-top: 0.5em;">SGX Centre on Shenton Way. SIMEX merged with the Stock Exchange of Singapore in 1999 to form the Singapore Exchange. (Photo: Nicolas Lannuzel, CC BY-SA 2.0, via Wikimedia Commons)</em>
</div>

The collapse was reported around the world as a London story, but the trading, the fraud and much of the investigation happened in Singapore. In early March the Commercial Affairs Department began a fraud investigation, and on 9 March the Minister for Finance, Richard Hu, appointed two inspectors to look into Baring Futures (Singapore). Their report, released on 17 October 1995, blamed Barings' senior management for failures that allowed Leeson's trades to go undetected, and found that SIMEX should have audited the firm sooner. In June 1996 the Commercial Affairs Department dropped its investigation into four other men, including two of Leeson's former supervisors, finding insufficient grounds for criminal charges.

SIMEX itself made no loss from the collapse, and no other financial institution in Singapore was affected. Even so, the Futures Trading Act was amended with effect from 1 April 1995, giving the Monetary Authority of Singapore closer oversight of futures traders and requiring them to be licensed, and further measures followed to strengthen the regulation of futures trading on SIMEX.

<div style="clear: both;"></div>

## A trader's view

At the time I was on the short-term interest rate trading desk at Security Pacific National Bank in Singapore, later part of Bank of America, and we were trading futures on SIMEX ourselves, so the scandal was the talk of the market. In the foreign exchange and money markets, Barings was not a name we came across much. It was known as a top British credit, and not much more. When the news broke, it sounded like a story you hear every so often in the markets: someone builds a reputation as a brilliant trader, and the results turn out to come from something illegal. The lesson I took from it, and never forgot, is that there is no such thing as a star trader. There are people who make money from speculation consistently, but they usually do it with a systematic approach to each day's trading, not by being stars.

## Could it happen again?

**Could it happen again?** The particular weakness at Barings Singapore, one person running both the trading and the settlement, is now ruled out in writing. The Monetary Authority of Singapore's guidelines on internal controls say a firm should have processes that stop any one member of staff from handling an entire transaction from start to finish, and they name trade execution combined with settlement and reconciliation as an example of inadequate separation of duties. Rogue trading has not disappeared, however. In January 2008 the French bank Société Générale announced losses of €4.9 billion from unauthorised trades by Jérôme Kerviel, and in September 2011 the Swiss bank UBS lost about US$2 billion through trades by Kweku Adoboli in London. Both banks survived, but in both cases the positions had grown very large before the bank's controls caught them. The [1914 run on a Singapore bank](/2026/10/01/the-run-on-the-banks-1914-when-war-in-europe-emptied-a-singapore-bank/) showed how quickly confidence can leave a bank; Barings showed how much damage one unchecked desk can do from inside it.

[See more photos related to this post →](/gallery/barings-1995-the-singapore-trading-desk-that-broke-a-233-year-old-bank/)

**Where it fits in the bigger story:** Barings is usually remembered as the bank that one man broke, but the controls that should have stopped him were missing on a trading floor at Raffles Place, and Singapore's own inspectors and lawmakers did much of the work of explaining what went wrong and tightening the rules afterwards. The most useful lesson from it is a simple one: a trader whose profits look too good to be true is a reason to look harder, not a reason to look away.

---

**Sources**

- [Collapse of Barings, Infopedia (National Library Board)](https://www.nlb.gov.sg/main/article-detail?cmsuuid=729d993f-496e-40c4-b65f-2c2a7368b6a6)
- [Baring Futures (Singapore) Pte Ltd: the report of the inspectors appointed by the Minister for Finance (1995), National Library Board catalogue](https://www.nlb.gov.sg/main/book-detail?cmsuuid=afc97ab2-d21f-470e-a1c1-4c2de3c57854)
- ["S'pore Report on Barings Collapse out Today", The Straits Times, 17 October 1995, page 1, NewspaperSG](https://eresources.nlb.gov.sg/newspapers/digitised/issue/straitstimes19951017-1)
- [Barings Bank, Wikipedia](https://en.wikipedia.org/wiki/Barings_Bank)
- [Nick Leeson, Wikipedia](https://en.wikipedia.org/wiki/Nick_Leeson)
- [Doubling: Nick Leeson's trading strategy, Stein, Brown and others (NYU Stern)](https://pages.stern.nyu.edu/~sbrown/leeson.PDF)
- [One Raffles Place (formerly OUB Centre), Wikipedia](https://en.wikipedia.org/wiki/One_Raffles_Place)
- [1995 Great Hanshin earthquake, Wikipedia](https://en.wikipedia.org/wiki/Great_Hanshin_earthquake)
- [Guidelines on Risk Management Practices: Internal Controls, Monetary Authority of Singapore, July 2024](https://www.mas.gov.sg/-/media/mas/regulations-and-financial-stability/regulatory-and-supervisory-framework/risk-management/guidelines-on-risk-management-practices--internal-controls-july-2024.pdf)
- [Jérôme Kerviel, Wikipedia](https://en.wikipedia.org/wiki/J%C3%A9r%C3%B4me_Kerviel)
- [Kweku Adoboli, Wikipedia](https://en.wikipedia.org/wiki/Kweku_Adoboli)
- [File:Fire of Great Hanshin earthquake Seen from Portisland.jpg, Wikimedia Commons](<https://commons.wikimedia.org/wiki/File:Fire_of_Great_Hanshin_earthquake_Seen_from_Portisland.jpg>)
- [File:Sir Francis Baring, 1st Baronet.jpg, Wikimedia Commons](<https://commons.wikimedia.org/wiki/File:Sir_Francis_Baring,_1st_Baronet.jpg>)
- [File:OUB Centre 3.JPG, Wikimedia Commons](<https://commons.wikimedia.org/wiki/File:OUB_Centre_3.JPG>)
- [File:Hanshin-Awaji earthquake 1995 Chuo-ku Kobe city Hyogo prefecture 350.jpg, Wikimedia Commons](<https://commons.wikimedia.org/wiki/File:Hanshin-Awaji_earthquake_1995_Chuo-ku_Kobe_city_Hyogo_prefecture_350.jpg>)
- [File:Junction of Bishopsgate and Threadneedle Street, London, July 1993.jpg, Wikimedia Commons](<https://commons.wikimedia.org/wiki/File:Junction_of_Bishopsgate_and_Threadneedle_Street,_London,_July_1993.jpg>)
- [File:SGX Centre, Singapore - 20121015.jpg, Wikimedia Commons](<https://commons.wikimedia.org/wiki/File:SGX_Centre,_Singapore_-_20121015.jpg>)
- [File:Messrs Baring Brothers & Co.jpg, Wikimedia Commons](<https://commons.wikimedia.org/wiki/File:Messrs_Baring_Brothers_&_Co.jpg>) (gallery)
- [File:Barings circular letter of credit 1892.jpg, Wikimedia Commons](<https://commons.wikimedia.org/wiki/File:Barings_circular_letter_of_credit_1892.jpg>) (gallery)
- [File:22 Bishopsgate, London 1993.jpg, Wikimedia Commons](<https://commons.wikimedia.org/wiki/File:22_Bishopsgate,_London_1993.jpg>) (gallery)
- [File:Images from The Great Hanshin-Awaji Earthquake-a001.jpg, Wikimedia Commons](<https://commons.wikimedia.org/wiki/File:Images_from_The_Great_Hanshin-Awaji_Earthquake-a001.jpg>) (gallery)
- [File:Hanshin-Awaji earthquake 1995 Chuo-ku Kobe city Hyogo prefecture 001.jpg, Wikimedia Commons](<https://commons.wikimedia.org/wiki/File:Hanshin-Awaji_earthquake_1995_Chuo-ku_Kobe_city_Hyogo_prefecture_001.jpg>) (gallery)
- [File:Hanshin-Awaji earthquake 1995 Chuo-ku Kobe city Hyogo prefecture 353.jpg, Wikimedia Commons](<https://commons.wikimedia.org/wiki/File:Hanshin-Awaji_earthquake_1995_Chuo-ku_Kobe_city_Hyogo_prefecture_353.jpg>) (gallery)
- [File:Hanshin-Awaji earthquake 1995 Hyogo-ku Kobe city Hyogo prefecture 001.jpg, Wikimedia Commons](<https://commons.wikimedia.org/wiki/File:Hanshin-Awaji_earthquake_1995_Hyogo-ku_Kobe_city_Hyogo_prefecture_001.jpg>) (gallery)
- [File:Hanshin-Awaji earthquake 1995 Tokyu Hands Sannomiya branch 001.jpg, Wikimedia Commons](<https://commons.wikimedia.org/wiki/File:Hanshin-Awaji_earthquake_1995_Tokyu_Hands_Sannomiya_branch_001.jpg>) (gallery)
- [File:Images from The Great Hanshin-Awaji Earthquake-b049.jpg, Wikimedia Commons](<https://commons.wikimedia.org/wiki/File:Images_from_The_Great_Hanshin-Awaji_Earthquake-b049.jpg>) (gallery)
- [File:Images from The Great Hanshin-Awaji Earthquake-g024.jpg, Wikimedia Commons](<https://commons.wikimedia.org/wiki/File:Images_from_The_Great_Hanshin-Awaji_Earthquake-g024.jpg>) (gallery)
- [File:Images from The Great Hanshin-Awaji Earthquake＝c117.jpg, Wikimedia Commons](<https://commons.wikimedia.org/wiki/File:Images_from_The_Great_Hanshin-Awaji_Earthquake＝c117.jpg>) (gallery)
- [File:Images from The Great Hanshin-Awaji Earthquake＝a040.jpg, Wikimedia Commons](<https://commons.wikimedia.org/wiki/File:Images_from_The_Great_Hanshin-Awaji_Earthquake＝a040.jpg>) (gallery)
- [File:OUB Centre Skyward.JPG, Wikimedia Commons](<https://commons.wikimedia.org/wiki/File:OUB_Centre_Skyward.JPG>) (gallery)
- [File:SGX Centre Two.JPG, Wikimedia Commons](<https://commons.wikimedia.org/wiki/File:SGX_Centre_Two.JPG>) (gallery)
- [File:Raffles Place in front of OUB Centre, Singapore - 20020829.jpg, Wikimedia Commons](<https://commons.wikimedia.org/wiki/File:Raffles_Place_in_front_of_OUB_Centre,_Singapore_-_20020829.jpg>) (video)
- [File:Evening view of UOB Plaza, OUB Centre and OCBC Centre near the Singapore River - 20010608.jpg, Wikimedia Commons](<https://commons.wikimedia.org/wiki/File:Evening_view_of_UOB_Plaza,_OUB_Centre_and_OCBC_Centre_near_the_Singapore_River_-_20010608.jpg>) (video)- [File:Evening view of UOB Plaza, OUB Centre and OCBC Centre near the Singapore River - 20010608.jpg, Wikimedia Commons](<https://commons.wikimedia.org/wiki/File:Evening_view_of_UOB_Plaza,_OUB_Centre_and_OCBC_Centre_near_the_Singapore_River_-_20010608.jpg>) (video)

[← Back to all posts](/)
