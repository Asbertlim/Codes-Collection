import time

print("             Vending Machine                     ")

print(" 1. Milo : $0.8 \n 2. Lemon Tea : $1.2 \n 3. Mineral Water : $0.2 \n 4. Wintermelon Tea : $0.8 \n 5. Orange Juice : $1.0 \n")

while True:
    choice = int(input("Select a drink: "))
    if choice == 1:
        drink = "Milo"
        price = 0.8
    elif choice == 2:
        drink = "Lemon Tea"
        price = 1.2
    elif choice == 3:
        drink = "Mineral Water"
        price = 0.5
    elif choice == 4:
        drink = "Wintermelon Tea"
        price = 0.8
    elif choice == 5:
        drink = "Orange Juice"
        price = 1.0
    else:
        print("Incorrect input. Please try again!")
        continue
    
    while True:
        cash = float(input("Insert cash: "))
        if cash < price:
            print("Insufficient \n")
            continue
        else:
            print("please wait..")
            time.sleep(3)
            print("chaa..ching..")
            print(f"Here's your {drink}")
            change = float(cash - price)
            print(f"Here's your change, {change} \n")
            break
