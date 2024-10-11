#-----------------------------------------------------------
#In this problem, you should write three functions:
#word_count, letter_count, and average_word_length.
#
#word_count should take as input a string. It should return
#the number of words in the string. You may assume that the
#number of words in the string will be one more than the
#number of spaces in the string.
#
#letter_count should take as input a string. It should return
#the number of letters in the string. You may assume that
#the string is only letters and spaces: no punctuation or
#numbers.
#
#average_word_length should take as input a string. It should
#return the average length of the words in the string. You
#can find the average length by dividing the number of letters
#by the number of words.
#
#Your implementation for average_word_length *must* call
#word_count and letter_count.


#Add your code here!
lower_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
upper_letters = ["A", "B", "C", "D", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
def word_count(string1):
    words = 1
    for num in range(len(string1)):
        if string1[num] == " ":
            words += 1
    #print(words)
    return words
def letter_count(string2):
    letter = 0
    for num in range(len(string2)):
        if string2[num] in lower_letters:
            letter += 1
        elif string2[num] in upper_letters:
            letter += 1
    #print(letter)
    return letter

def average_word_length(string3):
    word_counter = word_count(string3)
    word_counter = int(word_counter)
    letter_counter = letter_count(string3)
    letter_counter = int(letter_counter)
    average = letter_counter / word_counter
    return average



#Below are some lines of code that will test your function.
#You can change the value of the variable to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 3.5
a_string = "angst wakeup beforehand"

print(average_word_length(a_string))

