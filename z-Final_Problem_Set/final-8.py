#-----------------------------------------------------------
#The United States Social Security Administration publishes
#a list of all documented baby names each year, along with
#how often each name was used for boys and for girls. The
#list is used to see what names are most common in a given
#year.
#
#We've grabbed that data for any name used more than 25
#times, and provided it to you in a file called
#babynames.csv. The line below will open the file:

names_file = open('../resource/lib/public/babynames.csv', 'r')

#We've also provided a sample subset of the data in
#sample.csv.
#
#Each line of the file has three values, separated by
#commas. The first value is the name; the second value is
#the number of times the name was given in the 2010s (so
#far); and the third value is whether that count
#corresponds to girls or boys. Note that if a name is
#given to both girls and boys, it is listed twice: for
#example, so far in the 2010s, the name Jamie has been
#given to 611 boys and 1545 girls.
#
#Use this dataset to answer the questions below.
import csv

# Function to read the data from CSV file
def read_data(file_path):
    file = open(file_path, 'r', newline='', encoding='utf-8')
    reader = csv.reader(file)
    data = [row for row in reader]
    file.close()
    return data

# Read the data from the CSV file
file_path = '../resource/lib/public/babynames.csv'
data = read_data(file_path)

# How many total names are listed in the database?
total_names = len(data)
print(total_names)

# How many total births are covered by the names in the database?
total_births = sum(int(row[1]) for row in data)
print(total_births)

# -------------------------------------------------------------------------------------------------------------------#
# PROBLEM QUESTION(SSSSSSSS)

# How many different boys' names are there that begin with the letter Z?
z_boys_names = len([row for row in data if row[0][0] == 'Z' and row[2] == 'boy'])
print(z_boys_names)

# What is the most common girl's name that begins with the letter Q?
q_girls_names = [(row[0], int(row[1])) for row in data if row[0][0] == 'Q' and row[2] == 'girl']
if q_girls_names:
    most_common_q_name = max(q_girls_names, key=lambda x: x[1])[0]
else:
    most_common_q_name = ""
print(most_common_q_name)

# How many total babies were given names that both start and end with vowels (A, E, I, O, or U)?
vowel_start_end_names = [row for row in data if row[0][0] in 'AEIOU' and row[0][-1] in 'AEIOU']
total_vowel_names = sum(int(row[1]) for row in vowel_start_end_names)
print(total_vowel_names)


# -------------------------------------------------------------------------------------------------------------------#


# What letter is the least common first letter of a baby's name?
letters_count = {}
for row in data:
    first_letter = row[0][0]
    if first_letter.isalpha():
        if first_letter in letters_count:
            letters_count[first_letter] += int(row[1])
        else:
            letters_count[first_letter] = int(row[1])

least_common_letter = min(letters_count, key=letters_count.get)
print(least_common_letter)

# How many babies were born with names starting with that least-common letter?
least_common_count = letters_count[least_common_letter]
print(least_common_count)

# What letter is the most common first letter of a baby's name?
most_common_letter = max(letters_count, key=letters_count.get)
print(most_common_letter)

# How many babies were born with names starting with that most-common letter?
most_common_count = letters_count[most_common_letter]
print(most_common_count)

# If names were not separated by gender, what would be the most common name?
names_combined = {}
for row in data:
    name = row[0]
    if name in names_combined:
        names_combined[name] += int(row[1])
    else:
        names_combined[name] = int(row[1])

most_common_name = max(names_combined, key=names_combined.get)
max_occurrences = names_combined[most_common_name]
print(most_common_name)
print(max_occurrences)

# What name used for both genders has the smallest difference in which gender holds the name most frequently?
gender_difference = {}
for row in data:
    name = row[0]
    count = int(row[1])
    if name not in gender_difference:
        gender_difference[name] = {'boy': 0, 'girl': 0}
    if row[2] == 'boy':
        gender_difference[name]['boy'] += count
    elif row[2] == 'girl':
        gender_difference[name]['girl'] += count


# -------------------------------------------------------------------------------------------------------------------#
# PROBLEM QUESTION(SSSSSSSS)

# Calculate the smallest difference
smallest_difference_name = min(gender_difference, key=lambda x: abs(gender_difference[x]['boy'] - gender_difference[x]['girl']))
print(smallest_difference_name)



# -------------------------------------------------------------------------------------------------------------------#



#Here, add any code you want to allow you to answer the
#questions asked below over on edX. This is just a sandbox
#for you to explore the dataset: nothing is required for
#submission here.





