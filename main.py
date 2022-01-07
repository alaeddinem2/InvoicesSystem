from DbConnect import DBConnect
from InvoiceObj import Client,Product,Invoice,InvoiceItem
from datetime import date
from InvoiceReport import InvoiceReport


dbconnect=DBConnect()

# report=InvoiceReport("alaeddine")
# items=[("item1",200.00,5,100.00),("item2",250.00,3,750.00),("item1",300.00,6,1800.00)]
# report.add_items(items)

'''client1 = Client("Alaeddine","0664661955","contact@telliala.info","bp 198 rouissat ouargla")
client2 = Client("Bahaeddine","0664859632","baha@gmail.com","bp 198 rouissat")
client3 = Client("kamel","0777776648","kamel@gmail.com","sokra")

dbconnect.add_client(client1)
dbconnect.add_client(client2)
dbconnect.add_client(client3)

product1 = Product("iphone",2500.00)
product2 = Product("LG",1000.00)
product3 = Product("Redmi",1500.00)
product4 = Product("samsung",2000.00)
product5 = Product("Condor",500.00)
product6 = Product('Iris',750.00)

dbconnect.add_product(product1)
dbconnect.add_product(product2)
dbconnect.add_product(product3)
dbconnect.add_product(product4)
dbconnect.add_product(product5)
dbconnect.add_product(product6)


# #Invoices
invoice1 = Invoice("001",client1.id)
invoice2 = Invoice("002",client2.id)

dbconnect.add_Invoice(invoice1)
dbconnect.add_Invoice(invoice2)

invoice01_item01 = InvoiceItem(product1.id,invoice1.id,5)
invoice01_item02 = InvoiceItem(product2.id,invoice1.id,3)
invoice01_item03 = InvoiceItem(product3.id,invoice1.id,4)
invoice01_item04 = InvoiceItem(product4.id,invoice1.id,2)

invoice02_item01 = InvoiceItem(product1.id,invoice2.id,3)
invoice02_item02 = InvoiceItem(product5.id,invoice2.id,7)
invoice02_item03 = InvoiceItem(product6.id,invoice2.id,1)
invoice02_item04 = InvoiceItem(product2.id,invoice2.id,2)

dbconnect.add_item(invoice02_item01)
dbconnect.add_item(invoice02_item02)
dbconnect.add_item(invoice02_item03)
dbconnect.add_item(invoice02_item04)

dbconnect.add_item(invoice01_item01)
dbconnect.add_item(invoice01_item02)
dbconnect.add_item(invoice01_item03)
dbconnect.add_item(invoice01_item04)'''
 
#dbconnect.get_invoice_items(1)
#dbconnect.remove_client(2)
#print(invoice02_item03.id)
#dbconnect.remove_invoice(1)
#dbconnect.remove_product(5)
invoice_info=dbconnect.get_invoice_info(1)
print(invoice_info[0][0])
#total=dbconnect.total(invoice_info)
# print('--------------------')
# invoice_items=dbconnect.get_invoice_items(2)

# print('--------------------')
# dbconnect.total(invoice_items)
# client_invoices=dbconnect.get_client_invoices(1)
#print(client_invoices)















