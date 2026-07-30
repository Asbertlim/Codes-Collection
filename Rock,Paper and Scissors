import random
print("         Welcome To Rock, Paper, Scissors.       \n")

rps = ["r", "p", "s"]
streak = 0

while True:
    bot_move = rps[random.randint(0,2)]
    user_move = input("Enter a move (r/p/s): ").lower()
    
    if user_move == "r":
        print("You: Rock")
        if bot_move == "r":
            print("Bot: Rock")
            print("Tied")
        elif bot_move == "p":
            print("Bot: Paper")
            print("You lost.")
            streak = 0
        else:
            print("Bot: Scissors")
            print("You won.")
            streak += 1
        print(f"You have {streak} streaks currently.")
    elif user_move == "p":
        print("You: Paper")
        if bot_move == "p":
            print("Bot: Paper")
            print("Tied")
        elif bot_move == "s":
            print("Bot: Scissors")
            print("You lost.")
            streak = 0
        else:
            print("Bot: Rock")
            print("You won.")
            streak += 1
        print(f"You have {streak} streaks currently.")
    elif user_move == "s":
        print("You: Scissors")
        if bot_move == "s":
            print("Bot: Scissors")
            print("Tied")
        elif bot_move == "r":
            print("Bot: Rock")
            print("You lost.")
            streak = 0
        else:
            print("Bot: Paper")
            print("You won.")
            streak += 1
        print(f"You have {streak} streaks currently.")
    else:
        print("Wrong move, try again.")
        continue
