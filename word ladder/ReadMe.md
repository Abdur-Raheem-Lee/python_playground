# 🧩 Word Ladder

This project solves the **Word Ladder** problem, where you are given two words (`begin_word` and `end_word`), and a dictionary of valid words. Your goal is to transform the `begin_word` into the `end_word` by changing one letter at a time, with each intermediate word being a valid word in the dictionary.

## ✅ What This Program Does

- You can change one letter at a time to form a valid word.
- The new word must be in the given dictionary.
- Returns the **minimum number of transformations** needed to go from `begin_word` to `end_word`.
- If no transformation is possible, it returns `0`.

## 🧪 Examples

```python
word_ladder("hit", "cog", {"hot", "dot", "dog", "lot", "log", "cog"})  # ➞ 5 (hit → hot → dot → dog → cog)
word_ladder("hit", "dog", {"hot", "dot", "dog", "lot", "log", "cog"})  # ➞ 4 (hit → hot → dot → dog)
word_ladder("hit", "cog", {"hot", "dot", "dog", "lot", "log"})         # ➞ 0 (No valid transformation)
