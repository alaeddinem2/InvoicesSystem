import sqlite3

class Invoice:
    def __init__(self,code,client,status,create,update):
        #invoice attr
        self.code = code
        self.client = client
        self.status = status
        self.create = create
        self.update = update

        #create Invoice table in database
        self.db=sqlite3.connect("invoicesDB.db")
        self.db.row_factory=sqlite3.Row
        self.db.execute("create table if not exists Invoice (InvoiceID integer primary key autoincrement ,FOREIGN KEY(InvoiceClient_fk) REFERENCES Client(ClientID),InvoiceCode text,InvoiceStatus BOOLEAN,InvoiceCreated_At DATE,InvoiceUpdated_At DATE)")
        self.db.close()


class Client:
    def __init__(self,name,phone,email,address,joinDate):
        #client attr
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.joinDate = joinDate

        #create client table in database
        self.db=sqlite3.connect("invoicesDB.db")
        self.db.row_factory=sqlite3.Row
        self.db.execute("create table if not exists Client (ClientID integer primary key autoincrement , ClientName text,ClientPhone text NOT NULL UNIQUE, ClientEmail text NOT NULL UNIQUE ,ClientAddress text,ClientJoin DATE)")
        self.db.close()


class InvoiceItem:
    def __init__(self,client,invoice,quantity):
        #InvoiceItem attr
        self.client = client
        self.invoice = invoice
        self.quantity = quantity

        #create InvoiceItem table in databse
        self.db=sqlite3.connect("invoicesDB.db")
        self.db.row_factory=sqlite3.Row
        self.db.execute("create table if not exists InvoiceItem (InvoiceItemID integer primary key autoincrement ,FOREIGN KEY(InvoiceItemClient_fk) REFERENCES Client(ClientID),FOREIGN KEY(InvoiceItem_fk) REFERENCES Invoice(InvoiceID) ,InvoiceItemQuantity integer)")
        self.db.close()


class Product:
    def __init__(self,name,price,create,update):
        #product attr 
        self.name = name
        self.price = price
        self.create = create
        self.update = update

        #create product table in databse
        self.db=sqlite3.connect("invoicesDB.db")
        self.db.row_factory=sqlite3.Row
        self.db.execute("create table if not exists Product (ProductID integer primary key autoincrement , ProductName text, ProductPrice FLOAT text,ProductCreated_At DATE,ProductUpdated_At DATE)")
        self.db.close()

