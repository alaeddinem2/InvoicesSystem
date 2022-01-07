from DbConnect import DBConnect
from InvoiceObj import Client,Product,Invoice,InvoiceItem
from datetime import date
from InvoiceReport import InvoiceReport


dbconnect=DBConnect()

# item10=InvoiceItem(1,1,20)
# dbconnect.add_item(item10)
# product1 = Product("iphone",5000.00)
# dbconnect.update_product(product1,1)
#items=dbconnect.get_invoice_items(1)
invoice=dbconnect.get_invoice_info(3)

print(invoice)
#total=dbconnect.total(items)

#report=InvoiceReport(str(invoice[0][3])+"_report",items,invoice,total)


#print(invoice[3])