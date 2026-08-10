while True:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(" 1. Addition\n 2. Subtraction \n 3. Multiplication\n 4. Division\n 5. Modulo")
    
    choice = int(input("Select option: "))
    if choice == 1:
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif choice == 2:
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif choice == 3:
        result = num1 * num2
        print(f"{num1} x {num2} = {result}")
    elif choice == 4:
        result = num1 // num1
        print(f"{num1} ÷ {num2} = {result}")
    elif choice == 5:
        result = num1 % num1
        print(f"{num1} mod {num2} = {result}")
    else:
        print("Choice is invalid. Please try again.")
        continue
