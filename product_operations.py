from itertools import product
from tabnanny import check
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from DbConnect import DBConnect
from InvoiceObj import Product
from client_operations import clinetOperations


class productOPerations(DBConnect,Product):

    '''all product operations such create delete get update '''
    products = []
    check = False
    
    def __init__(self):
        self.dbconnect=DBConnect()
    

    def create_product(self):
        ''' preparing the Client creation by creating the Client object before send it to database  '''
         
        name=self.productName.text()
        price=self.productPrice.text()
        #quantity= self.productQuantity.text()
        #sellPrice=self.productSellPrice.text()

        if (name.strip(" ")  or price.strip(" ")) == "":

                QMessageBox.warning(self,"Warning","please enter all fields! ")
   
        else :
            product=Product(name,price)
            product=self.dbconnect.add_product(product)
            self.clear_line_text_product()
            QMessageBox.information(self,"secces",product)
            self.get_products()



    def get_products(self):
        '''get all products'''

        while self.productTable.rowCount() > 0 :
            self.productTable.removeRow(0)        
        
        self.products=self.dbconnect.get_all_products()
        for rows,product in enumerate(self.products):
            self.productTable.insertRow(rows)
                
            for col,data in enumerate(product[1:]):
                self.productTable.setItem(rows,col,QTableWidgetItem(str(data)))

    def del_product(self):
        if self.warning_message("Delete Product","are you sure that you want to delete Product ?!") is True:
            try: 
                
                data_del = self.select_product()
                print(data_del)    
                id = self.get_product_id(data_del[0])
                
                msg = self.dbconnect.remove_product(id)
                QMessageBox.information(self,"succes",msg)
                self.get_products()
            except:
                    QMessageBox.information(self,"info","please select product !")

    def select_product(self):
        ''' get data from table when we want to udpate or delete a client'''

        name = self.productTable.item(self.productTable.currentRow(),0).text()            
        price = self.productTable.item(self.productTable.currentRow(),1).text()
        #quantity = self.productTable.item(self.clientTable.currentRow(),2).text()
        #sell_price = self.productTable.item(self.clientTable.currentRow(),3).text()
        return name,price

    def get_product_id(self,name)-> int :
        ''' returned the  client id by passing email address '''

        self.products
        for product in self.products:
            if product[1] == name:
                return product[0]

    def clear_line_text_product(self):
        '''clear liens text'''

        self.productName.clear()
        self.productPrice.clear()
        #self.productQuantity.clear()
        #self.productSellPrice.clear()
    
    def load_product_data (self)-> bool :
         '''load data on lines text '''

         if self.warning_message("Update Client","are you sure that you want to Update client ?!") is True:
            try:
                data = self.select_product()
                self.productName.setText(data[0])
                self.productPrice.setText(data[1])
                #self.productQuantity.setText(data[2])
                #self.productSellPrice.setText(data[3])
                self.check = True
                print(self.check)
                return self.check
            except:
                QMessageBox.information(self,"info","please select an user !")

    
    def updateProduct(self):
        '''update the product information'''

        name=self.productName.text()
        price=self.productPrice.text()

        data = self.select_product()
        id = self.get_product_id(data[0])

        upload_product=Product(name,price)
        result = self.dbconnect.update_product(upload_product,id)

        QMessageBox.information(self,"succes",result)
        self.clear_line_text_product()
        self.get_products()
    

    def send_product_data(self):
        '''send database request to add or update Client  '''
        
        if self.check == True :
            self.updateProduct()
            self.check = False  
        else :
            self.create_product()
        
            

    