from DbConnect import DBConnect
from InvoiceObj import Client,Product,Invoice,InvoiceItem
from datetime import date


#create Clients objects
ala=Client("Alaeddine","0664661955","contact@telliala.info","BP 198 ROUISSAT OUARGLA ALGERIA",date.today())
# baha=Client("Bahaeddine","0778604044","contact@tellibaha.info","BP 198 ROUISSAT OUARGLA ALGERIA",date.today())
# moh=Client("Mohammed","0777776648","tellimohammed@gmail.com","BP 198 ROUISSAT OUARGLA ALGERIA",date.today())

#product1=Product("iphone",256.000,date.today(),date.today())
#print(product1.name)
# invoice1=Invoice("ala-2563",ala,False,date.today(),date.today())
# invoice_item=InvoiceItem(ala,invoice1,5)
dbop=DBConnect()

#add clients to db
dbop.add_client(ala)
# dbop.add_client(baha)
# dbop.add_client(moh)

#fetch all clients

dbop.get_all_clients()








