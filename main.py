"""Fortune Cookie Wisdom for Developers -- make.fun entry.

Writes exactly one original fortune-cookie line for a software
developer to /output/entry.txt. Python 3.13 standard library only.
"""

import os

LINE = "The legacy code you fear to touch was once a brave Friday deploy; treat it gently, and it will teach you patience."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
