#A common problem in academic settings is plagiarism
#detection. Fortunately, software can make this pretty easy!
#
#In this problem, you'll be given two files with text in
#them. Write a function called check_plagiarism with two
#parameters, each representing a filename. The function
#should find if there are any instances of 5 or more
#consecutive words appearing in both files. If there are,
#return the longest such string of words (in terms of number
#of words, not length of the string). If there are not,
#return the boolean False.
#
#For simplicity, the files will be lower-case text and spaces
#only: there will be no punctuation, upper-case text, or
#line breaks.
#
#We've given you three files to experiment with. file_1.txt
#and file_2.txt share a series of 5 words: we would expect
#check_plagiarism("file_1.txt", "file_2.txt") to return the
#string "if i go crazy then". file_1.txt and file_3.txt
#share two series of 5 words, and one series of 11 words:
#we would expect check_plagiarism("file_1.txt", "file_3.txt")
#to return the string "i left my body lying somewhere in the
#sands of time". file_2.txt and file_3.txt do not share any
#text, so we would expect check_plagiarism("file_2.txt",
#"file_3.txt") to return the boolean False.
#
#Be careful: there are a lot of ways to do this problem, but
#some would be massively time- or memory-intensive. If you
#get a MemoryError, it means that your solution requires
#storing too much in memory for the code to ever run to
#completion. If you get a message that says "KILLED", it
#means your solution takes too long to run.


#Add your code here!
def check_plagiarism(file1, file2):
    # Function to read a file and return a list of words
    def read_file(file):
        with open(file, 'r') as f:
            text = f.read().strip().split()
        return text
    
    # Read files
    text1 = read_file(file1)
    text2 = read_file(file2)
    
    # Function to find all sequences of 5 or more consecutive words in a text
    def find_sequences(text):
        sequences = []
        for i in range(len(text) - 4):
            sequence = ' '.join(text[i:i+5])
            sequences.append((sequence, i))
            # Generate longer sequences if possible
            length = 5
            while i + length < len(text):
                length += 1
                sequence = ' '.join(text[i:i+length])
                sequences.append((sequence, i))
        return sequences
    
    # Find sequences in both texts
    sequences1 = find_sequences(text1)
    sequences2 = find_sequences(text2)
    
    # Find longest common sequence
    longest_match = ""
    max_length = 0
    
    for seq1, start1 in sequences1:
        for seq2, start2 in sequences2:
            if seq1 == seq2:
                # Calculate length in terms of number of words
                length = seq1.count(' ') + 1
                if length > max_length:
                    max_length = length
                    longest_match = seq1
    
    # Return the longest match or False if no match found
    if max_length >= 5:
        return longest_match
    else:
        return False

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#if i go crazy then
#i left my body lying somewhere in the sands of time
#False
print(check_plagiarism("file_1.txt", "file_2.txt"))
print(check_plagiarism("file_1.txt", "file_3.txt"))
print(check_plagiarism("file_2.txt", "file_3.txt"))




