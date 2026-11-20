#!/usr/bin/env python3
"""Entry for the make.fun bounty news-image-20261120.

Writes the front-page summary of Friday 20 November 2026 world news
to /output/entry.png. The image is pre-rendered and stored in this
repository; this program only copies it, using the standard library.
It needs no network and writes the same bytes on every run.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    # Deterministic by construction: a byte copy of a fixed file.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(
        os.path.join(HERE, "entry.png"),
        os.path.join(out_dir, "entry.png"),
    )


if __name__ == "__main__":
    main()
