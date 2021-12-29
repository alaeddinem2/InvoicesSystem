
import sqlite3

class DBConnect :

    def __init__(self):
        self.connect_db()

    def connect_db(self):
        pass
    
    def add_client(self,client):
        try:
            self.db=sqlite3.connect("invoicesDB.db")
            self.db.row_factory=sqlite3.Row
            cursor=self.db.cursor()
            self.db.execute("insert into  Client (ClientName, ClientPhone, ClientEmail, ClientAddress, ClientJoin) values(?,?,?,?,?)",
                        (client.name,client.phone,client.email,client.address,client.joinDate))
            self.db.commit()
            cursor.close()
            self.db.close()
        except self.db.Error as error:
            print(error)
          
    def get_client(self,id):
        try:
            self.db=sqlite3.connect("invoicesDB.db")
            cursor=self.db.cursor()
            cursor.execute(""" SELECT * from Client where ClientID = ? """,(id,))
            clients=cursor.fetchone()
            for client in clients:
                print(client)
            cursor.close()
            self.db.close() 
            
        except self.db.Error as error:
            print('faild to get clients',error)
    def update_client(self,client,id):
        try:
            self.db=sqlite3.connect("invoicesDB.db")
            cursor=self.db.cursor()
            self.db.execute("""Update Client set ClientName = ?,ClientPhone=?, ClientEmail = ?,ClientAddress=? WHERE ClientID = ?""",
                            (client.name,client.phone,client.email,client.address,id))
            self.db.commit()
            cursor.close()
            self.db.close() 
        except self.db.Error as error:
            print('faild to update ',client.name,'information',error) 

    def remove_client(self,id):
        try:
            self.db=sqlite3.connect("invoicesDB.db")
            cursor=self.db.cursor()
            self.db.execute("""DELETE FROM Client WHERE ClientID = ?""",(id,))
            
            cursor.close()
            self.db.close() 
        except self.db.Error as error:
            print('faild to remove elemn',error) 
    
    def get_all_clients(self):
        try:
            self.db=sqlite3.connect("invoicesDB.db")
            cursor=self.db.cursor()
            cursor.execute(""" SELECT * from Client """)
            clients=cursor.fetchall()
            for row in clients:
                print("Id: ", row[0])
                print("Name: ", row[1])
                print("phone: ", row[2])
                print("Email: ", row[3])
                print("address: ", row[4])
                print("joinDate: ", row[5])
                print("\n")
            cursor.close()
            self.db.close() 
            
        except self.db.Error as error:
            print('faild to get clients',error)

        