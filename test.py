from DbConnect import DBConnect
from InvoiceObj import Client,Product,Invoice,InvoiceItem
from datetime import date

dbconnect=DBConnect()

client4 = Client("Adm","077556648","dem@gmail.com","sokra")
dbconnect.add_client(client4)

print(client4.clientID)


