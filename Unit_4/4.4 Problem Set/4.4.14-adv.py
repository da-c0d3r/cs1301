#We've given you a file called "top500.txt" which contains
#the name and lifetime gross revenue of the top 500
#films at the time this question was written. 
#
#Each line of the given file is formatted like so:
# <name>\t<gross revenue in dollars>
#
#In other words, you should call .split("\t") to split
#the line into the movie name (the first item) and the
#gross (the second item).
#
#Unfortunately, these movies are not in order. Write a 
#function called "sort_films" that accepts two parameters:
#a string of a source filename and a string of a
#destination filename. Your function should open the
#source file and sort the contents from greatest gross
#revenue to least gross revenue, and write the sorted
#contents to the destination filename. You may assume the
#source file is correctly formatted.
#
#Hint: one common issue on this problem is that every line
#in the input file ends with a line break except the last
#one. If the autograder gives you an index error, open
#top500result.txt and make sure there are 500 lines in your
#output file!


#Write your function here!
def sort_films(source_filename, destination_filename):
    # Open source file for reading
    source_file = open(source_filename, 'r')
    lines = source_file.readlines()
    
    # Close the source file
    source_file.close()
    
    # Parse each line into (name, gross) tuple
    movies = []
    for line in lines:
        name, gross = line.strip().split("\t")
        gross = int(gross)  # Convert gross to integer
        movies.append((name, gross))
    
    # Sort movies by gross revenue in descending order
    sorted_movies = sorted(movies, key=lambda x: x[1], reverse=True)
    
    # Open destination file for writing
    destination_file = open(destination_filename, 'w')
    
    # Write sorted movies to destination file
    for movie in sorted_movies:
        destination_file.write(f"{movie[0]}\t{movie[1]}\n")
    
    # Close the destination file
    destination_file.close()

#The line of code below will test your function and put
#your results in top500result.txt. Then, it will print
#"Done!"
sort_films("top500.txt", "top500result.txt")
print("Done!")





