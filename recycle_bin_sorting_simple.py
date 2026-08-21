import time

print("    This is an Automated Trash Sorting Machine   \n")

plastics = ["plastics", "plastic", "plastic bag", "plastic bottle", "bottle", "milk jug"]

metals = ["can", "cans", "aluminium", "iron", "tin", "thermos", "metal"]

papers = ["newspaper", "magazine", "paper", "brochure", "poster", "pamphlete", "old paper"]

while True:
    trash = input("Insert your trash: ").lower()
    if trash in plastics:
        category = "Plastics"
        print("Sorting...")
        time.sleep(1)
        print(f"Category = {category}\nRecyclable\n")
    elif trash in metals:
        category = "Metals"
        print("Sorting...")
        time.sleep(1)
        print(f"Category = {category}\nRecyclable\n")
    elif trash in papers:
        category = "Papers"
        print("Sorting...")
        time.sleep(1)
        print(f"Category = {category}\nRecyclable\n")
    else:
        print("Sorting...")
        time.sleep(1)
        print("Unrecyclable\n")
