import mysql.connector


class Database():
    def __init__(self,username,password):
        self.dbUser=username
        self.dbPassword=password
        

    def connect(self):
        try:
            mydb=mysql.connector.connect(host="localhost",user=f"{self.dbUser}",password=f"{self.dbPassword}",database="password_manager")
            return mydb
        except:
            raise Exception
        
    def insertPasswords(self,accountCredentials):
        try:
            db=self.connect()
            cur=db.cursor()
            query=("""INSERT INTO credentials(id,email, password,domainURL,domainName) VALUES (DEFAULT,%s,%s,%s,%s)""")
            values=(accountCredentials['e-mail'],accountCredentials['Password'],accountCredentials['Domain-URL'],accountCredentials['Domain-Name'])
            cur.execute(query,values)
            db.commit()
            db.close()
        except:
            raise Exception
        
    def findPasswords(self,domainName):
        try:
            db=self.connect()
            cur=db.cursor()
            query=("""SELECT id,email,password FROM credentials (WHERE domainName= %s)""")
            domain=(domainName)
            cur.execute(query,domain)
            db.commit()
            password=cur.fetchone()
            db.close()
            return password
        except:
            raise Exception
    def deletePasswords(self,id):
        try:
            db=self.connect()
            cur=db.cursor()
            query=("""DELETE FROM credentials WHERE id=%s""")
            
            cur.execute(query,id)
            db.commit()
            db.close()
        except:
            raise Exception
        
    def allUserCredentials(self):
        try:
            db=self.connect()
            cur=db.cursor()
            query=("""SELECT * FROM credentials""")
            cur.execute(query)
            credentials=cur.fetchall()
            db.close()
            return credentials 
        except:
            raise Exception
    

    def selectAllDomainNames(self):
        try:
            db=self.connect()
            cur=db.cursor()
            cur.execute("""SELECT domainName FROM credentials""")
            domainNames=cur.fetchall()
            db.close()
            return domainNames
        except:
            raise Exception
            

