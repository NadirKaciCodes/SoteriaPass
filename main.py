from generate_password import main
from see_password import see_password
from add_edit_password import add_edit_password
title = "*** Welcome to Soteria Pass ***"
header = "What would you like to do today"

while True :
    print(title)
    print(header)
    print("1| Generate password")
    print("2| Check a Credential")
    print("3| Add/Edit Credential")
    print("4| Account settings")
    print("5| Quit")

    answer = input()

    if answer == "1" :
        main()
    if answer == "2" :
        see_password()
    if answer == "3" :
        add_edit_password()
    if answer == "5":
        break

