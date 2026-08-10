def analyzer(nums):
    print("=============================================\n")
    print("             Number Analyzer                 \n")
    print("=============================================\n")
    
    while True:
        print("Features: ")
        print("1. Show Frequency")
        print("2. Find Most Frequent Number ")
        print("3. Find Largest Pair Product")
        print("4. Show Statistics")
        print("5. Exit")
        
        choice = int(input("Select a feature: "))
        
        if choice == 1:
            frequency = {}
            for num in nums:
                if num not in frequency:
                    frequency[num] = 1
                else:
                    frequency[num] += 1
            print(frequency)
        
        elif choice == 2:
            frequency = {}
            for num in nums:
                if num not in frequency:
                    frequency[num] = 1
                else:
                    frequency[num] += 1
            best_count = 0
            best_num = None
            for num in nums:
                if (frequency[num] > best_count or (frequency[num] == best_count and (best_num is None or num < best_num))):
                    
                    best_count = frequency[num]
                    best_num = num
                
            print(f"Most frequent number: {best_num}")
            print(f"Frequency: {best_count}")

            
        elif choice == 3:
            nums.sort()
            product = nums[-1]*nums[-2]
            
            print(f"The largest product: {product}")
        
        elif choice == 4:
            total = sum(nums)
            mx = max(nums)
            mini = min(nums)
            avg = total / len(nums)
            
            print(f"Total number: {len(nums)}")
            print(f"Sum: {total}")
            print(f"Max num: {mx}")
            print(f"Min num: {mini}")
            print(f"Average: {avg}")
            
        elif choice == 5:
            return "Thank you for visiting!"

        
        else:
            print("Incorrect choice, please try again")
            continue

