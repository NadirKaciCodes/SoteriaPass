from generate_password import main
from see_password import see_password
title = "*** Welcome to Soteria Pass ***"
header = "What would you like to do today"

while True :
    print(title)
    print(header)
    print("1| Generate password")
    print("2| See a password")
    print("3| Change a password")
    print("4| Account settings")

    answer = input()

    if answer == "1" :
        main()
    if answer == "2" :
        see_password()
