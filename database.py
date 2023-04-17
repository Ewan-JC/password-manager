import mysql.connector



#connect to the mysql database



def connect():
    try:
        mydb=mysql.connector.connect(host="localhost",user='ewan-jc',password='Randomguy007!',database="password-manager")
        return mydb
    except:
        raise Exception("Unable to connect to database")
    
def insertPasswords(username,userEmail,password,domainURL,domainName):
    try:
        db=connect(username)
        cur=db.cursor()
        query=("""INSERT INTO credentials (username, email, password,domainURL,domainName) VALUES (%s,%s,%s,%s,%s)""")
        values=(username,userEmail,password,domainURL,domainName)
        cur.execute(query,values)
        db.close()
    except:
        raise Exception


def findPasswords(username,domainName):
    try:

        db=connect()
        cur=db.cursor()
        query=("""SELECT email,password FROM credentials (WHERE domainName= %s)""")
        domain=(domainName)
        password=cur.execute(query,domain)
        db.close()
        return password
    except:
        raise Exception


def allUserCredentials():
    try:
        db=connect()
        cur=db.cursor()
        query=("""SELECT * FROM credentials""")
        cur.execute(query)
        credentials=cur.fetchall()
        db.close()
        return credentials 
    except:
        raise Exception
    

def selectAllDomainNames():
    try:
        db=connect()
        cur=db.cursor()
        cur.execute("""SELECT domainName FROM credentials""")
        domainNames=cur.fetchall()
        db.close()
        return domainNames
    except:
        raise Exception
        