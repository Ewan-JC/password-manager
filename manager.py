import sys
import interface
import database
import hashing


def checkMasterPwd(mPassword,mHash):
    userHash=hashing.hashPassword(mPassword)
    if userHash==mHash:
        return True
    else:
        return False 
    
def login(username,password):
    
    storedPassword=database.findUserPassword(username)
    if storedPassword ==None:
        print("There is no user associated with that username")
    else:
        check=checkMasterPwd(password,storedPassword)
        if check==True:
            print("Login Successful!")
            return True
        else:
            print("Login Unsuccessful :(")
            return False


def main():
    
    while True:
        username=input("Please enter your username")
        masterPassword=input("Please enter your password")
        if not login():
            continue
        else:
            break
    
    usrChoice=interface.optionMenu()
    match usrChoice:
        case 1:
            accountInfo=interface.credentialForm()
            database.insertPasswords(username,accountInfo['e-mail'],accountInfo['Password'],accountInfo['Domain-URL'],accountInfo['Domain-Name'])
        case 2:
            credentials=database.allUserCredentials()
            interface.displayAllCredentials(credentials)
        case 3:
            domains=database.selectAllDomainNames()
            interface.displayDomains(domains)
            selectedDomain=input()
            record=database.findPasswords(username,selectedDomain)
            interface.displayCredential(record)
        case default:
            sys.exit()

interface.credentialForm()