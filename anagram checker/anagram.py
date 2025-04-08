
def anagram(word1, word2):
    return sorted(word1.replace(" ", "")) == sorted(word2.replace(" ", ""))


if __name__ == "__main__":
    
    print(anagram("hello", "world"))