print("Welcome to my cricket quiz competition!")


playing = input("Do you want to play \n")

if playing != "yes":
    quit()

print("Okay, Let's play :)")     
score = 0

answer = input("Who is the goat of Cricket? \n")
if answer == "Babar Azam":
    print("Correct")
    score += 1
else:
    print("Incorrect")


answer = input("Which team is the best in the world? \n")
if answer == "Pakistan":
    print("Correct")
    score += 1 
else:
    print("Incorrect")    

answer = input("Which team has the best bonding within the players among all of the world? \n")
if answer == "Pakistan":
    print("Correct")
    score += 1
else:
    print("Incorrect")    

answer = input("Who hit the longest six in the world? \n")
if answer == "Shahid Afridi":
    print("Correct")
    score += 1
else:
    print("Incorrect")        

# print("You got"   + str(score)  +  "questions correct!")
    
print("You got"  +  str((score/4)*100)  +  "%")    
