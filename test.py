from DbConnect import DBConnect
from InvoiceObj import Client,Product,Invoice,InvoiceItem
from datetime import date

dbconnect=DBConnect()

client4 = Client("Adm","077556648","dem@gmail.com","sokra")
dbconnect.add_client(client4)

print(client4.clientID)


cursor.execute(""" SELECT ProductName from Product where ProductID=? """,(items[0],))
            product_name=cursor.fetchone()[0]   
            invoice_item=(product_name,items[1])


