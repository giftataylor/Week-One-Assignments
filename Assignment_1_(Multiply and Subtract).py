# Part 2: Multiplication and Division
print("Part 2: Multiplication and Division")

# Get user input for Part 2
num1_part2 = float(input("Enter the first number for multiplication and division: "))
num2_part2 = float(input("Enter the second number for multiplication and division: "))

# Multiplication
product_result = num1_part2 * num2_part2

# Division
if num2_part2 != 0:
    division_result = num1_part2 / num2_part2
    print("The division of the two numbers is:", division_result)
else:
    print("Division by zero is not allowed.")

# Display the result
print("The product of the two numbers is:", product_result)
