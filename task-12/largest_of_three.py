number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
number3 = float(input("Enter the third number: "))

if number1 == number2 == number3:
    print("All three numbers are equal.")

elif number1 == number2 and number1 > number3:
    print(f"{number1} is the largest. The first and second numbers are equal.")

elif number1 == number3 and number1 > number2:
    print(f"{number1} is the largest. The first and third numbers are equal.")

elif number2 == number3 and number2 > number1:
    print(f"{number2} is the largest. The second and third numbers are equal.")

elif number1 > number2 and number1 > number3:
    print(f"{number1} is the largest.")

elif number2 > number1 and number2 > number3:
    print(f"{number2} is the largest.")

else:
    print(f"{number3} is the largest.")