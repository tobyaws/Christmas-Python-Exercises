import re


def validate():
    while True:
        password = input("Enter a password: ")
        if len(password) < 8:
            print("Make sure your password is at least 8 characters")
        elif len(password) > 16:
            print("Make sure your password is less than 16 characters")
        elif re.search("[0-9]", password) is None:
            print("Make sure your password has a number in it")
        elif re.search("[A-Z]", password) is None:
            print("Make sure your password has a capital letter in it")
        elif re.search("[$#@]", password) is None:
            print("Make sure your password contains one of these characters $ # @")
        else:
            print("Password is valid")
            break


validate()
