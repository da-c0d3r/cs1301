# Open the file
marta_file = open('../resource/lib/public/marta_01-18-2016.csv', 'r')

# Initialize variables to store station data
station_taps = {}
total_taps = 0

# Read through each line in the file
for line in marta_file:
    # Split the line by commas
    parts = line.split(",")
    
    # Extract the station ID (index 3 in the list)
    station_id = parts[3]
    
    # Increment the tap count for this station
    if station_id in station_taps:
        station_taps[station_id] += 1
    else:
        station_taps[station_id] = 1
    
    # Increment total taps count
    total_taps += 1

# Close the file
marta_file.close()

# Calculate the average number of taps per station
average_taps = total_taps / len(station_taps)

# Find the station ID closest to the average number of taps
closest_station = None
closest_difference = float('inf')

for station_id, taps in station_taps.items():
    difference = abs(taps - average_taps)
    if difference < closest_difference:
        closest_difference = difference
        closest_station = station_id

# Print the results
print("Average number of Breeze Card taps per station:", average_taps)
print("Station ID closest to the average number of taps:", closest_station)
print("Number of taps at this station:", station_taps[closest_station])
