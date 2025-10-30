//VACUUM CLEANER
def vacuum_cleaner():
    print("*** WELCOME TO VACUUM CLEANER WORLD ***\n")
    print("Enter 0 for Clean and 1 for Dirty!\n")
    
    cost = 0
    loc = input("Enter The Vacuum location (A/B): ").upper()
    a = int(input("Enter Room A status: "))
    b = int(input("Enter Room B status: "))

    initial_dirty = (1 if a == 1 else 0) + (1 if b == 1 else 0)
    
    print(f"Initial Status: {{'A': {a}, 'B': {b}}}")
    print("\nSUCKING THE DIRT...")
    print("PLEASE WAIT...\n")

    if loc == "A":
        if a == 1:
            print("Cleaning A...")
            a = 0
            cost += 1
            print("CLEANED A\n")
        print("Moving to B...")
        print("MOVED TO B!\n")
        if b == 1:
            print("Cleaning B...")
            b = 0
            cost += 1
            print("CLEANED B!\n")
    elif loc == "B":
        if b == 1:
            print("Cleaning B...")
            b = 0
            cost += 1
            print("CLEANED B!\n")
        print("Moving to A...")
        print("MOVED TO A\n")
        if a == 1:
            print("Cleaning A...")
            a = 0
            cost += 1
            print("CLEANED A\n")

    final_dirty = (1 if a == 1 else 0) + (1 if b == 1 else 0)
    cleaned_rooms = initial_dirty - final_dirty
    performance_score = cleaned_rooms - cost
    
    print("Final Status: {'A': " + str(a) + ", 'B': " + str(b) + "}")
    print("Rooms Cleaned:", cleaned_rooms)
    print("\nTotal Cleaning Cost:", cost)
    print("\nPerformance Score:", performance_score)
    print("\nCOMPLETED THE TASK.")
    print("*** THANK YOU ***\n")

vacuum_cleaner()

