'''Swap Without Temp
Do variables swap karo bina koi third variable use kiye. Print before and after.
a = 10, b = 20
After swap → a = 20, b = 10'''

a = 10
b = 20

a = a ^ b
b = a ^ b
a = a ^ b

print(a,b)