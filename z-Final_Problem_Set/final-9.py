#The line below will open a file containing information
#about every pokemon through Generation 7:

pokedex = open('../resource/lib/public/pokedex.csv', 'r')

#We've also provided a sample subset of the data in
#sample.csv.
#
#Each line of the file has 13 values, separated by commas.
#They are: 
#
#
# - Number: The numbered ID of the Pokemon, an integer
# - Name: The name of the Pokemon, a string
# - Type1: The Pokemon's primary type, a string
# - Type2: The Pokemon's secondary type, a string (this
#   may be blank)
# - HP: The Pokemon's HP statistic, an integer in the range
#   1 to 255
# - Attack: The Pokemon's Attack statistic, an integer in
#   the range 1 to 255
# - Defense: The Pokemon's Defense statistic, an integer in
#   the range 1 to 255
# - SpecialAtk: The Pokemon's Special Attack statistic, an
#   integer in the range 1 to 255
# - SpecialDef: The Pokemon's Special Defense statistic, an
#   integer in the range 1 to 255
# - Speed: The Pokemon's Speed statistic, an integer in the
#   range 1 to 255
# - Generation: What generation the Pokemon debuted in, an
#   integer in the range 1 to 7
# - Legendary: Whether the Pokemon is considered "legendary"
#   or not, either TRUE or FALSE
# - Mega: Whether the Pokemon is "Mega" or not, either TRUE
#   or FALSE
#
#Use this dataset to answer the questions below.

#How many Pokemon have only one type? In other words, for how many Pokemon is Type2 blank?

#What is the most common type? Include both Type1 and Type2 in your count.

#What Pokemon has the highest HP statistic?

#Excluding Pokemon that are either Mega or Legendary, what Pokemon has the highest Defense statistic?

#Among Legendary Pokemon, what is the most common type? Include both Type1 and Type2 in your count.

#In terms of the sum of all six stats (HP, Attack, Defense, Special Attack, Special Defense, and Speed), what is the weakest Legendary Pokemon? If there is a tie, list any of the tying Pokemon.

#In terms of the sum of all six stats (HP, Attack, Defense, Special Attack, Special Defense, and Speed), what is the strongest non-Legendary, non-Mega Pokemon? If there is a tie, list any of the tying Pokemon.

#What type has the highest average Speed statistic? Include both Type1 and Type2 in your calculation.

#Rounded to the nearest integer, what is that highest average Speed statistic? Include both Type1 and Type2 in your calculation.

#Among all 7 Pokemon generations, which generation had the highest average sum of all six stats (HP, Attack, Defense, Special Attack, Special Defense, and Speed)?

#Rounded to the nearest integer, how much higher was that statistic than the next-closest generation's average sum of all six stats (HP, Attack, Defense, Special Attack, Special Defense, and Speed)?

#Rounded to the nearest integer, how much higher is the average sum of all six stats among Mega Pokemon than their non-Mega versions? Note that Mega Pokemon share the same Number (the first column) as their non-Mega versions, which will allow you to find all Pokemon that have a Mega version.

#Here, add any code you want to allow you to answer the
#questions asked below over on edX. This is just a sandbox
#for you to explore the dataset: nothing is required for
#submission here.

pokedex = open('../resource/lib/public/pokedex.csv', 'r')

# Skip the header
pokedex.readline()

# Initialize variables
one_type_count = 0
type_counts = {}
highest_hp_pokemon = None
highest_hp = 0
highest_defense_non_mega_legendary = None
highest_defense = 0
legendary_type_counts = {}
weakest_legendary_pokemon = None
weakest_legendary_stat_sum = float('inf')
strongest_non_mega_legendary_pokemon = None
strongest_non_mega_legendary_stat_sum = 0
type_speed_sums = {}
type_speed_counts = {}
generation_stat_sums = {}
generation_counts = {}
mega_stat_sums = {}
non_mega_stat_sums = {}

