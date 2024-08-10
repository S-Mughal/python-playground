def obtain_password():
    password = input("Enter Password:")
    return password
def securepassword(password) -> str:
    special_chars = ["!","@","$","%","^","&","^","*"]
    if len(password) < 16:
        print("Password does not meet requirements.")
    elif special_chars not in list(password):
        print("Password does not meet requirements!")
    elif not re.search("[A-Z]", password):
        print("Password does not meet requirements!")
    elif not re.search("[0-9]",password):
        print("Password does not meet requirements")


def check_password():
    securepassword(obtain_password())

check_password()
