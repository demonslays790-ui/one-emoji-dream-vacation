#!/usr/bin/env python3
"""One Emoji, One Dream Vacation — make.fun entry.

Contract: the program writes exactly one emoji to ``entry.txt`` in
the output directory. The chosen glyph is the desert-island emoji
U+1F3DD (🏝) — a beach, a palm tree and a faraway escape compressed
into a single character, the most postcard-vivid dream vacation
there is.

The file must be exactly those 4 UTF-8 bytes: no variation
selector, no trailing newline, no extra characters. The program
also sets the file mode to 0644.

The output directory is read from the ``MAKEFUN_OUTPUT_DIR``
environment variable and defaults to ``/output`` when unset.
Pure standard library — no dependencies.
"""

import os

EMOJI = "\U0001F3DD"  # 🏝 DESERT ISLAND
DEFAULT_OUTPUT_DIR = "/output"


def resolve_output_path() -> str:
    """Return the entry.txt path, creating the output directory."""
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR
    os.makedirs(output_dir, exist_ok=True)
    return os.path.join(output_dir, "entry.txt")


def main() -> None:
    path = resolve_output_path()
    data = EMOJI.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    codepoint = f"U+{ord(EMOJI):04X}"
    print(f"Wrote {EMOJI} ({codepoint}, {len(data)} bytes) to {path}")


if __name__ == "__main__":
    main()
