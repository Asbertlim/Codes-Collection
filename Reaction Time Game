import time
import random

print("================================================\n")
print("             Reaction Time Tester           \n")
print("================================================\n")

while True:
    choice = input("Are you ready? (y/n): ").lower()
    
    if choice == "y":
        start = time.time()
        i = input("Press Enter: ")
        end = time.time()
        result = round(end-start, 3)
        print(result)
        best = result
        
        if result < best:
            best = result
        
        print(f"Your current best is {best}s")
            
        
    else:
        continue
