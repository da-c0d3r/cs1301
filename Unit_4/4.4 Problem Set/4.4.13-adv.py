#Write a function called get_grade that will read a
#given .cs1301 file and return the student's grade.
#To do this, we would recommend you first pass the
#filename to your previously-written reader() function,
#then use the list that it returns to do your
#calculations. You may assume the file is well-formed.
#
#A student's grade should be 100 times the sum of each
#individual assignment's grade divided by its total,
#multiplied by its weight. So, if the .cs1301 just had
#these two lines:
#
# 1 exam_1 80 100 0.6
# 2 exam_2 30 50 0.4
#
#Then the result would be 72:
#
# (80 / 100) * 0.6 + (30 / 50) * 0.4 = 0.72 * 100 = 72


#Write your function here!
def get_grade(filename):
    total_grade = 0.0
    total_weight = 0.0
    
    try:
        # Open the file
        file = open(filename, 'r')
        
        # Read lines one by one
        for line in file:
            split_line = line.strip().split()
            
            # Convert each component to the appropriate type
            number = int(split_line[0])
            assignment_name = split_line[1]
            grade = int(split_line[2])
            total = int(split_line[3])
            weight = float(split_line[4])
            
            # Calculate contribution to total grade
            assignment_grade = (grade / total) * weight
            total_grade += assignment_grade
            total_weight += weight
        
        # Check if total weight adds up to 1
        if round(total_weight, 5) != 1.0:
            print(f"Warning: Total weight of assignments does not add up to 1.0 in {filename}.")
        
        # Close the file
        file.close()
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    
    return total_grade * 100


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 91.55 
print(get_grade("sample.cs1301"))





