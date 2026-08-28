def traffic_analyzer(traffic):
    print("==========================================")
    print("          Smart Traffic Analyzer")
    print("==========================================\n")

    print("1. Highest Traffic Minute\n2. Average Traffic\n3. Biggest Traffic Increase\n4. Detect Congestion\n5. Traffic Alert\n6. Exit")

    while True:
        opt = int(input("Select a feature: "))

        if opt == 1:
            highest = 0
            for i, value in enumerate(traffic):
                if value > highest:
                    highest = value
                    highest_min = i
                
            print(f"Highest Traffic: {highest}")
            print(f"Minute: {highest_min}")
        
        elif opt == 2:
            avg = sum(traffic) / len(traffic)
            print(f"Average traffic: {avg}")
        
        elif opt == 3:
            biggest_inc = 0
            for cars in range(len(traffic)-1):
                if traffic[cars + 1] - traffic[cars] > biggest_inc:
                    biggest_inc = traffic[cars + 1] - traffic[cars]
                    min1 = cars
                    min2 = cars+1
            print(f"Biggest increase: {biggest_inc}")
            print(f"From minute {min1} to minute {min2}")
        
        elif opt == 4:
            longest = 0
            current = 0

            for cars in traffic:
                if cars >= 30:
                    current += 1
                else:
                    current = 0
                
                if current > longest:
                    longest = current
            print(f"Longest congestion: {longest} minutes")
        
        elif opt == 5:
            for cars in range(len(traffic)-1):
                if traffic[cars+1] - traffic[cars] >= 10:
                    sudden_min = cars+1
                    inc = traffic[cars+1] - traffic[cars]

                    print(f"Traffic alert!\nSudden increase detected at minute {sudden_min}\nIncrease in {inc} vehicles\n")
                else:
                    print("No sudden increase detected.\n")
        
        elif opt == 6:
            print("Thank you for visiting.")
            break
        
        else:
            print("Please select correct option.\n")
            continue
