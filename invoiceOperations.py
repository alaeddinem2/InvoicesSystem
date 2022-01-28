from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from DbConnect import DBConnect
from InvoiceObj import Invoice ,InvoiceItem
from product_operations import productOPerations
from client_operations import clinetOperations

class incoiveOperations(productOPerations,clinetOperations,Invoice,InvoiceItem):
    invoices  = []
    invoice_id = 0
    invoice_items = []

    def __init__(self):
        self.dbconnect=DBConnect()
        
    def set_client_combobox(self):

        clients =[' ']
    
        for client in  self.clients :
            clients.append(client[1])
        self.clients_comboBox.addItems(clients)
        #self.clients_comboBox.setCurrentText(-1)
        #self.clients_comboBox.setPlaceholderText("--Choose One--")
        
         
        
    
    def get_client_id(self,name):

        for client in self.clients :
            if client[1] == name :
                return client[0]
    

    def set_product_combobox(self):
        self.product_combobox.clear()
        products =[' ']
        

        for product in self.products:
            products.append(product[1])

        self.product_combobox.addItems(products)
    
         
    
    def get_product_id(self,name):

        for product in self.products :
            if product[1] == name : 
                return product[0]
    
    
    
    def create_invoice(self):

        client_id = self.get_client_id(self.clients_comboBox.currentText())
        code = self.invoiceCode.text()
        
        if code == '':
            QMessageBox.warning(self,'warning',"please generate the code !")
        else :
            if self.invoiceStatus.isChecked():
                status = True
            else:
                status = False

            invoice = Invoice(code,client_id,status)
            msg = self.dbconnect.add_Invoice(invoice)
            QMessageBox.information(self,"secces",msg[0])
            self.code = self.invoice_textBrowser.setText(str(code))
            self.invoice_id =msg[1]
            self.set_invoive_compobox()
            self.display_invoice_info(self.invoice_id)
            self.invoiceCode.clear()
            
        
        return self.invoice_id

    def generate_code(self)-> str:
        client = self.clients_comboBox.currentText()
        invoice = self.invoices
        if client == ' ':
            QMessageBox.warning(self,'warning',"please select a client !")
        else :
            code="INV-" + str(client[:3].upper()) +"-00" + str(len(invoice)+1)
            self.invoiceCode.setText(code)
            self.clients_comboBox.setCurrentText(code)
        

    def display_invoice_info(self,id):
        invoice_info = self.dbconnect.get_invoice_info(id)
        self.clientLabel.setText(invoice_info[0][3])
        self.phoneLabel.setText(invoice_info[0][5])
        self.addressLabel.setText(invoice_info[0][6])
        

    

    def set_invoive_compobox(self):
        invoice_id =[]
        invoice_code = []
        self.invoices = self.dbconnect.get_all_invoices()
        for invoice in self.invoices:
            invoice_id.append(invoice[0])
            invoice_code.append(invoice[2])

        self.invoice_display_combobox.addItems(invoice_code)
        
        self.invoice_display_combobox.setCurrentText(invoice_code[-1])
        
    def get_invoice_id(self,code):
        for invoice in self.invoices :
            if invoice[2] == code :
                return invoice[0]


    def create_item(self):
        product_id = self.get_product_id(self.product_combobox.currentText())
        product_name = self.product_combobox.currentText()
        quantity = self.itemQuantity.value()
        invoice_id = self.get_invoice_id(self.invoice_display_combobox.currentText())
        res = self.is_item_exist(product_name)
                
        if res != None:
            quantity+= res[1]
            self.dbconnect.update_item(quantity,res[0])
            self.display_items()
            
        else:
            item = InvoiceItem(product_id,invoice_id,quantity)
            item_msg = self.dbconnect.add_item(item)
            QMessageBox.information(self,"secces",item_msg)
            self.display_items()
        
        self.display_total()
        

    def display_items(self):

        invoice_id = self.get_invoice_id(self.invoice_display_combobox.currentText())      
        self.invoice_items = self.dbconnect.get_invoice_items(invoice_id)
        self.invoice_textBrowser.setText(str(self.invoice_display_combobox.currentText()))
        self.display_invoice_info(invoice_id)
        self.display_total()
        print(self.invoice_items)

        while self.invoiceItemsTable.rowCount() > 0 :
            self.invoiceItemsTable.removeRow(0)        
        
        
        for rows,item in enumerate(self.invoice_items):
            self.invoiceItemsTable.insertRow(rows)
                
            for col,data in enumerate(item[1:]):
                self.invoiceItemsTable.setItem(rows,col,QTableWidgetItem(str(data)))


    def is_item_exist(self,productName):
        
        for item in self.invoice_items :
            if item[1] == productName :
                 return item[0], item[3]
        
        return

    def display_total(self):
        total = self.dbconnect.total(self.invoice_items)
        self.subTotal.display(total[0])
        self.TAV.display(total[1])
        self.Total.display(total[2])

         
