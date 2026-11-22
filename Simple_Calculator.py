#Simple_Calculator
count = int(input("Enter the Number of Operations:"))
i = 0

while i < count:
    
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))

    opr = input("Enter any operator('+','-','*','/'): ")

    match(opr):
        case '+':
            print(f"Sum of {num1} and {num2} is {num1 + num2}")
        case '-':
            print(f"Difference of {num1} and {num2} is {num1 - num2}")
        case '*':
            print(f"Product of {num1} and {num2} is {num1 * num2}")
        case '/':
            if num2 != 0:
                print(f"Division of {num1} and {num2} is {num1 / num2}")
            else:
                print("Cannot divide by zero!")
        case _:
            print("Invalid Input")
    
    i += 1
    print()
   
