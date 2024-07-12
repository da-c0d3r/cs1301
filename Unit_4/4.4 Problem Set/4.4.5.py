#Recall Coding Problem 4.3.9 (Advanced), the free body
#diagram problem. If you were unable to solve that, we've
#included the sample answer in the dropdown in the top left
#-- feel free to use that to write your answer to this
#problem.
#
#Revise your code from that problem to use a file instead of
#a list as its parameter. Name this new function
#find_net_force_from_file. The function should take one
#parameter, the name of a file. The function should return
#the net magnitude and direction, just as it did in the other
#problem.
#
#Each line of the file will have two numbers, both integers:
#the first number will be the magnitude, and the second
#number will be the angle (in degrees, from -180 to 180).
#There will be a space between them.
#
#HINT: You may have multiple functions in your code if you
#want!
#
#HINT 2: Try to write this such that you can reuse as much
#of your earlier code as possible. Remember, when loading
#from a file, any text you load is initially a string. You'll
#almost certainly need to use the split() method.

from math import sin, cos, tan, asin, acos, atan2, radians, degrees, sqrt

#Add your function here!
def find_net_force_from_file(filename):
    horizontal_sum = 0
    vertical_sum = 0
    
    # Open the file
    file = open(filename, 'r')
    
    # Read each line from the file
    for line in file:
        parts = line.strip().split()
        magnitude = int(parts[0])
        angle_degrees = int(parts[1])
        
        # Convert angle to radians
        angle_radians = radians(angle_degrees)
        
        # Calculate components of the force
        horizontal_component = magnitude * cos(angle_radians)
        vertical_component = magnitude * sin(angle_radians)
        
        # Sum up components
        horizontal_sum += horizontal_component
        vertical_sum += vertical_component
    
    # Close the file
    file.close()
    
    # Calculate net magnitude and direction
    net_magnitude = sqrt(horizontal_sum ** 2 + vertical_sum ** 2)
    net_direction_degrees = degrees(atan2(vertical_sum, horizontal_sum))
    
    # Round to two decimal places
    net_magnitude = round(net_magnitude, 1)
    net_direction_degrees = round(net_direction_degrees, 1)
    
    # Ensure direction is within -180 to 180 range
    if net_direction_degrees < -180:
        net_direction_degrees += 360
    elif net_direction_degrees > 180:
        net_direction_degrees -= 360
    
    return (net_magnitude, net_direction_degrees)


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: (87.0, 54.4)
print(find_net_force_from_file("a_few_angles.txt"))




