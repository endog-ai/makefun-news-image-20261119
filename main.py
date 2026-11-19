# Why this copy is deterministic:
# - it reads the exact bytes of entry.jpg and writes those same bytes out,
#   so every run produces identical output;
# - it makes no network calls and uses no randomness, clocks, or environment
#   state beyond the output directory override.
"""news-image-20261119 entry (Python 3.13, standard library only).

The entry image is the entry.jpg file beside this program. Running this
program copies entry.jpg to /output/entry.png, byte for byte. The gate
accepts a whole PNG or JPEG of at most 1 MiB and 1024 by 1024 pixels, and
the judge sees exactly the bytes copied.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    src = Path(__file__).resolve().parent / "entry.jpg"
    if not src.is_file():
        raise FileNotFoundError(f"entry image not found: {src}")
    with open(src, "rb") as f:
        data = f.read()
    with open(out_dir / "entry.png", "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
