def library(b):
    borrow = []
    
    print("---------------------------------------------")
    print("         Welcome To Library Manager      ")
    print("---------------------------------------------\n")
    
    print("Features:")
    print("1. Show All Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Count Available Books")
    print("5. Exit")

    while True:    
        opt = int(input("Enter option: "))
        
        if opt == 1:
            print(b)
            continue
        elif opt == 2:
            brw = input("Enter the name of the book: ")
            if brw in b:
                print("Book successfully borrowed!")
                b.remove(brw)
                borrow.append(brw)
                continue
            else:
                print("Sorry, this book is already borrowed.")
                continue
        elif opt == 3:
            rtn = input("Enter the name of the book: ")
            if rtn not in b:
                print("Book successfully returned!")
                b.append(rtn)
                continue
            else:
                print("This book is already in the library.")
                continue
        elif opt == 4:
            print(f"There are {len(b)} available books in the library.")
            continue
        elif opt == 5:
            return "Thank you for visiting."
            break
        else:
            print("Sorry, wrong input")
            continue
