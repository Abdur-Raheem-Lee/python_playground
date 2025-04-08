
import re

def pengram(sentence):
    
    return len(set([char for char in sentence.lower() if re.match(r'[a-z]', char)])) == 26
    

if __name__ == '__main__':    

    sentence = "The quick brown fox jumps over the lazy dog."
    print(pengram(sentence))