


# make this performance task ready for submission
# To give the user a fun experience hearing knock knock jokes



# Knock-knock jokes stored as a list






all_jokes=[]

def joke_game():
    jokes = {
        "robbers": ["Robbers ", "Calder police – I've been robbed!"],
        "tanks": ["Tanks ", "You are welcome!"],
        "pencils": ["Pencils ", "Nevermind, it's pointless!"]
    }

    answer = input("Do you want to hear a joke? ")

    if answer == "no":
        print("Okay suit yourself!")
        return

    while answer == "yes":
        choice = input("Choose: robbers, tanks, or pencils: ")

        if choice in jokes:
            input("Knock Knock ")
            input(jokes[choice][0])
            print(jokes[choice][1])
        else:
            print("That’s not an option.")

        answer = input("Do you want to hear another joke or are you finished? ")

    if answer == "finished":
        rate = int(input("Rate the game 1–10: "))
        print(str(rate * 10) + "% satisfaction rate")

        friend = input("Would you recommend this game to a friend? ")
        if friend in ("yes", "no"):
            print("Thanks, we appreciate it.")
        else:
            print("Sorry you did not enjoy it.")



joke_game()
all_jokes.append((rate))
print("\n--- List of all entries ---")
for entry in all_jokes:
    print(entry)
print("-------------------------------\n")