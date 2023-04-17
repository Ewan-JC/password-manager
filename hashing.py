import hashlib

def hashPassword(userPassword):
    m=hashlib.sha255()
    m.update(b"{0}".format(userPassword))
    return m.hexdigest()