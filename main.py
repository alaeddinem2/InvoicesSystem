from DbConnect import DBConnect
from InvoiceObj import Client,Product,Invoice,InvoiceItem
from datetime import date


#create Clients objects
ala=Client("Alaeddine","0664661955","contact@telliala.info","BP 198 ROUISSAT OUARGLA ALGERIA",date.today())
baha=Client("Bahaeddine","0778604044","contact@tellibaha.info","BP 198 ROUISSAT OUARGLA ALGERIA",date.today())
moh=Client("Mohammed","0777776648","tellimohammed@gmail.com","BP 198 ROUISSAT OUARGLA ALGERIA",date.today())
dbop=DBConnect()

#add clients to db
dbop.add_client(ala)
dbop.add_client(baha)
dbop.add_client(moh)

#fetch all clients

dbop.get_all_clients()







