#You've been sent a list of names. Unfortunately, the names
#come in two different formats:
#
#First Middle Last
#Last, First Middle
#
#You want the entire list to be the same. For this problem,
#we'll say you want the entire list to be Last, First Middle.
#
#Write a function called name_refixer. name_refixer should have two
#parameters: an output filename (the first parameter) and the
#input filename (the second parameter). You may assume that every
#line will match one of the two formats above: either First Middle
#Last or Last, First Middle. 
#
#name_refixer should write to the output file the names all
#structured as Last, First Middle. If the name was already structured
#as Last, First Middle, it should remain unchanged. If it was
#structured as First Middle Last, then Last should be moved
#to the front and a comma should be added after it.
#
#The names should appear in the same order as the original file.
#
#For example, if the input file contained the following lines:
#David Andrew Joyner
#Hart, Melissa Joan
#Cyrus, Billy Ray
#
#...then the output file should contain these lines:
#Joyner, David Andrew
#Hart, Melissa Joan
#Cyrus, Billy Ray


#Add your code here!
def name_refixer(output_filename, input_filename):
    # Open input file for reading
    with open(input_filename, 'r') as input_file:
        lines = input_file.readlines()
    
    # Open output file for writing
    with open(output_filename, 'w') as output_file:
        for line in lines:
            # Remove leading/trailing whitespace and split the line into parts based on spaces
            parts = line.strip().split()
            
            # Check if the line is already in the correct format (Last, First Middle)
            if len(parts) == 3 and ',' in parts[0]:
                # Join the parts into a single string and write to output file
                corrected_name = ' '.join(parts)
            else:
                # Assume the line is in the format First Middle Last or something similar
                # Reorder the parts to Last, First Middle format
                last_name = parts[-1]  # Last part is the last name
                first_middle_names = ' '.join(parts[:-1])  # Join remaining parts as first and middle names
                corrected_name = f"{last_name}, {first_middle_names}"
            
            # Write the corrected name to the output file
            output_file.write(corrected_name + '\n')
            
#The code below will test your function. You can find the two
#files it references in the drop-down in the top left. If your
#code works, output_file.txt should have the text:
#Joyner, David Andrew
#Hart, Melissa Joan
#Cyrus, Billy Ray
name_refixer("output_file.txt", "input_file.txt")
print("Done running! Check output_file.txt for the result.")

#If you accidentally erase input_file.txt, here's its original
#text to copy back in (remove the pound signs):
#David Andrew Joyner
#Hart, Melissa Joan
#Cyrus, Billy Ray


