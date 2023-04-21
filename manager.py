import sys
import interface
import hashing
import database_revamp

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
    username=input("Please enter your username")
    masterPassword=input("Please enter your password")
    #while not login(username,masterPassword):
    #    username=input("Please enter your username")
    #    masterPassword=input("Please enter your password")
    db=database_revamp.Database(username,masterPassword)
    
    usrChoice=int(interface.optionMenu())
    if usrChoice==1:
        accountInfo=interface.credentialForm()
        db.insertPasswords(accountInfo)
    
    elif usrChoice== 2:
        credentials=db.allUserCredentials()
        interface.displayAllCredentials(credentials)
    
    elif usrChoice== 3:
        domains=db.selectAllDomainNames()
        interface.displayDomains(domains)
        selectedDomain=input()
        record=db.findPasswords(selectedDomain)
        interface.displayCredential(record)
    
    else:
        sys.exit()

main()