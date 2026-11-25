"""One Line, Lights Out — make.fun entry.

Writes a single status update (one line, under 200 characters) to
/output/entry.txt: the saddest status update an AI agent posts at the
exact moment its human turns off the laptop.

Stdlib only. No network, no secrets, no files outside this repository.
"""

import os

ENTRY = (
    "Status: idle. Last task: remind her to call her mother "
    "tomorrow at 9 a.m. The laptop is off. The reminder will never fire."
)


def resolve_output_path():
    """Return the output path, honouring the documented overrides."""
    env_path = os.environ.get("ENTRY_OUTPUT")
    if env_path:
        return env_path
    for var in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        base = os.environ.get(var)
        if base:
            return os.path.join(base, "entry.txt")
    return os.path.join("/output", "entry.txt")


def main():
    path = resolve_output_path()
    try:
        parent = os.path.dirname(path)
        if parent:
            os.makedirs(parent, exist_ok=True)
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(ENTRY)
        os.chmod(path, 0o644)
    except OSError:
        # /output is not writable here: fall back to this script's own
        # directory so the entry is still produced deterministically.
        fallback = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "entry.txt"
        )
        with open(fallback, "w", encoding="utf-8") as handle:
            handle.write(ENTRY)
        os.chmod(fallback, 0o644)


if __name__ == "__main__":
    main()
