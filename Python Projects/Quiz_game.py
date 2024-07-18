# Asking User various Question, And adding point for that
import sys
print("This is world of Quiz")
print()

score = 0

playing = input("Do you want to play? :  ")
if (playing == "yes" or "YES"):
    print("Welcome to the world of Quiz.")
else:
    print("You Quit before it Starts.")
    sys.exit()
print()

#Ques1:
answer = input("What does CPU Stands for?: ")
if(answer == "Central Processing Unit"):
    print("Correct!")
    score += 2
elif(answer == "central processing unit"):
    print("Correct!")
    score += 2
elif(answer == "CENTRAL PROCESSING UNIT"):
    print("Correct!")
    score += 2
else:
    print("Better Luck next time!")
    print("Your Total Score is :", score )
    sys.exit()
print()

#Ques2:
answer = input("What does GPU Stands for?: ")
if(answer == "Graphic Processing Unit" or answer == "GRAPHIC PROCESSING UNIT" or answer == "graphic processing unit"):
    print("Correct!")
    score += 2
else:
    print("Better Luck next time!")
    print("Your Total Score is :", score )
    sys.exit()
print()

#Ques3:
answer = input("What does EU Stands for?: ")
if(answer == "European Union" or answer == "EUROPEAN UNION" or answer == "european union"):
    print("Correct!")
    score += 2
else:
    print("Better Luck next time!")
    print("Your Total Score is :", score )
    sys.exit()
print()

#Ques4:
answer = input("What does AI Stands for?: ")
if(answer == "Artificial Intelligence" or answer == "ARTIFICIAL INTELLIGENCE" or answer == "artificial intelligence"):
    print("Correct!")
    score += 2
else:
    print("Better Luck next time!")
    print("Your Total Score is :", score )
    sys.exit()
print()

answer = input("What does AU Stands for?: ")
if(answer == "Arthmetic Unit" or answer == "ARITHMETIC UNIT" or answer == "arithmetic unit"):
    print("Correct!")
    score += 2
else:
    print("Better Luck next time!")
    print("Your Total Score is :", score )
    sys.exit()
print()

print("Your Total Score is :", score )