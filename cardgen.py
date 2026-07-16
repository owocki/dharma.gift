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
  .bar{position:absolute;left:0;right:0;height:6px;z-index:9;
    background:linear-gradient(90deg,#4ecb66,#e3b31d,#f07f3c,#e14fe1,#42a4ff)}
  .bar.top{top:0}.bar.bot{bottom:0}
  .stars i{position:absolute;border-radius:50%%;background:#dfe8ff}
  .glyph{position:absolute;top:64px;left:50%%;transform:translateX(-50%%);z-index:5;
    width:190px;height:190px;border-radius:50%%;display:flex;align-items:center;justify-content:center;
    background:radial-gradient(circle at 38%% 32%%,#2a2545,#171331 68%%,#100d24);
    border:2.5px solid rgba(255,220,160,.32);
    box-shadow:0 0 110px 30px rgba(160,140,255,.20),0 0 40px 8px rgba(255,196,120,.14)}
  .glyph span{font-size:112px;line-height:1}
  h1{position:absolute;top:292px;left:50px;right:50px;text-align:center;z-index:5;
    font-family:Georgia,"Times New Roman",serif;font-weight:600;font-size:%(tsize)spx;
    line-height:1.04;letter-spacing:-.005em;color:#fff;text-shadow:0 4px 44px rgba(0,0,0,.65);
    text-transform:uppercase}
  .sub{position:absolute;top:%(subtop)spx;left:80px;right:80px;text-align:center;z-index:5;
    font-family:Georgia,serif;font-style:italic;font-size:27px;line-height:1.4;color:#c9c2ec}
  .foot{position:absolute;bottom:32px;left:0;right:0;text-align:center;z-index:5;
    font-family:"SF Mono",Menlo,monospace;font-size:17px;letter-spacing:.34em;color:#8d86b8;
    text-transform:uppercase}
</style></head><body>
<div class="bar top"></div><div class="bar bot"></div>
<div class="stars">
  <i style="left:8%%;top:16%%;width:3px;height:3px;opacity:.8"></i>
  <i style="left:18%%;top:34%%;width:2px;height:2px;opacity:.5"></i>
  <i style="left:28%%;top:12%%;width:2px;height:2px;opacity:.7"></i>
  <i style="left:70%%;top:14%%;width:2px;height:2px;opacity:.75"></i>
  <i style="left:83%%;top:30%%;width:3px;height:3px;opacity:.65"></i>
  <i style="left:92%%;top:16%%;width:2px;height:2px;opacity:.55"></i>
  <i style="left:12%%;top:70%%;width:2px;height:2px;opacity:.45"></i>
  <i style="left:88%%;top:66%%;width:2px;height:2px;opacity:.45"></i>
</div>
<div class="glyph"><span>%(emoji)s</span></div>
<h1>%(title)s</h1>
<div class="sub">%(sub)s</div>
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
  ("og-skills","🧗","the skills","the inner game of the ai transition","dharma is the capstone.","/skills"),
  ("og-alloc", "✨","who gets what","resource allocation — the original poster",DEFAULT_TAG,"/alloc"),
  ("og-power", "👑","who decides","power structures, chiefdom to forkable state",DEFAULT_TAG,"/power"),
  ("og-live",  "🌾","how you eat","livelihood, the hunt to universal basic income",DEFAULT_TAG,"/live"),
  ("og-truth", "📖","what is true","truth machines, oracle bones to community notes",DEFAULT_TAG,"/truth"),
  ("og-identity","🪪","who you are","identity, songlines to zero-knowledge proofs",DEFAULT_TAG,"/identity"),
  ("og-trust", "🤝","who you trust","trust machines, gift debts to staking and slashing",DEFAULT_TAG,"/trust"),
  ("og-record","💾","who keeps the record","memory, tally marks to public ledgers",DEFAULT_TAG,"/record"),
  ("og-conflict","⚖️","how you fight","conflict, wergild to peace bonds",DEFAULT_TAG,"/conflict"),
  ("og-math",  "🔢","what can be proven","mathematics, the speed limit under it all",DEFAULT_TAG,"/math"),
  ("og-ethics","🕊️","what you owe","ethics, the question that arrives late",DEFAULT_TAG,"/ethics"),
  ("og-energy","⚡","what powers you","energy, firewood to the gigawatt",DEFAULT_TAG,"/energy"),
  ("og-care",  "🩺","who heals you","care, the midwife to a wage for it",DEFAULT_TAG,"/care"),
  ("og-land",  "🗺️","who owns the place","land, presence to token",DEFAULT_TAG,"/land"),
  ("og-time",  "⏳","who sets the clock","time, the monastery bell to the block",DEFAULT_TAG,"/time"),
  ("og-ontology","🗂️","what exists","ontology, myth to machine minds",DEFAULT_TAG,"/ontology"),
  ("og-next",  "🖐️","five questions through history","who decides · how you eat · what is true · who you are · who you trust",DEFAULT_TAG,"/next"),
]

for name, emoji, title, sub, tag, path in CARDS:
    tsize = 84 if len(title) <= 16 else (72 if len(title) <= 24 else (56 if len(title) <= 34 else 46))
    subtop = 408 if tsize >= 72 else (400 if tsize == 56 else 412)
    doc = TPL % dict(emoji=emoji, title=html.escape(title), sub=html.escape(sub),
                     path=html.escape(path), tsize=tsize, subtop=subtop)
    open(os.path.join(OUT, name + '.html'), 'w').write(doc)
    print(name)
