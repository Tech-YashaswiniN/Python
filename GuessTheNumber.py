import random

target = random.randrange(1,101)

while True:
    guess = input("Guess the number between 1 to 100 or Quit(Q): ").upper()
     
    if guess == "Q":
        break

    guess = int(guess)

    if guess == target:
        print("Success! Correct Guess!!", target)
        break

    elif guess > target:
        print("Your guess is too large, Take a smaller guess.")

    elif guess < target:
        print("Your guess is too small, Take a larger guess.")
    
print("------GAME OVER------")
    