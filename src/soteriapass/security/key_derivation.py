from argon2.low_level import hash_secret_raw, Type
import secrets

def generate_salt():
    salt = secrets.token_bytes(16)

    return salt

def derive_key(password, salt):
    secret = password.encode()
    hashed = hash_secret_raw(secret, salt, 3, 65536, 4, 32, Type.ID)

    return hashed

