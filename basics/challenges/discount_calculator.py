'''Discount Calculator
MRP aur discount% lo. Final price nikalo. Agar final price 1000+ hai toh extra 5% discount do. Show all steps.
Input: MRP=2000, Discount=20%
After 20%: ₹1600
Extra 5%: ₹1520 (Final)'''

mrp = int(input("Enter MRP : "))

discount = int(input("Enter Discount in % : "))

input_discount = mrp * (1 - discount / 100)

if(mrp > 1000):
    extra_discunt = input_discount * (1 - 5 / 100)

print("After 20%: ",input_discount)

print("After 5%: ",extra_discunt, "(Final)")