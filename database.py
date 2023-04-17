import mysql.connector



#connect to the mysql database



def connect(username,passwordHash):
    try:
        mydb=mysql.connector.connect(host="localhost",user=username,password=passwordHash,database="password-manager")
        return mydb
    except:
        raise Exception("Unable to connect to database")
    
def insertPasswords(username,passwordHash,userEmail,password,domainURL,domainName):
    db=connect(username,passwordHash)
    cur=db.cursor()
    query=("""INSERT INTO credentials (username, email, password,domainURL,domainName) VALUES (%s,%s,%s,%s,%s)""")
    values=(username,userEmail,password,domainURL,domainName)
    cur.execute(query,values)
    db.close()


def findPasswords(username,passwordHash,domainName):
    db=connect(username,passwordHash)
    cur=db.cursor()
    query=("""SELECT password FROM credentials (WHERE domainName= %s AND username= %s)""")
    domain=(domainName,username)
    password=cur.execute(query,domain)
    return password


def allUserCredentials(username,passwordHash):
    db=connect(username,passwordHash)
    cur=db.cursor()
    query=("""SELECT * FROM credentials WHERE username= %s""")
    value=username
    credentials=cur.execute(query,value)
    return credentials 