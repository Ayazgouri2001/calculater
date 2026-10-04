num1 = int(input("Enter first number: "))
action = input("Enter operation (+, -, *, /): ")
num2 = int(input("Enter second number: "))

if action == "+":
    result = num1 + num2
    print("Result:", result)

elif action == "-":
    result = num1 - num2
    print("Result:", result)

elif action == "*":
    result = num1 * num2
    print("Result:", result)

elif action == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Cannot divide by zero.")

else:
    print("Something went wrong: Invalid operation")
