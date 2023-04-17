
def login():
    username=input("Please enter your username: ")
    password=input("Please enter your password: ")
    return username,password


def optionMenu():
    choice=input("""Please pick an option from the choices below:
    *****************************************************************
    1: Add new credentials\n
    2: List all credentials\n
    3: Search for specific credential\n
    4: Exit program
    *****************************************************************""")
    try:
        int(choice)
    except:
        raise TypeError
    return choice