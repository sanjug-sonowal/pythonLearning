class Factorial:
    def __init__(self,num):
        self.num = num

    def factorial(num):
        fact = 1
        for i in range(1,num + 1):
            fact *= i
        return fact

print(Factorial.factorial(5))