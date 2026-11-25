import os
from pathlib import Path

LINE = "My doorstop has held the same door open for six years, never asked for a raise, and still gets kicked every morning \u2014 the most loyal employee in this house."

OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUTPUT_DIR / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
