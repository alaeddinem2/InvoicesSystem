from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
# Creating Canvas
c = canvas.Canvas("invoice.pdf",pagesize=A4,bottomup=0)

x=21*cm
y=29.7*cm
# Logo Section
# Setting the origin to (10,40)
c.translate(10,40)
# Inverting the scale for getting mirror Image of logo
c.scale(1,-1)
# Inserting Logo into the Canvas at required position
c.drawImage("logo.jpg",0,-1*cm,width=2.5*cm,height=2*cm)

# Title Section
# Again Inverting Scale For strings insertion
c.scale(1,-1)
# Again Setting the origin back to (0,0) of top-left
c.translate(-10,-40)
# Setting the font for Name title of company
c.setFont("Helvetica-Bold",18)
# Inserting the name of the company
c.drawCentredString(0.5*x,2.5*cm,"XYZ PRIVATE LIMITED")

# For under lining the title
#c.line(70,22,180,22)
c.line(1*cm,2.75*cm,20*cm,2.75*cm)
# Changing the font size for Specifying Address
c.setFont("Helvetica-Bold",10)
c.drawCentredString(0.5*x,3.25*cm,"Block No. 101, Triveni Apartments, Pitam Pura,")
c.drawCentredString(0.5*x,3.75*cm,"New Delhi - 110034, India")
# Changing the font size for Specifying GST Number of firm
c.setFont("Helvetica-Bold",12)
c.drawCentredString(0.5*x,4.25*cm,"GSTIN : 07AABCS1429B1Z")
# Line Seprating the page header from the body
c.line(0.31*x,4.5*cm,0.7*x,4.5*cm)


# Document Information
# Changing the font for Document title
c.setFont("Courier-Bold",14)
c.drawCentredString(10.5*cm,5*cm,"TAX-INVOICE")
# This Block Consist of Costumer Details
c.roundRect(1*cm,5.5*cm,19*cm,3.25*cm,10,stroke=1,fill=0)

c.setFont("Times-Bold",10)
c.drawCentredString(0.5*x,6.25*cm,"INVOICE No. :")
c.drawCentredString(0.5*x,7*cm,"DATE :")
c.drawCentredString(0.5*x,7.75*cm,"CUSTOMER NAME :")
c.drawCentredString(0.5*x,8.5*cm,"PHONE No. :")
# # This Block Consist of Item Description
#c.roundRect()
c.rect(1*cm,9*cm,19*cm,13*cm,stroke=1,fill=0)
c.line(1*cm,10*cm,20*cm,10*cm)
c.drawCentredString(1.75*cm,9.6*cm,"SR No.")
c.drawCentredString(7*cm,9.6*cm,"GOODS DESCRIPTION")
c.drawCentredString(14*cm,9.6*cm,"PRICE")
c.drawCentredString(16*cm,9.6*cm,"QTY")
c.drawCentredString(18.5*cm,9.6*cm,"TOTAL")
c.drawCentredString(15*cm,22.6*cm,"SUB-TOTAL")
c.drawCentredString(15*cm,23.6*cm,"TAV (17%)")
c.drawCentredString(15*cm,24.6*cm,"TOTAL")
c.drawCentredString(18.5*cm,22.6*cm,"00.00")
c.drawCentredString(18.5*cm,23.6*cm,"00.00")
c.drawCentredString(18.5*cm,24.6*cm,"00.00")

# # Drawing table for Item Description
c.line(2.5*cm,9*cm,2.5*cm,22*cm)
c.line(13*cm,9*cm,13*cm,25*cm)
c.line(15*cm,9*cm,15*cm,22*cm)
c.line(17*cm,9*cm,17*cm,25*cm)
c.line(20*cm,9*cm,20*cm,25*cm)
#c.line(17*cm,9*cm,17*cm,25*cm)
c.line(13*cm,25*cm,20*cm,25*cm)
c.line(13*cm,24*cm,20*cm,24*cm)
c.line(13*cm,23*cm,20*cm,23*cm)

items=[("item1",200.00,5,100.00),("item2",250.00,3,750.00),("item1",300.00,6,1800.00)]
c.setFont("Times-Bold",14)
xi=11
item_number= 1
for item in items:
    c.drawCentredString(1.75*cm,xi*cm,"0"+str(item_number))
    c.drawRightString(4*cm,xi*cm,item[0])
    c.drawCentredString(14*cm,xi*cm,str(item[1]))
    c.drawCentredString(16*cm,xi*cm,str(item[2]))
    c.drawCentredString(18.5*cm,xi*cm,str(item[3]))
    xi+=1
    item_number+=1
# # End the Page and Start with new
c.showPage()
# Saving the PDF
c.save()


