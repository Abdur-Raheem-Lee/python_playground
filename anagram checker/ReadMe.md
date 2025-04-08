# Anagram Checker

An **anagram** is a word or phrase formed by rearranging the letters of another, using all the original letters exactly once. This project checks whether two strings are anagrams of each other.

## What This Program Does

- Takes two strings as input.
- Ignores spaces and punctuation.
- Treats uppercase and lowercase letters as the same.
- Returns `True` if the inputs are valid anagrams, otherwise `False`.

## Examples

```python
is_anagram("listen", "silent")           # ➞ True
is_anagram("The eyes", "They see")       # ➞ True
is_anagram("Dormitory", "Dirty room")    # ➞ True
is_anagram("hello", "world")             # ➞ False
