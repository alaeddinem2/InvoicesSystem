
import sqlite3
from sqlite3.dbapi2 import Date

class DBConnect :

    
    #Client operations
    def add_client(self,client):
        try:
            self.db=sqlite3.connect("invoicesDB.db")
            self.db.row_factory=sqlite3.Row
            cursor=self.db.cursor()
            self.db.execute("insert into  Client (ClientName, ClientPhone, ClientEmail, ClientAddress, ClientJoin) values(?,?,?,?,?)",
                        (client.name,client.phone,client.email,client.address,client.joinDate))            
            self.db.commit()
            cursor.execute('SELECT max(ClientID) FROM Client')
            client.id = cursor.fetchone()[0]
            
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
            self.db.commit()
            cursor.close()
            self.db.close() 
            print('client was delete')
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

    #product operations
    def add_product(self,product):
        try:
            self.db=sqlite3.connect("invoicesDB.db")
            self.db.row_factory=sqlite3.Row
            cursor=self.db.cursor()
            self.db.execute("insert into  Product (ProductName, ProductPrice, ProductCreated_At,ProductUpdated_At) values(?,?,?,?)",
                        (product.name,product.price,product.create,product.update))
            self.db.commit()
            cursor.execute('SELECT max(ClientID) FROM Client')
            product.id = cursor.fetchone()[0]
            cursor.close()
            self.db.close()
        except self.db.Error as error:
            print(error)

    def get_product(self,id):
        try:
            self.db=sqlite3.connect("invoicesDB.db")
            cursor=self.db.cursor()
            cursor.execute(""" SELECT * from Product where ProductID = ? """,(id,))
            clients=cursor.fetchone()
            for client in clients:
                print(client)
            cursor.close()
            self.db.close() 
            
        except self.db.Error as error:
            print('faild to get clients',error)

    def update_product(self,product,id):
        try:
            self.db=sqlite3.connect("invoicesDB.db")
            cursor=self.db.cursor()
            self.db.execute("""Update Client set ProductName = ?,ProductPrice=?, ProductCreated_At = ?,ProductUpdated_At=? WHERE ProductID = ?""",
                            (product.name,product.price,product.create,product.update,id))
            self.db.commit()
            cursor.close()
            self.db.close() 
        except self.db.Error as error:
            print('faild to update ',client.name,'information',error)

    def remove_product(self,id):
        try:
            self.db=sqlite3.connect("invoicesDB.db")
            cursor=self.db.cursor()
            self.db.execute("""DELETE FROM Product WHERE ProductID = ?""",(id,))
            self.db.commit()
            cursor.close()
            self.db.close() 
        except self.db.Error as error:
            print('faild to remove elemn',error)

    def get_all_products(self):
        try:
            self.db=sqlite3.connect("invoicesDB.db")
            cursor=self.db.cursor()
            cursor.execute(""" SELECT * from Product """)
            clients=cursor.fetchall()
            for row in clients:
                print("Id: ", row[0])
                print("Name: ", row[1])
                print("price: ", row[2])
                print("create: ", row[3])
                print("update: ", row[4])
                print("\n")
            cursor.close()
            self.db.close() 
            
        except self.db.Error as error:
            print('faild to get clients',error)

    #Invoice operations
    def add_Invoice(self,invoice):
        try:
            self.db=sqlite3.connect("invoicesDB.db")
            self.db.row_factory=sqlite3.Row
            cursor=self.db.cursor()
            self.db.execute("insert into  Invoice (InvoiceClient_fk, InvoiceCode, InvoiceStatus,InvoiceCreated_At,InvoiceUpdated_At) values(?,?,?,?,?)",
                        (invoice.client_id,invoice.code,invoice.status,invoice.create,None))
            self.db.commit()
            cursor.execute('SELECT max(ClientID) FROM Client')
            invoice.id = cursor.fetchone()[0]
            cursor.close()
            self.db.close()
        except self.db.Error as error:
            print(error)

    def get_invoice(self,id):
        try:
            self.db=sqlite3.connect("invoicesDB.db")
            cursor=self.db.cursor()
            cursor.execute(""" SELECT * from Invoice where InvoiceID = ? """,(id,))
            invoices=cursor.fetchone()
            for invoice in invoices:
                print(invoice)
            cursor.close()
            self.db.close() 
            
        except self.db.Error as error:
            print('faild to get clients',error)

    def update_invoice(self,invoiceStatus,id):
        try:
            self.db=sqlite3.connect("invoicesDB.db")
            cursor=self.db.cursor()
            self.db.execute("""Update Invoice set InvoiceStatus = ?,InvoiceUpdated_At WHERE InvoiceID = ?""",
                            (invoiceStatus,Date.today(),id))
            self.db.commit()
            cursor.close()
            self.db.close() 
        except self.db.Error as error:
            print('faild to update information',error) 

    def remove_invoice(self,id):
        try:
            self.db=sqlite3.connect("invoicesDB.db")
            cursor=self.db.cursor()
            self.db.execute("""DELETE FROM Invoice WHERE InvoiceID = ?""",(id,))
            self.db.commit()
            cursor.close()
            self.db.close() 
        except self.db.Error as error:
            print('faild to remove elemn',error)

    def get_all_invoices(self,client_id):

        try:
            self.db=sqlite3.connect("invoicesDB.db")
            cursor=self.db.cursor()
            cursor.execute(""" SELECT * from Invoice where InvoiceClient_fk=? """,(client_id))
            clients=cursor.fetchall()
            for row in clients:
                print("InvoiceID: ",        row[0])
                print("InvoiceCient: ",     row[2])
                print("InvoiceCode: ",      row[3])
                print("InvoiceStatus: ",    row[4])
                print("InvoiceCreated_At: ",row[5])
                print("InvoiceUpdated_At: ",row[6])
                print("\n")
            cursor.close()
            self.db.close() 
            
        except self.db.Error as error:
            print('faild to get clients',error)
    
    #Items operations 
    def add_item(self,invoiceItem):
        try:
            self.db=sqlite3.connect("invoicesDB.db")
            self.db.row_factory=sqlite3.Row
            cursor=self.db.cursor()
            self.db.execute("insert into  InvoiceItem (InvoiceItemProduct_fk, InvoiceItem_fk, InvoiceItemQuantity) values(?,?,?)",
                        (invoiceItem.product_id,invoiceItem.invoice_id,invoiceItem.quantity))
            self.db.commit()
            cursor.execute('SELECT max(ClientID) FROM Client')
            invoiceItem.id = cursor.fetchone()[0]
            cursor.close()
            self.db.close()
        except self.db.Error as error:
            print(error)

    def get_item(self,invoice_id):
        try:
            self.db=sqlite3.connect("invoicesDB.db")
            cursor=self.db.cursor()
            cursor.execute(""" SELECT InvoiceItemProduct_fk,InvoiceItemQuantity from InvoiceItem where InvoiceItem_fk=? """,(invoice_id,))
            items=cursor.fetchone()
            for item in items:
                print("product :",  item[1])
                print("quantity :", item[3])
            cursor.close()
            self.db.close() 
            
        except self.db.Error as error:
            print('faild to get invoice item',error)

    def update_item(self,itemQuantity,product_id,invoice_id):
        try:
            self.db=sqlite3.connect("invoicesDB.db")
            cursor=self.db.cursor()
            self.db.execute("""Update InvoiceItem set InvoiceItemQuantity=? WHERE InvoiceItemID = ?,InvoiceProductID""",
                            (itemQuantity.quantity,invoice_id,product_id))
            self.db.commit()
            cursor.close()
            self.db.close() 
        except self.db.Error as error:
            print('faild to update information',error)

    def remove_item(self,item_id):
        try:
            self.db=sqlite3.connect("invoicesDB.db")
            cursor=self.db.cursor()
            self.db.execute("""DELETE FROM InvoiceItem WHERE  InvoiceItemID = ?""",(item_id,))
            self.db.commit()
            cursor.close()
            self.db.close() 
            print("item deleted")
        except self.db.Error as error:
            print('faild to remove elemnt',error)

    def get_invoice_items(self,invoice_id):
        try:
            self.db=sqlite3.connect("invoicesDB.db")
            cursor=self.db.cursor()
            cursor.execute(""" SELECT InvoiceItemProduct_fk,InvoiceItemQuantity from InvoiceItem where InvoiceItem_fk=? """,(invoice_id,))
            items=cursor.fetchall()
            for item in items:
                print(item)
            
            cursor.execute(""" SELECT ProductName from Product where ProductID=? """,(items[0],))
            product_name=cursor.fetchone()[0]   
            invoice_item=(product_name,items[1])    
            cursor.close()
            self.db.close()
            return invoice_item
            
        except self.db.Error as error:
            print('faild to get Item',error)

    def get_item_name(self,id):
        try:
            self.db=sqlite3.connect("invoicesDB.db")
            cursor=self.db.cursor()
            cursor.execute(""" SELECT ProductName from Product where ProductID=? """,(id,))
            product_name=cursor.fetchone()[0]
            #print(product_name)    
            cursor.close()
            self.db.close()
            return product_name
            
        except self.db.Error as error:
            print('faild to get Item',error)
    