"""Jake"""
INVALID_NAME = ""


user_name = input("what is your name: ".strip())
while user_name == INVALID_NAME:
    print("invalid name")
    user_name = input("what is your name: ".strip())
for chr in user_name[::2]:
    print(chr)