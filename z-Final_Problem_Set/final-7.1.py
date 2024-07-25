import csv

# Function to calculate win-loss-tie record
def calculate_record(data, team):
    wins = sum(1 for game in data if game[1] == team and int(game[3]) > int(game[4]))
    losses = sum(1 for game in data if game[1] == team and int(game[3]) < int(game[4]))
    ties = sum(1 for game in data if game[1] == team and int(game[3]) == int(game[4]))
    return f"{wins}-{losses}-{ties}"

# Open the CSV file
record_file = open('../resource/lib/public/georgia_tech_football.csv', 'r')
csv_reader = csv.reader(record_file)

# Skip header
next(csv_reader)

# Read all data into a list
data = list(csv_reader)

# 1. Who was the first team Georgia Tech ever played against?
first_opponent = data[-1][1]
print(first_opponent)

# 2. How many points has Georgia Tech scored all-time against Auburn?
total_points_scored_vs_auburn = sum(int(game[3]) for game in data if game[1] == 'Auburn')
print(total_points_scored_vs_auburn)

# 3. How many points has Auburn scored all-time against Georgia Tech?
total_points_against_auburn = sum(int(game[4]) for game in data if game[1] == 'Auburn')
print(total_points_against_auburn)

# -------------------------------------------------------------------------------------------------------------------#
# PROBLEM QUESTION(SSSSSSSS)


# 4. What is Georgia Tech's all-time record in home games?
gt_home_record = calculate_record([game for game in data if game[2] == 'Home'], "Georgia Tech")
print(gt_home_record)

# 5. What was Georgia Tech's record in all games played in the 2009 calendar year?
gt_2009_record = calculate_record([game for game in data if game[0].startswith('2009')], "Georgia Tech")
print(gt_2009_record)

# 6. What is Georgia Tech's all-time record in the month of October?
gt_october_record = calculate_record([game for game in data if game[0][5:7] == '10'], "Georgia Tech")
print(gt_october_record)

# 7. Georgia Tech played in the SEC from 1933 to 1963. What was its record during this time?
sec_years_record = calculate_record([game for game in data if '1933' <= game[0][:4] <= '1963'], "Georgia Tech")
print(sec_years_record)

# -------------------------------------------------------------------------------------------------------------------#

# 8. Against what team has Georgia Tech scored the most points?
opponent_most_points = max(set(game[1] for game in data), key=lambda x: sum(int(game[3]) for game in data if game[1] == x))
print(opponent_most_points)

# 9. What is one of the two teams that Georgia Tech has played, and yet has never scored any points against? Name either team.
teams_never_scored = [team for team in set(game[1] for game in data) if sum(int(game[3]) for game in data if game[1] == team) == 0]
print(teams_never_scored[0])

# 10. How many teams has played Georgia Tech and never scored a point?
teams_zero_points = sum(1 for team in set(game[1] for game in data) if sum(int(game[4]) for game in data if game[1] == team) == 0)
print(teams_zero_points)

# 11. Against what team does Georgia Tech have the highest scoring differential (points for minus points against) all-time?
highest_scoring_diff_team = max(set(game[1] for game in data), key=lambda x: sum(int(game[3]) - int(game[4]) for game in data if game[1] == x))
print(highest_scoring_diff_team)

# 12. Among teams that Georgia Tech has played at least 5 times, against which team does Georgia Tech have the highest average score differential?
teams_played_at_least_5_times = [team for team in set(game[1] for game in data) if sum(1 for game in data if game[1] == team) >= 5]
avg_diff_dict = {team: (sum(int(game[3]) - int(game[4]) for game in data if game[1] == team) / sum(1 for game in data if game[1] == team)) for team in teams_played_at_least_5_times}
team_highest_avg_diff = max(avg_diff_dict, key=avg_diff_dict.get)
print(team_highest_avg_diff)

# Close the file
record_file.close()
