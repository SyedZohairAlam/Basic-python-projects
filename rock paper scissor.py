import random

user = 0
computer = 0

options = ["rock", "paper", "scissor"]

while True:

    user_input = input("Type Rock/Paper/Scissor or q to quit\n")
    if user_input == "q":
        break
    if user_input in options:
        continue

    random_no = random.randint(0,2)

    computer_pick = options[random_no]
    print("computer picks", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissor":
        print("user won")
        user += 1
    if user_input == "paper" and computer_pick == "rock":
        print("user won")
        user += 1
    if user_input == "scissor" and computer_pick == "paper":
        print("user won")
        user += 1
    else:
        print("you lost!")    

print("user won",user, "times." )

print("computer wins", computer, "times.")


