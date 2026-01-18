def solution(word):
    
    word_lst = []
    
    def create_word(cur_word):
        
        if len(cur_word) == 5:
            return
        
        for v in "AEIOU":
            new_word = cur_word + v
            word_lst.append(new_word)
            
            create_word(new_word)
    
    create_word("")
    return word_lst.index(word) + 1
