

def word_ladder(beginning_word, ending_word, words):
    
    if ending_word not in words or beginning_word == ending_word:
        return 0
    
    transformations = 0
    compared_words = set({})
    queue = [(beginning_word, transformations)]
    
    while queue:
        
        current_word, transformations = queue.pop(0)
            
        if current_word == ending_word:
            return transformations

        for word in one_letter_diff_word(current_word, words, compared_words):            
            if word not in compared_words:
                compared_words.add(word)
                queue.append((word, transformations+1))
                    
    
    
def one_letter_diff_word(beginning_word, words, compared_words):
    updated_words = []
    filtered_words = [word for word in words if word not in compared_words]
    
    for word in filtered_words:        
        different_letters = 0
        for char in range(len(word)):
            if beginning_word[char] != word[char]:
                different_letters+=1
                
        if different_letters == 1:
            updated_words.append(word)
        
    return updated_words