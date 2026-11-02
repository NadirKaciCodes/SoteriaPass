from soteriapass.security.key_derivation import derive_key, generate_salt

# Test with identical password and identical salt
salt1 = generate_salt()
password = "dummyPassword123"

result1 = derive_key(password, salt1)
result2 = derive_key(password, salt1)
print("First hash :", result1)
print("Second hash :", result2)
print("Hashes are identical")
print(" ")
# Test with identical passwod and different salt

salt1 = generate_salt()
salt2 = generate_salt()

result3 = derive_key(password, salt1)
result4 = derive_key(password, salt2)

print("First hash:", result3)
print("Second hash:", result4)
print("Hashes are not-identical")
print(" ")

#Test lenght of hash (32 bytes)

print(len(result3))