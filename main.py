import random

while True:
    user_action = input("Enter a choice (R for rock, P for paper,  S for scissors): ").upper()
    if user_action == "R":
        user_action = "rock"
    elif user_action == "P":
        user_action = "paper"
    elif user_action == "S":
        user_action = "scissors"

    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    

    if user_action == computer_action:
        print(f"\nPlayer({user_action}), Computer({computer_action}).\n")
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        print(f"\nPlayer({user_action}), Computer({computer_action}).\n")
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
        break
    elif user_action == "paper":
        print(f"\nPlayer({user_action}), Computer({computer_action}).\n")
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
        break
    elif user_action == "scissors":
        print(f"\nPlayer({user_action}), Computer({computer_action}).\n")
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
        break
    else:
        print("Wrong Input")
