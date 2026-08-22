from generate_password import generate_password
import json

title = "*** SoteriaPass Password Generator *** "


question = "How many characters would you like to include in your password ?"
key_question = "Provide account username or key for password"
num_chars = 8

# Store Key for the password
password_key = ""

# Load dictionairy from passwrod vault as dictionary
with open("password_vault.txt", "r") as f:
    passwords = json.load(f)
website = ""
print("Website title or url :")
website = input().capitalize()


while True :
    print(key_question)
    password_key = input()
    if password_key in passwords.keys() :
        print("You already have a password for this account")
        print("1| Overwrite Password")
        print("2| Go back")
        answer = input()

        if answer == "1":
            break
    else :
        break



#print (title,"\n\n", question)
#num_chars = int(input())
password = generate_password(num_chars)




passwords[website] = {
    "username": password_key,
    "password": password
    } 

with open ("password_vault.txt", "w") as f:
    json.dump(passwords, f, indent=4)


