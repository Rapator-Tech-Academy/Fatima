print("Welcome to my first basic calculator!")

num1 = input ("Please input your first numbe: ")
operator = input("Select your operator type (Examle: +, -, *, /): ")
num2 = input ("Please input your second numbe: ")

num1 = int(num1)
num2 = int(num2)


if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2

print("Your result is: " + str(result))