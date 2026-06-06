'''
2. Cricket Tournament Scorecard 
Problem Statement 
A batsman's scores in different matches are stored in a list. 
scores = [45, 78, 12, 100, 67, 8, 90, 55] 
Write a program to: 
• Count half-centuries and centuries.  
• Find the highest score.  
• Display all scores below 20.  
• Calculate the average score. 
'''
# List of batsman's scores
scores = [45, 78, 12, 100, 67, 8, 90, 55]

# Count Half-Centuries and Centuries

half_century = 0
century = 0

# Check each score one by one
for score in scores:

    # Score between 50 and 99 is a half-century
    if score >= 50 and score < 100:
        half_century += 1

    # Score 100 or more is a century
    elif score >= 100:
        century += 1

print("Half-Centuries =", half_century)
print("Centuries =", century)

# Find the Highest Score
# max() finds the largest value in the list
highest = max(scores)

print("Highest Score =", highest)

# Display Scores Below 20
print("Scores Below 20:")

# Print scores less than 20
for score in scores:
    if score < 20:
        print(score)

# Calculate Average Score

# sum() adds all scores
total = sum(scores)

# len() gives total number of scores
average = total / len(scores)

print("Average Score =", average)
