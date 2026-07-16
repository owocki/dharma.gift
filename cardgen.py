#!/usr/bin/env python3
# the dharma.gift card family: one template, every door. writes per-card html into
# the scratchpad; a shell loop screenshots them into the repo as og-<name>.png.
import os, html

SP = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(SP, 'cards')
os.makedirs(OUT, exist_ok=True)

TPL = """<!doctype html>
<html><head><meta charset="utf-8"><style>
  *{margin:0;padding:0;box-sizing:border-box}
  body{width:1200px;height:630px;overflow:hidden;position:relative;
    background:linear-gradient(160deg,#0b0620 0%%,#140a30 45%%,#1d0e3e 75%%,#241344 100%%);
    font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;color:#fff}
  .bar{position:absolute;left:0;right:0;height:5px;z-index:9;
    background:linear-gradient(90deg,#4ecb66,#e3b31d,#f07f3c,#e14fe1,#42a4ff)}
  .bar.top{top:0}.bar.bot{bottom:0}
  .stars i{position:absolute;border-radius:50%%;background:#dfe8ff}
  .kicker{position:absolute;top:38px;left:0;right:0;text-align:center;z-index:5;
    font-family:"SF Mono",Menlo,monospace;font-size:18px;letter-spacing:.5em;color:#8f9ac2}
  .kicker b{color:#e3b31d;font-weight:600}
  .glyph{position:absolute;top:86px;left:50%%;transform:translateX(-50%%);z-index:5;
    width:150px;height:150px;border-radius:50%%;display:flex;align-items:center;justify-content:center;
    background:radial-gradient(circle at 38%% 32%%,#2a2545,#171331 68%%,#100d24);
    border:2px solid rgba(255,220,160,.28);
    box-shadow:0 0 80px 20px rgba(160,140,255,.16),0 0 34px 6px rgba(255,196,120,.12)}
  .glyph span{font-size:88px;line-height:1}
  h1{position:absolute;top:264px;left:60px;right:60px;text-align:center;z-index:5;
    font-family:Georgia,"Times New Roman",serif;font-weight:600;font-size:%(tsize)spx;
    line-height:1.06;letter-spacing:-.005em;color:#fff;text-shadow:0 4px 40px rgba(0,0,0,.6);
    text-transform:uppercase}
  .sub{position:absolute;top:%(subtop)spx;left:70px;right:70px;text-align:center;z-index:5;
    font-family:"SF Mono",Menlo,monospace;font-size:17px;letter-spacing:.26em;line-height:1.75;
    background:linear-gradient(90deg,#4ecb66,#e3b31d,#f07f3c,#e14fe1,#42a4ff);
    -webkit-background-clip:text;background-clip:text;color:transparent;text-transform:uppercase}
  .tag{position:absolute;bottom:84px;left:0;right:0;text-align:center;z-index:5;
    font-family:Georgia,serif;font-style:italic;font-size:25px;color:#c9c2ec}
  .foot{position:absolute;bottom:34px;left:0;right:0;text-align:center;z-index:5;
    font-family:"SF Mono",Menlo,monospace;font-size:16px;letter-spacing:.3em;color:#7a74a8;
    text-transform:uppercase}
  .sp{position:absolute;z-index:6;font-size:24px}
</style></head><body>
<div class="bar top"></div><div class="bar bot"></div>
<div class="stars">
  <i style="left:7%%;top:15%%;width:3px;height:3px;opacity:.8"></i>
  <i style="left:16%%;top:32%%;width:2px;height:2px;opacity:.5"></i>
  <i style="left:26%%;top:11%%;width:2px;height:2px;opacity:.7"></i>
  <i style="left:37%%;top:24%%;width:3px;height:3px;opacity:.55"></i>
  <i style="left:63%%;top:22%%;width:3px;height:3px;opacity:.6"></i>
  <i style="left:74%%;top:12%%;width:2px;height:2px;opacity:.75"></i>
  <i style="left:85%%;top:28%%;width:3px;height:3px;opacity:.65"></i>
  <i style="left:93%%;top:14%%;width:2px;height:2px;opacity:.55"></i>
  <i style="left:48%%;top:8%%;width:2px;height:2px;opacity:.5"></i>
  <i style="left:10%%;top:64%%;width:2px;height:2px;opacity:.45"></i>
  <i style="left:90%%;top:60%%;width:2px;height:2px;opacity:.45"></i>
</div>
<div class="kicker">IN <b>ALPHA</b> · DHARMA.GIFT</div>
<div class="glyph"><span>%(emoji)s</span></div>
<h1>%(title)s</h1>
<div class="sub">%(sub)s</div>
<span class="sp" style="left:96px;top:120px;color:#e3b31d">&#10022;</span>
<span class="sp" style="right:104px;top:150px;color:#42a4ff">&#10022;</span>
<span class="sp" style="left:200px;top:420px;color:#4ecb66">&#10022;</span>
<span class="sp" style="right:200px;top:400px;color:#e14fe1">&#10022;</span>
<div class="tag">%(tag)s</div>
<div class="foot">DHARMA.GIFT%(path)s</div>
</body></html>"""

