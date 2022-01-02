import sqlite3
from sqlite3.dbapi2 import Error
id=input(" input id  : ") 
try:
    with sqlite3.connect("invoicesDB.db") as connection:
        cursor=connection.cursor()
    
    # Query for INNER JOIN
        sql = '''SELECT Invoice.InvoiceCode,Client.ClientName, Product.ProductName , Product.ProductPrice, InvoiceItem.InvoiceItemQuantity
    FROM   InvoiceItem
    INNER JOIN Invoice ON InvoiceID = InvoiceItem_fk 
    INNER JOIN Product on Product.ProductID = InvoiceItem.InvoiceItemProduct_fk 
    INNER JOIN Client on Client.ClientID = Invoice.InvoiceClient_fk 
    WHERE InvoiceID = ?   ;''' 
    
    # Executing the query
        cursor.execute(sql,id)
    
    # Fetching rows from the result table
        result = cursor.fetchall()
        print(result)
except TypeError :
    print('connection err',TypeError )
    
  
# Closing the connection











