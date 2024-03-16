
print("Operations:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter choice (1/2/3/4): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


if choice == "1":
    print(num1 + num2)

elif choice == "2":
    print(num1 - num2)
    
elif choice == "3":
    print(num1 * num2)
    
elif choice == "4":
    print(num1 / num2)

else:
    print("Invalid input. Please enter a valid choice (1/2/3/4).")
