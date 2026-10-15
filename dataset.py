"""
Shared data for the Mood Machine lab.

This file defines:
  - POSITIVE_WORDS: starter list of positive words
  - NEGATIVE_WORDS: starter list of negative words
  - SAMPLE_POSTS: short example posts for evaluation and training
  - TRUE_LABELS: human labels for each post in SAMPLE_POSTS
"""

# ---------------------------------------------------------------------
# Starter word lists
# ---------------------------------------------------------------------

POSITIVE_WORDS = [
    "happy",
    "great",
    "good",
    "love",
    "excited",
    "awesome",
    "fun",
    "chill",
    "relaxed",
    "amazing",
]

NEGATIVE_WORDS = [
    "sad",
    "bad",
    "terrible",
    "awful",
    "angry",
    "upset",
    "tired",
    "stressed",
    "hate",
    "boring",
]

# ---------------------------------------------------------------------
# Starter labeled dataset
# ---------------------------------------------------------------------

# Short example posts written as if they were social media updates or messages.
SAMPLE_POSTS = [
    "I love this class so much",
    "Today was a terrible day",
    "Feeling tired but kind of hopeful",
    "This is fine",
    "So excited for the weekend",
    "I am not happy about this",
    "Lowkey stressed but kind of proud of myself 🥲",
    "I absolutely love getting stuck in traffic 🙄",
    "no cap that concert was amazing, voice is gone 😂",
    "got the job!! but I have to move away from everyone 😭",
    "ugh this group project is killing me 💀",
    "just got home, gonna make some food and watch a show",
    "Highkey vibing today :)",
    "Not bad, I guess",
    "Oh great, another Monday meeting that could've been an email",
    "Love how my phone dies right when I need it most",
    "That new album is sick, the beats are fire 🔥",
    "I feel sick, been in bed all day",
    "I'm fine 🙂",
    "Exhausted but proud of myself",
    "Excited for the trip but nervous about flying 😬",
    "Wow, thanks for leaving me on read 🙃",
    "That final was brutal 💀 but I think I actually passed",
    "bruh my cat just knocked my coffee over, today is cooked 😭😂",
]

# Human labels for each post above.
# Allowed labels in the starter:
#   - "positive"
#   - "negative"
#   - "neutral"
#   - "mixed"
TRUE_LABELS = [
    "positive",  # "I love this class so much"
    "negative",  # "Today was a terrible day"
    "mixed",     # "Feeling tired but kind of hopeful"
    "neutral",   # "This is fine"
    "positive",  # "So excited for the weekend"
    "negative",  # "I am not happy about this"
    "mixed",     # "Lowkey stressed but kind of proud of myself 🥲"
    "negative",  # "I absolutely love getting stuck in traffic 🙄" (sarcasm)
    "positive",  # "no cap that concert was amazing, voice is gone 😂"
    "mixed",     # "got the job!! but I have to move away from everyone 😭"
    "negative",  # "ugh this group project is killing me 💀" (💀 is slang, edge case)
    "neutral",   # "just got home, gonna make some food and watch a show"
    "positive",  # "Highkey vibing today :)"
    "positive",  # "Not bad, I guess" (edge case: could be neutral)
    "negative",  # "Oh great, another Monday meeting..." (sarcasm: "great" is positive)
    "negative",  # "Love how my phone dies..." (sarcasm: "love" is positive)
    "positive",  # "That new album is sick, the beats are fire 🔥" (slang: sick/fire = good)
    "negative",  # "I feel sick, been in bed all day" (literal "sick" = ill)
    "neutral",   # "I'm fine 🙂" (edge case: could be negative, passive-aggressive)
    "mixed",     # "Exhausted but proud of myself"
    "mixed",     # "Excited for the trip but nervous about flying 😬"
    "negative",  # "Wow, thanks for leaving me on read 🙃" (sarcasm, 🙃 is ironic)
    "mixed",     # "That final was brutal 💀 but I think I actually passed"
    "mixed",     # "bruh my cat just knocked my coffee over..." (edge case: annoyed but amused)
]

# TODO: Add 5-10 more posts and labels.
#
# Requirements:
#   - For every new post you add to SAMPLE_POSTS, you must add one
#     matching label to TRUE_LABELS.
#   - SAMPLE_POSTS and TRUE_LABELS must always have the same length.
#   - Include a variety of language styles, such as:
#       * Slang ("lowkey", "highkey", "no cap")
#       * Emojis (":)", ":(", "🥲", "😂", "💀")
#       * Sarcasm ("I absolutely love getting stuck in traffic")
#       * Ambiguous or mixed feelings
#
# Tips:
#   - Try to create some examples that are hard to label even for you.
#   - Make a note of any examples that you and a friend might disagree on.
#     Those "edge cases" are interesting to inspect for both the rule based
#     and ML models.
#
# Example of how you might extend the lists:
#
# SAMPLE_POSTS.append("Lowkey stressed but kind of proud of myself")
# TRUE_LABELS.append("mixed")
#
# Remember to keep them aligned:
#   len(SAMPLE_POSTS) == len(TRUE_LABELS)
