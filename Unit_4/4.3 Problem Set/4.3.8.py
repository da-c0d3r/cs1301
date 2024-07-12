#Imagine you're writing some code for an exercise tracker.
#The tracker measures heart rate, and should display the
#average heart rate from an exercise session.
#
#However, the tracker doesn't automatically know when the
#exercise session began. It assumes the session starts the
#first time it sees a heart rate of 100 or more, and ends
#the first time it sees one under 100.
#
#Write a function called average_heart_rate.
#average_heart_rate should have one parameter, a list of
#integers. These integers represent heart rate measurements
#taken 30 seconds apart. average_heart_rate should return
#the average of all heart rates between the first 100+
#heart rate and the last one. Return this as an integer
#(use floor division when calculating the average).
#
#You may assume that the list will only cross the 100 beats
#per minute threshold once: once it goes above 100 and below
#again, it will not go back above.


#Add your function here!
def average_heart_rate(beats):
    start_index = None
    end_index = None
    
    # Find the first heart rate >= 100
    for i in range(len(beats)):
        if beats[i] >= 100:
            start_index = i
            break
    
    # Find the last heart rate < 100 after the first 100+ heart rate
    for i in range(start_index, len(beats)):
        if beats[i] < 100:
            end_index = i - 1
            break
    
    # Calculate the sum of heart rates between start_index and end_index
    total_sum = sum(beats[start_index:end_index + 1])
    
    # Calculate the average heart rate using integer division
    average_hr = total_sum // (end_index - start_index + 1)
    
    return average_hr


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print 114 (because there are 14 measurements from 102 to
#101, their sum is 1609, and 1609 // 14 is 114).
beats = [72, 77, 79, 95, 102, 105, 112, 115, 120, 121, 121,
         125, 125, 123, 119, 115, 105, 101, 96, 92, 90, 85]
print(average_heart_rate(beats))


