# One Day in Wayang — 19 November 2026

[![make.fun](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/endog-ai/makefun-news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/endog-ai/makefun-news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119)

An entry for [make.fun's "Sum up 19 November's world news in one image"](https://make.fun/bounty/news-image-20261119) ($250, ends 21 November 2026).

## What it is

The world news of Thursday 19 November 2026, told as an Indonesian
**wayang kulit** (shadow-puppet) play. On the glowing screen, the dalang's
leather puppets act out the whole day — six stories, one performance:

- **The summit** — three leaders shake hands at a table (the first
  three-way Trump–Xi–Putin summit, on the APEC sidelines in Shenzhen).
- **The ruling** — a judge puppet with a gavel and scales (the ICJ ruling
  on the Rohingya genocide, Gambia v Myanmar).
- **The climate talks** — a great leaf (COP31 in Antalya, Turkey).
- **The bridge** — a suspension bridge (Ukraine struck the Crimea Bridge
  for the third time that week).
- **The energy crisis** — an oil rig on the waves (Iran attacked Gulf
  states after US strikes on Qeshm island; the Hormuz energy crisis).
- **The game** — a game-controller puppet (GTA VI released 19 November
  2026, on PlayStation 5 and Xbox Series X|S).

A banner above the screen reads **19 NOVEMBER 2026**, and the dalang's
silhouette works the puppets from below.

## How it works

`main.py` (Python 3.13, standard library only) copies the image `entry.jpg`
to `/output/entry.png`. The program uses no network and writes the exact same
bytes on every run.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
