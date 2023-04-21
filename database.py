import mysql.connector


def connect():
    try:
        mydb=mysql.connector.connect(host="localhost",user='ewan-jc',password='Randomguy007!',database="password_manager")
        return mydb
    except:
        raise Exception("Unable to connect to database")
    
def insertPasswords(accountCredentials):
    try:
        db=connect()
        cur=db.cursor()
        query=("""INSERT INTO credentials(id,email, password,domainURL,domainName) VALUES (DEFAULT,%s,%s,%s,%s)""")
        values=(accountCredentials['e-mail'],accountCredentials['Password'],accountCredentials['Domain-URL'],accountCredentials['Domain-Name'])
        cur.execute(query,values)
        db.commit()
        db.close()
    except:
        raise Exception


def findPasswords(domainName):
    try:

        db=connect()
        cur=db.cursor()
        query=("""SELECT id,email,password FROM credentials (WHERE domainName= %s)""")
        domain=(domainName)
        password=cur.execute(query,domain)
        db.close()
        return password
    except:
        raise Exception

def deletePasswords(id):
    try:
        db=connect()
        cur=db.cursor()
        query=("""DELETE FROM credentials WHERE id=%s""")
        
        cur.execute(query,id)
        db.commit()
        db.close()
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
        