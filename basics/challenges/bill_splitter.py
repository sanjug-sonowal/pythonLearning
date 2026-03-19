'''Bill Splitter
Total bill, number of people, aur tip percentage lo as input. Calculate karo per person kitna dena hai (tip include karke). Round to 2 decimal places.
Input: bill=1500, people=4, tip=10%
Output: ₹412.50 per person'''

bill = int(input("Enter your total bill amount : "))

peoples = int(input("Enter how many peoples : "))

tip = int(input("Enter tip in % : "))

total = bill * (1 + tip / 100)

splitted_bill = total / peoples

print(splitted_bill)