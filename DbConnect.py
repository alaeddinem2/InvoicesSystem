
from datetime import date
from operator import rshift
import sqlite3
from sqlite3.dbapi2 import Date, Error
from unittest import result


class DBConnect :

    
    #Client operations
    def add_client(self,client):
  
        with sqlite3.connect("invoicesDB.db") as connection:
            cursor=connection.cursor()
            cursor.execute("insert into  Client (ClientName, ClientPhone, ClientEmail, ClientAddress, ClientJoin) values(?,?,?,?,?)",
                            (client.name,client.phone,client.email,client.address,client.joinDate))            
            connection.commit()
            cursor.execute('SELECT max(ClientID) FROM Client')
            client.id = cursor.fetchone()[0]
            result= str(client.name) + " was added to the database !"
            return result
        
            
        
            
                    
    def get_client(self,id):
        with sqlite3.connect("invoicesDB.db") as connection:
            cursor=connection.cursor()
            cursor.execute(""" SELECT * from Client where ClientID = ? """,(id,))
            client=cursor.fetchone()
            return client
 
            

    def update_client(self,client,id):
        with sqlite3.connect("invoicesDB.db") as connection:
            cursor=connection.cursor() 
            cursor.execute("""Update Client set ClientName = ?,ClientPhone=?, ClientEmail = ?,ClientAddress=? WHERE ClientID = ?""",
                            (client.name,client.phone,client.email,client.address,id))
            connection.commit()
            result = str(client.name)+" was updated"
            return result
             
         

    def remove_client(self,id):
        with sqlite3.connect("invoicesDB.db") as connection:
            cursor=connection.cursor()          
            cursor.execute("PRAGMA foreign_keys = ON")
            cursor.execute("""DELETE FROM Client WHERE ClientID = ?""",(id,))
            connection.commit() 
            return 'client was deleted'
         
    
    def get_all_clients(self):
        with sqlite3.connect("invoicesDB.db") as connection:
            cursor=connection.cursor()
            cursor.execute(""" SELECT * from Client """)
            clients=cursor.fetchall()
            return clients
    
    
    #product operations

    def add_product(self,product):
        with sqlite3.connect("invoicesDB.db") as connection:
            cursor=connection.cursor()
            cursor.execute("insert into  Product (ProductName, ProductPrice, ProductCreated_At,ProductUpdated_At) values(?,?,?,?)",
                        (product.name,product.price,product.create,product.update))
            connection.commit()
            cursor.execute('SELECT max(ProductID) FROM Product')
            product.id = cursor.fetchone()[0]

            result= str(product.name) + " was added to the database !"
            return result
        

    def get_product(self,id):
        with sqlite3.connect("invoicesDB.db") as connection:
            cursor=connection.cursor()
            cursor.execute(""" SELECT * from Product where ProductID = ? """,(id,))
            clients=cursor.fetchone()
            for client in clients:
                print(client)
           
    # TODO: modify this function below
    def update_product(self,product,id):
        with sqlite3.connect("invoicesDB.db") as connection:
            cursor=connection.cursor()
            cursor.execute("PRAGMA foreign_keys = ON")
            cursor.execute("""Update Product set ProductName = ?, ProductPrice=?,ProductUpdated_At=? WHERE ProductID = ?""",
                            (product.name,product.price,date.today(),id))
            connection.commit()
            result = str(product.name)+"was update"
            return result
             
        

    def remove_product(self,id):
        with sqlite3.connect("invoicesDB.db") as connection:
            cursor=connection.cursor()
            cursor.execute("PRAGMA foreign_keys = ON")
            cursor.execute("""DELETE FROM Product WHERE ProductID = ?""",(id,))
            connection.commit()
            result= "product was deleted !"
            return result
        

    def get_all_products(self):
        with sqlite3.connect("invoicesDB.db") as connection:
            cursor=connection.cursor()
            cursor.execute(""" SELECT * from Product """)
            products=cursor.fetchall()
            return products
            
             

    #Invoice operations

    def add_Invoice(self,invoice):
        with sqlite3.connect("invoicesDB.db") as connection:
            cursor=connection.cursor()
            cursor.execute("insert into  Invoice (InvoiceClient_fk, InvoiceCode, InvoiceStatus,InvoiceCreated_At,InvoiceUpdated_At) values(?,?,?,?,?)",
                        (invoice.client_id,invoice.code,invoice.status,invoice.create,None))
            connection.commit()
            cursor.execute('SELECT max(InvoiceID) FROM Invoice')
            invoice.id = cursor.fetchone()[0]
            result = "the invoice was added"
            return result,invoice.id
            

    def get_invoice(self,id):
        with sqlite3.connect("invoicesDB.db") as connection:
            cursor=connection.cursor()
            cursor.execute(""" SELECT * from Invoice where InvoiceID = ? """,(id,))
            invoice=cursor.fetchall()
            
            return invoice
            
    def update_invoice(self,invoiceStatus,id):
        with sqlite3.connect("invoicesDB.db") as connection:
            cursor=connection.cursor()
            cursor.execute("""Update Invoice set InvoiceStatus = ?,InvoiceUpdated_At WHERE InvoiceID = ?""",
                            (invoiceStatus,Date.today(),id))
            connection.commit()
             
         

    def remove_invoice(self,id):
        with sqlite3.connect("invoicesDB.db") as connection:
            cursor=connection.cursor()
            cursor.execute("PRAGMA foreign_keys = ON")
            cursor=self.db.cursor()
            cursor.execute("""DELETE FROM Invoice WHERE InvoiceID = ?""",(id,))
            connection.commit()
            

    def get_client_invoices(self,client_id):

        with sqlite3.connect("invoicesDB.db") as connection:
            cursor=connection.cursor()
            cursor.execute(""" SELECT * from Invoice where InvoiceClient_fk = ? """,(client_id,))
            invoices=cursor.fetchall()
            return invoices

    def get_all_invoices(self):

        with sqlite3.connect("invoicesDB.db") as connection:
            cursor=connection.cursor()
            cursor.execute(""" SELECT * from Invoice """)
            invoices=cursor.fetchall()
            return invoices
                
    
    #Items operations 

    def add_item(self,invoiceItem):
        with sqlite3.connect("invoicesDB.db") as connection:
            cursor=connection.cursor()
            cursor.execute("insert into  InvoiceItem (InvoiceItemProduct_fk, InvoiceItem_fk, InvoiceItemQuantity) values(?,?,?)",
                        (invoiceItem.product_id,invoiceItem.invoice_id,invoiceItem.quantity))
            connection.commit()
            cursor.execute('SELECT max(InvoiceItemID) FROM InvoiceItem')
            invoiceItem.id = cursor.fetchone()[0]
            return "the item has added"
            

    def get_item(self,invoice_id):
        with sqlite3.connect("invoicesDB.db") as connection:
            cursor=connection.cursor()
            cursor.execute(""" SELECT InvoiceItemProduct_fk,InvoiceItemQuantity from InvoiceItem where InvoiceItem_fk=? """,(invoice_id,))
            items=cursor.fetchone()
            for item in items:
                print("product :",  item[1])
                print("quantity :", item[3])
            

    def update_item(self,itemQuantity,item_id):
        with sqlite3.connect("invoicesDB.db") as connection:
            cursor=connection.cursor()
            cursor.execute("PRAGMA foreign_keys = ON")
            cursor.execute("""Update InvoiceItem set InvoiceItemQuantity=? WHERE InvoiceItemID =?""",
                            (itemQuantity,item_id))
            connection.commit()

            return "the item was update !"
             
        

    def remove_item(self,item_id):
        with sqlite3.connect("invoicesDB.db") as connection:
            cursor=connection.cursor()
            cursor.execute("""DELETE FROM InvoiceItem WHERE  InvoiceItemID = ?""",(item_id,))
            connection.commit() 
            print("item deleted")
        

    def get_invoice_items(self,id):
        try:
            with sqlite3.connect("invoicesDB.db") as connection:
                 cursor=connection.cursor()
            
            # Query for INNER JOIN
                 sql = """SELECT InvoiceItemID,Product.ProductName,Product.ProductPrice, InvoiceItem.InvoiceItemQuantity , InvoiceItem.InvoiceItemQuantity * Product.ProductPrice 
                            FROM   InvoiceItem
                            LEFT JOIN Product on Product.ProductID = InvoiceItem.InvoiceItemProduct_fk
                            LEFT JOIN Invoice on Invoice.InvoiceID = InvoiceItem.InvoiceItem_fk
                            WHERE InvoiceID = ? """ 
                 cursor.execute(sql,(id,))
                 items= cursor.fetchall()
                 return items
        
        except TypeError :
            print('connection err',TypeError )
    
    def get_invoice_info(self,id):
        try:
            with sqlite3.connect("invoicesDB.db") as connection:
                 cursor=connection.cursor()
            
            # Query for INNER JOIN
                 sql = """SELECT Invoice.InvoiceCode,Invoice.InvoiceStatus,InvoiceCreated_At, Client.ClientName,Client.ClientEmail,Client.ClientPhone,ClientAddress
                        FROM  invoice
                        LEFT JOIN Client on Client.ClientID = Invoice.InvoiceClient_fk
                        WHERE Invoice.InvoiceID = ? """ 
                 cursor.execute(sql,(id,))
                 invoice= cursor.fetchall()
                 return invoice
        
        except TypeError :
            print('connection err',TypeError )
            
        

    def get_item_name(self,id):
        with sqlite3.connect("invoicesDB.db") as connection:
            cursor=connection.cursor()
            cursor.execute(""" SELECT ProductName from Product where ProductID=? """,(id,))
            product_name=cursor.fetchone()[0]
            #print(product_name)    
            cursor.close()
            self.db.close()
            return product_name

    def total(self,invoice_items):
        total=0.0
        
        for item in invoice_items:
            
            total+=float(item[4])
        total_tva=total*0.19
        full_total=total+total_tva
        return total,total_tva,full_total

            
    