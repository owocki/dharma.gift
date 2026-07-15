# resourceallo / upwardspiral.io

a single-file living poster — `index.html` carries all 22 views (15 question posters + 7 whole-picture views). no build step. serve with `python3 -m http.server` or open directly.

## sharing write-ups on hackmd

use the mirrormirror push script — the hackmd api token is hardcoded inside it (kevin's choice, private repo):

```sh
# use the mirrormirror venv — system python3 lacks `requests`
~/Sites/mirrormirror/.venv/bin/python ~/Sites/mirrormirror/scripts/push_hackmd.py <file.md>              # guest-readable link
~/Sites/mirrormirror/.venv/bin/python ~/Sites/mirrormirror/scripts/push_hackmd.py <file.md> --read owner
```

`$HACKMD_API_TOKEN` overrides the baked-in token. one new note per push; title comes from the first h1.

## deploying

`./deploy.sh` — note it currently copies a mirrormirror draft over `index.html` before pushing; **do not run it blindly after editing index.html directly**, it will clobber your work. commit/push manually instead.

## design system notes

- theme: dark by default, persisted in `localStorage['ra-theme']`; tokens in `:root` at the top of the style block
- display face: fraunces (google fonts), lowercase; era ramp = `#2f9e44 #a17a00 #b0561f #b535bb #1c7ed6` (bright variants for dark: `#4ecb66 #e3b31d #f07f3c #e14fe1 #42a4ff`)
- glow is built from geometry (fat soft stroke under crisp stroke), never blur filters — mobile safari's compositor dies on animated filtered layers; perf guards live in a `@media (max-width:900px),(pointer:coarse)` block at the end of the stylesheet
- gradient-clipped text (`background-clip:text`) erases emoji and paints over text-shadows and negative-z pseudo-elements — the emoji rides in `span.emj`, and legibility pools live on sibling/back layers
- adding a tour step: extend `STEPS` + the `ORDER` array in the spiral scrollytell, then shift the `data-stage` gate numbers in the css
- adding a view: `MODES` entry + tab button + wrap div + `clearX`/`renderX` choreography in `setMode` + a redirect stub html for the clean url
