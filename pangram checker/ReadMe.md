# Pangram Checker

A **pangram** is a sentence that contains every letter of the English alphabet at least once. This project checks whether a given sentence is a pangram.

## What This Program Does

- Takes a string input.
- Ignores case (i.e., treats uppercase and lowercase letters the same).
- Ignores spaces and punctuation.
- Returns `True` if the sentence contains all 26 letters of the alphabet at least once, otherwise `False`.

## Examples

```python
is_pangram("The quick brown fox jumps over the lazy dog")  # ➞ True
is_pangram("Hello World")                                  # ➞ False
