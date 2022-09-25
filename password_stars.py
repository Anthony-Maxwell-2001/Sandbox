"""CP1404 Password Stars"""

minium_password_length = int(input("Minium password length: "))
password_name = input("Enter Password: ")
while len(password_name) < minium_password_length:
    print("Invalid password length")
    password_name = input("Enter Password: ")

print(len(password_name) * '*')

