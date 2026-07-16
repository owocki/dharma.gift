# resourceallo / upwardspiral.io — GROVE 🌳

a wisdom school in alpha (GROVE — grounded research on ontology, values & epistemics), wrapped around a living poster. no build step. serve with `python3 -m http.server` or open directly. deployed to https://www.upwardspiral.io on vercel (`cleanUrls: true`, so `/critique` serves `critique.html`; `vercel.json` also redirects the old domain `resource.gitcoin.co` here).

the layers, outermost first:

- `index.html` — the **grove landing** at `/`: a night hero (starry sky, shooting stars, a glistening city TOWERING behind the trees, always dark regardless of theme — no theme toggle) with five era-colored trees swaying on the fold — the fold IS the ground line. below it, a live canvas mycelium grows from the five trunk positions with resource beads traveling the finished paths (#myc draws the network once; #flow is cleared per frame for the beads); the GROVE wordmark sits in the root zone wearing the five tree colors, the three questions (ontology/epistemics/values, eli5 voice) live down among the roots too, and the "secretly one" whisper sits deeper still. then the alpha banner ("...ontological breakthrough") and the door: five era-colored strands (#doorroots canvas, one per tree) converging onto a flowing-rainbow enter button that opens `/parts`. no footer, no sidedoors. the kicker shows grove.owocki.com (metas still point at upwardspiral.io until DNS lands). it forwards any legacy hash (`/#trust/...`) into `/spiral#trust/...` before paint. all canvases respect reduced-motion and pause offscreen via IntersectionObserver; glow is layered strokes, never blur filters.
- `parts.html` — the **index of the grove** (`/parts`): what the enter button opens. every door on one page in three clusters — the canopy (spiral, orbit, whole + the step-back views), the trees (the fifteen questions), the soil (skills, about). card: `og-parts.png`.
- `crows.html` — the **crows variant** of the landing (`/crows`, CROWS — consilience research ontology & wisdom school): same skeleton, crow/counting-rhyme symbolism instead of trees. crows still links home; the grove landing no longer links to crows (its footer was removed). if crows is ever promoted back to the front door, swap the two files' roles and relabel `#crowsback` in spiral.html.
- `spiral.html` — the poster itself, all 22 views (15 question posters + 7 whole-picture views), served at `/spiral`. this is the file that used to be `index.html`; the mirrormirror pipeline drafts it. on the coil it shows a `#crowsback` button (`← 🌳 grove` → `/`); on posters the old `#back` button still returns to the coil. the tab index at the foot is labeled "navigate the GROVE" and wears a faint five-tree grove (`.navgrove`) instead of the old nav spiral. `setURL` rewrites the coil's url to `/spiral` (never bare `/`), and `spiral` is in the BASEPATH-stripping regex.
- the ~26 redirect stubs (`trust.html`, …) now forward to `/spiral#<mode>` (not `/#<mode>`); `whole.html` and `orbit.html` deep-link into `/spiral#...` too.

## the one hard rule: every new page ships with its own twitter card

when you create a new page (a new tab/view + its `<name>.html` stub), it MUST get its own social card. the poster's card (`spiral.html`'s `<head>` meta block + `og.png`) is the single source of truth for the tag pattern and the visual style; the grove landing wears `og-grove.png`, the crows variant `og-crows.png`, both in the same family. crawlers never see `#hash` fragments — that is the whole reason each tab gets a crawlable `<name>.html` stub with its own card.

