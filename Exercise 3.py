import random

randNum = random.randint(1, 9)
guess = int(input("Guess a number between 1 and 9: "))
if guess == randNum:
    print("Well guessed!")
    exit()
while guess != randNum:
    guess = int(input("Guess again: "))
    if guess == randNum:
        print("Well guessed!")
        break
