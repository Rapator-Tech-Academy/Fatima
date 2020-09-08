user = input ("Input your user name: ")

def write_username():
    with open ("./user_name.txt", mode="w") as f:
        f.write(user)


def read_username():
    with open ("./user_name.txt", mode="r") as f:
        user = f.read()
        print (user)


write_username()
read_username ()

