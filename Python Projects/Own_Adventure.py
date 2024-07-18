name = input("Type your name: ")
print("Welcome", name , "to this Adventure!!")

answer = input("""You are on dirt Road, 
               It has come to an End, Now you have 2 option either to go Left or Right. 
               Choice is yours:  """)
if (answer == "left"):
    answer = input("You came to a river, You type SWIM to swim, You type WALK to walk: ")

    if (answer == "swim"):
        print("You SWIM accros and eaten by Alligator.")

    elif(answer == "walk"):
        print("You went so far, and now you losse consciousness. And lost.")
    else:
        print("Not a valid option, You Losse.")

elif (answer == "right"):
    answer = input("""You cross a bridge, but it is woobly, 
                   Now its your choice to WALK or RETURN.(WALK/RETURN)?: """)
    if (answer == "WALK"):
        print("You WALK accros and Fallen Down.")

    elif(answer == "Return"):
        print("You have to search for new route.")
    else:
        print("Not a valid option, You Losse.")

else:
    print("Not a valid option, You Losse.")