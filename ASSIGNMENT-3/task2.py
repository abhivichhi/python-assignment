import math

def mathfunctions(num):
    sqrt = math.sqrt(int(num))
    logbase = math.log(int(num))
    radians = math.sin(int(num))
    print("Square root : " + str(sqrt))
    print("Logarithm  : " + str(logbase))
    print(" Sine : " + str(radians))



num1 = input("Enter a number: ")

mathfunctions(num1)