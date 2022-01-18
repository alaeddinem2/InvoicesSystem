from PyQt5.QtGui import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui,QtCore
from PyQt5.sip import delete

from PyQt5.uic import loadUiType
import sys

from PyQt5.uic.properties import QtWidgets
from client_operations import clinetOperations



ui,_ = loadUiType('main.ui')

class Main(QMainWindow ,clinetOperations, ui):
    def __init__(self , parent=None):
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.handel_buttons()
        self.Hnadel_UI()
        self.get_clients()
    
    def Hnadel_UI(self):
        self.setWindowTitle("Incoices system")
        self.setFixedSize(853,561)
        self.setWindowIcon(QtGui.QIcon("printer.svg"))

    def handel_buttons(self):
        self.addClient.clicked.connect(self.send_data)
        self.load.clicked.connect(self.get_clients)
        self.removeClient.clicked.connect(self.del_client)
        self.upClient.clicked.connect(self.load_client_data)
        #self.tableWidget.itemSelectionChanged.connect(self.select_client)
        self.cancelButt.clicked.connect(self.cancel)
        
        
        
        
    


    
    

        
        


    
    
    

        





def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()