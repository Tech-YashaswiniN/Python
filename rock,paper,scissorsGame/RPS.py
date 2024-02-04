import random

while True:
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, scissors?: ").lower()

    if player == computer:
        print("Player: ", player)
        print("Computer: ", computer)
        print("Tie!")

    elif player == "rock":
        if computer == "paper":
            print("Player: ", player)
            print("Computer: ", computer)
            print("You loose!")

        if computer == "scissors":
            print("Player: ", player)
            print("Computer: ", computer)
            print("You won!")

    elif player == "paper":
        if computer == "rock":
            print("Player: ", player)
            print("Computer: ", computer)
            print("You Won!")

        if computer == "scissors":
            print("Player: ", player)
            print("Computer: ", computer)
            print("You loose!")

    elif player == "scissors":
        if computer == "rock":
            print("Player: ", player)
            print("Computer: ", computer)
            print("You loose!")

        if computer == "paper":
            print("Playhher: ", player)
            print("Computer: ", computer)
            print("You won!")

    play_again = input("Play again? (yes/no) : ").lower()

    if play_again != "yes":
        break

print("Bye!")
