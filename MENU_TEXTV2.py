# [] list(multiple things)
# "" string (text)

choice = ""
while choice != "4":
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Option 4")
    choice = input("Choose a number (1-4): ")
    if choice == "1":
        input("you won the purple monkey")
        print("you won the purple monkey")
    elif choice == "2":
        input("you won the blue monkey")
        print("you won the blue monkey")
    elif choice == "3":
        input("you won the green monkey")
        print("you won the green monkey")
    elif choice == "4":
        input("you won the biggest and best monkey")
        print("you won the biggest and best monkey")
    else:        
        print("invalid choice, try again")
    
    