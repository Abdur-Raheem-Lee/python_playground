

def word_ladder(beginning_word, ending_word, words):
    
    if ending_word not in words or beginning_word == ending_word:
        return 0
    
    transformations = 0
    compared_words = []
    
    while True:
         
        oldw = one_letter_diff_word(beginning_word, words, compared_words)

        for word in oldw:
            
            if word not in compared_words:
                beginning_word = word
                compared_words.append(beginning_word)
                transformations+=1
                break  
            
        if beginning_word == ending_word:
            return transformations
              
        if not oldw:
            return 0
                    
    
    
def one_letter_diff_word(beginning_word, words, compared_words):
    updated_words = []
    for word in words:
        if word in compared_words:
            continue
        
        different_letters = 0
        for char in range(len(word)):
            if beginning_word[char] != word[char]:
                different_letters+=1
                
        if different_letters == 1:
            updated_words.append(word)
        
    return updated_words