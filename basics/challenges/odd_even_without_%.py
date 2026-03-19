'''Bitwise Oddness
Ek number lo aur bitwise AND operator use karke check karo even hai ya odd. (if/else allowed but % modulo NOT allowed).
Input: 7
Output: Odd (because 7 & 1 = 1)'''

num = 3

if(num & 1 == 1):
    print("Odd")
else:
    print("Even")