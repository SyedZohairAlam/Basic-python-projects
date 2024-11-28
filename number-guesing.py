import random

a = input("Type a number \n")

if a.isdigit():
    a = int(a)
if a <= 0:    
    print("Please enter a number that is greater than 0 next time")
    quit()
else:
    print("Please enter a number")    

random_no = random.randint(0, a)
guesses = 0

while True:
    guesses += 1
    user = input("Guess the number \n")
    if user.isdigit():
        user = int(user)
        print("Guess the number \n")
    else:
        print("Please enter a number next time!")
        continue
    if user == random_no:
        print("You got it , Correct!")
        break
    if user >= random_no:
        print("You were above the number")
    else:
        print("You were below the number")

print("You got it in", guesses, "guesses")        








