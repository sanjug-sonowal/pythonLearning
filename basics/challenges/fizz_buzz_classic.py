'''FizzBuzz Classic
1 se 50 tak loop karo. Multiple of 3 → "Fizz", 5 → "Buzz", both → "FizzBuzz", else number print karo.'''


for i in range(1,50):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)


