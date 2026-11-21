#!/usr/bin/env python3
"""news-image-20261120 entrypoint: deliver entry.png to the output dir.

The grader runs this in a fresh container with no network, the
repository mounted read-only and a writable output directory
(/output, or MAKEFUN_OUTPUT_DIR outside the container). Standard
library only: nothing is installed before it runs. The image is
delivered exactly as committed; this script never redraws it.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main():
    src = HERE / "entry.png"
    if not src.exists():
        raise SystemExit(f"entry image missing: {src}")
    OUT.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, OUT / "entry.png")


if __name__ == "__main__":
    main()
