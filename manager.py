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
        if checkMasterPwd(password,storedPassword):
            print("Login Successful!")
            return True
        else:
            print("Login Unsuccessful :(")
            return False


def main():
   # username=input("Please enter your username")
    #masterPassword=input("Please enter your password")
    #while not login(username,masterPassword):
    #    username=input("Please enter your username")
    #    masterPassword=input("Please enter your password")
    
    usrChoice=int(interface.optionMenu())
    if usrChoice==1:
        accountInfo=interface.credentialForm()
        database.insertPasswords(accountInfo)
    
    elif usrChoice== 2:
        credentials=database.allUserCredentials()
        interface.displayAllCredentials(credentials)
    
    elif usrChoice== 3:
        domains=database.selectAllDomainNames()
        interface.displayDomains(domains)
        selectedDomain=input()
        record=database.findPasswords(selectedDomain)
        interface.displayCredential(record)
    
    else:
        sys.exit()

main()