from PyQt5.QtGui import *

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui,QtCore
from PyQt5.sip import delete

from PyQt5.uic import loadUiType
import sys

from PyQt5.uic.properties import QtWidgets
from client_operations import clinetOperations
from invoiceOperations import incoiveOperations



ui,_ = loadUiType('main.ui')

class Main(QMainWindow ,incoiveOperations, ui):
    def __init__(self , parent=None):
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.client_buttons()
        self.product_buttons()
        self.Hnadel_UI()
        self.get_clients()
        self.get_products()
        self.set_product_combobox()
        self.invoice_buttons()
        self.set_invoive_compobox()
        #self.display_items()
        self.set_product_combobox()
        self.set_client_combobox()
        
    
    def Hnadel_UI(self):
        self.setWindowTitle("Incoices system")
        self.setFixedSize(853,561)
        self.setWindowIcon(QtGui.QIcon("printer.svg"))

    def client_buttons(self):
        ''' clients buttons'''

        self.sendClientData.clicked.connect(self.send_client_data)
        self.load.clicked.connect(self.get_clients)
        self.removeClient.clicked.connect(self.del_client)
        self.upClient.clicked.connect(self.load_client_data)
        #self.tableWidget.itemSelectionChanged.connect(self.select_client)
        self.cancelButt.clicked.connect(self.cancel)
    

    def product_buttons(self):
        '''products buttons'''

        self.sendProductData.clicked.connect(self.send_product_data)
        self.loadProducts.clicked.connect(self.get_products)
        self.removeProduct.clicked.connect(self.del_product)
        self.upProduct.clicked.connect(self.load_product_data)

    def invoice_buttons(self):
        self.generateCode.clicked.connect(self.generate_code)
        self.sendInvoiceData.clicked.connect(self.create_invoice)
        self.sendItemData.clicked.connect(self.create_item)
        self.loadItems.clicked.connect(self.display_items)
        
        
    # def enterEvent(self, event):
 
    #     # setting to the text to the label
        
    #     self.set_product_combobox()

    

        

    
    
        
        
        
        
    


    
    

        
        


    
    
    

        





def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()