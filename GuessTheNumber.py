import random

target = random.randrange(1,101)

while True:
    guess = input("Guess the number between 1 to 100 or Quit(Q): ").upper()
    print("---------------------------------------------------------------------------------------")
     
    if guess == "Q":
        break

    guess = int(guess)

    if guess == target:
        print("Success! Correct Guess!!", target)
        break

    elif guess > target:
        print("Your guess is too large, Take a smaller guess.")
        print("---------------------------------------------------------------------------------------")

    else:
        print("Your guess is too small, Take a larger guess.")
        print("---------------------------------------------------------------------------------------")
    
print("---------GAME OVER---------")
    