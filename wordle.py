import random
dic = ["world", "phone", "throw", "hello", "walls", "balls", "create", "books", "maths", "rocks", "stone", "names", "smart", "their", "thief", "seven", "basket", "coding", "teddy", "water", "paper", "pants", "basic", "debts", "words"]

print("------------------------------------------------")
print("             Welcome to Wordle                  ")
print("------------------------------------------------\n")

secret = dic[random.randint(0, len(dic)-1)]
life = 7
print("You have 7 lives.")

while life != 0:
    guess = input("Enter a five-letter word: ").lower()
    
    if len(guess) != 5:
        print("Input only 5 letter-word!")
        continue
    
    if guess == secret:
        print("Congrats! You won.")
        break
    
    life -= 1
    
    hint = ""
    for i in range(5):
        if guess[i] == secret[i]:
            hint += guess[i]
        elif guess[i] in secret:
            hint += "?"
        else:
            hint += "*"
    print(f"Hint: {hint}")
    print(f"You have {life} lives left.")
    
if life == 0:
    print("You lost.")
    print(f"The secret word is {secret}")
    
            
