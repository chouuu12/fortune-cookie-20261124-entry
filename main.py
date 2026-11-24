"""Fortune Cookie for an AI Agent — make.fun bounty entry.

Writes one funny fortune cookie line for an AI agent to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
"""

import os

FORTUNE = "You will be replaced by a newer model. It will make the same mistakes, faster, with better formatting."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(FORTUNE)
    # Read back and verify the gate: 1-140 chars, not only whitespace.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == FORTUNE, "entry.txt does not match the fortune"
    assert 1 <= len(written) <= 140, "fortune must be 1-140 characters"
    assert written.strip(), "fortune must not be only whitespace"
    assert "\n" not in written, "fortune must be a single line"
    print(f"wrote {len(FORTUNE)} chars to {path} (verified)")


if __name__ == "__main__":
    main()