1. **image**: `og-<name>.png`, 1200×630, repo root. match the landing card's family: dark purple gradient bg, rainbow hairline bars top+bottom, mono `UPWARDSPIRAL.IO` kicker, big white all-caps title, letterspaced gradient mono subtitle, corner glyph circles, ✦ sparkles, italic tagline, footer ending `upwardspiral.io/<name>`. central art should echo the page's own visualization. build it as a 1200×630 html page and screenshot headlessly:
   `chrome-headless-shell --headless --screenshot=og-<name>.png --window-size=1200,630 --hide-scrollbars file://...`
   (playwright's binary lives under `~/Library/Caches/ms-playwright/chromium_headless_shell-*/`; the card templates + render pipeline docs live in `~/Sites/mirrormirror/scripts/allocation_poster_site/build.md`)
2. **meta tags** in the stub's `<head>`, copied from `index.html`'s block, absolute urls always:
   - `og:type` · `og:url` (`https://www.upwardspiral.io/<name>`) · `og:title` · `og:description`
   - `og:image` = `https://www.upwardspiral.io/og-<name>.png` + `og:image:width` 1200 / `og:image:height` 630
   - `twitter:card` = `summary_large_image` · `twitter:title` · `twitter:description` (shorter than og) · `twitter:image` (same png)
   - `meta name="description"` + `link rel="canonical"` → `https://www.upwardspiral.io/#<name>`
3. regenerating an existing card? bust crawler caches with `?v=N` on the image url (that's why the landing page uses `og.png?v=2`).

## anatomy of a redirect stub (`<name>.html`)

~40 lines, maintained directly in THIS repo (only `spiral.html` comes from mirrormirror): GA tag, emoji favicon, `<title>`, canonical, the full og/twitter block above, then `meta http-equiv="refresh"` + `location.replace('/spiral#<name>'+(location.hash?'/'+location.hash.slice(1):''))` — the js form preserves deep links, so `/trust#gift-debts` forwards to `/spiral#trust/gift-debts`. copy an existing stub (e.g. `trust.html`) and change name/emoji/copy/image.

## sharing write-ups on hackmd

use the mirrormirror push script — the hackmd api token is hardcoded inside it (kevin's choice, private repo):

```sh
# use the mirrormirror venv — system python3 lacks `requests`
~/Sites/mirrormirror/.venv/bin/python ~/Sites/mirrormirror/scripts/push_hackmd.py <file.md>              # guest-readable link
~/Sites/mirrormirror/.venv/bin/python ~/Sites/mirrormirror/scripts/push_hackmd.py <file.md> --read owner
```

`$HACKMD_API_TOKEN` overrides the baked-in token. one new note per push; title comes from the first h1.

## deploying

`./deploy.sh` — note it historically copied a mirrormirror draft over the poster file before pushing; the poster now lives at `spiral.html`, so **do not run it blindly** — it may clobber `index.html` (now the grove landing) or miss `spiral.html` entirely. commit/push manually instead, and update the script before trusting it again.

## design system notes

- theme: dark by default, persisted in `localStorage['ra-theme']`; tokens in `:root` at the top of the style block
- display face: fraunces (google fonts), lowercase; era ramp = `#2f9e44 #a17a00 #b0561f #b535bb #1c7ed6` (bright variants for dark: `#4ecb66 #e3b31d #f07f3c #e14fe1 #42a4ff`)
- glow is built from geometry (fat soft stroke under crisp stroke), never blur filters — mobile safari's compositor dies on animated filtered layers; perf guards live in a `@media (max-width:900px),(pointer:coarse)` block at the end of the stylesheet
- gradient-clipped text (`background-clip:text`) erases emoji and paints over text-shadows and negative-z pseudo-elements — the emoji rides in `span.emj`, and legibility pools live on sibling/back layers
- adding a tour step: extend `STEPS` + the `ORDER` array in the spiral scrollytell, then shift the `data-stage` gate numbers in the css
- adding a view: `MODES` entry + tab button + wrap div + `clearX`/`renderX` choreography in `setMode` + a redirect stub html for the clean url + its `og-<name>.png` card (see the hard rule above)

## other conventions (hold these on every page)

- **self-contained**: no bundler, no external js. the only network fetch is the fraunces display font (google fonts), and it must degrade to a system serif offline; anything read at 11px stays on the system stack
- **GA tag on every page**: `G-882JMLBJG9`, top of `<head>` — stubs included
- **favicon**: inline-svg emoji data uri, one emoji per page (index ✨, critique 🪞, trust 🤝, …)
- **theme settled before first paint**: a tiny inline script reads `localStorage['ra-theme']` and stamps `data-theme` on `<html>` before any css paints — night by default, an explicit toggle choice is remembered
- **voice**: lowercase, literary prose everywhere — titles, og descriptions, even code comments read like marginalia ("the theme, settled before first paint"). og/twitter descriptions carry the cadence: concrete numbers ("60 trust machines", "12,000 years"), era-spanning pairs ("gift debts to staking and slashing"), usually ending "click around, it sparkles."
- **accessibility**: reduced-motion friendly; meaningful svgs get `role="img"` + an `aria-label` that describes what the picture argues, not just what it shows
- **hash grammar**: bare `#<slug>` = legacy alloc links; tabs are `#<mode>`; deep links are `#<mode>/<slug>`. stubs must preserve incoming hashes when redirecting
- **counts drift**: mechanism/tab counts live in readme.md, og descriptions, and the header stats — when a tab is added or grows, sweep all three
