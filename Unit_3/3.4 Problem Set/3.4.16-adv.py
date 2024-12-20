#In this problem, your goal is to write a function that can
#either count all the vowels in a string or all the consonants
#in a string.
#
#Call this function count_letters. It should have two
#parameters: the string in which to search, and a boolean
#called find_consonants. If find_consonants is True, then the
#function should count consonants. If it's False, then it
#should instead count vowels.
#
#Return the number of vowels or consonants in the string
#depending on the value of find_consonants. Do not count
#any characters that are neither vowels nor consonants (e.g.
#punctuation, spaces, numbers).
#
#You may assume the string will be all lower-case letters
#(no capital letters).


#Add your code here!
vowels = ["a", "e", "i", "o", "u"]
consonants = ["q", "w", "r", "t", "p", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "y"]
def count_letters(da_string, which):
    value = 0
    if which == True:
        for num in range(len(da_string)):
            if da_string[num] in consonants:
                value += 1
    elif which == False:
        for num in range(len(da_string)):
            if da_string[num] in vowels:
                value += 1
    return value

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print 14, then 7.

a_string = "up with the white and gold"

print(count_letters(a_string, True))
print(count_letters(a_string, False))