# Read and process each line of the file
for line in pokedex:
    data = line.strip().split(',')
    number = int(data[0])
    name = data[1]
    type1 = data[2]
    type2 = data[3]
    hp = int(data[4])
    attack = int(data[5])
    defense = int(data[6])
    special_atk = int(data[7])
    special_def = int(data[8])
    speed = int(data[9])
    generation = int(data[10])
    legendary = data[11] == 'TRUE'
    mega = data[12] == 'TRUE'
    
    # Count Pokemon with only one type
    if type2 == "":
        one_type_count += 1
    
    # Count types
    if type1 not in type_counts:
        type_counts[type1] = 0
    type_counts[type1] += 1
    if type2:
        if type2 not in type_counts:
            type_counts[type2] = 0
        type_counts[type2] += 1
    
    # Find Pokemon with highest HP
    if hp > highest_hp:
        highest_hp = hp
        highest_hp_pokemon = name
    
    # Find highest Defense excluding Mega or Legendary
    if not mega and not legendary and defense > highest_defense:
        highest_defense = defense
        highest_defense_non_mega_legendary = name
    
    # Count Legendary types
    if legendary:
        if type1 not in legendary_type_counts:
            legendary_type_counts[type1] = 0
        legendary_type_counts[type1] += 1
        if type2:
            if type2 not in legendary_type_counts:
                legendary_type_counts[type2] = 0
            legendary_type_counts[type2] += 1
    
    # Find weakest Legendary in terms of stat sum
    stat_sum = hp + attack + defense + special_atk + special_def + speed
    if legendary and stat_sum < weakest_legendary_stat_sum:
        weakest_legendary_stat_sum = stat_sum
        weakest_legendary_pokemon = name
    
    # Find strongest non-Mega, non-Legendary in terms of stat sum
    if not mega and not legendary and stat_sum > strongest_non_mega_legendary_stat_sum:
        strongest_non_mega_legendary_stat_sum = stat_sum
        strongest_non_mega_legendary_pokemon = name
    
    # Calculate type speed sums and counts
    if type1 not in type_speed_sums:
        type_speed_sums[type1] = 0
        type_speed_counts[type1] = 0
    type_speed_sums[type1] += speed
    type_speed_counts[type1] += 1
    if type2:
        if type2 not in type_speed_sums:
            type_speed_sums[type2] = 0
            type_speed_counts[type2] = 0
        type_speed_sums[type2] += speed
        type_speed_counts[type2] += 1
    
    # Calculate generation stat sums and counts
    if generation not in generation_stat_sums:
        generation_stat_sums[generation] = 0
        generation_counts[generation] = 0
    generation_stat_sums[generation] += stat_sum
    generation_counts[generation] += 1
    
    # Calculate Mega and non-Mega stat sums
    if mega:
        if number not in mega_stat_sums:
            mega_stat_sums[number] = 0
        mega_stat_sums[number] += stat_sum
    else:
        if number not in non_mega_stat_sums:
            non_mega_stat_sums[number] = 0
        non_mega_stat_sums[number] += stat_sum

pokedex.close()

# Calculate the most common type
most_common_type = max(type_counts, key=type_counts.get)

# Calculate the most common Legendary type
most_common_legendary_type = max(legendary_type_counts, key=legendary_type_counts.get)

# Calculate the type with the highest average Speed statistic
highest_avg_speed_type = max(type_speed_sums, key=lambda t: type_speed_sums[t] / type_speed_counts[t])
highest_avg_speed = round(type_speed_sums[highest_avg_speed_type] / type_speed_counts[highest_avg_speed_type])

# Calculate the generation with the highest average stat sum
highest_avg_stat_generation = max(generation_stat_sums, key=lambda g: generation_stat_sums[g] / generation_counts[g])
highest_avg_stat_sum = round(generation_stat_sums[highest_avg_stat_generation] / generation_counts[highest_avg_stat_generation])

# Find the second highest average stat sum
sorted_generations = sorted(generation_stat_sums.items(), key=lambda x: x[1] / generation_counts[x[0]], reverse=True)
second_highest_avg_stat_sum = round(sorted_generations[1][1] / generation_counts[sorted_generations[1][0]])

# Calculate the difference between the highest and second highest average stat sums
avg_stat_sum_diff = highest_avg_stat_sum - second_highest_avg_stat_sum

# Calculate the average stat sum difference between Mega and non-Mega versions
total_mega_stat_sum = sum(mega_stat_sums.values())
total_non_mega_stat_sum = sum(non_mega_stat_sums.values())
average_mega_stat_sum = total_mega_stat_sum / len(mega_stat_sums)
average_non_mega_stat_sum = total_non_mega_stat_sum / len(non_mega_stat_sums)
average_stat_sum_diff = round(average_mega_stat_sum - average_non_mega_stat_sum)

# Answers to questions (last one is wrong)
print("Pokemon with only one type:", one_type_count)
print("Most common type:", most_common_type)
print("Pokemon with the highest HP:", highest_hp_pokemon)
print("Highest Defense non-Mega, non-Legendary Pokemon:", highest_defense_non_mega_legendary)
print("Most common type among Legendary Pokemon:", most_common_legendary_type)
print("Weakest Legendary Pokemon:", weakest_legendary_pokemon)
print("Strongest non-Mega, non-Legendary Pokemon:", strongest_non_mega_legendary_pokemon)
print("Type with the highest average Speed:", highest_avg_speed_type)
print("Highest average Speed statistic:", highest_avg_speed)
print("Generation with the highest average stat sum:", highest_avg_stat_generation)
print("Difference between highest and second highest average stat sums:", avg_stat_sum_diff)
print("Average stat sum difference between Mega and non-Mega versions:", average_stat_sum_diff)


