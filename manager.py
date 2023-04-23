import sys
import interface
import hashing
import database_revamp

def main():
    username=input("Please enter your username")
    masterPassword=input("Please enter your password")

    #Add a call to a function that hashes masterPassword
    #Check if the entered masterPassword has the same hash as the stored password
    #If they have the same hash then continue with the program
    #If not inform the user that they entered the wrong details and offer them to try again


    db=database_revamp.Database(username,masterPassword)
    
    usrChoice=int(interface.optionMenu())
    if usrChoice==1:
        accountInfo=interface.credentialForm()
        #Add a call to a function that encrypts the password in the credential form
        #Reinsert the encrypted password into the credential tuple of the db record
        db.insertPasswords(accountInfo)
    
    elif usrChoice== 2:
        credentials=db.allUserCredentials()
        interface.displayAllCredentials(credentials) #Edit this to style display
    
    elif usrChoice== 3: 
        
        domains=db.selectAllDomainNames()
        interface.displayDomains(domains)
        selectedDomain=input()
        record=db.findPasswords(selectedDomain)
        interface.displayCredential(record)
    
    elif usrChoice==4:
        newPassword=hashing.createPassword()
        createCredential=input("Do you want to add a credential to the database (y/n): ")
        if createCredential.casefold()=="y":
            accountInfo=interface.credentialForm(newPassword)
            db.insertPasswords(accountInfo)
    else:
        sys.exit()

main()