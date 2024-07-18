#Encription of Password - 
from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:  #wb stands for write in bites
        key_file.write(key)

write_key()
'''

def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key

key = load_key() 
fer = Fernet(key) 

print("To ADD new password, Type add")
print("To VIEW password, Type pass")
print("Press Q to Quit")

def view():
    with open ("password.txt","r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user,passw = data.split("|")
            print("User:", user ,"| Password:",fer.decrypt(passw.encode()).decode())

def add():
    name = input("Account Name: ")
    password = input("Password: ")

    with open("password.txt","a") as f: #with will close file automatically
    # a - here represents add mode
    # w - will cleare and rewrite 
    # r - read only mode
        f.write(name + '|' + fer.encrypt(password.encode()).decode() + "\n")

while True:
    mode = input(("VIEW / ADD / Q : ").lower())
    if (mode =="q"):
        print("Thank you!!!!")
        break
    
    if (mode == "view"):
        view()
    elif(mode == "add"):
        add()
    else:
        print("Invalid")
        continue