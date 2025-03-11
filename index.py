#Step 1: Take user input 
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the Operation(+,-,*,/): ")

#Step 2: Perform the operation
if operator == "+":
    result = num1 + num2
elif operator == "-":       
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 == 0:
      result = "Error! Division by zero is not allowed."
    else:
      result = num1 / num2

else:
    result = "Invalid operator!"

#Step 3: Display the result
print(f"{num1} {operator} {num2} = {result}")