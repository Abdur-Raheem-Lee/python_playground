import re

def isogram(phrase):
    checked = []
    for char in phrase.lower():
        if re.match(r'[a-z]', char):
            if char in checked:
                return False
            checked.append(char)            
    return True


if __name__ == "__main__":
    phrase = "Alphabet"
    print(isogram(phrase))