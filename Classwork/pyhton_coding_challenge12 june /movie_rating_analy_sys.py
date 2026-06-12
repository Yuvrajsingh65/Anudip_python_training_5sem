'''
Problem 10: Movie Rating Analysis System 
Problem Statement 
Ratings given by users for movies are stored below. 
Sample Data 
ratings = { 
    "Inception": 4.8, 
    "Avatar": 4.3, 
    "Titanic": 4.5, 
    "Joker": 4.7, 
    "Frozen": 3.8, 
    "Interstellar": 4.9, 
    "Dune": 4.6, 
    "Up": 4.1, 
    "Coco": 4.4, 
    "Cars": 3.9 
} 
Tasks 
1. Display movies rated above 4.5.  
2. Find the highest-rated movie.  
3. Find the lowest-rated movie.  
4. Calculate average rating.  
5. Create a recommendation list (rating ≥ 4.5). 
'''
# Movie Rating Analysis System

# Dictionary storing movie names and their ratings
ratings = {
    "Inception": 4.8,
    "Avatar": 4.3,
    "Titanic": 4.5,
    "Joker": 4.7,
    "Frozen": 3.8,
    "Interstellar": 4.9,
    "Dune": 4.6,
    "Up": 4.1,
    "Coco": 4.4,
    "Cars": 3.9
}

# Task 1: Display movies rated above 4.5
print("Movies Rated Above 4.5:")

for movie in ratings:
    if ratings[movie] > 4.5:
        print(movie, ":", ratings[movie])

# Task 2: Find the highest-rated movie
highest_movie = max(ratings, key=ratings.get)

print("\nHighest Rated Movie:")
print(highest_movie, ":", ratings[highest_movie])

# Task 3: Find the lowest-rated movie
lowest_movie = min(ratings, key=ratings.get)

print("\nLowest Rated Movie:")
print(lowest_movie, ":", ratings[lowest_movie])

# Task 4: Calculate average rating
average_rating = sum(ratings.values()) / len(ratings)

print("\nAverage Rating:", average_rating)

# Task 5: Create a recommendation list
# Movies with rating 4.5 or higher are recommended
recommendation_list = []

for movie in ratings:
    if ratings[movie] >= 4.5:
        recommendation_list.append(movie)

print("\nRecommended Movies:")
print(recommendation_list)
