import hashlib
import menu
import database
import hashing


def checkMasterPwd(mPassword,mHash):
    m=hashlib.sha256()
    m.update(b"{0}".format(mPassword))
    passHash=m.hexdigest()

    if passHash==mHash:
        return True
    else:
        return False 
    

usrChoice=input(menu.optionMenu())