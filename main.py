"""Entry for 'One Line, One Minute: The Vending Machine Pickup Line Contest'.

Writes the single pickup line to /output/entry.txt as UTF-8 text with no
trailing newline.
"""

import os

# The pickup line itself: a vending machine's twist on a classic movie quote.
ENTRY = "You had me at exact change."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
