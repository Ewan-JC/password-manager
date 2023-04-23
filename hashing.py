import hashlib
import random
import string

def createPassword(passLength=16,specialChars=True,upperCase=True,digits=True):
    
    if upperCase==False:
        characters=string.ascii_lowercase
    else:
        characters=string.ascii_letters
    if specialChars==True:
        characters+=string.punctuation
    if digits==True:
        characters+=string.digits

    return "".join(random.choice(characters) for i in range(passLength))

def generateHash(password,secretKey):
    raise NotImplementedError

def encryptPassword(plainPassword):
    raise NotImplementedError

def decrpyptPassword(cypherPassword):
    raise NotImplementedError