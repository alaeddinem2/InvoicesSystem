from PyQt5.QtGui import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui,QtCore

from PyQt5.uic import loadUiType
import sys

from PyQt5.uic.properties import QtWidgets
from DbConnect import DBConnect
from InvoiceObj import Client,Product,Invoice,InvoiceItem

from InvoiceReport import InvoiceReport


ui,_ = loadUiType('main.ui')

class Main(QMainWindow ,DBConnect,Client, ui):
    def __init__(self , parent=None):
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        #self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow())
        self.dbconnect=DBConnect()
        self.handel_buttons()
        self.Hnadel_UI()
        self.get_clients()
    
    def Hnadel_UI(self):
        self.setWindowTitle("Incoices system")
        self.setFixedSize(853,561)
        self.setWindowIcon(QtGui.QIcon("printer.svg"))

    def handel_buttons(self):
        self.addClient.clicked.connect(self.add_client)
        self.load.clicked.connect(self.get_all_clients)
        self.tableWidget.currentItemChanged.connect(self.select_changed)
        
        
    


    def add_client(self):
        
        name=self.clientName.text()
        phone=self.clientPhone.text()
        email= self.clientEmail.text()
        address=self.clientAddress.text()
        if name.strip(" ") and phone.strip(" ")  and email.strip(" ")  and address.strip(" ") !="":
            client=Client(name,phone,email,address)
            self.dbconnect.add_client(client)
        else:
             QMessageBox.warning(self,"Warning","please enter all fields! ")

        self.clientName.clear()
        self.clientPhone.clear()
        self.clientEmail.clear()
        self.clientAddress.clear()
    
    def get_clients(self):
        clients=self.dbconnect.get_all_clients()
        for rows,client in enumerate(clients):
            self.tableWidget.insertRow(rows)
            
            for col,data in enumerate(client[1:]):
                self.tableWidget.setItem(rows,col,QTableWidgetItem(str(data)))


    def select_changed(self):
        value = self.tableWidget.currentRow()
        values =self.tableWidget.item(value,1).text()
        print(values)

        





def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()