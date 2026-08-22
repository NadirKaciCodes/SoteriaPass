import secrets

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