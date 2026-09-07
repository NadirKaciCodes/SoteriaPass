import secrets
import json

def generate_password(password, num_chars='8'):
    password = []

    Upper_Case = ["A", "B", "C", "D", "E", "F"]
    Lower_Case = ["a", "b", "c", "d", "e", "f"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]

    for i in range(0, 10) :
        char = secrets.choice(Upper_Case + Lower_Case + numbers + symbols )
        password.append(char)

    password = ''.join(password)
    print(''.join(password))
    return password

import json

title = "*** SoteriaPass Password Generator *** "


#question = "How many characters would you like to include in your password ?"
key_question = "Provide account username or key for password"
num_chars = 8

# Store Key for the password
account_name = ""

existing_account = None

create_password = False

#overwrite flag
overwrite = False

# Load dictionairy from passwrod vault as dictionary
with open("password_vault.txt", "r") as f:
    passwords = json.load(f)
website = ""
print("Website title or url :")
website = input().capitalize()

print(key_question)
account_name = input()

if website in passwords :
    for account in passwords[website] :
        if account["username"] == account_name :
            print("Password already found for account, would you like to overwrite it")
            print("1| Overwrite")
            print("2| Cancel")
            answer = input()
            if answer == "1" :
                password = generate_password(num_chars)
                overwrite = True
                existing_account = account
                break
            else :
                create_password = False
                break
        else :
            password = generate_password(num_chars)


#print (title,"\n\n", question)
#num_chars = int(input())
#password = generate_password(num_chars)



if overwrite:
    existing_account["password"] = password
elif not create_password :
    print("No changes")
else:    
    if website in passwords :
        passwords[website].append({
            "username": account_name,
            "password": password
            }) 
    else :
        passwords[website] = []
        passwords[website].append({
            "username": account_name,
            "password": password 
        })

with open ("password_vault.txt", "w") as f:
    json.dump(passwords, f, indent=4)

