'''Type Detective
User se ek input lo. Print karo ki wo int, float, ya str hai. Agar number hai toh even/odd bhi batao.
Input: 42
Output: Type: int, Even'''

num = int(input("Enter your number : "))

if(num % 2 == 0):
    print(type(num),",","Even")
else:
    print(type(num),",","Odd")