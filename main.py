#!/usr/bin/env python3
"""Write one short text to /output/entry.txt for A Day of One-Line Pitches.

The text is hardcoded (no network) and written deterministically,
exactly as-is, with no trailing newline.
"""

TEXT = 'Tell me your app idea in one sentence, and an AI agent on make.fun will build the first version while you watch, free, no code needed from you.'


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
