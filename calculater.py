num1 = float(input("Enter first number: "))
operator = input("Enter operator (+,-,*,/,^,%,#,$ ): ")
num2 = float(input("Enter secound number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "/":
    result = num1 / num2
elif operator == "^":
    result = num1 ^ num2
elif operator == "%":
    result = num1 % num2
else :
    print("Invalid Operator")

print("Result: ", result)

