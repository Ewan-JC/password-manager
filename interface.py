import re


def optionMenu():
    choice=input("""Please pick an option from the choices below:
    *****************************************************************
    1: Add new credentials\n
    2: List all credentials\n
    3: Search for specific credential\n
    Press any other key to exit the program
    *****************************************************************
    Input: """)
    try:
        int(choice)
    except:
        raise TypeError
    return choice

def displayDomains(domainList):
    print("Domains linked to credentials: \n")
    for i, domain in enumerate(domainList):
        print(f"{i+1}: {domain}\n")


def credentialForm():
    accountInformation={'e-mail':"",'Password':"",'Domain-URL':"",'Domain-Name':""}
    
    accountInformation['e-mail']=input("Please enter the email associated with this account: ")
    while not validateEmail(accountInformation['e-mail']):
        print("E-mail was not in expected format\n Would you like to retry? (y/n) ")
        retry=input()
        if retry.casefold()=="y":
            continue
        else:
            break
    accountInformation['Password']=input("Please enter the password associated with this account: ")
    accountInformation['Domain-URL']=input("Please enter the domain URL associated with this account: ")
    accountInformation['Domain-Name']=input("Please enter the domain name associated with this account: ")
    return accountInformation

def validateEmail(email):
    validForm="^[a-zA-Z0-9-_]+@[a-zA-z0-9]+\.[a-z]{1,3}$"
    if re.match(validForm,email):
        return True
    return False

def displayAllCredentials(allCredentials):
    for x in allCredentials:
        print(x)

def displayCredential(credential):
    raise NotImplementedError
    ...
