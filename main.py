from DbConnect import DBConnect
from InvoiceObj import Client,Product,Invoice,InvoiceItem
from datetime import date

dbconnect=DBConnect()
# client1 = Client("Alaeddine","0664661955","contact@telliala.info","bp 198 rouissat ouargla")
# client2 = Client("Bahaeddine","0664859632","baha@gmail.com","bp 198 rouissat")
# client3 = Client("kamel","0777776648","kamel@gmail.com","sokra")



# dbconnect.add_client(client1)
# dbconnect.add_client(client2)
# dbconnect.add_client(client3)



# product1 = Product("iphone",2500.00)
# product2 = Product("LG",1000.00)
# product3 = Product("Redmi",1500.00)
# product4 = Product("samsung",2000.00)
# product5 = Product("Condor",500.00)
# product6 = Product('Iris',750.00)

# dbconnect.add_product(product1)
# dbconnect.add_product(product2)
# dbconnect.add_product(product3)
# dbconnect.add_product(product4)
# dbconnect.add_product(product5)
# dbconnect.add_product(product6)

# #Invoices
# invoice1 = Invoice("001",1)
# invoice2 = Invoice("002",2)

# dbconnect.add_Invoice(invoice1)
# dbconnect.add_Invoice(invoice2)


# invoice01_item01 = InvoiceItem(1,1,3)
# invoice01_item02 = InvoiceItem(2,1,2)
# invoice01_item03 = InvoiceItem(3,1,4)
# invoice01_item04 = InvoiceItem(4,1,1)

# dbconnect.add_item(invoice01_item01)
# dbconnect.add_item(invoice01_item02)
# dbconnect.add_item(invoice01_item03)
# dbconnect.add_item(invoice01_item04)

# invoice02_item01 = InvoiceItem(1,2,6)
# invoice02_item02 = InvoiceItem(2,2,4)
# invoice02_item03 = InvoiceItem(5,2,3)
# invoice02_item04 = InvoiceItem(6,2,7)

# dbconnect.add_item(invoice02_item01)
# dbconnect.add_item(invoice02_item02)
# dbconnect.add_item(invoice02_item03)
# dbconnect.add_item(invoice02_item04)

#dbconnect.get_invoice_items(1)
dbconnect.remove_item(2)
dbconnect.remove_client(3)










