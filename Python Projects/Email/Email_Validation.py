#Using String Function

Email = input("Enter your Email: ")

if len(Email)>= 6:
    if Email[0].isalpha():
        if ("@" in Email) and (Email.count("@") == 1):
            if (Email[-4] ==".") or (Email[-3] == "."):
                print("Your Email is Valid and Email is:",Email)

        else:
            print("Wrong Email 3")
    else:
        print("Wrong Email 2")
else:
    print("Wrong Email 1 ")