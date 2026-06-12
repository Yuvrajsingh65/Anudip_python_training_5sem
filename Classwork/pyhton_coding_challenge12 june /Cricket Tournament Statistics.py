'''
Problem 7: Cricket Tournament Statistics 
Problem Statement 
Runs scored by players in a tournament are given below. 
Sample Data 
runs = { 
    "Virat": 645, 
    "Rohit": 512, 
    "Gill": 698, 
    "Rahul": 435, 
    "Hardik": 278, 
    "Pant": 534, 
    "Surya": 389, 
    "Jadeja": 301, 
    "Iyer": 455, 
    "KL": 410 
} 
Tasks 
1. Find the Orange Cap winner.  
2. Find the lowest scorer.  
3. Calculate total runs scored.  
4. Display players scoring more than 500 runs.  
5. Create a list of players scoring below 400. 
'''
# Cricket Tournament Statistics

# Dictionary storing player names and their runs
runs = {
    "Virat": 645,
    "Rohit": 512,
    "Gill": 698,
    "Rahul": 435,
    "Hardik": 278,
    "Pant": 534,
    "Surya": 389,
    "Jadeja": 301,
    "Iyer": 455,
    "KL": 410
}

# Task 1: Find the Orange Cap winner
# Orange Cap is given to the player with the highest runs
orange_cap = max(runs, key=runs.get)

print("Orange Cap Winner:")
print(orange_cap, ":", runs[orange_cap])

# Task 2: Find the lowest scorer
lowest_scorer = min(runs, key=runs.get)

print("\nLowest Scorer:")
print(lowest_scorer, ":", runs[lowest_scorer])

# Task 3: Calculate total runs scored by all players
total_runs = sum(runs.values())

print("\nTotal Runs Scored:", total_runs)

# Task 4: Display players scoring more than 500 runs
print("\nPlayers Scoring More Than 500 Runs:")

for player in runs:
    if runs[player] > 500:
        print(player, ":", runs[player])

# Task 5: Create a list of players scoring below 400 runs
below_400 = []

for player in runs:
    if runs[player] < 400:
        below_400.append(player)

print("\nPlayers Scoring Below 400 Runs:")
print(below_400)
