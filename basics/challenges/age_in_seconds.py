'''Age in Seconds
User se age lo (in years). Convert karo seconds, minutes, hours, aur days me. Leap years ignore karo for simplicity.
Input: 21
Output: Days: 7665, Hours: 183960, Minutes: 11037600, Seconds: 662256000'''

age = int(input("Enter your age : "))

year_in_days = 365

hours_in_day = 24

minutes_in_hour = 60

seconds_in_minutes = 60

days = age * year_in_days

hours = age * year_in_days * hours_in_day

minutes = age * year_in_days * hours_in_day * minutes_in_hour

seconds = age * year_in_days * hours_in_day * minutes_in_hour * seconds_in_minutes

print("Days: ", days,",","Hours: ",hours,",","Minutes: ",minutes,",","Seconds: ",seconds)