from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm

class InvoiceReport:
    
    x=21*cm
    y=29.7*cm

    def __init__(self,file_name,items,invoice_info,total):
        self.x = InvoiceReport.x
        self.y = InvoiceReport.y
        self.file = file_name
        self.items = items
        self.invoice_info = invoice_info
        self.c=canvas.Canvas(self.file+".pdf",pagesize=A4,bottomup=0)
        self.c.translate(10,40)
        # Inverting the scale for getting mirror Image of logo
        self.c.scale(1,-1)
        # Inserting Logo into the Canvas at required position
        self.c.drawImage("logo.jpg",0,-1*cm,width=2.5*cm,height=2*cm)

        # Title Section
        # Again Inverting Scale For strings insertion
        self.c.scale(1,-1)
        # Again Setting the origin back to (0,0) of top-left
        self.c.translate(-10,-40)
        # Setting the font for Name title of company
        self.c.setFont("Helvetica-Bold",18)
        # Inserting the name of the company
        self.c.drawCentredString(0.5*self.x,2.5*cm,"XYZ PRIVATE LIMITED")

        # For under lining the title
        #c.line(70,22,180,22)
        self.c.line(1*cm,2.75*cm,20*cm,2.75*cm)
        # Changing the font size for Specifying Address
        self.c.setFont("Helvetica-Bold",10)
        self.c.drawCentredString(0.5*self.x,3.25*cm,"Block No. 101, Triveni Apartments, Pitam Pura,")
        self.c.drawCentredString(0.5*self.x,3.75*cm,"New Delhi - 110034, India")
        # Changing the font size for Specifying GST Number of firm
        self.c.setFont("Helvetica-Bold",12)
        self.c.drawCentredString(0.5*self.x,4.25*cm,"GSTIN : 07AABCS1429B1Z")
        # Line Seprating the page header from the body
        self.c.line(0.31*self.x,4.5*cm,0.7*self.x,4.5*cm)


        # Document Information
        # Changing the font for Document title
        self.c.setFont("Courier-Bold",14)
        self.c.drawCentredString(10.5*cm,5*cm,"TAX-INVOICE")
        # This Block Consist of Costumer Details
        self.c.roundRect(1*cm,5.5*cm,19*cm,3.25*cm,10,stroke=1,fill=0)

        self.c.setFont("Times-Bold",10)
        self.c.drawCentredString(0.5*self.x,6.25*cm,"INVOICE No. :")
        self.c.drawCentredString(0.5*self.x,7*cm,"DATE :")
        self.c.drawCentredString(0.5*self.x,7.75*cm,"CUSTOMER NAME :")
        self.c.drawCentredString(0.5*self.x,8.5*cm,"PHONE No. :")
        # # This Block Consist of Item Description
        #c.roundRect()
        self.c.rect(1*cm,9*cm,19*cm,13*cm,stroke=1,fill=0)
        self.c.line(1*cm,10*cm,20*cm,10*cm)
        self.c.drawCentredString(1.75*cm,9.6*cm," No.")
        self.c.drawCentredString(7*cm,9.6*cm,"GOODS DESCRIPTION")
        self.c.drawCentredString(14*cm,9.6*cm,"PRICE")
        self.c.drawCentredString(16*cm,9.6*cm,"QTY")
        self.c.drawCentredString(18.5*cm,9.6*cm,"TOTAL")
        self.c.drawCentredString(15*cm,22.6*cm,"SUB-TOTAL")
        self.c.drawCentredString(15*cm,23.6*cm,"TAV (17%)")
        self.c.drawCentredString(15*cm,24.6*cm,"TOTAL")
        self.c.drawCentredString(18.5*cm,22.6*cm,str(total[0]))
        self.c.drawCentredString(18.5*cm,23.6*cm,str(total[1]))
        self.c.drawCentredString(18.5*cm,24.6*cm,str(total[2]))

        # # Drawing table for Item Description
        self.c.line(2.5*cm,9*cm,2.5*cm,22*cm)
        self.c.line(13*cm,9*cm,13*cm,25*cm)
        self.c.line(15*cm,9*cm,15*cm,22*cm)
        self.c.line(17*cm,9*cm,17*cm,25*cm)
        self.c.line(20*cm,9*cm,20*cm,25*cm)
        #c.line(17*cm,9*cm,17*cm,25*cm)
        self.c.line(13*cm,25*cm,20*cm,25*cm)
        self.c.line(13*cm,24*cm,20*cm,24*cm)
        self.c.line(13*cm,23*cm,20*cm,23*cm)

        
        self.c.setFont("Times-Bold",14)
        xi=11
        item_number= 1
        for item in items:
            self.c.drawCentredString(1.75*cm,xi*cm,"0"+str(item_number))
            self.c.drawCentredString(4*cm,xi*cm,str(item[1]))
            self.c.drawCentredString(14*cm,xi*cm,str(item[2]))
            self.c.drawCentredString(16*cm,xi*cm,str(item[3]))
            self.c.drawCentredString(18.5*cm,xi*cm,str(item[4]))
            xi+=1
            item_number+=1
            
            
        
        
        self.c.setFont("Times-Bold",10)
        self.c.drawCentredString(15*cm,6.25*cm,invoice_info[0][0])
        self.c.drawCentredString(15*cm,7*cm,str(invoice_info[0][2]))
        self.c.drawCentredString(15*cm,7.75*cm,invoice_info[0][3])
        self.c.drawCentredString(15*cm,8.5*cm,invoice_info[0][5])   
            

        self.c.showPage()
            # Saving the PDF
        self.c.save()
    
    
        

