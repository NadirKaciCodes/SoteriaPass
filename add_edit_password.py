from vault import load_passwords, save_passwords
from master_password import check_password



def add_credential():
    passwords = load_passwords()

    print("Enter website or url name :")
    website = input()
    if website in passwords :
        print("Enter ID/Username for credential")
        user_account = input()
        for account in passwords[website] :
            
            if account["username"] == user_account :
                            print("Credential with this ID already exists")
                            print("1| Edit credential")
                            print("2| Go back ")
                            print("3| Menu ")
                            answer = input()
                            if answer == "1" :
                                edit_credential()
                                return
                            if answer == "2":
                                break
                            if answer == "3":
                                break
        else :
            password_match = False
            while not password_match:
                print("Insert password")
                password1 = input()
                print("Confirm password")
                password2 = input()

            
                if password1 == password2 :
                    passwords[website].append(
                    {"username": user_account,
                    "password": password1
                    })
                    save_passwords(passwords)
                    password_match = True
                    break
                else :
                    print("Passwords do not match, Please try again")
    else :
        print("Enter ID/Username for credential")
        user_account = input()
        password_match = False
        while not password_match:
            print("Insert password")
            password1 = input()
            print("Confirm password")
            password2 = input()

        
            if password1 == password2 :
                passwords[website] = []
                passwords[website].append({
                "username": user_account,
                "password": password2 
                })
                save_passwords(passwords)
                password_match = True
                break
            else :
                print("Passwords do not match, Please try again")

def edit_credential():
    while True:
        passwords = load_passwords()
        print("Websites with saved passwords: ")

        i = 1
        for website in passwords :
            print(f"{i}| {website.capitalize()}")
            i+=1        
    
        print("Enter website or url name :")
        website = input()

        if website in passwords :
            print(f"accounts found for {website}")
            i=1
            for account in passwords[website]:
                print(f"{i}| {account["username"]}")
                i+=1

            print("Enter ID/Username for Credential")
            user_account = input()

            for account in passwords[website]:
                if user_account == account["username"]:
                    print("Credential found, Would you like to edit the passwords")
                    print("1| Yes")
                    print("2| No")

                    answer = input()
                    if answer == "1" :
                        print("For security reasons we require your master password :")
                        password_flag = False 
                        attempt_counter = 0
                        while not password_flag and attempt_counter < 3 :

                            user_pass_attempt = input()
                            password_flag = check_password(user_pass_attempt)
                            attempt_counter += 1
                            print(attempt_counter)
                            if password_flag :
                                break
                            elif not password_flag and 1 <= attempt_counter <= 2 :
                                print("Incorrect password,Try again")
                                print(f"{3 - attempt_counter} attempts left")
            
                            else :
                                print("Too many attempts, access denied")
                        password_match = False
                        if password_flag :
                            while not password_match:
                                print("Insert password")
                                password1 = input()
                                print("Confirm password")
                                password2 = input()

                            
                                if password1 == password2 :
                                    account["password"] = password2
                                    save_passwords(passwords)
                                    password_match = True
                                    return
                                else :
                                    print("Passwords do not match, Please try again")                    
                        else :
                            break
        
    
def delete_credential():
    passwords = load_passwords()
    print("***Soteria Pass***")
    print("***Delete a credential***")
    print("Websites with saved passwords: ")
    
    i = 1
    for website in passwords :
        print(f"{i}| {website.capitalize()}")
        i+=1

    print("Please type out the url for the password")
    website = input()

    if website in passwords:
            print(f"Accounts found for {website}")
            i=1
            for account in passwords[website]:
                print(f"{i}| {account["username"]}")
                i+=1

            print("Enter ID/Username for Credential")
            user_account = input()

            for account in passwords[website]:
                if user_account == account["username"]:
                    print("Credential found, are you sure you want to delete it")
                    print("1| Yes")
                    print("2| No")

                    answer = input()
                    if answer == "1" :
                        print("For security reasons we require your master password :")
                        password_flag = False 
                        attempt_counter = 0
                        while not password_flag and attempt_counter < 3 :

                            user_pass_attempt = input()
                            password_flag = check_password(user_pass_attempt)
                            attempt_counter += 1
                            print(attempt_counter)
                            if password_flag :
                                break
                            elif not password_flag and 1 <= attempt_counter <= 2 :
                                print("Incorrect password,Try again")
                                print(f"{3 - attempt_counter} attempts left")
            
                            else :
                                print("Too many attempts, access denied")
                                break
                        if password_flag :
                            passwords[website].remove(account)
                            save_passwords(passwords)
                            print("Credential Deleted")
                            print("Press enter to continue")
                            input()
                            return
                            


    else :
        print("No records found for this website/app")
        print("Press Enter to continue")
        input()

def add_edit_password():
    while True :
        print("***Soteria Pass***")
        print("What would you like to do")
        print("1| Add a credential")
        print("2| Edit a credential")
        print("3| Delete a credential")
        print("4| Back to Main Menu")
        answer = input()

        if answer == "1":
            # Adding a credential function
            add_credential()
        elif answer == "2" :
            # Editing a credential functiion
            edit_credential()
            placeholder = ""
        elif answer == "3" :
            #Deleting a credential code
            delete_credential()
        elif answer == "4":
            break



