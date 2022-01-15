
from os import name
from sqlite3.dbapi2 import Error
from tabnanny import check
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import re
from DbConnect import DBConnect
from InvoiceObj import Client,Product,Invoice,InvoiceItem
from InvoiceReport import InvoiceReport


class guiOperations(DBConnect,Client) :
    global clients
    
    check = False

    

    def __init__(self):
        self.dbconnect=DBConnect()


    def select_client(self):

        name = self.tableWidget.item(self.tableWidget.currentRow(),0).text()
                    
        phone = self.tableWidget.item(self.tableWidget.currentRow(),1).text()
        email = self.tableWidget.item(self.tableWidget.currentRow(),2).text()
        address = self.tableWidget.item(self.tableWidget.currentRow(),3).text()
                    
        
        return name,phone,email,address 
        
        
        
    def load_client_data (self)-> bool :
        try:
            data = self.select_client()
            
            self.clientName.setText(data[0])
            self.clientPhone.setText(data[1])
            self.clientEmail.setText(data[2])
            self.clientAddress.setText(data[3])
            self.check = True
            print(self.check)
            return self.check
            
     
        except:
            QMessageBox.information(self,"info","please select an user !")

    def get_id(self,email)-> int :
        self.clients
        for client in self.clients:
            if client[3] == email:
                return client[0]


    def is_email_exist(self,email)-> bool:
        
        for client in self.clients:
            if client[3] == email:
                return True 

    def add_client(self):
        
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        name=self.clientName.text()
        phone=self.clientPhone.text()
        email= self.clientEmail.text()
        address=self.clientAddress.text()

        if (name.strip(" ")  or phone.strip(" ")  or  address.strip(" ")) == "":

                QMessageBox.warning(self,"Warning","please enter all fields! ")
                
        elif email.strip(" ") == "" or not (re.fullmatch(regex, email)):
                QMessageBox.warning(self,"Warning","please enter a correct email ! ")

        elif self.is_email_exist(email) is True :
            QMessageBox.warning(self,"Warning","email is exist ! ")
            
        else :
            client=Client(name,phone,email,address)
            client=self.dbconnect.add_client(client)
            QMessageBox.information(self,"secces",client)
            self.clientName.clear()
            self.clientPhone.clear()
            self.clientEmail.clear()
            self.clientAddress.clear()

            self.get_clients()       

    def updateClient(self):
        name=self.clientName.text()
        phone=self.clientPhone.text()
        email= self.clientEmail.text()
        address=self.clientAddress.text()
        data = self.select_client()
        id = self.get_id(data[2])

        upload_client=Client(name,phone,email,address)
        result = self.dbconnect.update_client(upload_client,id)
        QMessageBox.information(self,"secces",result)
        self.clientName.clear()
        self.clientPhone.clear()
        self.clientEmail.clear()
        self.clientAddress.clear()

    def send_data(self):
        print(self.check)
        if self.check == True :
            self.updateClient()  
        else :
            self.add_client()

        self.check = False


    def del_client(self):
        try: 
            data= self.select_client()
            id = self.get_id(data[2])
            self.dbconnect.remove_client(id)
            print(id)
            #self.get_clients()
        except:
            QMessageBox.information(self,"info","please select an user !")
        
        
        


    def get_clients(self):
        
        while self.tableWidget.rowCount()  > 0 :

            self.tableWidget.removeRow(0)
        
        self.clients=self.dbconnect.get_all_clients()
        for rows,client in enumerate(self.clients):
            self.tableWidget.insertRow(rows)
                
            for col,data in enumerate(client[1:]):
                self.tableWidget.setItem(rows,col,QTableWidgetItem(str(data)))