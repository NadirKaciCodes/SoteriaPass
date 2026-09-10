import json

def load_passwords():
    # Load dictionairy from password vault as dictionary
    with open("password_vault.txt", "r") as f:
        passwords = json.load(f)
        return passwords 


def save_passwords(passwords):
    with open ("password_vault.txt", "w") as f:
        json.dump(passwords, f, indent=4)