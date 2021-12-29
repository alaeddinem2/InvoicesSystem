from Client import Client
from DbConnect import DBConnect
from datetime import date


client1=Client("bahaeddine","0664661955","telliala@gmail.com","BP 198 ROUISSAT OUARGLA",date.today())
client2=Client("ala","066466955","teliala@gmail.com","BP 198 ROUISSAT OUARGLA",date.today())
client3=Client("baha","06641955","tellla@gmail.com","BP 198 ROUISSAT OUARGLA",date.today())

dbConnect=DBConnect()
# dbConnect.add_client(client1)
# dbConnect.add_client(client2)
# dbConnect.add_client(client3)
# client=dbConnect.get_client(2)
#dbConnect.get_all_clients()
client4=Client('bahaeddine',"06686695","ala@ala.co","rouissat",date.today())
dbConnect.update_client(client4,2)
client=dbConnect.get_client(2)




