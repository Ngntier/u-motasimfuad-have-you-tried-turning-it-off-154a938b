"""One-line tech-support reply.

The joke: a hopeless support agent whose entire troubleshooting playbook
is the classic "turn it off and on again" — and who cheerfully admits
that step is also step two, step three, and the whole of their training.
"""

import os

LINE = (
    "Have you tried turning it off and on again? "
    "Wonderful \u2014 that's also step two, step three, and my entire training."
)


def main() -> None:
    line = LINE
    # Gate check: 1-199 chars, single line, not blank.
    assert line.strip(), "entry must not be blank"
    assert "\n" not in line and "\r" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 199, f"entry length {len(line)} outside 1-199 chars"
    assert line == line.strip(), "entry must not have leading/trailing whitespace"
    assert all(ord(ch) >= 32 or ch == "\t" for ch in line), (
        "entry must not contain control characters"
    )

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
