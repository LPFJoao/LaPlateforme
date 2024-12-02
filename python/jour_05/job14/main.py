def my_long_word(n, sentence):
    
    words = []  
    current_word = ""  
    result = ""  

    
    for char in sentence:
        if char == " ":  
            if current_word:  
                words.append(current_word)
                current_word = ""  
        else:
            current_word += char  
    
    if current_word:
        words.append(current_word)

    
    for word in words:
        word_length = 0  
        for char in word:  
            word_length += 1

        
        if word_length > n:
            
            if result:
                result += " "  
            result += word

    
    return result


sentence = str(input("Write here your sentece to be checked : "))
print(my_long_word(int(input("Input here your desired number of characters : ")), sentence))