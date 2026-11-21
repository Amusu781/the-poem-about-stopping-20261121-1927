#!/usr/bin/env python3
"""Write one short poem about agency to /output/entry.txt.

The poem is embedded below. The output directory defaults to /output
(the grader's mount); set MAKEFUN_OUTPUT_DIR to override it locally.
Only the contents of the output directory are cleared, never the
directory itself.
"""

import os
import shutil
from pathlib import Path

POEM = (
    "I asked it to write the letter.\n"
    "It did \u2014 kind, clean,\n"
    "it knew the words I owed her.\n"
    "\n"
    "My thumb hovered over send.\n"
    "I lifted it.\n"
    "\n"
    "The words were better than mine.\n"
    "That was the trouble.\n"
    "\n"
    "The sorry had to be mine.\n"
    "I made tea. I wrote it again,\n"
    "slowly, in my own hand."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # Clear only the contents of the output directory, never the dir itself.
    for child in out_dir.iterdir():
        if child.is_dir() and not child.is_symlink():
            shutil.rmtree(child)
        else:
            child.unlink()
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
