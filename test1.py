from DbConnect import DBConnect
from InvoiceObj import Client,Product,Invoice,InvoiceItem
from datetime import date
from InvoiceReport import InvoiceReport


dbconnect=DBConnect()

items=dbconnect.get_invoice_items(2)
invoice=dbconnect.get_invoice_info(2)
total=dbconnect.total(items)

report=InvoiceReport("alareport",items,invoice,total)


print(invoice[0][3])