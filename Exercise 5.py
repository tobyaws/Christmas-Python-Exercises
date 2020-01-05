import random


def rules(player, cpu):
    results = {
        ("Rock", "Paper"): False,
        ("Rock", "Scissors"): True,
        ("Paper", "Rock"): True,
        ("Paper", "Scissors"): False,
        ("Scissors", "Paper"): True,
        ("Scissors", "Rock"): False,
    }
    return results[(player, cpu)]


def play():
    p_choice = input("Rock, Paper, Scissors... ").capitalize()
    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
    cpu_choice = choices[random.randint(1, 3)]
    if p_choice == cpu_choice:
        return print("Draw!")
    if rules(p_choice, cpu_choice):
        return print("You Win!")
    else:
        return print("You Lose!")


def game():
    begin = input(
        "Would you like to play Rock, Paper, Scissors? (Yes or No) "
    ).capitalize()
    while begin != "Yes":
        if begin == "No":
            print("Game Over")
            exit()
        else:
            print("Please try again ")
            begin = input(
                "Would you like to play Rock, Paper, Scissors? (Yes or No)"
            ).capitalize()
    play()
    while True:
        begin = input("Play again? (Yes or No) ").capitalize()
        while begin != "Yes":
            if begin == "No":
                print("Game Over")
                exit()
            else:
                print("Please try again")
                begin = input("Play again? (Yes or No ").capitalize()
        play()


game()