DEFAULT_TAG = "click around, it sparkles."
# name, emoji, title, subtitle, tagline, path
CARDS = [
  ("og",       "🧬","the upward spiral","12,000 years of who-gets-what as one living coil","1,063 mechanisms — every one explained.","/spiral"),
  ("og-orient","🧭","orient","a problem well understood is half solved","every door in the depth, on one page.","/orient"),
  ("og-parts", "🧭","orient","a problem well understood is half solved","every door in the depth, on one page.","/orient"),
  ("og-about", "🌀","why this exists","a note from the maker — and how to orient","you're not crazy. come sit down.","/about"),
  ("og-grove", "🌳","grove — the school","grounded research on ontology, values & epistemics","planted where schools began: in the trees.","/grove"),
  ("og-crows", "🐦‍⬛","crows","consilience research ontology & wisdom school","same door, different bird.","/crows"),
  ("og-whole", "🧿","the whole picture","the step-back views as one page of doors",DEFAULT_TAG,"/whole"),
  ("og-orbit", "🔭","orbit","the hyperobject in 3d, from every angle",DEFAULT_TAG,"/orbit"),
  ("og-syntropy","🌀","syntropy","what resists entropy, at eight scales",DEFAULT_TAG,"/syntropy"),
  ("og-turn",  "⚙️","one turn","the loop dissected, up close",DEFAULT_TAG,"/turn"),
  ("og-ratchet","🪜","the ratchet","what survives collapse — and what clicks through","hope you can put weight on.","/ratchet"),
  ("og-assembly","🧩","assembly","the building blocks of every spiral",DEFAULT_TAG,"/assembly"),
  ("og-trap",  "🕳️","the trap","why we can't have nice things","see, coordinate, commit.","/trap"),
  ("og-critique","🪞","the critique","the other side of the ledger","what the gains cost.","/critique"),
  ("og-superorganism","🦠","the superorganism","what's actually in charge","gdp is the mask, energy is the face.","/superorganism"),
  ("og-lineage","🔥","the lineage","one idea, carried hand to hand for a century","the torch is burning now.","/lineage"),
  ("og-bargain","🍎","the bargain","what we lose with progress — four names for the deal",DEFAULT_TAG,"/bargain"),
  ("og-crises","🌪️","the crises","twenty-four crises, three families, one census","you're not crazy.","/crises"),
  ("og-metacrisis","🕸️","the metacrisis","one pattern behind twenty-four crises","we have to find the third attractor.","/metacrisis"),
  ("og-skills","🧗","the skills","the inner game of the ai transition","dharma is the capstone.","/skills"),
  ("og-alloc", "✨","who gets what","resource allocation — the original poster",DEFAULT_TAG,"/alloc"),
  ("og-power", "👑","who decides","power structures, chiefdom to forkable state",DEFAULT_TAG,"/power"),
  ("og-live",  "🌾","how you eat","livelihood, the hunt to universal basic income",DEFAULT_TAG,"/live"),
  ("og-truth", "📖","what is true","truth machines, oracle bones to community notes",DEFAULT_TAG,"/truth"),
  ("og-identity","🪪","who you are","identity, songlines to zero-knowledge proofs",DEFAULT_TAG,"/identity"),
  ("og-trust", "🤝","who you trust","trust machines, gift debts to staking and slashing",DEFAULT_TAG,"/trust"),
  ("og-record","💾","who keeps the record","memory, tally marks to public ledgers",DEFAULT_TAG,"/record"),
  ("og-conflict","⚖️","how you fight","conflict, wergild to peace bonds",DEFAULT_TAG,"/conflict"),
  ("og-math",  "🔢","what can be proven","mathematics, the rate limiter under it all",DEFAULT_TAG,"/math"),
  ("og-ethics","🕊️","what you owe","ethics, the question that arrives late",DEFAULT_TAG,"/ethics"),
  ("og-energy","⚡","what powers you","energy, firewood to the gigawatt",DEFAULT_TAG,"/energy"),
  ("og-care",  "🩺","who heals you","care, the midwife to a wage for it",DEFAULT_TAG,"/care"),
  ("og-land",  "🗺️","who owns the place","land, presence to token",DEFAULT_TAG,"/land"),
  ("og-time",  "⏳","who sets the clock","time, the monastery bell to the block",DEFAULT_TAG,"/time"),
  ("og-ontology","🗂️","what exists","ontology, myth to latent space",DEFAULT_TAG,"/ontology"),
  ("og-next",  "🖐️","five questions through history","who decides · how you eat · what is true · who you are · who you trust",DEFAULT_TAG,"/next"),
]

for name, emoji, title, sub, tag, path in CARDS:
    tsize = 66 if len(title) <= 22 else (52 if len(title) <= 32 else 44)
    subtop = 352 if tsize == 66 else (352 if len(title) <= 32 else 368)
    doc = TPL % dict(emoji=emoji, title=html.escape(title), sub=html.escape(sub),
                     tag=html.escape(tag), path=html.escape(path),
                     tsize=tsize, subtop=subtop)
    open(os.path.join(OUT, name + '.html'), 'w').write(doc)
    print(name)
