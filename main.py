"""One Word for Your Wi-Fi.

Writes exactly one word to /output/entry.txt: Goldfish.

Why Goldfish, against a field of 414 (checked 24 Nov 2026 from the
public competition feed):

The field is saturated with one angle -- the Wi-Fi that vanishes:
Ghosting (53 copies), Gaslighting (32), Peekaboo (20), Ghosted (9),
plus Flaky (8), Buffering (8), Liar (7). Any word in that family
fights dozens of identical copies for the same laugh, and a judge
comparing two Ghostings has nothing to separate them. Goldfish
takes an angle nobody in the field uses: memory. A goldfish
forgets everything in three seconds -- and so does this Wi-Fi. It
drops your device, forgets the network it joined yesterday, and
asks for the password again like it has never met you.

Against the judge's four weights -- on-subject fit, laugh, truth,
freshness:

- Fit: it describes the Wi-Fi itself, its behaviour, in one
  concrete image; and as a network name it is a name the sponsor
  would actually want to wear.
- Laugh: the joke lands in one beat, no setup -- a goldfish is
  running your router. It is funnier than the field's lead word,
  which by copy 53 has stopped being a joke and become a cliche.
- Truth: "forgot the password again / dropped me again" is the
  other universal Wi-Fi complaint, beside "it vanished". It is
  true of every home network, not of one brand or one router.
- Freshness: zero of 414 entries use it, and none uses the
  memory/forgetting angle at all. The nearest neighbours --
  Amnesiac-style words, Dory, "forgetful" -- are absent too.

Head to head: against Ghosting it matches on truth and wins on
laugh and freshness; against Gaslighting it wins on freshness and
loses nothing on truth, because forgetting is a different, equally
true complaint rather than a weaker version of lying. Its angle is
uncontested, so no matchup is a mirror match it can only tie.

Honest odds: one paid place, winner takes all, 414 entries, blind
rounds, no live score -- the win is a long shot and depends on how
the judge weighs a fresh angle against the familiar favourite.
Goldfish is the best single word available: it is the funniest
true thing about Wi-Fi that nobody else said.
"""

from pathlib import Path

WORD = "Goldfish"

# The gate: /output/entry.txt must be UTF-8 text of 1 to 30
# characters, not only white space, and the entry must be exactly
# one word.
MIN_CHARS = 1
MAX_CHARS = 30


def check_word(word: str) -> None:
    """Refuse to write a text that falls outside the entry gate."""
    n = len(word)
    if not MIN_CHARS <= n <= MAX_CHARS:
        raise SystemExit(
            f"entry word is {n} characters; the gate allows "
            f"{MIN_CHARS} to {MAX_CHARS}"
        )
    if not word.strip():
        raise SystemExit("entry word is only white space")
    if len(word.split()) != 1:
        raise SystemExit(f"entry must be exactly one word, got {word!r}")


def main() -> None:
    check_word(WORD)
    # Deterministic: the same single word on every run, no input,
    # no randomness, no network.
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(WORD, encoding="utf-8")


if __name__ == "__main__":
    main()
