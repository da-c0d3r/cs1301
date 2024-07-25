#Last problem, you wrote a function that generated the all-
#time win-loss-tie record for Georgia Tech against any other
#team.
#
#That dataset had a lot of other information in it. Let's
#use it to answer some more questions. As a reminder, the
#data will be a CSV file, meaning that each line will be a
#comma-separated list of values. Each line will describe one
#game.
#
#The columns, from left-to-right, are:
#
# - Date: the date of the game, in Year-Month-Day format.
# - Opponent: the name of the opposing team
# - Location: Home, Away, or Neutral
# - Points For: Points scored by Georgia Tech
# - Points Against: Points scored by the opponent

#This line will open the file:
import csv
from collections import defaultdict

# File path
file_path = '../resource/lib/public/georgia_tech_football.csv'

def process_data():
    # Initialize data structures
    teams_points = defaultdict(int)
    teams_points_against = defaultdict(int)
    location_records = {'Home': {'wins': 0, 'losses': 0, 'ties': 0},
                        'Away': {'wins': 0, 'losses': 0, 'ties': 0}}
    year_records = defaultdict(lambda: {'wins': 0, 'losses': 0, 'ties': 0})
    month_records = defaultdict(lambda: {'wins': 0, 'losses': 0, 'ties': 0})
    sec_records = {'SEC': {'wins': 0, 'losses': 0, 'ties': 0}}
    team_stats = defaultdict(lambda: {'points_for': 0, 'points_against': 0, 'games': 0})
    teams_no_points = set()
    all_teams = set()
    
    # Read and process the CSV file
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip header
        
        for row in reader:
            date = row[0]
            opponent = row[1]
            location = row[2]
            points_for = int(row[3])
            points_against = int(row[4])
            
            # Track all teams
            all_teams.add(opponent)
            
            # Track points scored and points against
            teams_points[opponent] += points_for
            teams_points_against[opponent] += points_against
            
            # Track home/away records
            if location in location_records:
                if points_for > points_against:
                    location_records[location]['wins'] += 1
                elif points_for < points_against:
                    location_records[location]['losses'] += 1
                else:
                    location_records[location]['ties'] += 1
            
            # Track record by year
            year = date[:4]
            if year:
                if points_for > points_against:
                    year_records[year]['wins'] += 1
                elif points_for < points_against:
                    year_records[year]['losses'] += 1
                else:
                    year_records[year]['ties'] += 1
            
            # Track record by month
            month = date[5:7]
            if month:
                if points_for > points_against:
                    month_records[month]['wins'] += 1
                elif points_for < points_against:
                    month_records[month]['losses'] += 1
                else:
                    month_records[month]['ties'] += 1
            
            # Track SEC records
            if 1933 <= int(date[:4]) <= 1963:
                if points_for > points_against:
                    sec_records['SEC']['wins'] += 1
                elif points_for < points_against:
                    sec_records['SEC']['losses'] += 1
                else:
                    sec_records['SEC']['ties'] += 1
            
            # Track no-point games
            if points_for == 0:
                teams_no_points.add(opponent)
            
            # Track scoring differentials
            team_stats[opponent]['points_for'] += points_for
            team_stats[opponent]['points_against'] += points_against
            team_stats[opponent]['games'] += 1
    
    # Determine answers
    def first_team_played():
        first_game_date = None
        first_team = None
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                date = row[0]
                opponent = row[1]
                if first_game_date is None or date < first_game_date:
                    first_game_date = date
                    first_team = opponent
        return first_team
    
    def total_points_scored_against(opponent_name):
        return teams_points[opponent_name]
    
    def total_points_against(opponent_name):
        return teams_points_against[opponent_name]
    
    def record_by_location(location):
        return f"{location_records[location]['wins']}-{location_records[location]['losses']}-{location_records[location]['ties']}"
    
    def record_by_year(year):
        return f"{year_records[year]['wins']}-{year_records[year]['losses']}-{year_records[year]['ties']}"
    
    def record_by_month(month):
        return f"{month_records[month]['wins']}-{month_records[month]['losses']}-{month_records[month]['ties']}"
    
    def record_by_year_range(start_year, end_year):
        wins = 0
        losses = 0
        ties = 0
        for year in range(int(start_year), int(end_year) + 1):
            year_str = str(year)
            wins += year_records[year_str]['wins']
            losses += year_records[year_str]['losses']
            ties += year_records[year_str]['ties']
        return f"{wins}-{losses}-{ties}"
    
    def team_with_most_points_scored():
        return max(teams_points, key=teams_points.get)
    
    def teams_with_no_points_scored():
        return teams_no_points
    
    def team_with_highest_scoring_differential():
        highest_diff = float('-inf')
        best_team = None
        for team, stats in team_stats.items():
            diff = stats['points_for'] - stats['points_against']
            if diff > highest_diff:
                highest_diff = diff
                best_team = team
        return best_team
    
    def team_with_highest_avg_scoring_diff():
        highest_avg_diff = float('-inf')
        best_team = None
        for team, stats in team_stats.items():
            avg_diff = (stats['points_for'] - stats['points_against']) / stats['games'] if stats['games'] > 0 else 0
            if avg_diff > highest_avg_diff:
                highest_avg_diff = avg_diff
                best_team = team
        return best_team
    
    # Print results
    print("First team Georgia Tech ever played against:", first_team_played())
    print("Total points Georgia Tech scored against Auburn:", total_points_scored_against("Auburn"))
    print("Total points scored by Auburn against Georgia Tech:", total_points_against("Auburn"))
    print("Georgia Tech's all-time record in home games:", record_by_location('Home'))
    print("Georgia Tech's record in 2009:", record_by_year("2009"))
    print("Georgia Tech's all-time record in October:", record_by_month("10"))
    print("Georgia Tech's record in the SEC (1933-1963):", record_by_year_range("1933", "1963"))
    print("Team Georgia Tech has scored the most points against:", team_with_most_points_scored())
    print("Teams Georgia Tech has played and never scored against:", teams_with_no_points_scored())
    print("Number of teams Georgia Tech has played and never scored a point against:", len(teams_with_no_points_scored()))
    print("Team with the highest scoring differential:", team_with_highest_scoring_differential())
    print("Team with the highest average scoring differential:", team_with_highest_avg_scoring_diff())

# Run the processing
process_data()



#Here, add any code you want to allow you to answer the
#questions asked below over on edX. This is just a sandbox
#for you to explore the dataset: nothing is required for
#submission here.





