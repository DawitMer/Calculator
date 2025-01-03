def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


# operation["+"] = add
# operation["-"] = subtract
# operation["*"] = multiply
# operation["/"] = divide

operation = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

def operation_print():
    print("+")
    print("-")
    print("*")
    print("/")

number1 = 0
choice = ""
while True:
    if choice != "y":
        number1 = float(input("What's the first number?: "))

    operation_print()

    type_operation = input("operation: ")
    number2 = float(input("What's the second number?: "))
    result = operation[type_operation](number1, number2)

    print(f"{number1} {type_operation} {number2} = {result}")
    choice = input(f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation: ").lower()

    if choice == "y":
        number1 = result








