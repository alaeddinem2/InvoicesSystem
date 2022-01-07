import sqlite3
from datetime import date
class Invoice:
    id = None
    create = date.today()
    update = None
    status = False
    def __init__(self,code,client_id):
        #invoice attr
        self.id=Invoice.id
        self.code = code
        self.client_id = client_id
        self.status = Invoice.status
        self.create = Invoice.create
        self.update = Invoice.update

        #create Invoice table in database
        with sqlite3.connect("invoicesDB.db") as connection:
            cursor=connection.cursor()
            connection.row_factory=sqlite3.Row
            cursor.execute("create table if not exists Invoice (InvoiceID integer primary key autoincrement ,InvoiceClient_fk integer,InvoiceCode text,InvoiceStatus BOOLEAN,InvoiceCreated_At DATE,InvoiceUpdated_At DATE,FOREIGN KEY(InvoiceClient_fk) REFERENCES Client(ClientID) ON DELETE CASCADE ON UPDATE CASCADE )")
    
    
        


class Client:
    joinDate = date.today()
    id = None
    def __init__(self,name,phone,email,address):
        #client attr
        self.id=Client.id
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.joinDate = Client.joinDate

        #create client table in database
        with sqlite3.connect("invoicesDB.db") as connection:
            cursor=connection.cursor()
            connection.row_factory=sqlite3.Row
            cursor.execute("create table if not exists Client (ClientID integer primary key autoincrement , ClientName text,ClientPhone text NOT NULL UNIQUE, ClientEmail text NOT NULL UNIQUE ,ClientAddress text,ClientJoin DATE)")
        


class InvoiceItem:
    id = None
    def __init__(self,product_id,invoice_id,quantity):
        #InvoiceItem attr
        self.id=InvoiceItem.id
        self.product_id = product_id
        self.invoice_id = invoice_id
        self.quantity = quantity

        #create InvoiceItem table in databse
        with sqlite3.connect("invoicesDB.db") as connection:
            cursor=connection.cursor()
            connection.row_factory=sqlite3.Row
            cursor.execute("create table if not exists InvoiceItem (InvoiceItemID integer primary key autoincrement ,InvoiceItemProduct_fk integer,InvoiceItem_fk integer ,InvoiceItemQuantity integer,FOREIGN KEY(InvoiceItemProduct_fk) REFERENCES Product(ProductID) ON DELETE CASCADE  ON UPDATE CASCADE ,FOREIGN KEY(InvoiceItem_fk) REFERENCES Invoice(InvoiceID) ON DELETE CASCADE ON UPDATE CASCADE )")
            


class Product:
    id = None
    create = date.today()
    update = None
    def __init__(self,name,price):
        #product attr 
        self.id = Product.id
        self.name = name
        self.price = price
        self.create = Product.create
        self.update = Product.update

        #create product table in databse
        with sqlite3.connect("invoicesDB.db") as connection:
            cursor=connection.cursor()
            connection.row_factory=sqlite3.Row
            cursor.execute("create table if not exists Product (ProductID integer primary key autoincrement , ProductName text, ProductPrice FLOAT text,ProductCreated_At DATE,ProductUpdated_At DATE)")
            

