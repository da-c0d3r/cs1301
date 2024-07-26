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
#open dataset

#Use this dataset to answer the questions below.

baby_list=[]

for line in names_file:
    line=line.strip().split(",")
    name=line[0]
    count=int(line[1])
    gender=line[2]
    baby_list.append([name,count,gender])

#How many total names are listed in the database?
print('Total names:',len(baby_list))

#How many total births are covered by the names in the database?
births=0
for data in baby_list:
    births=births+data[1]

print('total births:',births)

#How many different boys' names are there that begin with the letter Z?
#(Count the names, not the people.)
names_with_z=0
for data in baby_list:
    if data[0][0]=='Z' and data[2]=='Boy':
        names_with_z=names_with_z+1

print('Different boys names are there that begin with the letter Z:',names_with_z)

#What is the most common girl's name that begins with the letter Q?
names_with_Q=0
for data in baby_list:
    if data[0][0]=='Q' and data[2]=='Girl' and data[1]> names_with_Q:
        girl_name=data[0]
        names_with_Q=data[1]

print('The most common girl\'s name that begins with the letter Q:',names_with_Q)

#How many total babies were given names that both start and end with vowels (A, E, I, O, or U)?
vowels='AEIOUaeiou'
total_names=0
for data in baby_list:
    if data[0][0] in vowels and data[0][-1] in vowels:
        total_names=total_names+ data[1]

print('The total babies were given names that both start and end with vowels(A,E,I,O,or U):'\
      ,total_names)

#Here, add any code you want to allow you to answer the
#questions asked below over on edX. This is just a sandbox
#for you to explore the dataset: nothing is required for
#submission here.

#What letter is the least common first letter of a baby's name
name_list = {}
for i in range(len(baby_list)):
    fl = list(baby_list[i][0])[0]
    if fl not in name_list.keys():
        name_list[fl] = 1
    else:
        name_list[fl] = int(name_list[fl]) + 1
#What letter is the least common first letter of a baby's name
leastKey = 9999
mostKey = 0
least=''
most=''
print(name_list.keys())
for key in name_list.keys():
    if name_list[key] < leastKey:
        least = key
        leastKey = name_list[key]
    if name_list[key] > mostKey:
        most = key
        mostKey = name_list[key]
print('\nThe letter is the least common first letter of a baby\'s name is: ',least)
#How many babies were born with names starting with that least-common letter?
print('\nNumber of babie names starting with that least-common letter',name_list[least])
#What letter is the most common first letter of a baby's name
print("\nThe letter is the most common first letter of a baby's name is: ",most)
#How many babies were born with names starting with that most-common letter?
print('\nNumber of babie names starting with that most-common letter: ',name_list[most])

'''
#By default, the Social Security Administration's data separates out names by gender.
#For example, Jamie is listed separately for girls and for boys.
#If you were to remove this separation, what would be the most common name
in the 2010s regardless of gender?
'''
name_list = {}
for i in range(len(baby_list)):
    name = baby_list[i][0]
    ctr = baby_list[i][1]
    gndr = baby_list[i][2]
    if name in name_list.keys():
        name_list[name] = int(name_list[name]) + 1
    else:
        name_list[name] = 1
mostKey = 0
most=''
for key in name_list.keys():
    if name_list[key] > mostKey:
        most = key
        mostKey = name_list[key]
print('\nThe most common name in the 2010s regardless of gender: ',most)

#How many people would have that name?
print('\nThe number of people have most common name regardless of gender: ',mostKey)

'''
What name that is used for both genders has the smallest difference in
which gender holds the name most frequently? In case of a tie,
enter any one of the correct answers.
'''
mini = name_list[most]
name_list = {}
for i in range(len(baby_list)):
    name = baby_list[i][0]
    ctr = baby_list[i][1]
    gndr = baby_list[i][2]
    if name in name_list.keys() and gndr != name_list[name][1]:
        name_list[name] = [int(name_list[name][0]) -1, gndr, 1]
    else:
        name_list[name] = [1, gndr, 0]

for x in name_list.keys():
    if name_list[x][2] == 1 and name_list[x][0] < mini:
        mini = name_list[x][0]
        nme = x
print('Name that is used for both genders has the smallest difference: ',x)