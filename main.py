#Adventure Game
print("Welcome to my Adventure! Make the right decisions and you might survive.... Good luck!\n")

print("Let's set the scene! You're on a cruise ship and it just crashed near an uninhabited island.\nPeople are rushing to the life boats to get to shore. You have 3 choices.")

while True:
    choice = input("\nChoice: 1) Stay on the boat and wait to be saved, 2) Pack your bags and rush to a life boat, 3) Go straight for the life boat.\nType 1, 2, or 3 for your answer.")
    
    if choice == "1":
        print("Oh no! Crashing caused a crack in the boat and the boat sank with you inside! Sorry, you lose!")
        quit()
    elif choice == "2":
        print("Good choice! You made it to the life boat and are on your way to the island!")
        print("You see a shark! You can paddle hard and try to get to the island before the shark gets to you or stay very still and hope the shark swims by.")
        
        while True:
            choice = input("Type 1 to paddle away or 2 to stay there")
            if choice == "1":
                print("Oh no! You paddling got the sharks attention and it ate you! Sorry, you lose!")
                quit()
            elif choice == "2":
                print("Good choice! Because you stayed perfectly still the shark swam right past you and you were able to get to shore safely!")
                print("Good thing you packed your bags, you packed enough food to last you until you were saved.\nCongratulations, you win!")
                quit()
            else:
                print("Not a valid answer. Try Again!")
                continue
    
    elif choice == "3":
        print("Good choice! You made it to the life boat and are on your way to the island!")
        print("You see a shark! You can paddle hard and try to get to the island before the shark gets to you or stay very still and hope the shark swims by.")
        
        while True:
            choice = input("Type 1 to paddle away or 2 to stay there")
            if choice == "1":
                print("Oh no! You paddling got the sharks attention and it ate you! Sorry, you lose!")
                quit()
            elif choice == "2":
                print("Good choice! Because you stayed perfectly still the shark swam right past you and you were able to get to shore safely!")
                print("Unfortunately, you didn't pack anything with you so you starved. Sorry, you lose!")
                quit()
            else:
                print("Not a valid answer. Try Again!")
                continue
        
    else:
        print("Not a valid answer. Try Again!")
        continue
