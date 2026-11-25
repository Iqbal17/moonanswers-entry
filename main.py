"""The Moon Finally Answers Back — make.fun entry.

Decision record (weighed against the judge's criteria, in the judge's order:
1) speaks as the Moon answering wishes/howls/promises, 2) funny on one read,
3) sounds like the Moon — wry, old, a little tired of being wished upon,
4) lands as a comeback in one read, 5) wastes none of its 240 characters).

Candidates:
A. "I have heard every wish you've ever made. None of them were about me."
   (74 chars) — Strong: directly answers the wishes, wry, instant turn in
   the second sentence. Loses because the joke could be said by ANY ignored
   listener — a bartender, a therapist, a dog. It scores weakly on
   criterion 3: nothing in it could only be said by the Moon.
B. "Stop promising me you'll change. I've watched you make the same
   promise for four billion years." (105 chars) — Strongest on criterion 3:
   the four-billion-year age is unmistakably the Moon, and it answers the
   late-night promises head on. Loses because the laugh is a slow burn:
   the reader has to do the arithmetic of "four billion years" before the
   joke lands, and it scolds rather than comebacks — criterion 2 and 4
   are weaker than the winner's.
C. "You wished on me, howled at me, and promised me things. I was a rock.
   I am still a rock." (96 chars) — Strong reserve: covers all three
   prompts (wishes, howls, promises) in one line, deadpan, very Moon.
   Loses because the punchline is a shrug, not a comeback: "I am still a
   rock" ends the conversation instead of winning it, and the turn arrives
   as a flat statement rather than a surprise (criterion 4).
D. "You keep howling at me like I did something. I just reflect light,
   Karen." (79 chars) — The "I just reflect light" fact is genuinely
   Moon-only and funny. Loses because "Karen" is a borrowed meme that
   dates the line and hands the laugh to a reference instead of the Moon's
   voice; the judge weighs the Moon's own voice, not a pop-culture tag.
E. WINNER: "I grant exactly one wish a night, and tonight's winner is the
   tide." (67 chars) — Wins because it beats every candidate on the
   criteria in order: (1) it answers the wishes directly, playing along
   with the premise that the Moon grants wishes; (2) the laugh is instant
   — "tonight's winner is the tide" subverts the wish in one beat;
   (3) the punchline uses a fact ONLY the Moon can claim (the tides are
   literally the Moon's doing), so the voice could belong to no one else;
   (4) the turn is the final word, arriving inside the line; (5) 67
   characters, nothing wasted.

Writing passes on the winner (genuine revisions):
Pass 1 — The early leader was candidate A ("I have heard every wish
   you've ever made..."). It was replaced by E because A scores on
   criteria 1-2 but fails criterion 3: any ignored listener could say it.
   E keeps A's wish-answering frame but makes the punchline Moon-only
   (the tide), which is exactly what the judge weighs third and what
   separates a Moon line from a generic complaint.
Pass 2 — Wording revision on E itself. First draft: "I grant one wish
   every night, and tonight the winner is the tide." Revised to "I grant
   exactly one wish a night, and tonight's winner is the tide." Reasons:
   "exactly" adds the deadpan of a weary clerk rationing wishes (more
   Moon-tired, criterion 3); "tonight's winner" tightens the reveal into
   a prize announcement; "a night" keeps the rhythm tighter than "every
   night". A trailing "Sorry." was tried and dropped: it explains the
   joke and softens the comeback, and the judge brief says a line that
   explains its own joke has already lost the laugh.
"""

import os

LINE = "I grant exactly one wish a night, and tonight's winner is the tide."
MAX_CHARS = 240


def check_gate(text):
    """Mirror the sealed gate: UTF-8 text, 1-240 chars, not only whitespace."""
    if not (1 <= len(text) <= MAX_CHARS):
        raise SystemExit("gate: entry must be 1-240 characters, got %d" % len(text))
    if not text.strip():
        raise SystemExit("gate: entry must not be only whitespace")
    text.encode("utf-8")


def entry_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main():
    check_gate(LINE)
    with open(entry_path(), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
