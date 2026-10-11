def find_pair(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
      if numbers[left] + numbers[right] < target:
        left += 1
      elif numbers[left] + numbers[right] > target:
        right -= 1
      else:
        return (numbers[left], numbers[right])
        break
    return None

print(find_pair([1, 3, 4, 6, 8, 11], 10))
# Expected: (4, 6)

print(find_pair([1, 2, 5, 9], 7))
# Expected: (2, 5)

print(find_pair([2, 4, 6], 20))
# Expected: None
print(find_pair([1, 2, 3], 100))
# Expected: None
