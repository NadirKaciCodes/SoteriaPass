master_password = "supersecretword123"

def check_password(user_password):
    check_pass = False
    if user_password == master_password :
        check_pass = True
    else :
        check_pass = False
    return check_pass
