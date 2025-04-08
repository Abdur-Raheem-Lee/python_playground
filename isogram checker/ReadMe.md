# Isogram Checker

An **isogram** is a word or phrase with no repeating letters. This project checks whether a given input is an isogram.

## What This Program Does

- Takes a word or phrase as input.
- Ignores hyphens and spaces.
- Treats uppercase and lowercase letters as the same.
- Returns `True` if the input contains no repeated letters, otherwise `False`.

## Examples

```python
is_isogram("lumberjacks")       # ➞ True
is_isogram("background")        # ➞ True
is_isogram("six-year-old")      # ➞ True
is_isogram("isograms")          # ➞ False
is_isogram("Alphabet")          # ➞ False (case-insensitive)
