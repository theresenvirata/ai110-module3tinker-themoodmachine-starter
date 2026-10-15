# mood_analyzer.py
"""
Rule based mood analyzer for short text snippets.

This class starts with very simple logic:
  - Preprocess the text
  - Look for positive and negative words
  - Compute a numeric score
  - Convert that score into a mood label
"""

import re
from typing import List, Dict, Tuple, Optional

from dataset import POSITIVE_WORDS, NEGATIVE_WORDS

# Matches, in order: emoticons, emojis, then words (with inner apostrophes).
# Emoticons are matched first so ":)" isn't discarded as punctuation.
TOKEN_PATTERN = re.compile(
    r"[:;=]-?[()dpo/\\|]"
    r"|[\U0001F300-\U0001FAFF☀-➿]"
    r"|[a-z0-9]+(?:'[a-z]+)*"
)

NEGATORS = {
    "not", "no", "never", "dont", "don't", "isn't", "wasn't", "aren't",
    "can't", "cannot", "won't", "didn't", "doesn't",
    # Apostrophe-less and dialect forms
    "aint", "ain't", "isnt", "wasnt", "arent", "cant", "wont", "didnt", "doesnt",
}

# Emoticons/emojis treated as sentiment signals. Ambiguous ones (🥲, 💀) are left out.
POSITIVE_SIGNALS = {":)", ":-)", ":d", ":-d", "😊", "😍", "😂", "🥰", "❤"}
NEGATIVE_SIGNALS = {":(", ":-(", "😞", "😡", "😭", "☹"}


class MoodAnalyzer:
    """
    A very simple, rule based mood classifier.
    """

    def __init__(
        self,
        positive_words: Optional[List[str]] = None,
        negative_words: Optional[List[str]] = None,
    ) -> None:
        # Use the default lists from dataset.py if none are provided.
        positive_words = positive_words if positive_words is not None else POSITIVE_WORDS
        negative_words = negative_words if negative_words is not None else NEGATIVE_WORDS

        # Store as sets for faster lookup.
        self.positive_words = set(w.lower() for w in positive_words)
        self.negative_words = set(w.lower() for w in negative_words)

    # ---------------------------------------------------------------------
    # Preprocessing
    # ---------------------------------------------------------------------

    def preprocess(self, text: str) -> List[str]:
        """
        Convert raw text into a list of tokens the model can work with.

        Steps:
          - Strips whitespace and lowercases
          - Normalizes repeated characters ("soooo" -> "soo")
          - Keeps emoticons (":)", ":-(") and emojis ("🥲", "😂") as their own tokens
          - Drops punctuation, keeping apostrophes inside words ("don't")
        """
        cleaned = text.strip().lower()
        cleaned = re.sub(r"(.)\1{2,}", r"\1\1", cleaned)

        return TOKEN_PATTERN.findall(cleaned)

    # ---------------------------------------------------------------------
    # Scoring logic
    # ---------------------------------------------------------------------

    def score_text(self, text: str) -> int:
        """
        Compute a numeric "mood score" for the given text.

        Positive words increase the score.
        Negative words decrease the score.

        Modeling improvements:
          - Negation: a word right after a negator ("not happy", "not bad")
            has its sign flipped.
          - Emoticons and emojis (":)", ":(", "😭") count as signals too.
        """
        score, _, _ = self._score_tokens(self.preprocess(text))
        return score

    def _score_tokens(self, tokens: List[str]) -> Tuple[int, List[str], List[str]]:
        """Return (score, positive_hits, negative_hits) for a token list."""
        score = 0
        positive_hits: List[str] = []
        negative_hits: List[str] = []

        for i, token in enumerate(tokens):
            if token in self.positive_words or token in POSITIVE_SIGNALS:
                value = 1
            elif token in self.negative_words or token in NEGATIVE_SIGNALS:
                value = -1
            else:
                continue

            if i > 0 and tokens[i - 1] in NEGATORS:
                value = -value
                token = f"not {token}"

            score += value
            (positive_hits if value > 0 else negative_hits).append(token)

        return score, positive_hits, negative_hits

    # ---------------------------------------------------------------------
    # Label prediction
    # ---------------------------------------------------------------------

    def predict_label(self, text: str) -> str:
        """
        Turn the numeric score for a piece of text into a mood label.

        The default mapping is:
          - score > 0  -> "positive"
          - score < 0  -> "negative"
          - score == 0 -> "neutral"

        Adjustment: a score of 0 is "mixed" when the text contained both
        positive and negative signals that cancelled out, and "neutral" when
        it contained no signals at all. This matches the labels in TRUE_LABELS.
        """
        score, positive_hits, negative_hits = self._score_tokens(self.preprocess(text))

        if score > 0:
            return "positive"
        if score < 0:
            return "negative"
        if positive_hits and negative_hits:
            return "mixed"
        return "neutral"

    # ---------------------------------------------------------------------
    # Explanations (optional but recommended)
    # ---------------------------------------------------------------------

    def explain(self, text: str) -> str:
        """
        Return a short string explaining WHY the model chose its label.

        TODO:
          - Look at the tokens and identify which ones counted as positive
            and which ones counted as negative.
          - Show the final score.
          - Return a short human readable explanation.

        Example explanation (your exact wording can be different):
          'Score = 2 (positive words: ["love", "great"]; negative words: [])'

        The current implementation is a placeholder so the code runs even
        before you implement it.
        """
        score, positive_hits, negative_hits = self._score_tokens(self.preprocess(text))

        return (
            f"Score = {score} "
            f"(positive: {positive_hits or '[]'}, "
            f"negative: {negative_hits or '[]'})"
        )
