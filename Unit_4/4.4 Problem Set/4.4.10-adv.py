#This is a long one -- our answer is 20 lines of code, but
#yours will probably be longer. That's because it's one of the
#more authentic problems we've done so far. This is a real
#problem you'll start to face if you want to start creating
#useful programs.
#
#One of the reasons that filetypes work is that everyone 
#agrees how they are structured. A ".png" file, for example, 
#always contains "PNG" in the first four characters to 
#assure the program that the file is actually a png. If these
#standards were not set, it would be hard to write programs 
#that know how to open and read the file. 
#
#Let’s define a new filetype called ".cs1301". 
#In this file, every line should be structured like so:
#
#number assignment_name grade total weight
#
#In this file, each component will meet the following
#description:
#
# - number: an integer-like value of the assignment number 
#
# - assignment_name: a string value of the assignment name
#
# - grade: an integer-like value of a student’s grade
#
# - total: an integer-like value of the total possible
#   number of points
#
# - weight: a float-like value ranging from 0 to 1 
#   representing the percent of the student’s grade this 
#   assignment is worth. All the weights should add up to 1.
#
#Each component should be separated with exactly one space. 
#A good sample file is available to view as 
#"sample.cs1301".
#
#Write a function called format_checker that accepts a 
#filename and returns True if the file contents accurately 
#conform to the described format. Otherwise the function 
#should return False. In other words, it should return True
#if:
#
# - Each line has five elements separated by spaces, AND
# - The first, third, and fourth elements are integers, AND
# - The fifth element is a decimal number, AND
# - All the fifth elements add to 1.
#
#You can make changes to test.cs1301 to test your function,
#or test it with sample.cs1301. Right now, running it on
#sample.cs1301 should return True, and on test.cs1301
#should return False.
#
#Hint 1: .split() will likely help separate each line into 
#its components.
#Hint 2: .split() returns a list. So, if you were to do
#something like say split_line = line.split(), then
#split_line[0] would give the first item, split_line[1] would
#give the second item, etc.
#Hint 3: If you're having trouble, try breaking it down by
#parts. First check the file to see if it has the right
#number of items per line, then whether the items are of
#the correct type, then whether the fifth elements add to
#1. Remember, you know how to do each individual check
#(checking types, adding numbers, finding list lengths) --
#the hard part is knitting this all together into one bigger
#solution.


#Write your function here!
def format_checker(filename):
    total_weight = 0.0
    file = None
    
    try:
        file = open(filename, 'r')
        for line in file:
            split_line = line.strip().split()
            
            # Check if the line has exactly 5 elements
            if len(split_line) != 5:
                return False
            
            # Check if first, third, and fourth elements are integers
            try:
                number = int(split_line[0])
                grade = int(split_line[2])
                total = int(split_line[3])
            except ValueError:
                return False
            
            # Check if fifth element is a float and accumulate total weight
            try:
                weight = float(split_line[4])
                total_weight += weight
            except ValueError:
                return False
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return False
    
    finally:
        if file:
            file.close()
    
    # Check if total weight adds up to 1
    if round(total_weight, 5) != 1.0:  # Round to avoid floating point precision issues
        return False
    
    return True



#Test your function below. With the original values of these
#files, these should print True, then False:
print(format_checker("sample_1.cs1301"))
print(format_checker("sample_2.cs1301"))




