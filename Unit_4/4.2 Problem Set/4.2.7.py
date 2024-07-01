#Recall that input from a user is always in the form of a string. 
#Write a function called "input_type" that gets user input and 
#determines what kind of string the user entered. The user input
#will be supplied as an argument to the function like normal.
#
#  - Your function should return "integer" if the string only
#    contains characters 0-9.
#  - Your function should return "float" if the string only
#    contains the numbers 0-9 and at most one period.
#  - You should return "boolean" if the user enters "True" or
#    "False". 
#  - Otherwise, you should return "string".


#Write your function here!
# lists
boolean = ["True", "False"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
combined_letter = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", 
                   "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
def input_type(string):
    lister = list(string)
    if string in boolean:
        return "boolean"
    # counter(s)
    char = 0
    for i in range(len(lister)):
        if lister[i] in combined_letter:
            return "string"
        elif lister[i] == ".":
            return "float"
    if string == "":
        return "string"
    else:
        return "integer"

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#string
#boolean
#float
#integer
print(input_type(""))
print(input_type("False"))
print(input_type("7.432621"))
print(input_type("2788"))



