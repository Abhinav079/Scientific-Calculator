import math

def scientific_calculator():
    print("Scientific Calculator\n")
    print("Choose the operation you want to perform:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Sine")
    print("6. Cosine")
    print("7. Tangent")
    print("8. Square root")
    print("9. Logarithm")
    print("10. Exponent")
    choice = int(input("\nEnter your choice: "))
    if choice == 1:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 + num2
        print("The sum of {0} and {1} is {2}".format(num1, num2, result))
    elif choice == 2:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 - num2
        print("The difference between {0} and {1} is {2}".format(num1, num2, result))
    elif choice == 3:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 * num2
        print("The product of {0} and {1} is {2}".format(num1, num2, result))
    elif choice == 4:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 / num2
        print("The quotient of {0} and {1} is {2}".format(num1, num2, result))
    elif choice == 5:
        angle = float(input("Enter the angle in degrees: "))
        result = math.sin(math.radians(angle))
        print("The sine of {0} degrees is {1}".format(angle, result))
    elif choice == 6:
        angle = float(input("Enter the angle in degrees: "))
        result = math.cos(math.radians(angle))
        print("The cosine of {0} degrees is {1}".format(angle, result))
    elif choice == 7:
        angle = float(input("Enter the angle in degrees: "))
        result = math.tan(math.radians(angle))
        print("The tangent of {0} degrees is {1}".format(angle, result))
    elif choice == 8:
        num = float(input("Enter the number: "))
        result = math.sqrt(num)
        print("The square root of {0} is {1}".format(num, result))
    elif choice == 9:
        num = float(input("Enter the number: "))
        base = float(input("Enter the base: "))
        result = math.log(num, base)
        print("The logarithm of {0} with base {1} is {2}".format(num, base, result))
    elif choice == 10:
        num = float(input("Enter the number: "))
        exponent = float(input("Enter the exponent: "))
        result = math.pow(num, exponent)
        print("{0} raised to the power of {1} is {2}".format(num, exponent, result))
    else:
        print("Invalid choice!")
        
scientific_calculator()
