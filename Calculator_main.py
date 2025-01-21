import art

print(art.logo)

def add(n1, n2):
    return n1 + n2

# TODO: Write out the other 3 functions - subtract, multiply and divide.


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2

# TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# TODO: Use the dictionary operations to perform the calculations. Multiply 4*8 using the dictionary

# print(operations["*"](4,8))


num1 = 0
continuous = True

while continuous:
    if num1 == 0:
        num1 = float(input("Please type the first number"))

    operator = input("Please the mathematical operator:")
    for symbol in operations:
        print(symbol)

    num2 = float(input("Please input the second number"))

    result = operations[operator](num1, num2)
    print(f"{num1} {operator} {num2} = {result}")

    con = input(f"type 'y' to continue calculating with {result}, or type 'n' to start a new calculation.").upper()
    num1 = result

    if con == "N":
        num1 = 0
        print("\n" * 20)
        print(art.logo)



