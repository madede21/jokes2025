# Code Requirements
# Input: Use any valid input source such as a keyboard, mouse, microphone, data stream, or file.
# Output: Must depend on the input provided.
# List Usage:
# Must justify why a list is better than alternatives.
# Examples include picking items, random selections, or using list methods like append.
# Function Requirements:
# Must have a parameter.
# Include sequencing (multiple lines of code).
# Utilize selection (e.g., if/else statements).
# Use iteration (e.g., loops like for or while).
# Take different paths based on parameter values.
all_entries = []

def joke_game():
    jokes = {
        "robbers": ["Robbers ", "Calder police – I've been robbed!"],
        "tanks": ["Tanks ", "You are welcome!"],
        "pencils": ["Pencils ", "Nevermind, it's pointless!"]
    }

    answer = input("Do you want to hear a joke? ")

    if answer == "no":
        print("Okay suit yourself!")
        return None, None 

    while answer == "yes":
        choice_question = input("Choose: robbers, tanks, or pencils: ")

        if choice_question in jokes:
            input("Knock Knock ")
            input(jokes[choice_question][0])
            print(jokes[choice_question][1])
        else:
            print("That’s not an option.")

        answer = input("Do you want to hear another joke or are you finished? ")

    if answer == "finished":
        rate_game = int(input("Rate the game 1–10: "))
        print(str(rate_game * 10) + "% satisfaction rate")

        friend_question = input("Would you recommend this game to a friend? ")
        if friend_question in ("yes", "no"):
            print("Thanks, we appreciate it.")
        else:
            print("Sorry you did not enjoy it.")

        return rate_game, friend_question

    return None, None



rate_game, friend_question = joke_game()


if rate_game is not None and friend_question is not None:
    all_entries.append((rate_game, friend_question))

print("\n--- List of all entries so far ---")
for entry in all_entries:
    print(entry)
    print("-------------------------------\n")
