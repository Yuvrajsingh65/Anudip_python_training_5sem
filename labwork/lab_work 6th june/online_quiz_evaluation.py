'''
7. Online Quiz Evaluation 
Problem Statement 
Correct answers: 
correct = ['A', 'C', 'B', 'D', 'A'] 
Student answers: 
student = ['A', 'B', 'B', 'D', 'C'] 
Write a program to: 
• Calculate score.  
• Display incorrectly answered question numbers.  
• Count correct and wrong answers.  
• Determine pass/fail (minimum 60%). 
'''
# Correct answers
correct = ['A', 'C', 'B', 'D', 'A']

# Student answers
student = ['A', 'B', 'B', 'D', 'C']

# Variables to count correct and wrong answers
correct_count = 0
wrong_count = 0

print("Incorrectly Answered Question Numbers:")

# Check each answer
for i in range(len(correct)):

    # If answer is correct
    if correct[i] == student[i]:
        correct_count += 1

    # If answer is wrong
    else:
        wrong_count += 1
        
        # Display question number
        print(i + 1)

# Calculate Score
score = correct_count

print("\nScore =", score, "out of", len(correct))

# Count Correct and Wrong Answers
print("Correct Answers =", correct_count)
print("Wrong Answers =", wrong_count)

# Determine Pass or Fail
percentage = (correct_count / len(correct)) * 100

print("Percentage =", percentage, "%")

# Minimum 60% required to pass
if percentage >= 60:
    print("Result : PASS")
else:
    print("Result : FAIL")
