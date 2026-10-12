# Project : Pair Hunter game

def generate_puzzle():
  population = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
  numbers = random.sample(population, 6)
  numbers.sort()
  target = random.randint(5, 20)

  output = (numbers, target)
  return output
  
def find_all_pairs(numbers, target):
  left = 0
  right = len(numbers) - 1
  lst = []

  while left < right:
    total = numbers[left] + numbers[right]

    if total > target:
      right -= 1
    elif total < target:
      left += 1
    else:
      output = (numbers[left], numbers[right])
      lst.append(output)
      right -= 1
      left += 1
      while left < right and numbers[left] == numbers[left-1]:
        left += 1

      while left < right and numbers[right] == numbers[right+1]:
        right -= 1
  return lst
  
import random


def count_pairs():
  print("====== Pair Hunter ======")
  numbers, target = generate_puzzle()
  print("Numbers:", numbers)
  print("Target:", target)
  pairs = find_all_pairs(numbers, target)
  guess = int(input("How many unique pairs do you predict: "))

  if guess == len(pairs):
    print("Correct!")
    print("The pairs are:", pairs)
  else:
    print("Incorrect!")
    print(f"There are {len(pairs)} pairs and the pairs are", pairs)

  return "Thanks for playing."
  
