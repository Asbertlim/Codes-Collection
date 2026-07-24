import random
print("---------------------------------------------------")
print("          WELCOME TO GUESS THE NUMBER                ")
print("---------------------------------------------------\n")

print("Game Mode:\n 1. Easy\n 2. Medium \n 3. Hard \n")

while True:
    mode = int(input("Enter game mode: "))
    if mode == 1:
        life = 10
        end = 50
    elif mode == 2:
        life = 8
        end = 100
    elif mode == 3:
        life = 8
        end = 500
    else:
        print("You selected a wrong game mode.")
        continue
        
    secret = random.randint(1,end)
    while life != 0:
        guess = int(input(f"Guess a number from 1 to {end}: "))
        
        if guess > secret:
            print("Too big!")
            life -= 1
        elif guess < secret:
            print('Too small!')
            life -= 1
        print(f"You now have {life} lives left.")
        
            
        if guess == secret:
            print("Congrats! You guessed the correct number!")
            print(f"You now have {life} lives left.")
            break
        
    if life == 0:
        print("You lost.")
        
    restart = input("Would you like to restart? (y/n): ").lower()
    if restart == "n":
        break
    elif restart == "y":
        continue

