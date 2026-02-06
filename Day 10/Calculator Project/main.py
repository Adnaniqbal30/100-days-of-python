import art
print(art.logo)
def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

calculator={
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculators():
    num1 = float(input("Enter the first number: "))
    should_accumulate = True
    while should_accumulate:
        for symbol in calculator:
            print(symbol)
        operation_symbol = input("Enter the operation you want to perform: ")
        num2 = float(input("Enter the second number: "))
        answer = calculator[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice=input("Type 'y' to continue calculating with 0.0, or type 'n' to start a new calculation: ")

        if choice=="yes":
            num1=answer
        elif choice=="no":
            should_accumulate=False
            print("\n"*25)
            calculators()
calculators()








