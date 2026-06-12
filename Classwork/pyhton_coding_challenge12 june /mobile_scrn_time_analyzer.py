'''
Problem 5: Mobile Screen Time Analyzer 
Problem Statement 
Daily mobile screen time (in minutes) of a student is recorded for 10 days. 
Sample Data 
screen_time = [180, 220, 150, 300, 120, 250, 190, 210, 175, 260] 
Tasks 
1. Calculate average screen time.  
2. Find the highest and lowest screen time.  
3. Count days exceeding 200 minutes.  
4. Display days with healthy usage (<180 minutes).  
5. Categorize usage:  
o Healthy (<180)  
o Moderate (180-240)  
o Excessive (>240) 
'''
# Sample Data
screen_time = [180, 220, 150, 300, 120, 250, 190, 210, 175, 260]
# 1. Calculate average screen time
average_screen_time = sum(screen_time) / len(screen_time)
print(f"Average Screen Time: {average_screen_time:.2f} minutes")
# 2. Find the highest and lowest screen time
highest_screen_time = max(screen_time)
lowest_screen_time = min(screen_time)
print(f"Highest Screen Time: {highest_screen_time} minutes")
print(f"Lowest Screen Time: {lowest_screen_time} minutes")
# 3. Count days exceeding 200 minutes
days_exceeding_200 = sum(1 for time in screen_time if time > 200)
print(f"Days exceeding 200 minutes: {days_exceeding_200}")
# 4. Display days with healthy usage (<180 minutes)
healthy_usage_days = [time for time in screen_time if time < 180]
print(f"Days with healthy usage (<180 minutes): {healthy_usage_days}")
# 5. Categorize usage
healthy = [time for time in screen_time if time < 180]
moderate = [time for time in screen_time if 180 <= time <= 240]
excessive = [time for time in screen_time if time > 240]

print(f"Healthy Usage (<180 minutes): {healthy}")
print(f"Moderate Usage (180-240 minutes): {moderate}")
print(f"Excessive Usage (>240 minutes): {excessive}")   

