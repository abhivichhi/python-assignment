
def calcFactorial(num):
    if num < 2:
        return 1
    else:
        return num * calcFactorial(num - 1)

num1 = input("Enter a number: ")

resultFactorial = calcFactorial(int(num1))

print("Factorial of", num1, "is", resultFactorial)