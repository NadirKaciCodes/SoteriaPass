
def see_password():
    import json
    from vault import load_passwords, save_passwords
    from master_password import check_password

    passwords = load_passwords()

    title = "soteria Pass"
    header = "See a password"
    quit = False 
    print(title)
    print(header)
    while not quit :
        print("1| See a password")
        print("2| Back to Main Menu")
        answer = input()
        if answer == "1" :
            print("Websites with saved passwords: ")

            i = 1
            for website in passwords :
                print(f"{i}| {website.capitalize()}")
                i+=1

            print("Please type out the url for the password")
            answer = input()

            if answer in passwords:
                    print(f"Accounts found for {answer}")
                    i=1
                    for account in passwords[answer]:
                        print(f"{i}| {account["username"]}")
                        i+=1
            else :
                print("No records found for this website/app")
                print("Press Enter to continue")
                input()

            print("Type username for account you want the password for :")
            answer_account = input()

            password_flag = False 
            attempt_counter = 0
            while not password_flag and attempt_counter < 3 :
                
                print("Please enter master password :")
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
                    quit = True

            if password_flag :
                print(f"password for {answer_account}:")
                for account in passwords[website]:
                    print(account["password"])
                    print("Press Enter to continue")#
                    input()
        if answer == "2" :
            break
