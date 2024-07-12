def length_words(sentence):
    # Normalize the input: convert to lowercase and remove punctuation
    sentence = sentence.lower().strip()
    sentence = sentence.replace(".", "").replace(",", "").replace("?", "").replace("!", "").replace("'", "")
    
    # Split sentence into words
    words = sentence.split()
    
    # Dictionary to store word lengths and corresponding words
    lengths = {}
    
    # Iterate through words
    for word in words:
        length = len(word)
        if length in lengths:
            lengths[length].append(word)
        else:
            lengths[length] = [word]
    
    return lengths