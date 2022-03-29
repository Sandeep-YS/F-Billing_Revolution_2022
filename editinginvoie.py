from cgitb import text
from distutils import command
from itertools import count
from pydoc import describe
from select import select
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.tix import Select
from PIL import ImageTk, Image
from numpy import empty
import pandas as pd
from tkinter.messagebox import showinfo
import tkinter.scrolledtext as scrolledtext
from tkinter.filedialog import askopenfilename
import os, sys
# from win32 import win32print
# import win32api
##############################################################
import tkinter as tk
##############################################################
from errno import E2BIG
import webbrowser
from tkcalendar import Calendar
from tkcalendar import DateEntry
import tkcalendar
import pandas
from datetime import timedelta
from datetime import date
import datetime
from tkinter import filedialog
import subprocess
import mysql.connector
import io
import smtplib
from textmagic.rest import TextmagicRestClient
import pdfkit
import base64
import os
from datetime import datetime
from PyPDF2 import PdfFileWriter, PdfFileReader
# from models import *
fbilldb = mysql.connector.connect(
  host="localhost", user="root", password="", database=" fbillingsintgrtd", port="3306"
 )
fbcursor = fbilldb.cursor()
def reset():
  global root
  root.destroy()

root=Tk()
root.geometry("1360x730")
root.resizable(False, False)
root.title("F-Billing Revolution 2022(FREE version) | Company database:fbillingdb | User:Administrator")
p1 = PhotoImage(file = 'images/fbicon.png')
root.iconphoto(False, p1)


s = ttk.Style()
s.theme_use('default')
s.configure('TNotebook.Tab', background="#999999", width=20, padding=10)
invoices= PhotoImage(file="images/invoice.png")
orders = PhotoImage(file="images/order.png")
estimates = PhotoImage(file="images/estimate.png")
recurring = PhotoImage(file="images/recurring.png")
purchase = PhotoImage(file="images/purchase.png")
expenses = PhotoImage(file="images/expense.png")
customer = PhotoImage(file="images/customer.png")
product = PhotoImage(file="images/package.png")
reports = PhotoImage(file="images/report.png")
setting = PhotoImage(file="images/setting.png")
tick = PhotoImage(file="images/check.png")
warnin = PhotoImage(file="images/sign_warning.png")
cancel = PhotoImage(file="images/close.png")
saves = PhotoImage(file="images/save.png")
folder = PhotoImage(file="images/folder-black.png")
photo11 = PhotoImage(file = "images/invoice-pvt.png")
customer = PhotoImage(file="images/customer.png")
smslog = PhotoImage(file = "images/smslog.png")
video = PhotoImage(file = "images/video.png")
mark1 = PhotoImage(file="images/mark.png")
mark2 = PhotoImage(file="images/mark2.png")
photo10 = PhotoImage(file = "images/text-message.png")
addnew = PhotoImage(file="images/plus.png")
delete = PhotoImage(file="images/delete_E.png")
tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3=  ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)
tab5 = ttk.Frame(tabControl)
tab6=  ttk.Frame(tabControl)
tab7 = ttk.Frame(tabControl)
tab8 = ttk.Frame(tabControl)
tab9 =  ttk.Frame(tabControl)
tab10=  ttk.Frame(tabControl)
tabControl.add(tab1,image=invoices,compound = LEFT, text ='Invoices',)
tabControl.add(tab2,image=orders,compound = LEFT, text ='Orders')
tabControl.add(tab3,image=estimates,compound = LEFT, text ='Estimates')
tabControl.add(tab4,image=recurring,compound = LEFT, text ='Recurring')
tabControl.add(tab5,image=purchase,compound = LEFT, text ='Purchase Orders') 
tabControl.add(tab6,image=expenses,compound = LEFT, text ='Expenses')
tabControl.add(tab7,image=customer,compound = LEFT, text ='Customers')
tabControl.add(tab8,image=product,compound = LEFT, text ='Product/Services')
tabControl.add(tab9,image=reports,compound = LEFT, text ='Report')
tabControl.add(tab10,image=setting,compound = LEFT, text ='Settings')
tabControl.pack(expand = 1, fill ="both")


selectall = PhotoImage(file="images/table_select_all.png")
cut = PhotoImage(file="images/cut.png")
copy = PhotoImage(file="images/copy.png")
paste = PhotoImage(file="images/paste.png")

undo = PhotoImage(file="images/undo.png")
redo = PhotoImage(file="images/redo.png")
bold = PhotoImage(file="images/bold.png")

italics = PhotoImage(file="images/italics.png")
underline = PhotoImage(file="images/underline.png")
left = PhotoImage(file="images/left.png")

right = PhotoImage(file="images/right.png")
center = PhotoImage(file="images/center.png")
hyperlink = PhotoImage(file="images/hyperlink.png")
remove = PhotoImage(file="images/eraser.png")


photo = PhotoImage(file = "images/plus.png")
photo1 = PhotoImage(file = "images/edit.png")
photo2 = PhotoImage(file = "images/delete_E.png")
photo3 = PhotoImage(file = "images/export-file.png")
photo4 = PhotoImage(file = "images/seo.png")
photo5 = PhotoImage(file = "images/printer.png")
photo6 = PhotoImage(file = "images/gmail.png")
photo7 = PhotoImage(file = "images/priewok.png")
photo8 = PhotoImage(file = "images/refresh_E.png")
photo9 = PhotoImage(file = "images/sum.png")
photo10 = PhotoImage(file = "images/text-message.png")



####################################### TAB1 INVOICE SANDEEP ############################################

#create new invoice

def createmaininvoice():
  pop=Toplevel(midFrame)
  pop.title("Invoice")
  pop.geometry("950x690+150+0")


  #select customer
 

  def selectcustomer():
    global custselection

    custselection=Toplevel()
    custselection.title("Select Customer")
    custselection.geometry("930x650+240+10")
    custselection.resizable(False, False)
  


    #add new customer
    def createcustomer():
      global checkvar1,checkvar2,custid,bname,baddress,cat,sname,saddress,contp,cemail,ctel,cfax,cmob,scontp,scemail,sctel,scfax,ccountry,ccity,cnotes
      ven=Toplevel(midFrame)
      ven.title("Add new vendor")
      ven.geometry("930x650+240+10")
      checkvar1=IntVar()
      checkvar2=IntVar()
      radio=IntVar()
      createFrame=Frame(ven, bg="#f5f3f2", height=650)
      createFrame.pack(side="top", fill="both")
      labelframe1 = LabelFrame(createFrame,text="Customer",bg="#f5f3f2",font=("arial",15))
      labelframe1.place(x=10,y=5,width=910,height=600)
      text1=Label(labelframe1, text="Customer ID:",bg="#f5f3f2",fg="blue").place(x=5 ,y=10)
      custid=Entry(labelframe1,width=25)
      custid.place(x=150,y=10)
      text2=Label(labelframe1, text="Category:",bg="#f5f3f2").place(x=390 ,y=10)
      cat=ttk.Combobox(labelframe1,width=25,value="Default")
      cat.place(x=460 ,y=10)
      text3=Label(labelframe1, text="Status:",bg="#f5f3f2").place(x=710 ,y=10)
      Checkbutton(labelframe1,text="Active",variable=checkvar1,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=760 ,y=10)
      
      labelframe2 = LabelFrame(labelframe1,text="Invoice to (appears on invoices)",bg="#f5f3f2")
      labelframe2.place(x=5,y=40,width=420,height=150)
      name = Label(labelframe2, text="Ship to name:",bg="#f5f3f2",fg="blue").place(x=5,y=5)
      sname = Entry(labelframe2,width=28)
      sname.place(x=130,y=5)
      addr = Label(labelframe2, text="Address:",bg="#f5f3f2",fg="blue").place(x=5,y=40)
      saddress = Entry(labelframe2,width=28)
      saddress.place(x=130,y=40,height=80)
      
      btn1=Button(labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=440, y=90)

      labelframe3 = LabelFrame(labelframe1,text="Ship to (appears on invoices)",bg="#f5f3f2")
      labelframe3.place(x=480,y=40,width=420,height=150)
      name = Label(labelframe3, text="Business name:",bg="#f5f3f2").place(x=5,y=5)
      bname = Entry(labelframe3,width=28)
      bname.place(x=130,y=5)
      addr = Label(labelframe3, text="Address:",bg="#f5f3f2").place(x=5,y=40)
      baddress = Entry(labelframe3,width=28)
      baddress.place(x=130,y=40,height=80)
      
      labelframe4 = LabelFrame(labelframe1,text="Contact",bg="#f5f3f2")
      labelframe4.place(x=5,y=195,width=420,height=150)
      name = Label(labelframe4, text="Contact person:",bg="#f5f3f2").place(x=5,y=5)
      contp = Entry(labelframe4,width=28)
      contp.place(x=130,y=5)
      email = Label(labelframe4, text="E-mail address:",bg="#f5f3f2",fg="blue").place(x=5,y=35)
      cemail = Entry(labelframe4,width=28)
      cemail.place(x=130,y=35)
      tel = Label(labelframe4, text="Tel.number:",bg="#f5f3f2").place(x=5,y=65)
      ctel = Entry(labelframe4,width=11)
      ctel.place(x=130,y=65)
      fax = Label(labelframe4, text="Fax:",bg="#f5f3f2").place(x=240,y=65)
      cfax = Entry(labelframe4,width=11)
      cfax.place(x=280,y=65)
      sms = Label(labelframe4, text="Mobile number for SMS notifications:",bg="#f5f3f2").place(x=5,y=95)
      cmob = Entry(labelframe4,width=15)
      cmob.place(x=248,y=95)      

      btn1=Button(labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=440, y=250)

      
      labelframe5 = LabelFrame(labelframe1,text="Ship to contact",bg="#f5f3f2")
      labelframe5.place(x=480,y=195,width=420,height=125)
      name = Label(labelframe5, text="Contact person:",bg="#f5f3f2").place(x=5,y=5)
      scontp = Entry(labelframe5,width=28)
      scontp.place(x=130,y=5)
      email = Label(labelframe5, text="E-mail address:",bg="#f5f3f2").place(x=5,y=35)
      scemail = Entry(labelframe5,width=28)
      scemail.place(x=130,y=35)
      tel = Label(labelframe5, text="Tel.number:",bg="#f5f3f2").place(x=5,y=65)
      sctel = Entry(labelframe5,width=11)
      sctel.place(x=130,y=65)
      fax = Label(labelframe5, text="Fax:",bg="#f5f3f2").place(x=240,y=65)
      scfax = Entry(labelframe5,width=11)
      scfax.place(x=280,y=65)

      labelframe6 = LabelFrame(labelframe1,text="Contact",bg="#f5f3f2")
      labelframe6.place(x=5,y=350,width=420,height=100)
      Checkbutton(labelframe6,text="Tax Exempt",variable=checkvar2,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=5 ,y=5)
      tax = Label(labelframe6, text="Specific Tax1 %:",bg="#f5f3f2").place(x=180,y=5)
      e1 = Entry(labelframe6,width=10).place(x=290,y=5)
      discount = Label(labelframe6, text="Discount%:",bg="#f5f3f2").place(x=5,y=35)
      e2 = Entry(labelframe6,width=10).place(x=100,y=35)

      labelframe7 = LabelFrame(labelframe1,text="Contact",bg="#f5f3f2")
      labelframe7.place(x=480,y=330,width=420,height=100)
      country = Label(labelframe7, text="country:",bg="#f5f3f2").place(x=5,y=5)
      ccountry = Entry(labelframe7,width=28)
      ccountry.place(x=130,y=5)
      city = Label(labelframe7, text="City:",bg="#f5f3f2").place(x=5,y=35)
      ccity = Entry(labelframe7,width=28)
      ccity.place(x=130,y=35)

      labelframe8 = LabelFrame(labelframe1,text="Customer Type",bg="#f5f3f2")
      labelframe8.place(x=5,y=460,width=420,height=100)
      R1=Radiobutton(labelframe8,text=" Client ",variable=radio,value=1,bg="#f5f3f2").place(x=5,y=15)
      R2=Radiobutton(labelframe8,text=" Vendor ",variable=radio,value=2,bg="#f5f3f2").place(x=150,y=15)
      R3=Radiobutton(labelframe8,text=" Both(client/vendor)",variable=radio,value=3,bg="#f5f3f2").place(x=250,y=15)
      

      labelframe9 = LabelFrame(labelframe1,text="Notes",bg="#f5f3f2")
      labelframe9.place(x=480,y=430,width=420,height=150)
      cnotes = Entry(labelframe9)
      cnotes.place(x=10,y=10,height=100,width=390)

      btn1=Button(ven,width=60,height=10,bg="#f5f3f2",compound = LEFT,image=tick ,text="OK",command=ord_cust_reg).place(x=20, y=615)
      btn2=Button(ven,width=60,height=10,bg="#f5f3f2",compound = LEFT,image=cancel,text="Cancel").place(x=800, y=615)




    
               

    # enter=Label(custselection, text="Enter filter text").place(x=5, y=10)
    # e1=Entry(custselection, width=20).place(x=110, y=10)
    # text=Label(custselection, text="Filtered column").place(x=340, y=10)
    # e2=Entry(custselection, width=20).place(x=450, y=10)
    
    global selectcusttree;

    selectcusttree=ttk.Treeview(custselection, height=27)
    selectcusttree["columns"]=["1","2","3","4"]
    selectcusttree.column("#0", width=35)
    selectcusttree.column("1", width=160)
    selectcusttree.column("2", width=160)
    selectcusttree.column("3", width=140)
    selectcusttree.column("4", width=140)
    selectcusttree.heading("#0",text="")
    selectcusttree.heading("1",text="Customer/Ventor ID")
    selectcusttree.heading("2",text="Customer/Ventor Name")
    selectcusttree.heading("3",text="Tel.")
    selectcusttree.heading("4",text="Contact Person")
    selectcusttree.place(x=5, y=45)

    def filter_cust():
      # global filttxt 
  
      filtr = filttxt.get()
      for record in selectcusttree.get_children():
        selectcusttree.delete(record)

      sqlcusven = "SELECT * FROM Customer WHERE businessname=%s"
      valcusven = (filtr, )
      fbcursor.execute(sqlcusven, valcusven)
      records = fbcursor.fetchall()
      print(records)

  
      count=0
      for i in records:
        if True:
         selectcusttree.insert(parent='', index='end', iid=i, text='', values=(i[0],i[4],i[10],i[8]))  
        else:
          pass
      count += 1

    # global filttxt
    enter=Label(custselection, text="Enter filter text").place(x=5, y=10)
    filttxt=Entry(custselection, width=20)
    filttxt.place(x=110, y=10)
    fltrbutton=Button(custselection,text = 'Click Here',command=filter_cust)
    fltrbutton.place(x=236,y=7,height=25,width=70)


    # def prodtreefetch():
    #  itemid = selectcusttree.item(selectcusttree.focus())["values"][1]
    #  sql = "select * from Customer where customerid = %s"
    #  val = (itemid, )
    #  fbcursor.execute(sql, val)
    #  global slctcstr
    #  slctcstr = fbcursor.fetchone()
    #  e1.delete(0,'end')
    #  e1.insert(0, slctcstr[4])

    def cancelcustomselection():
      custselection.destroy()

 
    
    fbcursor.execute('SELECT * FROM Customer;') 
    j = 0
    for i in fbcursor:
      selectcusttree.insert(parent='', index='end', iid=i, text='', values=(i[0],i[4],i[10],i[8]))
      j += 1


    categtree=ttk.Treeview(custselection, height=27)
    categtree["columns"]=["1"]
    categtree.column("#0", width=35, minwidth=20)
    categtree.column("1", width=205, minwidth=25, anchor=CENTER)    
    categtree.heading("#0",text="", anchor=W)
    categtree.heading("1",text="View filter by category", anchor=CENTER)
    categtree.place(x=660, y=45)

    listbox = Listbox(custselection,height = 33,  
              width = 40,  
              bg = "white",
              activestyle = 'dotbox',  
              fg = "black",
              highlightbackground="white")
    
    listbox.insert(0, "                               View all records")
    listbox.insert(1, "                               View all products")
    listbox.insert(2, "                               View all services")
    listbox.place(x=660,y=65,)
    listbox.bind('<<ListboxSelect>>')

    # scrollbar = Scrollbar(custselection)
    # scrollbar.place(x=640, y=45, height=560)
    # scrollbar.config( command=tree.yview )

    scrollbar = Scrollbar(custselection)
    scrollbar.place(x=1016+300+25, y=120, height=280+20)

    btn1=Button(custselection,compound = LEFT,image=tick ,text="ok", width=60,command=prodtreefetch).place(x=15, y=610)
    btn1=Button(custselection,compound = LEFT,image=tick,text="Edit selected customer", width=150,command=createcustomer).place(x=250, y=610)
    btn1=Button(custselection,compound = LEFT,image=tick, text="Add new customer", width=150,command=createcustomer).place(x=435, y=610)
    btn1=Button(custselection,compound = LEFT,image=cancel ,text="Cancel",command= cancelcustomselection,width=60).place(x=740, y=610)   



    

  #add new line item
  def addnewline():

    try:
      if not cmb.get():
        messagebox.showerror('F-Billing Revolution', 'Add a customer before adding new line.') 
      else:
        newselection=Toplevel()
        newselection.title("Select Product")
        newselection.geometry("930x650+240+10")
        newselection.resizable(False, False)


        #add new product
        def add_product():  
          global codeentry,nameentry,country,desentry,unitentry,pcsentry,costentry,priceentry,stockentry,lowentry,wareentry,txt,checkvarStatus,checkvarStatus2,checkvarStatus3
          top = Toplevel()  
          top.title("Add a new Product/Service")
          p2 = PhotoImage(file = 'images/fbicon.png')
          top.iconphoto(False, p2)

          top.geometry("700x550+390+15")
          tabControl = ttk.Notebook(top)
          s = ttk.Style()
          s.theme_use('default')
          s.configure('TNotebook.Tab', background="#999999",padding=10,bd=0)


          tab1 = ttk.Frame(tabControl)
          tab2 = ttk.Frame(tabControl)

          tabControl.add(tab1,compound = LEFT, text ='Product/Service')
          tabControl.add(tab2,compound = LEFT, text ='Product Image')

          tabControl.pack(expand = 1, fill ="both")

          innerFrame = Frame(tab1,bg="#f5f3f2", relief=GROOVE)
          innerFrame.pack(side="top",fill=BOTH)

          Customerlabelframe = LabelFrame(innerFrame,text="Product/Service",width=580,height=485)
          Customerlabelframe.pack(side="top",fill=BOTH,padx=10)

          code1=Label(Customerlabelframe,text="Code or SKU:",fg="blue",pady=10,padx=10)
          code1.place(x=20,y=0)
          codeentry = Entry(Customerlabelframe,width=35)
          codeentry.place(x=120,y=8)

          checkvarStatus=IntVar()
          status1=Label(Customerlabelframe,text="Status:")
          status1.place(x=500,y=8)
          Button1 = Checkbutton(Customerlabelframe,
                            variable = checkvarStatus,text="Active",compound="right",
                            onvalue =0 ,
                            offvalue = 1,

                            width = 10)

          Button1.place(x=550,y=5)

          category1=Label(Customerlabelframe,text="Category:",pady=5,padx=10)
          category1.place(x=20,y=40)
          n = StringVar()
          country = ttk.Combobox(Customerlabelframe, width = 40, textvariable = n )

          country['values'] = ('Default',' India',' China',' Australia',' Nigeria',' Malaysia',' Italy',' Turkey',)

          country.place(x=120,y=45)
          country.current(0)


          name1=Label(Customerlabelframe,text="Name :",fg="blue",pady=5,padx=10)
          name1.place(x=20,y=70)
          nameentry = Entry(Customerlabelframe,width=60)
          nameentry.place(x=120,y=75)

          des1=Label(Customerlabelframe,text="Description :",pady=5,padx=10)
          des1.place(x=20,y=100)
          desentry = Entry(Customerlabelframe,width=60)
          desentry.place(x=120,y=105)

          uval = IntVar(Customerlabelframe, value='$0.00')
          unit1=Label(Customerlabelframe,text="Unit Price:",fg="blue",pady=5,padx=10)
          unit1.place(x=20,y=130)
          unitentry = Entry(Customerlabelframe,width=20,textvariable=uval)
          unitentry.place(x=120,y=135)

          pcsval = IntVar(Customerlabelframe, value='0')
          pcs1=Label(Customerlabelframe,text="Pcs/Weight:",fg="blue",pady=5,padx=10)
          pcs1.place(x=320,y=140)
          pcsentry = Entry(Customerlabelframe,width=20,textvariable=pcsval)
          pcsentry.place(x=410,y=140)

          costval = IntVar(Customerlabelframe, value='$0.00')
          cost1=Label(Customerlabelframe,text="Cost:",pady=5,padx=10)
          cost1.place(x=20,y=160)
          costentry = Entry(Customerlabelframe,width=20,textvariable=costval)
          costentry.place(x=120,y=165)

          priceval = IntVar(Customerlabelframe, value='$0.00')
          price1=Label(Customerlabelframe,text="(Price-Cost):",pady=5,padx=10)
          price1.place(x=20,y=190)
          priceentry = Entry(Customerlabelframe,width=20,textvariable=priceval)
          priceentry.place(x=120,y=195)

          checkvarStatus2=IntVar()

          Button2 = Checkbutton(Customerlabelframe,variable = checkvarStatus2,
                            text="Taxable Tax1rate",compound="right",
                            onvalue =0 ,
                            offvalue = 1,
                            height=2,
                            width = 12)

          Button2.place(x=415,y=170)


          checkvarStatus3=IntVar()

          Button3 = Checkbutton(Customerlabelframe,variable = checkvarStatus3,
                            text="No stock Control",
                            onvalue =1 ,
                            offvalue = 0,
                            height=3,
                            width = 15)

          Button3.place(x=40,y=220)


          stockval = IntVar(Customerlabelframe)
          stock1=Label(Customerlabelframe,text="Stock:",pady=5,padx=10)
          stock1.place(x=90,y=260)
          stockentry = Entry(Customerlabelframe,width=15,textvariable=stockval)
          stockentry.place(x=150,y=265)

          lowval = IntVar(Customerlabelframe)
          low1=Label(Customerlabelframe,text="Low Stock Warning Limit:",pady=5,padx=10)
          low1.place(x=300,y=260)
          lowentry = Entry(Customerlabelframe,width=10,textvariable=lowval)
          lowentry.place(x=495,y=265)


          ware1=Label(Customerlabelframe,text="Warehouse:",pady=5,padx=10)
          ware1.place(x=60,y=290)
          wareentry = Entry(Customerlabelframe,width=50)
          wareentry.place(x=150,y=295)

          text1=Label(Customerlabelframe,text="Private notes(not appears on invoice):",pady=5,padx=10)
          text1.place(x=20,y=330)

          txt = scrolledtext.ScrolledText(Customerlabelframe, undo=True,width=72,height=4)
          txt.place(x=32,y=358)




          okButton = Button(innerFrame,compound = LEFT,image=tick , text ="Ok",command=ord_prdt_reg,width=60)
          okButton.pack(side=LEFT)

          cancelButton = Button(innerFrame,compound = LEFT,image=cancel ,text="Cancel",width=60)
          cancelButton.pack(side=RIGHT)

          imageFrame = Frame(tab2, relief=GROOVE,height=580)
          imageFrame.pack(side="top",fill=BOTH)

          browseimg=Label(imageFrame,text=" Browse for product image file(recommended image type:JPG,size 480x320 pixels) ",bg='#f5f3f2')
          browseimg.place(x=15,y=35)

          browsebutton=Button(imageFrame,text = 'Browse')
          browsebutton.place(x=580,y=30,height=30,width=50)

          removeButton = Button(imageFrame,compound = LEFT,image=cancel, text ="Remove Product Image",width=150)
          removeButton.place(x=400,y=450)





        # enter=Label(newselection, text="Enter filter text").place(x=5, y=10)
        # e1=Entry(newselection, width=20).place(x=110, y=10)
        # text=Label(newselection, text="Filtered column").place(x=340, y=10)
        # e2=Entry(newselection, width=20).place(x=450, y=10)

        addprodtree=ttk.Treeview(newselection, height=27)
        addprodtree["columns"]=["1","2","3", "4","5"]
        addprodtree.column("#0", width=35)
        addprodtree.column("1", width=160)
        addprodtree.column("2", width=160)
        addprodtree.column("3", width=140)
        addprodtree.column("4", width=70)
        addprodtree.column("5", width=70)
        addprodtree.heading("#0",text="")
        addprodtree.heading("1",text="ID/SKU")
        addprodtree.heading("2",text="Product/Service Name")
        addprodtree.heading("3",text="Unit price")
        addprodtree.heading("4",text="Service")
        addprodtree.heading("5",text="Stock")
        addprodtree.place(x=5, y=45)

        def filter_prod():
        # global filttxt 
     
         filtr = filttxt.get()
         for record in addprodtree.get_children():
           addprodtree.delete(record)
    
         sqlcusven = "SELECT * FROM Productservice WHERE name=%s"
         valcusven = (filtr, )
         fbcursor.execute(sqlcusven, valcusven)
         records = fbcursor.fetchall()
         print(records)
  
    
         count=0
         for i in records:
           if True:
            addprodtree.insert(parent='', index='end', iid=i, text='', values=(i[0],i[4],i[10],i[8]))  
           else:
             pass
         count += 1
  
    #   global filttxt
        enter=Label(newselection, text="Enter filter text").place(x=5, y=10)
        filttxt=Entry(newselection, width=20)
        filttxt.place(x=110, y=10)
        fltrbutton=Button(newselection,text = 'Click Here',command=filter_prod)
        fltrbutton.place(x=236,y=7,height=25,width=70)
        



        def cancelnewselection():
         newselection.destroy()

        def select_prod():
            selected = addprodtree.focus()
            global valuep
            valuep= addprodtree.item(selected)["values"][0]
            # messagebox.showinfo("",valuep)

            sql = "SELECT * FROM productservice  WHERE productserviceid= %s"
            i=(valuep,)
            fbcursor.execute(sql,i)

            a=0
            j = 0
            for i in fbcursor:
                tree07.insert(parent='', index='end', iid=i, text='', values=(i[0],i[4],i[5],i[7],1,i[8],i[10],(i[7]*1)))
                for line in tree07.get_children():
                  idsave=tree07.item(line)['values'][7]
                  a+=idsave
            j += 1
            priceco1.config(text=a)

            # try:
            #   k = 0
            #   for s in fbcursor:
            #     prstree.insert(parent='', index='end', iid=s, text='', values=(s[2],s[4],S[5],s[7],s[13],s[8],S[10],(s[7]*s[13])))
            #   k += 1
            # except:
            #   pass
            valu10= tree07.item(selected)["values"][0]
            sqllll = "SELECT * FROM productservice  WHERE productserviceid= %s"
            r=(valu10,)
            fbcursor.execute(sqllll,r)
            child=fbcursor.fetchone()

            qurz=int(1)
            sql21= 'INSERT INTO storingproduct(Productserviceid,invoiceid,sku,category,name,description,status,unitprice,peices,cost,taxable,priceminuscost,serviceornot,stock,stocklimit,warehouse,privatenote,quantity) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            vatree=(child[0],invodata,child[2],child[3],child[4],child[5],child[6],child[7],child[8],child[9],child[10],child[11],child[12],child[13],child[14],child[15],child[16],qurz)
            fbcursor.execute(sql21,vatree,)
            fbilldb.commit()





            newselection.destroy()


            # sql = "SELECT * FROM productservice  WHERE productserviceid= %s"
            # i=(valuep,)
            # x=fbcursor.execute(sql,i)
            # print(x)
            # k = 0
            # for s in x:
            #  prstree.insert(parent='', index='end', iid=s, text='', values=(s[2],s[4],S[5],s[7],s[13],s[8],S[10],(s[7]*s[13])))
            # k += 1


        fbcursor.execute('SELECT * FROM Productservice;') 
        j = 0
        for i in fbcursor:
          addprodtree.insert(parent='', index='end', iid=i, text=' ', values=(i[0],i[4],i[7],i[12],i[13]))
        j += 1




        ctegorytree=ttk.Treeview(newselection, height=27)
        ctegorytree["columns"]=["1"]
        ctegorytree.column("#0", width=35, minwidth=20)
        ctegorytree.column("1", width=205, minwidth=25, anchor=CENTER)    
        ctegorytree.heading("#0",text="", anchor=W)
        ctegorytree.heading("1",text="View filter by category", anchor=CENTER)
        ctegorytree.place(x=660, y=45)

        listbox = Listbox(newselection,height = 33,  
                      width = 40,  
                      bg = "white",
                      activestyle = 'dotbox',  
                      fg = "black",
                      highlightbackground="white")
      
        listbox.insert(0, "                               View all records")
        listbox.insert(1, "                               View all products")
        listbox.insert(2, "                               View all services")
        listbox.place(x=660,y=65,)
        listbox.bind('<<ListboxSelect>>')


        



        # scrollbar = Scrollbar(newselection)
        # scrollbar.place(x=640, y=45, height=560)
        # scrollbar.config( command=tree.yview )
        scrollbar = Scrollbar(newselection)
        scrollbar.place(x=1016+300+25, y=120, height=280+20)



        btn1=Button(newselection,compound = LEFT,image=tick ,text="ok", width=60,command=select_prod).place(x=15, y=610)
        btn1=Button(newselection,compound = LEFT,image=tick , text="Edit product/Service", width=150,command=add_product).place(x=250, y=610)
        btn1=Button(newselection,compound = LEFT,image=tick , text="Add product/Service", width=150,command=add_product).place(x=435, y=610)
        btn1=Button(newselection,compound = LEFT,image=cancel ,text="Cancel", width=60,command=cancelnewselection).place(x=740, y=610)
    except:
     try:
      newselection.destroy()
     except:
      pass



  #preview new line
  def previewline():
    messagebox.showerror("F-Billing Revolution","line is required,please select customer for this order before printing.")


  
  #sms notification
  def sms1():
    send_SMS=Toplevel()
    send_SMS.geometry("700x480+240+150")
    send_SMS.title("Send SMS notification")

    style = ttk.Style()
    style.theme_use('default')
    style.configure('TNotebook.Tab', background="#999999", padding=5)
    sms_Notebook = ttk.Notebook(send_SMS)
    SMS_Notification = Frame(sms_Notebook, height=470, width=700)
    SMS_Service_Account = Frame(sms_Notebook, height=470, width=700)
    sms_Notebook.add(SMS_Notification, text="SMS Notification")
    sms_Notebook.add(SMS_Service_Account, text="SMS Service Account")
    sms_Notebook.place(x=0, y=0)

    numlbel=Label(SMS_Notification, text="SMS number or comma seperated SMS number list(Please start each SMS number with the country code)")
    numlbel.place(x=10, y=10)
    numentry=Entry(SMS_Notification, width=92).place(x=10, y=30)
    stexbel=Label(SMS_Notification, text="SMS Text").place(x=10, y=60)
    stex=Entry(SMS_Notification, width=40).place(x=10, y=85,height=120)
    
    dclbel=Label(SMS_Notification, text="Double click to insert into text")
    dclbel.place(x=410, y=60)
    dcl=Entry(SMS_Notification, width=30)
    dcl.place(x=400, y=85,height=200)
    
    smstype=LabelFrame(SMS_Notification, text="SMS message type", width=377, height=60)
    smstype.place(x=10, y=223)
    snuvar=IntVar()
    normal_rbtn=Radiobutton(smstype, text="Normal SMS(160 chars)", variable=snuvar, value=1)
    normal_rbtn.place(x=5, y=5)
    unicode_rbtn=Radiobutton(smstype, text="Unicode SMS(70 chars)", variable=snuvar, value=2)
    unicode_rbtn.place(x=190, y=5)
    tiplbf=LabelFrame(SMS_Notification, text="Tips", width=680, height=120)
    tiplbf.place(x=10, y=290)
    tiplabl=Label(tiplbf,justify=LEFT,fg="red",  text="Always start the SMS nymber with the country code. Do not use the + sign at the beginning(example\nUS number:8455807546). Do not use any special characters in your normal SMS text. Please use the\nstndard SMS characters or the English alphabet and numbers only. Otherwise the SMS will be\nunreadable or undeliverable. If you need to enter international characters, accents,email address, or\nspecial characters to the SMS text field then choose the Unicode SMS format.")
    tiplabl.place(x=5, y=5)

    btn1=Button(SMS_Notification, width=20, text="Send SMS notification").place(x=10, y=420)
    btn2=Button(SMS_Notification, width=25, text="Confirm SMS cost before sending").place(x=280, y=420)
    btn3=Button(SMS_Notification, width=15, text="Cancel").place(x=550, y=420)
    

    smstype=LabelFrame(SMS_Service_Account, text="Select the notification service provider", width=670, height=65)
    smstype.place(x=10, y=5)
    snumvar=IntVar()
    normal_rbtn=Radiobutton(smstype,text="BULKSMS(www.bulksms.com)",variable=snumvar,value=1,)
    normal_rbtn.place(x=5, y=5)
    unicode_rbtn=Radiobutton(smstype, text="Unicode SMS(70 chars)-Recommended", variable=snumvar, value=2)
    unicode_rbtn.place(x=290, y=5)

    sms1type=LabelFrame(SMS_Service_Account, text="Your BULKSMS.COM Account", width=670, height=100)
    sms1type.place(x=10, y=80)
    name=Label(sms1type, text="Username").place(x=10, y=5)
    na=Entry(sms1type, width=20).place(x=100, y=5)
    password=Label(sms1type, text="Password").place(x=10, y=45)
    pas=Entry(sms1type, width=20).place(x=100, y=45)
    combo=Label(sms1type, text="Route").place(x=400, y=5)
    n = StringVar()
    combo1 = ttk.Combobox(sms1type, width = 20, textvariable = n ).place(x=450,y=5)
    btn1=Button(sms1type, width=10, text="Save settings").place(x=550, y=45)

    
    tiplbf=LabelFrame(SMS_Service_Account, text="Terms of service", width=680, height=250)
    tiplbf.place(x=10, y=190)
    tiplabl=Label(tiplbf,justify=LEFT,fg="red",  text="The SMS notification service is not free.This service costs you creadit.You must have your own account\nat BULKSMS.COM and you need to have sufficient creadit and an active internet connection to use\nthis feature.Please review all fields in this form for accuracy")
    tiplabl.place(x=0, y=5)
    tiplabl1=Label(tiplbf,justify=LEFT,fg="black",  text="visit www.bulksms.com website to create your own account.please make sure the BULKSMS .COM\n service works well in your country before you busy creadit")
    tiplabl1.place(x=0, y=60)
    tiplabl2=Label(tiplbf,justify=LEFT,fg="black",  text="Our SMS notification tool comes without any warranty.our software only forwards your SMS message\nthe BULKSMS API server .The BULKSMS API server will try to sent SMS message your recipient")
    tiplabl2.place(x=0, y=100)
    tiplabl3=Label(tiplbf,justify=LEFT,fg="red",  text="Please note that you access and use the SMS notification tool your own risk.F-Billing software is not\nresponsible for any type of loss or damage or undelivered SMS massage which you may as a result\nof accessing and using the SMS notification service.")
    tiplabl3.place(x=0, y=140)
    checkvar1=IntVar()
    chkbtn1=Checkbutton(tiplbf,text="I have read and agree to the terms of service above",variable=checkvar1,onvalue=1,offvalue=0).place(x=70, y=200) 

#void invoice
  def void_invoice():
    for x in (selectcustomer, addline, deleteline, markinvo):
      x.config(state = 'disabled')
    for y in(cmb,spt,eml,smsno,orddte,duedte,xtracstnme,xtracst,tmplte,dscntrte,taxx,period1,period2,recurentry1,recurentry2):
      y.config(state = 'disabled')
    for z in (addrs,adrs):
      z.config(state = 'disabled')
    
    # cmbodto=cmb.get()
    # addrsfrm=addrs.get('1.0', 'end-1c')
    # sptto=spt.get()
    # adrsto=adrs.get('1.0', 'end-1c')
    # emlfrm=eml.get()
    # smsfrm=smsno.get()
    # # ordrid=ord.get()
    # orddatein=orddte.get_date()
    # ordduein=duedte.get_date()
    # trmsin=trms.get()
    # extracstnme=xtracstnme.get()
    # discountrte=dscntrte.get()
    # extracst=xtracst.get()
    # taax=taxx.get()
    # tplts=tmplte.get()
    # slzprzn=salesprsn.get()
    # ctgryy=ctgry.get()
    # ordrefer=ordref.get()


    # recurring_period = month_var.get()
    # recurring_period_month = current_var.get()
    # next_invoice = recurentry1.get_date() 
    # stop_invoice = recurentry2.get_date() 

    ab="void"


    # sql3='INSERT INTO invoice2 (invoiceid, invodate, duedate, businessname, status, extracostname, extracost, template, salesper, discourate, tax1, category, businessaddress, shipname, shipaddress, cpemail, cpmobileforsms, recurring_period, recurring_period_month, next_invoice, stop_recurring) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    # val2=(invodata,orddatein,ordduein,cmbodto,ab,extracstnme,extracst,tplts,slzprzn,discountrte,taax,ctgryy,addrsfrm,sptto,adrsto,emlfrm,smsfrm,recurring_period,recurring_period_month,next_invoice,stop_invoice)
    # fbcursor.execute(sql3,val2,)
    # fbilldb.commit()

    sql4='UPDATE invoice SET status=%s where invoiceid=%s'
    val3=(ab,invodata)
    fbcursor.execute(sql4,val3,)
    fbilldb.commit()


    

#void invoice
  def enable_invoice():
    for x in (selectcustomer, addline, deleteline, markinvo):
      x.config(state = 'normal')
    for y in(cmb,spt,eml,smsno,orddte,duedte,xtracstnme,xtracst,tmplte,dscntrte,taxx,period1,period2,recurentry1,recurentry2):
      y.config(state = 'normal')
    for z in (addrs,adrs):
      z.config(state = 'normal')








    # if ((selectcustomer["state"] == "normal") and (addline["state"] == "normal") and (deleteline["state"] == "normal") and (markinvo["state"] == "normal")):
    #     selectcustomer["state"] = "disabled"
    #     addline["state"] == "disabled"
    #     deleteline["state"] == "disabled"
    #     markinvo["state"] == "disabled"



    # invovoid = messagebox.askyesno("F-Billing Revolution","Are you sure to void this invoice?\nAll products will be placed back into stock and all payemnts will be voided.")
    # if invovoid == True:
    #   if selectcustomer["state"] == "normal":
    #     selectcustomer["state"] = "disabled"
    #   elif addline["state"] == "normal":
    #             addline["state"] == "disabled"
    #   elif deleteline["state"] == "normal":
    #             deleteline["state"] == "disabled"
    #   elif markinvo["state"] == "normal":
    #             markinvo["state"] == "disabled"
    #   else:
    #     pass






  
  #delete line item  
  def delete_prod():
      xyz = tree07.item(tree07.focus())["values"][0]
      print(xyz,)
      dltnow=invodata
      sql = 'DELETE FROM storingproduct WHERE invoiceid=%s AND Productserviceid=%s'
      val = (dltnow,xyz,)
      fbcursor.execute(sql, val)
      fbilldb.commit()
      tree07.delete(tree07.selection()[0])
      for record in tree07.get_children():
           tree07.delete(record)        
      sql = "SELECT * FROM storingproduct WHERE invoiceid= %s"
      i=(dltnow,)
      fbcursor.execute(sql,i)
      b=0
      j = 0
      for i in fbcursor:
        tree07.insert(parent='', index='end', iid=i, text='', values=(i[4],i[6],i[7],i[9],i[22],i[10],i[12],(i[9]*i[22])))
        for line in tree07.get_children():
            idsave=tree07.item(line)['values'][7]
        b+=idsave
      j += 1
      priceco1.config(text=b)


################################################ CREATE INVOICE #############################################
  def createinvoice():
    cmbodto=cmb.get()
    addrsfrm=addrs.get('1.0', 'end-1c')
    sptto=spt.get()
    adrsto=adrs.get('1.0', 'end-1c')
    emlfrm=eml.get()
    smsfrm=smsno.get()
    # ordrid=ord.get()
    orddatein=orddte.get_date()
    ordduein=duedte.get_date()
    trmsin=trms.get()
    extracstnme=xtracstnme.get()
    discountrte=dscntrte.get()
    extracst=xtracst.get()
    taax=taxx.get()
    tplts=tmplte.get()
    slzprzn=salesprsn.get()
    ctgryy=ctgry.get()
    ordrefer=ordref.get()


    recurring_period = month_var.get()
    recurring_period_month = current_var.get()
    next_invoice = recurentry1.get_date() 
    stop_invoice = recurentry2.get_date() 

    stat="Draft"


    sql3='UPDATE invoice SET  invodate=%s, duedate=%s, businessname=%s, extracostname=%s, extracost=%s, template=%s, salesper=%s, discourate=%s, tax1=%s, category=%s, businessaddress=%s, shipname=%s, shipaddress=%s, cpemail=%s, cpmobileforsms=%s,	orderid=%s, recurring_period=%s, recurring_period_month=%s, next_invoice=%s, stop_recurring=%s WHERE invoiceid=%s' 
    val2=(orddatein,ordduein,cmbodto,extracstnme,extracst,tplts,slzprzn,discountrte,taax,ctgryy,addrsfrm,sptto,adrsto,emlfrm,smsfrm, ordrefer,recurring_period,recurring_period_month,next_invoice,stop_invoice,invodata)
    fbcursor.execute(sql3,val2,)
    fbilldb.commit()

    sql5='SELECT * FROM invoice WHERE invoiceid=%s'
    val5=(invodata,)
    fbcursor.execute(sql5,val5,)
    new=fbcursor.fetchone()
    print(new)
    if new[4]=="void":
      pass
    else:
      sql6='UPDATE invoice SET status=%s WHERE invoiceid=%s'
      val6=(stat,invodata,)
      fbcursor.execute(sql6,val6,)
      fbilldb.commit()


    for record in invotree.get_children():
      invotree.delete(record)
    fbcursor.execute("select *  from invoice")
    pandsdata = fbcursor.fetchall()
    countp = 0
    for i in pandsdata:
      invotree.insert(parent='', index='end', iid=i, text='', values=('',i[0], i[2], i[3], i[18], i[4], i[5], i[6], i[7], i[8], i[9], i[10]))
      invototalinput=0
      for line in invotree.get_children():
          idsave1=invotree.item(line)['values'][9]
          invototalinput += idsave1
    countp += 1
    invototalrowcol.config(text=invototalinput)
    messagebox.showinfo('Successfully Added','Successfully Added')
    pop.destroy()


    # sql4='INSERT INTO invoice (recurring_period, recurring_period_month, next_invoice, stop_recurring) VALUES (%s,%s,%s, %s)'
    # val4=(recurring_period,recurring_period_month,next_invoice,stop_invoice)
    # fbcursor.execute(sql4,val4,)
    # fbilldb.commit()

    # inv = 'SELECT invoiceid FROM invoice'
    # print(inv)
    

    # custselection.destroy()
      # save1111=save1111.append(idsave)
      # print(save1111)
    # for i in idsave:
    #   print(idsave[i])
      # for value in tree07.item(line)['values']:
        # print(value[0])
      

    # prdctidvar=valuep
    # print(prdctidvar)
    

      

      #######################################################################################################################################################
  # def Add():
  #     order = e1.get()
  #     address = e2.get()
  #     ship = e3.get()
  #     address1 = e4.get()
  #     email = e5.get()
  #     sms = e6.get()
  
  #     mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="fbilldb" , port="3306")
  #     mycursor=mysqldb.cursor()
  
  #     try:
  #       sql = "INSERT INTO  Customer (businessname,businessaddress,shipname,shipaddress,cpemail,cpmobileforsms) VALUES (%s, %s, %s, %s, %s, %s)"
  #       val = (order,address,ship,address1,email,sms)
  #       mycursor.execute(sql, val)
  #       mysqldb.commit()
  #       lastid = mycursor.lastrowid
  #       #messagebox.showinfo("information", "Employee inserted successfully...")
  #       e1.delete(0, END)
  #       e2.delete(0, END)
  #       e3.delete(0, END)
  #       e4.delete(0, END)
  #       e5.delete(0, END)
  #       e6.delete(0, END)
  #       e1.focus_set()
  #     except Exception as e:
  #       print(e)
  #       mysqldb.rollback()
  #       mysqldb.close()
      
    

  firFrame=Frame(pop, bg="#f5f3f2", height=60)
  firFrame.pack(side="top", fill=X)

  w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  selectcustomer = Button(firFrame,compound="top", text="Select\nCustomer",relief=RAISED, image=customer,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=selectcustomer)
  selectcustomer.pack(side="left", pady=3, ipadx=4)


  w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  addline= Button(firFrame,compound="top", text="Add new\nline item",relief=RAISED, image=photo,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=addnewline)
  addline.pack(side="left", pady=3, ipadx=4)

  deleteline= Button(firFrame,compound="top", text="Delete line\nitem",relief=RAISED, image=photo2,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=delete_prod)
  deleteline.pack(side="left", pady=3, ipadx=4)

  w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  # prev= Button(firFrame,compound="top", text="Preview\nInvoice",relief=RAISED, image=photo4,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=previewline)
  # prev.pack(side="left", pady=3, ipadx=4)

  prin= Button(firFrame,compound="top", text="Print \nInvoice",relief=RAISED, image=photo5,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=printsele)
  prin.pack(side="left", pady=3, ipadx=4)

  w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  mail= Button(firFrame,compound="top", text="Email\nInvoice",relief=RAISED, image=photo6,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=email_invoice_recurring)
  mail.pack(side="left", pady=3, ipadx=4)

  sms1= Button(firFrame,compound="top", text="Send SMS\nnotification",relief=RAISED, image=photo10,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=sms1)
  sms1.pack(side="left", pady=3, ipadx=4)

  w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  markinvo= Button(firFrame,compound="top", text="Mark Invoice\n as Paid",relief=RAISED, image=mark1,bg="#f5f3f2", fg="black", height=55, bd=1, width=55)
  markinvo.pack(side="left", pady=3, ipadx=4)

  voidinvo= Button(firFrame,compound="top", text="Void\nInvoice",relief=RAISED, image=mark2,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=void_invoice)
  voidinvo.pack(side="left", pady=3, ipadx=4)

  enableinvo= Button(firFrame,compound="top", text="Reactivate \nInvoice",relief=RAISED, image=mark2,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=enable_invoice)
  enableinvo.pack(side="left", pady=3, ipadx=4)


  w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  calc= Button(firFrame,compound="top", text="Open\nCalculator",relief=RAISED, image=photo9,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=calcu)
  calc.pack(side="left", pady=3, ipadx=4)

  w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="right", padx=5)

  Createorder= Button(firFrame,compound="top", text="Save",relief=RAISED, image=tick,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=createinvoice)
  Createorder.pack(side="right", pady=3, ipadx=4)

  fir1Frame=Frame(pop, height=180,bg="#f5f3f2")
  fir1Frame.pack(side="top", fill=X)

    
  # fbcursor.execute('SELECT * FROM Productservice;') 
  # j = 0
  # for i in fbcursor:
  #     labelframe1.insert(parent='', index='end', iid=i, text='', values=(' ',i[0],i[4],i[5],i[7],i[8],i[10],))
  #     j += 1


  labelframe1 = LabelFrame(fir1Frame,text="Customers",font=("arial",15))
  labelframe1.place(x=10,y=5,width=640,height=160)





  # sql = "select Customer.businessname from Customer where Customer.customerid = Orders.customerid"
  # sql = "select Customer.businessname from Customer INNER JOIN Orders ON Customer.customerid = Orders.customerid"
  sql = "select businessname from Customer"
  fbcursor.execute(sql,)
  pdata = fbcursor.fetchall()





  def prodtreefetch():
    itemid = selectcusttree.item(selectcusttree.focus())["values"][0]
    sql = "select * from Customer where customerid = %s"
    val = (itemid, )
    fbcursor.execute(sql, val)
    global slctcstr
    slctcstr = fbcursor.fetchone()
    cmb.delete(0,'end')
    cmb.insert(0, slctcstr[4])
    addrs.delete('1.0','end')
    addrs.insert("1.0", slctcstr[5])
    spt.delete(0,'end')
    spt.insert(0, slctcstr[6])
    adrs.delete('1.0','end')
    adrs.insert('1.0', slctcstr[7])
    eml.delete(0,'end')
    eml.insert(0, slctcstr[9])
    smsno.delete(0,'end')
    smsno.insert(0, slctcstr[10])
    custselection.destroy()

    cmbodto=cmb.get()
    addrsfrm=addrs.get('1.0', 'end-1c')
    sptto=spt.get()
    adrsto=adrs.get('1.0', 'end-1c')
    emlfrm=eml.get()
    smsfrm=smsno.get()
    # ordrid=ord.get()
    



    sql3='INSERT INTO invoice ( invoiceid,businessname, businessaddress, shipname, shipaddress, cpemail, cpmobileforsms) VALUES (%s,%s,%s,%s,%s,%s,%s)'
    val2=(invodata,cmbodto,addrsfrm,sptto,adrsto,emlfrm,smsfrm)
    fbcursor.execute(sql3,val2,)
    fbilldb.commit()
    
    custselection.destroy()

  invoice = Label(labelframe1, text="Invoice to").place(x=10,y=5)
  cmb = ttk.Combobox(labelframe1,values=pdata,width=28)
  cmb.place(x=80,y=5)

  # q = e1.focus()

  # sql = "select * from Customer where businessname=%s"
  # i=(e1)
  # fbcursor.execute(sql,i,)
  # sltn = fbcursor.fetchone()

  # sql = "select Customer.businessaddress from Customer where pdata = Orders.businessname"
  # fbcursor.execute(sql,)
  # addrs = fbcursor.fetchall()
  # print(addrs)                                values="addrs",

  # mycursor=mysql.cursor()
  # fbcursor.execute("SELECT businessname FROM Customer")
  # myresult= fbcursor.fetchone()
  # for row in myresult:
  #   print(row)

  # sql = "select businessname from Customer"
  # sql1 = "select businessname from Order"

  # if sql == sql1:
  #     itemid = invotree.item(invotree.focus())["values"][1]
  #     print(itemid,)
  #     sql = 'SELECT FROM Customer.businessaddress WHERE customerid=%s'
  #     val = (itemid,)
  #     fbcursor.execute(sql, val)
  #     fbilldb.commit()
  #     invotree.selection_get(invotree.selection()[0])
  # else:
  #     pass  


  # sql    = "SELECT * FROM Customer.businessaddress WHERE Address='$businessaddress'"


  # sql = "select Customer.businessaddress from Customer where pdata = Orders.businessname"
  # fbcursor.execute(sql,)
  # addrs = fbcursor.fetchone()
  # print(addrs)

  # sql = "SELECT * from Customer where businessaddress =%s"
  # val = ("businessaddress", )
  # fbcursor.execute(sql,val)
  # pdata = fbcursor.fetchone()
  # print(pdata)
  #     entry.insert(0, pdata[3])






  address=Label(labelframe1,text="Address").place(x=10,y=30)
  addrs=scrolledtext.Text(labelframe1, undo=True,width=23)
  addrs.place(x=80,y=30,height=70)
 
  
  ship=Label(labelframe1,text="Ship to").place(x=342,y=5)
  spt=Entry(labelframe1,width=30)
  spt.place(x=402,y=3)

  address1=Label(labelframe1,text="Address").place(x=340,y=30)
  adrs=scrolledtext.Text(labelframe1, undo=True,width=23)
  adrs.place(x=402,y=30,height=70)

  def changedone():
    # shpdlt=spt1.get(osdata[17])
    spt.delete(0,'end')
    spt.insert(0, slctcstr[4])
    adrs.delete('1.0','end')
    adrs.insert('1.0', slctcstr[5])

  btn1=Button(labelframe1,width=3,height=2,compound = LEFT,text=">>",command=changedone).place(x=280, y=50)
  
  labelframe2 = LabelFrame(fir1Frame,text="")
  labelframe2.place(x=10,y=130,width=640,height=42)

  email=Label(labelframe2,text="Email").place(x=10,y=5)
  eml=Entry(labelframe2,width=30)
  eml.place(x=80,y=5)

  sms=Label(labelframe2,text="SMS Number").place(x=328,y=5)
  smsno=Entry(labelframe2,width=30)
  smsno.place(x=402,y=5)
    
  labelframe = LabelFrame(fir1Frame,text="Invoice",font=("arial",15))
  labelframe.place(x=652,y=5,width=290,height=170)


 ##
  fbcursor.execute("SELECT * FROM invoice ORDER BY invoiceid DESC LIMIT 1")
  result = fbcursor.fetchone()
 ##
  order=Label(labelframe,text="Invoice#").place(x=5,y=5)
  ord=Entry(labelframe,width=25)
  ord.place(x=100,y=5,)
  ord.delete(0,'end')
  if not result== None:
   invodata=result[0]+1
  else:
    invodata=1
  ord.insert(0, invodata)
 ##
  def duecheckinv1():
     if checkvarStatus5.get()==0:
       duedte['state'] = DISABLED  
     else:
       duedte['state'] = NORMAL




  orderdate=Label(labelframe,text="Invoice date").place(x=5,y=33)
  orddte=DateEntry(labelframe,width=20)
  orddte.place(x=150,y=33)
  checkvarStatus5=IntVar()
  duedate=Checkbutton(labelframe,variable = checkvarStatus5,text="Due date",onvalue =0 ,offvalue = 1, command=duecheckinv1).place(x=5,y=62)
  duedte=DateEntry(labelframe,width=20)
  duedte.place(x=150,y=62)
  terms=Label(labelframe,text="Terms").place(x=5,y=92)
  trms=ttk.Combobox(labelframe, value="",width=25)
  trms.place(x=100,y=92)
  
  ref=Label(labelframe,text="Order ref#").place(x=5,y=118)
  ordref=Entry(labelframe,width=27)
  ordref.place(x=100,y=118)

  fir2Frame=Frame(pop, height=150,width=100,bg="#f5f3f2")
  fir2Frame.pack(side="top", fill=X)
  listFrame = Frame(fir2Frame, bg="white", height=140,borderwidth=5,  relief=RIDGE)


  
  tree07=ttk.Treeview(listFrame)
  tree07["columns"]=["1","2","3","4","5","6","7","8"]

  tree07.column("#0", width=40)
  tree07.column("1", width=80)
  tree07.column("2", width=190)
  tree07.column("3", width=190)
  tree07.column("4", width=80)
  tree07.column("5", width=60)
  tree07.column("6", width=60)
  tree07.column("7", width=60)
  tree07.column("8", width=80)

  tree07.heading("#0")
  tree07.heading("1",text="ID/SKU")
  tree07.heading("2",text="Product/Service")
  tree07.heading("3",text="Description")
  tree07.heading("4",text="Unit Price")
  tree07.heading("5",text="Quantity")
  tree07.heading("6",text="Pcs/Weight")
  tree07.heading("7",text="Tax1")
  tree07.heading("8",text="Price")
  priceco1 = Label(listFrame,bg="#f5f3f2")
  priceco1.place(x=850,y=200,width=78,height=18)

  # fbcursor.execute('SELECT * FROM Productservice;') 
  # j = 0
  # for i in fbcursor:
  #   viwedttree.insert(parent='', index='end', iid=i, text='', values=(' ',i[2],i[12],i[5],i[7],i[13],i[8],i[10]))
  #   j += 1

  
  tree07.pack(fill="both", expand=1)
  listFrame.pack(side="top", fill="both", padx=5, pady=3, expand=1)
  
  new_value = tk.StringVar()

  def edit_window_box(val):
    
    edit_window = Toplevel(root)
    edit_window.title("Edit the value or cancel")
    edit_window.geometry("400x200")
    label_edit = tk.Label(edit_window , text='Enter value to edit', 
    font = ("Times New Roman", 12)).place(x=68,y=60)
    #create edit box
    edit_box = tk.Entry(edit_window)
    edit_box.insert(0,val)
    edit_box.place(x=200,y=63)
    #auto select edit window 
    edit_window.focus()
    
    def value_assignment(event):
        printing = edit_box.get()
        # print(printing)
        indexcolaa=int(cola)-1
        new_value.set(printing)
        # print(col)
        #only destroy will not update the value (perhaps event keeps running in background)
        #quit allows event to stop n update value in tree but does not close the window in single click 
        #rather on dbl click shuts down entire app 

        selected0 = tree07.focus()
        valuz1= tree07.item(selected0)["values"]
        idgettingprdt=valuz1[0]
        valuz1[indexcolaa]=printing
        # print(valuz1)

        sql2z0= 'UPDATE storingproduct SET sku=%s,name=%s,description=%s,unitprice=%s,quantity=%s,peices=%s,taxable=%s WHERE invoiceid=%s AND Productserviceid=%s'
        val0z1=(valuz1[0],valuz1[1],valuz1[2],valuz1[3],valuz1[4],valuz1[5],valuz1[6],invodata,idgettingprdt)
        # dnz=(ordrid,sql2z0,)
        # print(val0z1)
        fbcursor.execute(sql2z0,val0z1)
        fbilldb.commit()

        qntsql= 'UPDATE Productservice SET quantity=%s WHERE Productserviceid=%s'
        qntval=(valuz1[4],idgettingprdt)
        fbcursor.execute(qntsql,qntval)
        fbilldb.commit()

        # for record in tree07.get_children():
        #   tree07.delete(record)
        # tree07.delete(tree07.get_children())

        fbcursor.execute("SELECT * FROM storingproduct ORDER BY invoiceid DESC LIMIT 1")
        bol = fbcursor.fetchone()[2]
        # print(bol)
        # print(invodata)

        if bol==invodata:        
         for record in tree07.get_children():
          tree07.delete(record)
         m="SELECT * FROM storingproduct  WHERE invoiceid=%s"
         i=(invodata,)
         fbcursor.execute(m,i)
         panrefrdata = fbcursor.fetchall()
         az=0
         countp = 0
         for i in panrefrdata:
           tree07.insert(parent='', index='end', iid=i, text='', values=(i[4],i[6],i[7],i[9],i[22],i[10],i[12],(i[9]*i[22])))

           az+=(i[9]*i[22])
         countp += 1
         priceco1.config(text=az)
        else:
          pass
        edit_window.quit()
        edit_window.destroy()
    
    edit_window.bind('<Return>', value_assignment )
    


    B1 = tk.Button(edit_window, text=" Okay ")
    B1.bind('<Button-1>',value_assignment)
    B1.place(x=70,y=130)
    
    
    B2 = tk.Button(edit_window, text="Cancel", command = edit_window.destroy).place(x=276,y=130)
    edit_window.mainloop()
    
  #will explain
  #variable to hold col value (col clicked)
  shape1 = tk.IntVar()
  #tracks both col , row on mouse click
  def tree_click_handler(event):
      global cola
      cur_item = tree07.item(tree07.focus())
      cola = tree07.identify_column(event.x)[1:]
      rowid = tree07.identify_row(event.y)[1:]
     
      # print(rowid)
      #updates list
      shape1.set(cola)
      try:
          x,y,w,h = tree07.bbox('I'+rowid,'#'+cola)
      except:pass
      #tree.tag_configure("highlight", background="yellow")
      return(cola)

  #code linked to event    
  tree07.bind('<ButtonRelease-1>', tree_click_handler)

  #edit a value in a clicked cell
  def edit(event):
      try:
          selected_item = tree07.selection()[0]
          temp = list(tree07.item(selected_item , 'values'))
          tree_click_handler
          col_selected = int(shape1.get())-1
          edit_window_box(temp[col_selected])
          #do not run if edit window is open
          #use edit_window.mainloop() so value assign after window closes
          temp[col_selected] = new_value.get()
          tree07.item(selected_item, values= temp)
      except: pass


    
    
  #binding allows to edit on screen double click
  tree07.bind('<Double-Button-1>' , edit)

  # sql = "SELECT * FROM productservice  WHERE productserviceid= %s"
  # i=(valuep)
  # fbcursor.execute(sql,i)
  
  # j = 0
  # for i in fbcursor:
  #         tree07.insert(parent='', index='end', iid=i, text='', values=(i[0], i[1], i[2], i[3], i[4],i[5], i[6], i[7], i[8], i[9]))
  # j += 1

  fir3Frame=Frame(pop,height=200,width=700,bg="#f5f3f2")
  fir3Frame.place(x=0,y=490)

  tabStyle = ttk.Style()
  tabStyle.theme_use('default')
  tabStyle.configure('TNotebook.Tab', background="#999999", width=12, padding=5)
  myNotebook=ttk.Notebook(fir3Frame)
  invoiceFrame = Frame(myNotebook, height=200, width=800)
  recurFrame = Frame(myNotebook, height=200, width=800)
  payementFrame = Frame(myNotebook, height=200, width=800)
  headerFrame = Frame(myNotebook, height=200, width=800)
  commentFrame = Frame(myNotebook, height=200, width=800)
  termsFrame = Frame(myNotebook, height=200, width=800)
  noteFrame = Frame(myNotebook, height=200, width=800)
  documentFrame = Frame(myNotebook, height=200, width=800)
  
  myNotebook.add(invoiceFrame,compound="left", text="Invoice")
  myNotebook.add(recurFrame,compound="left", text="Recurring")
  myNotebook.add(payementFrame,compound="left", text="Payements")
  myNotebook.add(headerFrame,compound="left",  text="Header/Footer")
  myNotebook.add(commentFrame,compound="left",  text="Comments")
  myNotebook.add(termsFrame,compound="left", text="Terms")
  myNotebook.add(noteFrame,compound="left",  text="Private notes")
  myNotebook.add(documentFrame,compound="left",  text="Documents")
  myNotebook.pack(expand = 1, fill ="both") 

##
  sql = "select extracostname from invoice"
  fbcursor.execute(sql,)
  excodata = fbcursor.fetchall()  
## 

  labelframe1 = LabelFrame(invoiceFrame,text="",font=("arial",15))
  labelframe1.place(x=1,y=1,width=800,height=170)
  cost1=Label(labelframe1,text="Extra cost name").place(x=2,y=5)
  xtracstnme=ttk.Combobox(labelframe1, value=excodata,width=20)
  xtracstnme.place(x=115,y=5)
  rate=Label(labelframe1,text="Discount rate").place(x=370,y=5)
  dscntrte=Spinbox(labelframe1,width=6,  from_=0, to=100, font="italic 10")
  dscntrte.place(x=460,y=5)
  cost2=Label(labelframe1,text="Extra cost").place(x=35,y=35)
  xtracst=Entry(labelframe1,width=10)
  xtracst.place(x=115,y=35)
  tax=Label(labelframe1,text="Tax1").place(x=420,y=35)
  taxx=Entry(labelframe1,width=7)
  taxx.place(x=460,y=35)
##
  sql = "select template from invoice"
  fbcursor.execute(sql,)
  tmpdata = fbcursor.fetchall()  
##
  template=Label(labelframe1,text="Template").place(x=37,y=70)
  tmplte=ttk.Combobox(labelframe1, value=tmpdata,width=25)
  tmplte.place(x=115,y=70)
  sales=Label(labelframe1,text="Sales Person").place(x=25,y=100)
  salesprsn=Entry(labelframe1,width=18)
  salesprsn.place(x=115,y=100)
  category=Label(labelframe1,text="Category").place(x=300,y=100)
  ctgry=Entry(labelframe1,width=22)
  ctgry.place(x=370,y=100)
  
  statusfrme = LabelFrame(labelframe1,text="Status",font=("arial",15))
  statusfrme.place(x=540,y=0,width=160,height=160)
  draft=Label(statusfrme, text="Draft",font=("arial", 15, "bold"), fg="grey").place(x=50, y=3)
  on1=Label(statusfrme, text="Emailed on:").place( y=50)
  nev1=Label(statusfrme, text="Never").place(x=100,y=50)
  on2=Label(statusfrme, text="Printed on:").place( y=90)
  nev2=Label(statusfrme, text="Never").place(x=100,y=90)

  text1=Label(headerFrame,text="Title text").place(x=50,y=5)
  e1=ttk.Combobox(headerFrame, value="",width=60).place(x=125,y=5)
  text2=Label(headerFrame,text="Page header text").place(x=2,y=45)
  e1=ttk.Combobox(headerFrame, value="",width=60).place(x=125,y=45)
  text3=Label(headerFrame,text="Footer text").place(x=35,y=85)
  e1=ttk.Combobox(headerFrame, value="",width=60).place(x=125,y=85)

  text=Label(noteFrame,text="Private notes(not shown on invoice/order/estimates)").place(x=10,y=10)
  e1=Text(noteFrame,width=100,height=7).place(x=10,y=32)

  e1=Text(termsFrame,width=100,height=9).place(x=10,y=10)

  e1=Text(commentFrame,width=100,height=9).place(x=10,y=10)

  btn1=Button(documentFrame,height=2,width=3,text="+").place(x=5,y=10)
  btn2=Button(documentFrame,height=2,width=3,text="-").place(x=5,y=50)
  text=Label(documentFrame,text="Attached documents or image files.If you attach large email then email taken long time to send").place(x=50,y=10)
  cusventtree=ttk.Treeview(documentFrame, height=5)
  cusventtree["columns"]=["1","2","3"]
  cusventtree.column("#0", width=20)
  cusventtree.column("1", width=250)
  cusventtree.column("2", width=250)
  cusventtree.column("2", width=200)
  cusventtree.heading("#0",text="", anchor=W)
  cusventtree.heading("1",text="Attach to Email")
  cusventtree.heading("2",text="Filename")
  cusventtree.heading("3",text="Filesize")  
  cusventtree.place(x=50, y=45)
  

  fir4Frame=Frame(pop,height=190,width=210,bg="#f5f3f2")
  fir4Frame.place(x=740,y=520)
  summaryfrme = LabelFrame(fir4Frame,text="Summary",font=("arial",15))
  summaryfrme.place(x=0,y=0,width=200,height=170)
  discount=Label(summaryfrme, text="Discount").place(x=0 ,y=0)
  discount1=Label(summaryfrme, text="$0.00").place(x=130 ,y=0)
  sub=Label(summaryfrme, text="Subtotal").place(x=0 ,y=21)
  sub1=Label(summaryfrme, text="$0.00").place(x=130 ,y=21)
  tax=Label(summaryfrme, text="Tax1").place(x=0 ,y=42)
  tax1=Label(summaryfrme, text="$0.00").place(x=130 ,y=42)
  cost=Label(summaryfrme, text="Extra cost").place(x=0 ,y=63)
  cost=Label(summaryfrme, text="$0.00").place(x=130 ,y=63)
  order=Label(summaryfrme, text="Order total").place(x=0 ,y=84)
  order1=Label(summaryfrme, text="$0.00").place(x=130 ,y=84)
  total=Label(summaryfrme, text="Total paid").place(x=0 ,y=105)
  total1=Label(summaryfrme, text="$0.00").place(x=130 ,y=105)
  balance=Label(summaryfrme, text="Balance").place(x=0 ,y=126)
  balance1=Label(summaryfrme, text="$0.00").place(x=130 ,y=126)

  def calculatesummary0():
    #  global discount1,sub1,tax1,cost1z,order1
    #  totalpriceinput.config(text="")
     ttlprzinptinv=priceco1.cget("text")
     ratediscntinv=dscntrte.get()
     xtaxinv=taxx.get()
     cstxtrainv=xtracst.get()
     print(ttlprzinptinv,ratediscntinv,xtaxinv,cstxtrainv)
  
     isdd=round(int(ratediscntinv),3)
     pidd=ttlprzinptinv
     p=round(pidd, 4)
     dsctedd=(isdd*pidd)/100
     dscdd=round(dsctedd, 4)
     discount=Label(summaryfrme, text=str(isdd)+"% Discount").place(x=0 ,y=0)
     discount1=Label(summaryfrme,text='Rs. '+str(dscdd))
     discount1.place(x=130 ,y=0)
  
     sbtotlhee=p-dscdd
     subtotl=round(sbtotlhee, 4)
     sub=Label(summaryfrme, text="Subtotal").place(x=0 ,y=21)
     sub100=Label(summaryfrme, text='Rs. '+str(subtotl))
     sub100.place(x=130 ,y=21)
  
     taxval91=int(xtaxinv)
     tax1dsplay=(taxval91*subtotl)/100
     taxvalu=round(tax1dsplay,2)
     tax=Label(summaryfrme, text="Tax1").place(x=0 ,y=42)
     tax100=Label(summaryfrme, text='Rs. '+str(taxvalu))
     tax100.place(x=130 ,y=42)
  
     xtracstvaluzz=int(cstxtrainv)
     xtra1cst=round(xtracstvaluzz, 4)
     cost=Label(summaryfrme, text="Extra cost").place(x=0 ,y=63)
     cost100=Label(summaryfrme, text='Rs. '+str(xtra1cst)).place(x=130 ,y=63)
  
     otherttlval=subtotl+taxvalu+xtra1cst
     ot1v1=round(otherttlval, 4)
     order=Label(summaryfrme, text="Invoice total").place(x=0 ,y=84)
     order100=Label(summaryfrme, text='Rs. '+str(ot1v1)).place(x=130 ,y=84)
  
     itemidot = invodata
     ordttl=ot1v1
     for record in invotree.get_children():
       invotree.delete(record)
     sqlordttl = "UPDATE invoice SET invoicetot=%s WHERE invoiceid = %s"
     valqordttl = (ordttl,itemidot, )
     fbcursor.execute(sqlordttl, valqordttl,)
     fbilldb.commit()
     fbcursor.execute('SELECT * FROM invoice')   
     j = 0
     for i in fbcursor:
      invotree.insert(parent='', index='end', iid=i, text='', values=('',i[0], i[2], i[3], i[18], i[4], i[5], i[6], i[7], i[8], i[9], i[10]))
     j += 1
  

  fir5Frame=Frame(pop,height=38,width=210)
  fir5Frame.place(x=735,y=485)
  btndown=Button(fir5Frame, compound="left", text="Show summary",command=calculatesummary0).place(x=75, y=0, height=35)
#   btnup=Button(fir5Frame, compound="left", text="Line Up").place(x=150, y=0)




  # recureframe = LabelFrame(recurFrame,text="",font=("arial",15))
  # recureframe.place(x=1,y=1,width=800,height=170)
  # checkvarStatus6=IntVar()
  # recure=Checkbutton(recureframe,variable = checkvarStatus6,text="Recurring",onvalue =0 ,offvalue = 1).place(x=5,y=5)
  # recurper=Label(recureframe,text="Recurring period(interval)").place(x=65,y=35)
  # e2=Entry(recureframe,width=13).place(x=240,y=35)
  # e1=ttk.Combobox(recureframe, value="",width=20).place(x=325,y=35)
  # nextinvo=Label(recureframe,text="Next Invoice").place(x=240,y=65)
  # e1=ttk.Combobox(recureframe, value="",width=20).place(x=325,y=65)
  # recalc = Button(recureframe, text="Recalculate").place(x=480,y=65)
  # checkvarStatus7=IntVar()
  # stoprecur=Checkbutton(recureframe,variable = checkvarStatus7,text="Stop recurring after",onvalue =0 ,offvalue = 1).place(x=180,y=95)
  # e1=ttk.Combobox(recureframe, value="",width=20).place(x=325,y=95)

  global recurentry1, recurentry2,checkvarStatus6,period2, current_var, month_var
  
  recureframe = LabelFrame(recurFrame,text="",font=("arial",15))
  recureframe.place(x=1,y=1,width=800,height=170)
  checkvarStatus6=IntVar()
  current_var = StringVar()
  month_var = StringVar()
  # checkvarStatus6.set(0)
  
  Checkbutton(recureframe,variable = checkvarStatus6,text="Recurring", offvalue=0, onvalue=1).place(x=5,y=5)
  # Checkbutton(ws, text="accept T&C", variable=cb, onvalue=1, offvalue=0, command=isChecked).pack()
  period=Label(recureframe,text="Recurring period(interval)").place(x=65,y=35)
  # period1=Entry(recureframe,width=13, textvariable=month_var)
  # period1.place(x=240,y=35)
  period1 = Spinbox(recureframe, from_=1, to=10000, font="italic 10", width=9, text="Months(s)" ,textvariable=month_var)
  period1.place(x=240,y=35)
  # period1.delete(0,'end')
  # period1.insert(0, osdata[24]) 
  
  # period1.delete(0,'end')
  # period1.insert(0, psdata[20])
                              
  nextinvo=Label(recureframe,text="Next Invoice").place(x=240,y=65)
  recurentry1=DateEntry(recureframe,width=20, )
  recurentry1.place(x=325,y=65)
  # recurentry1['state'] = DISABLED 
  # recurentry1.delete(0,'end')
  # recurentry1.insert(0, osdata[26].strftime('%m/%d/%y'))
  
  recalc = Button(recureframe, text="Recalculate")
  recalc.place(x=490,y=65)

  # saverec= Button(recureframe, text="Save" , command=insertrecur).place(x=570,y=65)
  
  checkvarStatus7=IntVar()
  # checkvarStatus7.set(0)
  stoprecur=Checkbutton(recureframe,variable = checkvarStatus7,text="Stop recurring after",onvalue =1 ,offvalue = 0).place(x=180,y=95)
  recurentry2=DateEntry(recureframe, value="",width=20)
  recurentry2.place(x=325,y=95)
  # recurentry2['state'] = DISABLED 
  # recurentry2.delete(0,'end')
  # recurentry2.insert(0, osdata[27].strftime('%m/%d/%y'))
  def month():
    period2["values"] = ["Month(s)", "Days(s)"] 
  period2=ttk.Combobox(recureframe,width=20, 
                            values=["Month(s)", "Day(s)"],textvariable=current_var)
  # period2=Entry(recureframe,width=13, textvariable=current_var)

  period2.place(x=325,y=35)
  period2.delete(0,'end')
  # period2.insert(0, osdata[25])
  # period2['state'] = DISABLED





  btn1=Button(payementFrame,height=2,width=3,text="+").place(x=5,y=10)
  btn2=Button(payementFrame,height=2,width=3,text="-").place(x=5,y=50)
  cusventtree=ttk.Treeview(payementFrame, height=5)
  cusventtree["columns"]=["1","2","3","4","5"]
  cusventtree.column("#0", width=20)
  cusventtree.column("1", width=140)
  cusventtree.column("2", width=140)
  cusventtree.column("3", width=110)
  cusventtree.column("4", width=140)
  cusventtree.column("5", width=110)
  cusventtree.heading("#0",text="", anchor=W)
  cusventtree.heading("1",text="Payement ID")
  cusventtree.heading("2",text="Payement date")
  cusventtree.heading("3",text="Paid by")
  cusventtree.heading("4",text="Description")
  cusventtree.heading("5",text="Amount")      
  cusventtree.place(x=50, y=45)




#printselected order
  
def printsele():
  # subprocess.Popen('C:\\Windows\\System32\\spoolsv.exe')

  def property1():
    propert=Toplevel()
    propert.title("Microsoft Print To PDF Advanced Document Settings")
    propert.geometry("670x500+240+150")

    def property2():
      propert1=Toplevel()
      propert1.title("Microsoft Print To PDF Advanced Document Settings")
      propert1.geometry("670x500+240+150")

      name=Label(propert1, text="Microsoft Print To PDF Advanced Document Settings").place(x=10, y=5)
      paper=Label(propert1, text="Paper/Output").place(x=30, y=35)
      size=Label(propert1, text="Paper size").place(x=55, y=65)
      n = StringVar()
      search = ttk.Combobox(propert1, width = 15, textvariable = n )
      search['values'] = ('letter')
      search.place(x=150,y=65)
      search.current(0)
      copy=Label(propert1, text="Copy count:").place(x=55, y=95)

      okbtn=Button(propert1,compound = LEFT,image=tick , text="Ok", width=60).place(x=460, y=450)
      canbtn=Button(propert1,compound = LEFT,image=cancel, text="Cancel", width=60).place(x=570, y=450)
      
      


    style = ttk.Style()
    style.theme_use('default')
    style.configure('TNotebook.Tab', background="#999999", padding=5)
    property_Notebook = ttk.Notebook(propert)
    property_Frame = Frame(property_Notebook, height=500, width=670)
    property_Notebook.add(property_Frame, text="Layout")
    property_Notebook.place(x=0, y=0)

    name=Label(property_Frame, text="Orientation:").place(x=10, y=5)
    n = StringVar()
    search = ttk.Combobox(property_Frame, width = 23, textvariable = n )
    search['values'] = ('Portrait')
    search.place(x=10,y=25)
    search.current(0)

    text=Text(property_Frame,width=50).place(x=250, y=5,height=350)

    btn=Button(property_Frame, text="Advanced",command=property2).place(x=550, y=380)
    btn=Button(property_Frame,compound = LEFT,image=tick  ,text="OK", width=60,).place(x=430, y=420)
    btn=Button(property_Frame,compound = LEFT,image=cancel , text="Cancel", width=60,).place(x=550, y=420)     


    
  if(False):
      messagebox.showwarning("FBilling Revelution 2020", "Customer is required, Please select customer for this invoice\nbefore printing")
  elif(False):
      messagebox.showinfo("FBilling Revelution 2020", "Print job has been completed.")
  else:
      print1=Toplevel()
      print1.title("Print")
      print1.geometry("670x400+240+150")
      
      printerframe=LabelFrame(print1, text="Printer", height=80, width=650)
      printerframe.place(x=7, y=5)      
      name=Label(printerframe, text="Name:").place(x=10, y=5)
      e1= ttk.Combobox(printerframe, width=40).place(x=70, y=5)
      where=Label(printerframe, text="Where:").place(x=10, y=30)
      printocheckvar=IntVar()
      printochkbtn=Checkbutton(printerframe,text="Print to file",variable=printocheckvar,onvalue=1,offvalue=0,height=1,width=10)
      printochkbtn.place(x=450, y=30)
      btn=Button(printerframe, text="Properties", width=10,command=property1).place(x=540, y=5)

      pageslblframe=LabelFrame(print1, text="Pages", height=140, width=320)
      pageslblframe.place(x=10, y=90)
      radvar=IntVar()
      radioall=Radiobutton(pageslblframe, text="All", variable=radvar, value="1").place(x=10, y=5)
      radiocpage=Radiobutton(pageslblframe, text="Current Page", variable=radvar, value="2").place(x=10, y=25)
      radiopages=Radiobutton(pageslblframe, text="Pages: ", variable=radvar, value="3").place(x=10, y=45)
      pagecountentry = Entry(pageslblframe, width=23).place(x=80, y=47)
      pageinfolabl=Label(pageslblframe, text="Enter page numbers and/or page ranges\nseperated by commas. For example:1,3,5-12")
      pageinfolabl.place(x=5, y=75)

      copylblframe=LabelFrame(print1, text="Copies", height=140, width=320)
      copylblframe.place(x=335, y=90)
      nolabl=Label(copylblframe, text="Number of copies").place(x=5, y=5)      
      noentry = Entry(copylblframe, width=18).place(x=130, y=5)      
      one=Frame(copylblframe, width=30, height=40, bg="black").place(x=20, y=40)     
      two=Frame(copylblframe, width=30, height=40, bg="grey").place(x=15, y=45)     
      three=Frame(copylblframe, width=30, height=40, bg="white").place(x=10, y=50)      
      four=Frame(copylblframe, width=30, height=40, bg="black").place(x=80, y=40)      
      fiv=Frame(copylblframe, width=30, height=40, bg="grey").place(x=75, y=45)      
      six=Frame(copylblframe, width=30, height=40, bg="white").place(x=70, y=50)      
      collatecheckvar=IntVar()
      collatechkbtn=Checkbutton(copylblframe,text="Collate",variable=collatecheckvar,onvalue=1,offvalue=0,height=1,width=10)
      collatechkbtn.place(x=130, y=70)

      othrlblframe=LabelFrame(print1, text="Other", height=120, width=320)
      othrlblframe.place(x=10, y=235)
      printlb=Label(othrlblframe, text="Print").place(x=5, y=0)
      dropprint = ttk.Combobox(othrlblframe, width=23).place(x=80, y=0)
      orderlb=Label(othrlblframe, text="Order").place(x=5, y=25)
      dropord = ttk.Combobox(othrlblframe, width=23).place(x=80, y=25)
      duplexlb=Label(othrlblframe, text="Duplex").place(x=5, y=50)
      droplex = ttk.Combobox(othrlblframe, width=23).place(x=80, y=50)

      prmodelblframe=LabelFrame(print1, text="Print mode", height=120, width=320)
      prmodelblframe.place(x=335, y=235)
      dropscal = ttk.Combobox(prmodelblframe, width=30).place(x=5, y=5)
      poslb=Label(prmodelblframe, text="Print on sheet").place(x=5, y=35)
      droppos = ttk.Combobox(prmodelblframe, width=10).place(x=155, y=35)

      okbtn=Button(print1,compound = LEFT,image=tick , text="Ok", width=60).place(x=460, y=370)
      canbtn=Button(print1,compound = LEFT,image=cancel, text="Cancel", width=60).place(x=570, y=370)
      


#email
      
def email_invoice_recurring():
  mailDetail=Toplevel()
  mailDetail.title("Invoice E-Mail")
  mailDetail.geometry("1080x550")
  mailDetail.resizable(False, False)
  def my_SMTP():
      if True:
          em_ser_conbtn.destroy()
          mysmtpservercon=LabelFrame(account_Frame,text="SMTP server connection(ask your ISP for your SMTP settings)", height=165, width=380)
          mysmtpservercon.place(x=610, y=110)
          lbl_hostn=Label(mysmtpservercon, text="Hostname").place(x=5, y=10)
          hostnent=Entry(mysmtpservercon, width=30).place(x=80, y=10)
          lbl_portn=Label(mysmtpservercon, text="Port").place(x=5, y=35)
          portent=Entry(mysmtpservercon, width=30).place(x=80, y=35)
          lbl_usn=Label(mysmtpservercon, text="Username").place(x=5, y=60)
          unament=Entry(mysmtpservercon, width=30).place(x=80, y=60)
          lbl_pasn=Label(mysmtpservercon, text="Password").place(x=5, y=85)
          pwdent=Entry(mysmtpservercon, width=30).place(x=80, y=85)
          ssl_chkvar=IntVar()
          ssl_chkbtn=Checkbutton(mysmtpservercon, variable=ssl_chkvar, text="This server requires a secure connection(SSL)", onvalue=1, offvalue=0)
          ssl_chkbtn.place(x=50, y=110)
          em_ser_conbtn1=Button(account_Frame, text="Test E-mail Server Connection").place(x=610, y=285)
      else:
          pass
    
  style = ttk.Style()
  style.theme_use('default')
  style.configure('TNotebook.Tab', background="#999999", padding=5)
  email_Notebook = ttk.Notebook(mailDetail)
  email_Frame = Frame(email_Notebook, height=500, width=1080)
  account_Frame = Frame(email_Notebook, height=550, width=1080)
  email_Notebook.add(email_Frame, text="E-mail")
  email_Notebook.add(account_Frame, text="Account")
  email_Notebook.place(x=0, y=0)

  messagelbframe=LabelFrame(email_Frame,text="Message", height=500, width=730)
  messagelbframe.place(x=5, y=5)
  lbl_emailtoaddr=Label(messagelbframe, text="Email to address").place(x=5, y=5)
  emailtoent=Entry(messagelbframe, width=50).place(x=120, y=5)
  sendemail_btn=Button(messagelbframe, text="Send Email", width=10, height=1,command=addacnt).place(x=600, y=10)
  lbl_carcopyto=Label(messagelbframe, text="Carbon copy to").place(x=5, y=32)
  carcopyent=Entry(messagelbframe, width=50).place(x=120, y=32)
  stopemail_btn=Button(messagelbframe, text="Stop sending", width=10, height=1).place(x=600, y=40)
  lbl_subject=Label(messagelbframe, text="Subject").place(x=5, y=59)
  subent=Entry(messagelbframe, width=50).place(x=120, y=59)

  
  style = ttk.Style()
  style.theme_use('default')
  style.configure('TNotebook.Tab', background="#999999", width=20, padding=5)
  mess_Notebook = ttk.Notebook(messagelbframe)
  emailmessage_Frame = Frame(mess_Notebook, height=350, width=710)
  htmlsourse_Frame = Frame(mess_Notebook, height=350, width=710)
  mess_Notebook.add(emailmessage_Frame, text="E-mail message")
  mess_Notebook.add(htmlsourse_Frame, text="Html sourse code")
  mess_Notebook.place(x=5, y=90)

  btn1=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=selectall).place(x=0, y=1)

  
  btn2=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=cut).place(x=36, y=1)
  btn3=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=copy).place(x=73, y=1)
  btn4=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=paste).place(x=105, y=1)
  btn5=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=undo).place(x=140, y=1)
  btn6=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=redo).place(x=175, y=1)
  btn7=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=bold).place(x=210, y=1)
  btn8=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=italics).place(x=245, y=1)
  btn9=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=underline).place(x=280, y=1)
  btn10=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=left).place(x=315, y=1)
  btn11=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=right).place(x=350, y=1)
  btn12=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=center).place(x=385, y=1)
  btn13=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=hyperlink).place(x=420, y=1)
  
  btn14=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=remove).place(x=455, y=1)


  dropcomp = ttk.Combobox(emailmessage_Frame, width=12, height=3).place(x=500, y=5)
  dropcompo = ttk.Combobox(emailmessage_Frame, width=6, height=3).place(x=600, y=5)
  mframe=Frame(emailmessage_Frame, height=350, width=710, bg="white")
  mframe.place(x=0, y=28)



  btn1=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=selectall).place(x=0, y=1)

  
  btn2=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=cut).place(x=36, y=1)
  btn3=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=copy).place(x=73, y=1)
  btn4=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=paste).place(x=105, y=1)
  mframe=Frame(htmlsourse_Frame, height=350, width=710, bg="white")
  mframe.place(x=0, y=28)

  attachlbframe=LabelFrame(email_Frame,text="Attachment(s)", height=350, width=280)
  attachlbframe.place(x=740, y=5)
  htcodeframe=Frame(attachlbframe, height=220, width=265, bg="white").place(x=5, y=5)
  lbl_btn_info=Label(attachlbframe, text="Double click on attachment to view").place(x=30, y=230)
  btn17=Button(attachlbframe, width=20, text="Add attacment file...").place(x=60, y=260)
  btn18=Button(attachlbframe, width=20, text="Remove attacment").place(x=60, y=295)
  lbl_tt_info=Label(email_Frame, text="You can create predefined invoice, order, estimate\nand payment receipt email templates under Main\nmenu/Settings/E-Mail templates tab")
  lbl_tt_info.place(x=740, y=370)

  ready_frame=Frame(mailDetail, height=20, width=1080, bg="#b3b3b3").place(x=0,y=530)
  
  sendatalbframe=LabelFrame(account_Frame,text="E-Mail(Sender data)",height=270, width=600)
  sendatalbframe.place(x=5, y=5)
  lbl_sendermail=Label(sendatalbframe, text="Your company email address").place(x=5, y=30)
  sentent=Entry(sendatalbframe, width=40).place(x=195, y=30)
  lbl_orcompanyname=Label(sendatalbframe, text="Your name or company name").place(x=5, y=60)
  nament=Entry(sendatalbframe, width=40).place(x=195, y=60)
  lbl_reply=Label(sendatalbframe, text="Reply to email address").place(x=5, y=90)
  replyent=Entry(sendatalbframe, width=40).place(x=195, y=90)
  lbl_sign=Label(sendatalbframe, text="Signature").place(x=5, y=120)
  signent=Entry(sendatalbframe,width=50).place(x=100, y=120,height=75)
  confirm_chkvar=IntVar()
  confirm_chkbtn=Checkbutton(sendatalbframe, variable=confirm_chkvar, text="Confirmation reading", onvalue=1, offvalue=0)
  confirm_chkbtn.place(x=200, y=215)
  btn18=Button(account_Frame, width=15, text="Save settings",command=savesettings).place(x=25, y=285)

  sendatalbframe=LabelFrame(account_Frame,text="SMTP Server",height=100, width=380)
  sendatalbframe.place(x=610, y=5)
  servar=IntVar()
  SMTP_rbtn=Radiobutton(sendatalbframe, text="Use the Built-In SMTP Server Settings", variable=servar, value=1)
  SMTP_rbtn.place(x=10, y=10)
  MySMTP_rbtn=Radiobutton(sendatalbframe, text="Use My Own SMTP Server Settings(Recommended)", variable=servar, value=2, command=my_SMTP)
  MySMTP_rbtn.place(x=10, y=40)
  em_ser_conbtn=Button(account_Frame, text="Test E-mail Server Connection")
  em_ser_conbtn.place(x=710, y=110)




#sms notification order
  
def sms():
  send_SMS=Toplevel()
  send_SMS.geometry("700x480+240+150")
  send_SMS.title("Send SMS notification")

  style = ttk.Style()
  style.theme_use('default')
  style.configure('TNotebook.Tab', background="#999999", padding=5)
  sms_Notebook = ttk.Notebook(send_SMS)
  SMS_Notification = Frame(sms_Notebook, height=470, width=700)
  SMS_Service_Account = Frame(sms_Notebook, height=470, width=700)
  sms_Notebook.add(SMS_Notification, text="SMS Notification")
  sms_Notebook.add(SMS_Service_Account, text="SMS Service Account")
  sms_Notebook.place(x=0, y=0)

  numlbel=Label(SMS_Notification, text="SMS number or comma seperated SMS number list(Please start each SMS number with the country code)")
  numlbel.place(x=10, y=10)
  numentry=Entry(SMS_Notification, width=92).place(x=10, y=30)
  stexbel=Label(SMS_Notification, text="SMS Text").place(x=10, y=60)
  stex=Entry(SMS_Notification, width=40).place(x=10, y=85,height=120)
  
  dclbel=Label(SMS_Notification, text="Double click to insert into text")
  dclbel.place(x=410, y=60)
  dcl=Entry(SMS_Notification, width=30)
  dcl.place(x=400, y=85,height=200)
  
  smstype=LabelFrame(SMS_Notification, text="SMS message type", width=377, height=60)
  smstype.place(x=10, y=223)
  snuvar=IntVar()
  normal_rbtn=Radiobutton(smstype, text="Normal SMS(160 chars)", variable=snuvar, value=1)
  normal_rbtn.place(x=5, y=5)
  unicode_rbtn=Radiobutton(smstype, text="Unicode SMS(70 chars)", variable=snuvar, value=2)
  unicode_rbtn.place(x=190, y=5)
  tiplbf=LabelFrame(SMS_Notification, text="Tips", width=680, height=120)
  tiplbf.place(x=10, y=290)
  tiplabl=Label(tiplbf,justify=LEFT,fg="red",  text="Always start the SMS nymber with the country code. Do not use the + sign at the beginning(example\nUS number:8455807546). Do not use any special characters in your normal SMS text. Please use the\nstndard SMS characters or the English alphabet and numbers only. Otherwise the SMS will be\nunreadable or undeliverable. If you need to enter international characters, accents,email address, or\nspecial characters to the SMS text field then choose the Unicode SMS format.")
  tiplabl.place(x=5, y=5)

  btn1=Button(SMS_Notification, width=20, text="Send SMS notification").place(x=10, y=420)
  btn2=Button(SMS_Notification, width=25, text="Confirm SMS cost before sending").place(x=280, y=420)
  btn3=Button(SMS_Notification, width=15, text="Cancel").place(x=550, y=420)
  

  smstype=LabelFrame(SMS_Service_Account, text="Select the notification service provider", width=670, height=65)
  smstype.place(x=10, y=5)
  snumvar=IntVar()
  normal_rbtn=Radiobutton(smstype,text="BULKSMS(www.bulksms.com)",variable=snumvar,value=1,)
  normal_rbtn.place(x=5, y=5)
  unicode_rbtn=Radiobutton(smstype, text="Unicode SMS(70 chars)-Recommended", variable=snumvar, value=2)
  unicode_rbtn.place(x=290, y=5)

  sms1type=LabelFrame(SMS_Service_Account, text="Your BULKSMS.COM Account", width=670, height=100)
  sms1type.place(x=10, y=80)
  name=Label(sms1type, text="Username").place(x=10, y=5)
  na=Entry(sms1type, width=20).place(x=100, y=5)
  password=Label(sms1type, text="Password").place(x=10, y=45)
  pas=Entry(sms1type, width=20).place(x=100, y=45)
  combo=Label(sms1type, text="Route").place(x=400, y=5)
  n = StringVar()
  combo1 = ttk.Combobox(sms1type, width = 20, textvariable = n ).place(x=450,y=5)
  btn1=Button(sms1type, width=10, text="Save settings").place(x=550, y=45)

  
  tiplbf=LabelFrame(SMS_Service_Account, text="Terms of service", width=680, height=250)
  tiplbf.place(x=10, y=190)
  tiplabl=Label(tiplbf,justify=LEFT,fg="red",  text="The SMS notification service is not free.This service costs you creadit.You must have your own account\nat BULKSMS.COM and you need to have sufficient creadit and an active internet connection to use\nthis feature.Please review all fields in this form for accuracy")
  tiplabl.place(x=0, y=5)
  tiplabl1=Label(tiplbf,justify=LEFT,fg="black",  text="visit www.bulksms.com website to create your own account.please make sure the BULKSMS .COM\n service works well in your country before you busy creadit")
  tiplabl1.place(x=0, y=60)
  tiplabl2=Label(tiplbf,justify=LEFT,fg="black",  text="Our SMS notification tool comes without any warranty.our software only forwards your SMS message\nthe BULKSMS API server .The BULKSMS API server will try to sent SMS message your recipient")
  tiplabl2.place(x=0, y=100)
  tiplabl3=Label(tiplbf,justify=LEFT,fg="red",  text="Please note that you access and use the SMS notification tool your own risk.F-Billing software is not\nresponsible for any type of loss or damage or undelivered SMS massage which you may as a result\nof accessing and using the SMS notification service.")
  tiplabl3.place(x=0, y=140)
  checkvar1=IntVar()
  chkbtn1=Checkbutton(tiplbf,text="I have read and agree to the terms of service above",variable=checkvar1,onvalue=1,offvalue=0).place(x=70, y=200)  



#print preview order
def printpreview():
  messagebox.showerror("F-Billing Revolution","Customer is required,please select customer for this order before printing.")

################VIEW/EDITinvoice#######################################################

def edit_invoice():
  try:
    itemid = invotree.item(invotree.focus())["values"][1]
    invonewid = invotree.item(invotree.focus())["values"][5]
    print(invonewid)
    try:
      sql5='SELECT * FROM invoice WHERE invoiceid=%s'
      val5=(itemid,)
      fbcursor.execute(sql5,val5,)
      new=fbcursor.fetchone()
      print(new)

      if invonewid=="void":
        # void_invoice2()
        for x in (selectcustomer2, addline2, deleteline2, markinvo2):
          x.config(state = 'disabled')
        for y in(cmb1,spt1,eml,smsno,e2,e3,xtracstnme,xtracst,tmplte,dscntrte,taxx):
          y.config(state = 'disabled')
        for z in (addrs1,adrs):
          z.config(state = 'disabled')
      else:
        pass
    except:
      pass
    #   void_invoice2()
    # else:
    #   pass

  # sql = "select * from Orders where orderid = %s"
  # val = (itemid, )
  # fbcursor.execute(sql, val)
  # osdata = fbcursor.fetchone()

  # # itemid = invotree.item(invotree.focus())["values"][1]
  # sql = "select * from Orders where orderid = %s"
  # # val = (itemid, )
  # fbcursor.execute(sql,)
  # psdata = fbcursor.fetchone()
  # print(psdata)

        
    pop=Toplevel(midFrame)
    pop.title("Invoice")
    pop.geometry("950x690+150+0")

    


    #select customer
    def selectcustomer1():
      global custselection
      custselection=Toplevel()
      custselection.title("Select Customer")
      custselection.geometry("930x650+240+10")
      custselection.resizable(False, False)


      #add new customer
      def createcustomer1():
        global checkvar1,checkvar2,custid,bname,baddress,cat,sname,saddress,contp,cemail,ctel,cfax,cmob,scontp,scemail,sctel,scfax,ccountry,ccity,cnotes
        ven=Toplevel(midFrame)
        ven.title("Add new vendor")
        ven.geometry("930x650+240+10")
        checkvar1=IntVar()
        checkvar2=IntVar()
        radio=IntVar()
        createFrame=Frame(ven, bg="#f5f3f2", height=650)
        createFrame.pack(side="top", fill="both")
        labelframe1 = LabelFrame(createFrame,text="Customer",bg="#f5f3f2",font=("arial",15))
        labelframe1.place(x=10,y=5,width=910,height=600)
        text1=Label(labelframe1, text="Customer ID:",bg="#f5f3f2",fg="blue").place(x=5 ,y=10)
        custid=Entry(labelframe1,width=25)
        custid.place(x=150,y=10)
        text2=Label(labelframe1, text="Category:",bg="#f5f3f2").place(x=390 ,y=10)
        cat=ttk.Combobox(labelframe1,width=25,value="Default")
        cat.place(x=460 ,y=10)
        text3=Label(labelframe1, text="Status:",bg="#f5f3f2").place(x=710 ,y=10)
        Checkbutton(labelframe1,text="Active",variable=checkvar1,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=760 ,y=10)
        
        labelframe2 = LabelFrame(labelframe1,text="Invoice to (appears on invoices)",bg="#f5f3f2")
        labelframe2.place(x=5,y=40,width=420,height=150)
        name = Label(labelframe2, text="Ship to name:",bg="#f5f3f2",fg="blue").place(x=5,y=5)
        sname = Entry(labelframe2,width=28)
        sname.place(x=130,y=5)
        addr = Label(labelframe2, text="Address:",bg="#f5f3f2",fg="blue").place(x=5,y=40)
        saddress = Entry(labelframe2,width=28)
        saddress.place(x=130,y=40,height=80)
        
        btn1=Button(labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=440, y=90)

        labelframe3 = LabelFrame(labelframe1,text="Ship to (appears on invoices)",bg="#f5f3f2")
        labelframe3.place(x=480,y=40,width=420,height=150)
        name = Label(labelframe3, text="Business name:",bg="#f5f3f2").place(x=5,y=5)
        bname = Entry(labelframe3,width=28)
        bname.place(x=130,y=5)
        addr = Label(labelframe3, text="Address:",bg="#f5f3f2").place(x=5,y=40)
        baddress = Entry(labelframe3,width=28)
        baddress.place(x=130,y=40,height=80)
        
        labelframe4 = LabelFrame(labelframe1,text="Contact",bg="#f5f3f2")
        labelframe4.place(x=5,y=195,width=420,height=150)
        name = Label(labelframe4, text="Contact person:",bg="#f5f3f2").place(x=5,y=5)
        contp = Entry(labelframe4,width=28)
        contp.place(x=130,y=5)
        email = Label(labelframe4, text="E-mail address:",bg="#f5f3f2",fg="blue").place(x=5,y=35)
        cemail = Entry(labelframe4,width=28)
        cemail.place(x=130,y=35)
        tel = Label(labelframe4, text="Tel.number:",bg="#f5f3f2").place(x=5,y=65)
        ctel = Entry(labelframe4,width=11)
        ctel.place(x=130,y=65)
        fax = Label(labelframe4, text="Fax:",bg="#f5f3f2").place(x=240,y=65)
        cfax = Entry(labelframe4,width=11)
        cfax.place(x=280,y=65)
        sms = Label(labelframe4, text="Mobile number for SMS notifications:",bg="#f5f3f2").place(x=5,y=95)
        cmob = Entry(labelframe4,width=15)
        cmob.place(x=248,y=95)      

        btn1=Button(labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=440, y=250)

        
        labelframe5 = LabelFrame(labelframe1,text="Ship to contact",bg="#f5f3f2")
        labelframe5.place(x=480,y=195,width=420,height=125)
        name = Label(labelframe5, text="Contact person:",bg="#f5f3f2").place(x=5,y=5)
        scontp = Entry(labelframe5,width=28)
        scontp.place(x=130,y=5)
        email = Label(labelframe5, text="E-mail address:",bg="#f5f3f2").place(x=5,y=35)
        scemail = Entry(labelframe5,width=28)
        scemail.place(x=130,y=35)
        tel = Label(labelframe5, text="Tel.number:",bg="#f5f3f2").place(x=5,y=65)
        sctel = Entry(labelframe5,width=11)
        sctel.place(x=130,y=65)
        fax = Label(labelframe5, text="Fax:",bg="#f5f3f2").place(x=240,y=65)
        scfax = Entry(labelframe5,width=11)
        scfax.place(x=280,y=65)

        labelframe6 = LabelFrame(labelframe1,text="Contact",bg="#f5f3f2")
        labelframe6.place(x=5,y=350,width=420,height=100)
        Checkbutton(labelframe6,text="Tax Exempt",variable=checkvar2,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=5 ,y=5)
        tax = Label(labelframe6, text="Specific Tax1 %:",bg="#f5f3f2").place(x=180,y=5)
        e1 = Entry(labelframe6,width=10).place(x=290,y=5)
        discount = Label(labelframe6, text="Discount%:",bg="#f5f3f2").place(x=5,y=35)
        e2 = Entry(labelframe6,width=10).place(x=100,y=35)

        labelframe7 = LabelFrame(labelframe1,text="Contact",bg="#f5f3f2")
        labelframe7.place(x=480,y=330,width=420,height=100)
        country = Label(labelframe7, text="country:",bg="#f5f3f2").place(x=5,y=5)
        ccountry = Entry(labelframe7,width=28)
        ccountry.place(x=130,y=5)
        city = Label(labelframe7, text="City:",bg="#f5f3f2").place(x=5,y=35)
        ccity = Entry(labelframe7,width=28)
        ccity.place(x=130,y=35)

        labelframe8 = LabelFrame(labelframe1,text="Customer Type",bg="#f5f3f2")
        labelframe8.place(x=5,y=460,width=420,height=100)
        R1=Radiobutton(labelframe8,text=" Client ",variable=radio,value=1,bg="#f5f3f2").place(x=5,y=15)
        R2=Radiobutton(labelframe8,text=" Vendor ",variable=radio,value=2,bg="#f5f3f2").place(x=150,y=15)
        R3=Radiobutton(labelframe8,text=" Both(client/vendor)",variable=radio,value=3,bg="#f5f3f2").place(x=250,y=15)
        

        labelframe9 = LabelFrame(labelframe1,text="Notes",bg="#f5f3f2")
        labelframe9.place(x=480,y=430,width=420,height=150)
        cnotes = Entry(labelframe9)
        cnotes.place(x=10,y=5,height=100,width=390)

        btn1=Button(ven,width=60,height=10,bg="#f5f3f2",compound = LEFT,image=tick ,text="OK",command=ord_cust_reg).place(x=20, y=615)
        btn2=Button(ven,width=60,height=10,bg="#f5f3f2",compound = LEFT,image=cancel,text="Cancel").place(x=800, y=615)
          
                

      # enter=Label(custselection, text="Enter filter text").place(x=5, y=10)
      # e1=Entry(custselection, width=20).place(x=110, y=10)
      # text=Label(custselection, text="Filtered column").place(x=340, y=10)
      # e2=Entry(custselection, width=20).place(x=450, y=10)

      def cancelcustomselection1():
        custselection.destroy()

      global cusventtree1
      cusventtree1=ttk.Treeview(custselection, height=27)
      cusventtree1["columns"]=["1","2","3","4"]
      cusventtree1.column("#0", width=35)
      cusventtree1.column("1", width=160)
      cusventtree1.column("2", width=160)
      cusventtree1.column("3", width=140)
      cusventtree1.column("4", width=140)
      cusventtree1.heading("#0",text="")
      cusventtree1.heading("1",text="Customer/Ventor ID")
      cusventtree1.heading("2",text="Customer/Ventor Name")
      cusventtree1.heading("3",text="Tel.")
      cusventtree1.heading("4",text="Contact Person")
      cusventtree1.place(x=5, y=45)

      def filter_cust():
      # global filttxt 
   
       filtr = filttxt.get()
       for record in cusventtree1.get_children():
         cusventtree1.delete(record)
  
       sqlcusven = "SELECT * FROM Customer WHERE businessname=%s"
       valcusven = (filtr, )
       fbcursor.execute(sqlcusven, valcusven)
       records = fbcursor.fetchall()
       print(records)

  
       count=0
       for i in records:
         if True:
          cusventtree1.insert(parent='', index='end', iid=i, text='', values=(i[0],i[4],i[10],i[8]))  
         else:
           pass
       count += 1

    # global filttxt
      enter=Label(custselection, text="Enter filter text").place(x=5, y=10)
      filttxt=Entry(custselection, width=20)
      filttxt.place(x=110, y=10)
      fltrbutton=Button(custselection,text = 'Click Here',command=filter_cust)
      fltrbutton.place(x=236,y=7,height=25,width=70)


      
      fbcursor.execute('SELECT * FROM Customer;') 
      j = 0
      for i in fbcursor:
        cusventtree1.insert(parent='', index='end', iid=i, text='', values=(i[0],i[4],i[10],i[8]))
        j += 1
    


      categtree=ttk.Treeview(custselection, height=27)
      categtree["columns"]=["1"]
      categtree.column("#0", width=35, minwidth=20)
      categtree.column("1", width=205, minwidth=25, anchor=CENTER)    
      categtree.heading("#0",text="", anchor=W)
      categtree.heading("1",text="View filter by category", anchor=CENTER)
      categtree.place(x=660, y=45)


      def items_selected(event):
        selected_indices = listbox.curselection()
        selected_filter = ",".join([listbox.get(i) for i in selected_indices])

        sqloooo = 'select * from Productservice'
        fbcursor.execute(sqloooo)
        pandsdatazbn = fbcursor.fetchall()

        psql = "select * from Productservice where serviceornot = %s"
        val = ('Not Service', )
        fbcursor.execute(psql, val)
        pdata = fbcursor.fetchall()
    
        ssql = "select * from Productservice where serviceornot = %s"
        val = ('Service', )
        fbcursor.execute(ssql, val)
        sdata = fbcursor.fetchall()

        if selected_filter == "View all records":
          for record in editprodtree.get_children():
            editprodtree.delete(record)
          countp = 0
          for i in pandsdatazbn:
            editprodtree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7],i[12],i[13]))
          countp += 1
        elif selected_filter == "View all products":
          for record in editprodtree.get_children():
            editprodtree.delete(record)
          countp = 0
          for i in pdata:
            editprodtree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7],i[12],i[13]))
          countp += 1
        else: 
          if selected_filter == "View all services":
            for record in editprodtree.get_children():
              editprodtree.delete(record)
            countp = 0
            for i in sdata:
              editprodtree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7],i[12],i[13]))
            countp += 1
        # mydb.close()
  
      listbox = Listbox(custselection,height = 33,  
                            width = 40,  
                            bg = "white",
                            activestyle = 'dotbox',  
                            fg = "black",
                            highlightbackground="white")
     
      listbox.insert(0, "                               View all records")
      listbox.insert(1, "                               View all products")
      listbox.insert(2, "                               View all services")
      listbox.place(x=660,y=65,)
      listbox.bind('<<ListboxSelect>>', items_selected)


      # scrollbar = Scrollbar(custselection)
      # scrollbar.place(x=640, y=45, height=560)
      # scrollbar.config( command=tree.yview )
      scrollbar = Scrollbar(custselection)
      scrollbar.place(x=1016+300+25, y=120, height=280+20)
      btn1=Button(custselection,compound = LEFT,image=tick ,text="ok",command=prodtreefetch1, width=60).place(x=15, y=610)
      btn1=Button(custselection,compound = LEFT,image=tick,text="Edit selected customer", width=150,command=createcustomer1).place(x=250, y=610)
      btn1=Button(custselection,compound = LEFT,image=tick, text="Add new customer", width=150,command=createcustomer1).place(x=435, y=610)
      btn1=Button(custselection,compound = LEFT,image=cancel ,text="Cancel", width=60,command=cancelcustomselection1).place(x=740, y=610)   



      

    #add new line item
    def addnewline():
      newselection=Toplevel()
      newselection.title("Select Product")
      newselection.geometry("930x650+240+10")
      newselection.resizable(False, False)


      #add new product
      def add_product():  
        global codeentry,nameentry,country,desentry,unitentry,pcsentry,costentry,priceentry,stockentry,lowentry,wareentry,txt,checkvarStatus,checkvarStatus2,checkvarStatus3
        top = Toplevel()  
        top.title("Add a new Product/Service")
        p2 = PhotoImage(file = 'images/fbicon.png')
        top.iconphoto(False, p2)
      
        top.geometry("700x550+400+15")
        tabControl = ttk.Notebook(top)
        s = ttk.Style()
        s.theme_use('default')
        s.configure('TNotebook.Tab', background="#999999",padding=10,bd=0)




        tab1 = ttk.Frame(tabControl)
        tab2 = ttk.Frame(tabControl)
      
        tabControl.add(tab1,compound = LEFT, text ='Product/Service')
        tabControl.add(tab2,compound = LEFT, text ='Product Image')
      
        tabControl.pack(expand = 1, fill ="both")
      
        innerFrame = Frame(tab1,bg="#f5f3f2", relief=GROOVE)
        innerFrame.pack(side="top",fill=BOTH)

        Customerlabelframe = LabelFrame(innerFrame,text="Product/Service",width=580,height=485)
        Customerlabelframe.pack(side="top",fill=BOTH,padx=10)

        code1=Label(Customerlabelframe,text="Code or SKU:",fg="blue",pady=10,padx=10)
        code1.place(x=20,y=0)
        codeentry = Entry(Customerlabelframe,width=35)
        codeentry.place(x=120,y=8)

        checkvarStatus=IntVar()
        status1=Label(Customerlabelframe,text="Status:")
        status1.place(x=500,y=8)
        Button1 = Checkbutton(Customerlabelframe,
                          variable = checkvarStatus,text="Active",compound="right",
                          onvalue =0 ,
                          offvalue = 1,
                        
                          width = 10)

        Button1.place(x=550,y=5)

        category1=Label(Customerlabelframe,text="Category:",pady=5,padx=10)
        category1.place(x=20,y=40)
        n = StringVar()
        country = ttk.Combobox(Customerlabelframe, width = 40, textvariable = n )
        
        country['values'] = ('Default',' India',' China',' Australia',' Nigeria',' Malaysia',' Italy',' Turkey',)
        
        country.place(x=120,y=45)
        country.current(0)


        name1=Label(Customerlabelframe,text="Name :",fg="blue",pady=5,padx=10)
        name1.place(x=20,y=70)
        nameentry = Entry(Customerlabelframe,width=60)
        nameentry.place(x=120,y=75)

        des1=Label(Customerlabelframe,text="Description :",pady=5,padx=10)
        des1.place(x=20,y=100)
        desentry = Entry(Customerlabelframe,width=60)
        desentry.place(x=120,y=105)

        uval = IntVar(Customerlabelframe, value='$0.00')
        unit1=Label(Customerlabelframe,text="Unit Price:",fg="blue",pady=5,padx=10)
        unit1.place(x=20,y=130)
        unitentry = Entry(Customerlabelframe,width=20,textvariable=uval)
        unitentry.place(x=120,y=135)

        pcsval = IntVar(Customerlabelframe, value='0')
        pcs1=Label(Customerlabelframe,text="Pcs/Weight:",fg="blue",pady=5,padx=10)
        pcs1.place(x=320,y=140)
        pcsentry = Entry(Customerlabelframe,width=20,textvariable=pcsval)
        pcsentry.place(x=410,y=140)

        costval = IntVar(Customerlabelframe, value='$0.00')
        cost1=Label(Customerlabelframe,text="Cost:",pady=5,padx=10)
        cost1.place(x=20,y=160)
        costentry = Entry(Customerlabelframe,width=20,textvariable=costval)
        costentry.place(x=120,y=165)

        priceval = IntVar(Customerlabelframe, value='$0.00')
        price1=Label(Customerlabelframe,text="(Price-Cost):",pady=5,padx=10)
        price1.place(x=20,y=190)
        priceentry = Entry(Customerlabelframe,width=20,textvariable=priceval)
        priceentry.place(x=120,y=195)

        checkvarStatus2=IntVar()
      
        Button2 = Checkbutton(Customerlabelframe,variable = checkvarStatus2,
                          text="Taxable Tax1rate",compound="right",
                          onvalue =0 ,
                          offvalue = 1,
                          height=2,
                          width = 12)

        Button2.place(x=415,y=170)


        checkvarStatus3=IntVar()
      
        Button3 = Checkbutton(Customerlabelframe,variable = checkvarStatus3,
                          text="No stock Control",
                          onvalue =1 ,
                          offvalue = 0,
                          height=3,
                          width = 15)

        Button3.place(x=40,y=220)


        stockval = IntVar(Customerlabelframe)
        stock1=Label(Customerlabelframe,text="Stock:",pady=5,padx=10)
        stock1.place(x=90,y=260)
        stockentry = Entry(Customerlabelframe,width=15,textvariable=stockval)
        stockentry.place(x=150,y=265)

        lowval = IntVar(Customerlabelframe)
        low1=Label(Customerlabelframe,text="Low Stock Warning Limit:",pady=5,padx=10)
        low1.place(x=300,y=260)
        lowentry = Entry(Customerlabelframe,width=10,textvariable=lowval)
        lowentry.place(x=495,y=265)

      
        ware1=Label(Customerlabelframe,text="Warehouse:",pady=5,padx=10)
        ware1.place(x=60,y=290)
        wareentry = Entry(Customerlabelframe,width=50)
        wareentry.place(x=150,y=295)

        text1=Label(Customerlabelframe,text="Private notes(not appears on invoice):",pady=5,padx=10)
        text1.place(x=20,y=330)

        txt = scrolledtext.ScrolledText(Customerlabelframe, undo=True,width=72,height=4)
        txt.place(x=32,y=358)




        okButton = Button(innerFrame,compound = LEFT,image=tick , text ="Ok",command=ord_prdt_reg,width=60)
        okButton.pack(side=LEFT)

        cancelButton = Button(innerFrame,compound = LEFT,image=cancel ,text="Cancel",width=60)
        cancelButton.pack(side=RIGHT)

        imageFrame = Frame(tab2, relief=GROOVE,height=580)
        imageFrame.pack(side="top",fill=BOTH)

        browseimg=Label(imageFrame,text=" Browse for product image file(recommended image type:JPG,size 480x320 pixels) ",bg='#f5f3f2')
        browseimg.place(x=15,y=35)

        browsebutton=Button(imageFrame,text = 'Browse')
        browsebutton.place(x=580,y=30,height=30,width=50)
        
        removeButton = Button(imageFrame,compound = LEFT,image=cancel, text ="Remove Product Image",width=150)
        removeButton.place(x=400,y=450)



      
                      
      # enter=Label(newselection, text="Enter filter text").place(x=5, y=10)
      # e1=Entry(newselection, width=20).place(x=110, y=10)
      # text=Label(newselection, text="Filtered column").place(x=340, y=10)
      # e2=Entry(newselection, width=20).place(x=450, y=10)
      global editprodtree
      editprodtree=ttk.Treeview(newselection, height=27)
      editprodtree["columns"]=["1","2","3", "4","5"]
      editprodtree.column("#0", width=35)
      editprodtree.column("1", width=160)
      editprodtree.column("2", width=160)
      editprodtree.column("3", width=140)
      editprodtree.column("4", width=70)
      editprodtree.column("5", width=70)
      editprodtree.heading("#0",text="")
      editprodtree.heading("1",text="ID/SKU")
      editprodtree.heading("2",text="Product/Service Name")
      editprodtree.heading("3",text="Unit price")
      editprodtree.heading("4",text="Service")
      editprodtree.heading("5",text="Stock")
      editprodtree.place(x=5, y=45)

      def filter_prod():
      # global filttxt 
   
       filtr = filttxt.get()
       for record in editprodtree.get_children():
         editprodtree.delete(record)
  
       sqlcusven = "SELECT * FROM Productservice WHERE name=%s"
       valcusven = (filtr, )
       fbcursor.execute(sqlcusven, valcusven)
       records = fbcursor.fetchall()
       print(records)

  
       count=0
       for i in records:
         if True:
          editprodtree.insert(parent='', index='end', iid=i, text='', values=(i[0],i[4],i[10],i[8]))  
         else:
           pass
       count += 1

    # global filttxt
      enter=Label(newselection, text="Enter filter text").place(x=5, y=10)
      filttxt=Entry(newselection, width=20)
      filttxt.place(x=110, y=10)
      fltrbutton=Button(newselection,text = 'Click Here',command=filter_prod)
      fltrbutton.place(x=236,y=7,height=25,width=70)

      def cancelnewselection():
       newselection.destroy()
      
      def select_prod2():
          selected = editprodtree.focus()
          global valuep,ttlp
          valuep= editprodtree.item(selected)["values"][0]
          sql = "SELECT * FROM productservice  WHERE productserviceid= %s"
          i=(valuep,)
          fbcursor.execute(sql,i)
          ttlp=0
          j = 0
          for i in fbcursor:
           viewditree.insert(parent='', index='end', iid=i, text='', values=(i[0],i[4],i[5],i[7],1,i[8],i[10],(i[7]*1)))
           for line in viewditree.get_children():
              idsave1=viewditree.item(line)['values'][7]
              ttlp+=idsave1
              j += 1

              
          priceco0.config(text=ttlp)

          valu10= editprodtree.item(selected)["values"][0]
          sqllll = "SELECT * FROM productservice  WHERE productserviceid= %s"
          r=(valu10,)
          fbcursor.execute(sqllll,r)
          child=fbcursor.fetchone()

          sql21= 'INSERT INTO storingproduct(Productserviceid,invoiceid,sku,category,name,description,status,unitprice,peices,cost,taxable,priceminuscost,serviceornot,stock,stocklimit,warehouse,privatenote,quantity) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
          vatree=(child[0],osdata[0],child[2],child[3],child[4],child[5],child[6],child[7],child[8],child[9],child[10],child[11],child[12],child[13],child[14],child[15],child[16],1)
          fbcursor.execute(sql21,vatree,)
          fbilldb.commit()    

          newselection.destroy()

      # def selectp2():
      #     selected = editprodtree.focus()
      #     valuesp= editprodtree.item(selected)["values"][0]
  
      #     sql = "SELECT * FROM productservice  WHERE productserviceid= %s"
      #     i=(valuesp,)
      #     x=fbcursor.execute(sql,i)
      #     print(x)

      #     k = 0
      #     for i in fbcursor:
      #      prstree.insert(parent='', index='end', iid=i, text='', values=(i[4], i[14], i[7], i[9], i[15],i[10],i[12],(i[9]*i[15])))
      #     k += 1

      #     newselection.destroy()

      # def selectp1_and_selectp2():
      #   selectp1()
      #   selectp2()
        
  
  
  
      fbcursor.execute('SELECT * FROM Productservice;') 
      j = 0
      for i in fbcursor:
        editprodtree.insert(parent='', index='end', iid=i, text=' ', values=(i[0],i[4],i[7],i[12],i[13]))
      j += 1
  
  


      categtree=ttk.Treeview(newselection, height=27)
      categtree["columns"]=["1"]
      categtree.column("#0", width=35, minwidth=20)
      categtree.column("1", width=205, minwidth=25, anchor=CENTER)    
      categtree.heading("#0",text="", anchor=W)
      categtree.heading("1",text="View filter by category", anchor=CENTER)
      categtree.place(x=660, y=45)

      def items_selected(event):
        selected_indices = listbox.curselection()
        selected_filter = ",".join([listbox.get(i) for i in selected_indices])

        sqloooo = 'select * from Productservice'
        fbcursor.execute(sqloooo)
        pandsdatazbn = fbcursor.fetchall()

        psql = "select * from Productservice where serviceornot = %s"
        val = ('Not Service', )
        fbcursor.execute(psql, val)
        pdata = fbcursor.fetchall()
    
        ssql = "select * from Productservice where serviceornot = %s"
        val = ('Service', )
        fbcursor.execute(ssql, val)
        sdata = fbcursor.fetchall()

        if selected_filter == "                               View all records":
          # sqloooo = 'SELECT * FROM Productservice'
          # fbcursor.execute(sqloooo)
          # pandsdatazbn = fbcursor.fetchall()
          for record in editprodtree.get_children():
           editprodtree.delete(record)
          countp = 0
          for i in pandsdatazbn:
            editprodtree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7],i[12],i[13]))
          countp += 1
        # elif selected_filter == "                               View all products":
        #   for record in editprodtree.get_children():
        #     editprodtree.delete(record)
        #   countp = 0
        #   for i in pdata:
        #     editprodtree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7],i[12],i[13]))
        #   countp += 1
        # else: 
        #   if selected_filter == "View all services":
        #     for record in editprodtree.get_children():
        #       editprodtree.delete(record)
        #     countp = 0
        #     for i in sdata:
        #       editprodtree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7],i[12],i[13]))
        #     countp += 1
        # mydb.close()
      # def items_selected(event):
      #  selected_indices = listbox.curselection()
      #  selected_filter = ",".join([listbox.get(i) for i in selected_indices])
      #  mydb = mysql.connector.connect(host='localhost', user='root', password='', port='3306', database='fbilldb')
      #  mycursor = mydb.cursor()
      #  sql = 'select * from Productservice'
      #  mycursor.execute(sql)
      #  pandsdatazbn = mycursor.fetchall()
      #  psql = "select * from Productservice where serviceornot = %s"
      #  val = ('0', )
      #  mycursor.execute(psql, val)
      #  pdata = mycursor.fetchall()
       
      #  ssql = "select * from Productservice where serviceornot = %s"
      #  val = ('1', )
      #  mycursor.execute(ssql, val)
      #  sdata = mycursor.fetchall()
      #  if selected_filter == "View all records":
      #    for record in editprodtree.get_children():
      #      editprodtree.delete(record)
      #    countp = 0
      #    for i in pandsdatazbn:
      #      editprodtree.insert(parent='', index='end', iid=countp, text='hello', values=('',i[2],i[4],i[7],i[12],i[13]))
      #      countp += 1
      #  elif selected_filter == "View all products":
      #    for record in editprodtree.get_children():
      #      editprodtree.delete(record)
      #    countp = 0
      #    for i in pdata:
      #      editprodtree.insert(parent='', index='end', iid=countp, text='productdata',values=('',i[2],i[4],i[7],i[12],i[13]))
      #      countp += 1
      #  else:
      #    for record in editprodtree.get_children():
      #      editprodtree.delete(record)
      #    countp = 0
      #    for i in sdata:
      #      editprodtree.insert(parent='', index='end', iid=countp, text='servicedata', values=('',i[2],i[4],i[7],i[12],i[13]))
      #      countp += 1
  
      listbox = Listbox(newselection,height = 33,  
                            width = 40,  
                            bg = "white",
                            activestyle = 'dotbox',  
                            fg = "black",
                            highlightbackground="white")
      
      listbox.insert(0, "                               View all records")
      listbox.insert(1, "                               View all products")
      listbox.insert(2, "                               View all services")
      listbox.place(x=660,y=65,)
      listbox.bind('<<ListboxSelect>>', items_selected)

  
      

      # scrollbar = Scrollbar(newselection)
      # scrollbar.place(x=640, y=45, height=560)
      # scrollbar.config( command=tree.yview )
      scrollbar = Scrollbar(newselection)
      scrollbar.place(x=1016+300+25, y=120, height=280+20)      

      # scrollbar = Scrollbar(newselection)
      # scrollbar.place(x=640, y=45, height=560)
      # scrollbar.config( command=tree.yview )
    

      btn1=Button(newselection,compound = LEFT,image=tick ,text="ok",command=select_prod2,width=60).place(x=15, y=610)
      btn1=Button(newselection,compound = LEFT,image=tick , text="Edit product/Service", width=150,command=add_product).place(x=250, y=610)
      btn1=Button(newselection,compound = LEFT,image=tick , text="Add product/Service", width=150,command=add_product).place(x=435, y=610)
      btn1=Button(newselection,compound = LEFT,image=cancel ,text="Cancel", width=60,command=cancelnewselection).place(x=740, y=610)



    #preview new line
    def previewline():
      messagebox.showerror("F-Billing Revolution","line is required,please select customer for this order before printing.")


    
    #sms notification
    def sms1():
      send_SMS=Toplevel()
      send_SMS.geometry("700x480+240+150")
      send_SMS.title("Send SMS notification")

      style = ttk.Style()
      style.theme_use('default')
      style.configure('TNotebook.Tab', background="#999999", padding=5)
      sms_Notebook = ttk.Notebook(send_SMS)
      SMS_Notification = Frame(sms_Notebook, height=470, width=700)
      SMS_Service_Account = Frame(sms_Notebook, height=470, width=700)
      sms_Notebook.add(SMS_Notification, text="SMS Notification")
      sms_Notebook.add(SMS_Service_Account, text="SMS Service Account")
      sms_Notebook.place(x=0, y=0)

      numlbel=Label(SMS_Notification, text="SMS number or comma seperated SMS number list(Please start each SMS number with the country code)")
      numlbel.place(x=10, y=10)
      numentry=Entry(SMS_Notification, width=92).place(x=10, y=30)
      stexbel=Label(SMS_Notification, text="SMS Text").place(x=10, y=60)
      stex=Entry(SMS_Notification, width=40).place(x=10, y=85,height=120)
      
      dclbel=Label(SMS_Notification, text="Double click to insert into text")
      dclbel.place(x=410, y=60)
      dcl=Entry(SMS_Notification, width=30)
      dcl.place(x=400, y=85,height=200)
      
      smstype=LabelFrame(SMS_Notification, text="SMS message type", width=377, height=60)
      smstype.place(x=10, y=223)
      snuvar=IntVar()
      normal_rbtn=Radiobutton(smstype, text="Normal SMS(160 chars)", variable=snuvar, value=1)
      normal_rbtn.place(x=5, y=5)
      unicode_rbtn=Radiobutton(smstype, text="Unicode SMS(70 chars)", variable=snuvar, value=2)
      unicode_rbtn.place(x=190, y=5)
      tiplbf=LabelFrame(SMS_Notification, text="Tips", width=680, height=120)
      tiplbf.place(x=10, y=290)
      tiplabl=Label(tiplbf,justify=LEFT,fg="red",  text="Always start the SMS nymber with the country code. Do not use the + sign at the beginning(example\nUS number:8455807546). Do not use any special characters in your normal SMS text. Please use the\nstndard SMS characters or the English alphabet and numbers only. Otherwise the SMS will be\nunreadable or undeliverable. If you need to enter international characters, accents,email address, or\nspecial characters to the SMS text field then choose the Unicode SMS format.")
      tiplabl.place(x=5, y=5)

      btn1=Button(SMS_Notification, width=20, text="Send SMS notification").place(x=10, y=420)
      btn2=Button(SMS_Notification, width=25, text="Confirm SMS cost before sending").place(x=280, y=420)
      btn3=Button(SMS_Notification, width=15, text="Cancel").place(x=550, y=420)
      

      smstype=LabelFrame(SMS_Service_Account, text="Select the notification service provider", width=670, height=65)
      smstype.place(x=10, y=5)
      snumvar=IntVar()
      normal_rbtn=Radiobutton(smstype,text="BULKSMS(www.bulksms.com)",variable=snumvar,value=1,)
      normal_rbtn.place(x=5, y=5)
      unicode_rbtn=Radiobutton(smstype, text="Unicode SMS(70 chars)-Recommended", variable=snumvar, value=2)
      unicode_rbtn.place(x=290, y=5)

      sms1type=LabelFrame(SMS_Service_Account, text="Your BULKSMS.COM Account", width=670, height=100)
      sms1type.place(x=10, y=80)
      name=Label(sms1type, text="Username").place(x=10, y=5)
      na=Entry(sms1type, width=20).place(x=100, y=5)
      password=Label(sms1type, text="Password").place(x=10, y=45)
      pas=Entry(sms1type, width=20).place(x=100, y=45)
      combo=Label(sms1type, text="Route").place(x=400, y=5)
      n = StringVar()
      combo1 = ttk.Combobox(sms1type, width = 20, textvariable = n ).place(x=450,y=5)
      btn1=Button(sms1type, width=10, text="Save settings").place(x=550, y=45)

      
      tiplbf=LabelFrame(SMS_Service_Account, text="Terms of service", width=680, height=250)
      tiplbf.place(x=10, y=190)
      tiplabl=Label(tiplbf,justify=LEFT,fg="red",  text="The SMS notification service is not free.This service costs you creadit.You must have your own account\nat BULKSMS.COM and you need to have sufficient creadit and an active internet connection to use\nthis feature.Please review all fields in this form for accuracy")
      tiplabl.place(x=0, y=5)
      tiplabl1=Label(tiplbf,justify=LEFT,fg="black",  text="visit www.bulksms.com website to create your own account.please make sure the BULKSMS .COM\n service works well in your country before you busy creadit")
      tiplabl1.place(x=0, y=60)
      tiplabl2=Label(tiplbf,justify=LEFT,fg="black",  text="Our SMS notification tool comes without any warranty.our software only forwards your SMS message\nthe BULKSMS API server .The BULKSMS API server will try to sent SMS message your recipient")
      tiplabl2.place(x=0, y=100)
      tiplabl3=Label(tiplbf,justify=LEFT,fg="red",  text="Please note that you access and use the SMS notification tool your own risk.F-Billing software is not\nresponsible for any type of loss or damage or undelivered SMS massage which you may as a result\nof accessing and using the SMS notification service.")
      tiplabl3.place(x=0, y=140)
      checkvar1=IntVar()
      chkbtn1=Checkbutton(tiplbf,text="I have read and agree to the terms of service above",variable=checkvar1,onvalue=1,offvalue=0).place(x=70, y=200) 



    
    #delete line item  
    def delete_prod2():
      # selected_item = viewditree.selection()[0]
      # print=(selected_item)
      # viewditree.delete(selected_item)
      itemid = viewditree.item(viewditree.focus())["values"][0]
      print(itemid,)
      dlting=osdata[0]
      sql = 'DELETE FROM storingproduct WHERE invoiceid=%s AND Productserviceid=%s'
      val = (dlting,itemid,)
      fbcursor.execute(sql, val)
      fbilldb.commit()
      viewditree.delete(viewditree.selection()[0])
      for record in viewditree.get_children():
           viewditree.delete(record)        
      sql = "SELECT * FROM storingproduct WHERE invoiceid= %s"
      i=(dlting,)
      fbcursor.execute(sql,i)
      b=0
      j = 0
      for i in fbcursor:
        viewditree.insert(parent='', index='end', iid=i, text='', values=(i[4],i[6],i[7],i[9],i[22],i[10],i[12],(i[9]*i[22])))
        for line in viewditree.get_children():
            idsave=viewditree.item(line)['values'][7]
        b+=idsave
      j += 1
      priceco0.config(text=b) 
      
  except:
    try:
      pop.destroy()
    except:
      pass
      messagebox.showerror('F-Billing Revolution', 'Select a record to edit.') 

  # #delete orders  
  # def dele():
  #   delmess = messagebox.askyesno("Delete Invoice", "Are you sure to delete this Order?")
  #   messagebox.showerror("F-Billing Revolution","Customer is required,please select customer before deleting line item .")

  #   if delmess == True:
  #     itemid = invotree.item(invotree.focus())["values"][1]
  #     print(itemid,)
  #     sql = 'DELETE FROM invoice WHERE invoiceid=%s'
  #     val = (itemid,)
  #     fbcursor.execute(sql, val)
  #     fbilldb.commit()
  #     invotree.delete(invotree.selection()[0])
  #   else:
  #     pass  
######################################## UPDATING invoice ##############################################
  def updateorder():
    cmbodto=cmb1.get()
    addrsfrm=addrs1.get('1.0', 'end-1c')
    sptto=spt1.get('1.0', 'end-1c')
    adrsto=adrs.get('1.0', 'end-1c')
    emlfrm=eml.get('1.0', 'end-1c')
    smsfrm=smsno.get('1.0', 'end-1c')
    ordrid=sctxt.get()
    orddatein=e2.get_date()
    ordduein=e3.get_date()
    trmsin=e4.get()
    extracstnme=xtracstnme.get()
    discountrte=dscntrte.get()
    extracst=extra_cost.get()
    taax=taxx.get()
    tplts=tmplte.get()
    slzprzn=salesprsn.get()
    ctgryy=ctgry.get()
    bc="Draft"
    idorder= osdata[0]

    recurring_period = month_var.get()
    recurring_period_month = current_var.get()
    next_invoice = recurentry1.get_date() 
    stop_invoice = recurentry2.get_date() 


    for line in viewditree.get_children():
      idsave=viewditree.item(line)['values'][0]
      sql1= 'SELECT * FROM  Productservice WHERE Productserviceid = %s'
      val=(idsave,)
      print(val)
      fbcursor.execute(sql1,val,)
      child=fbcursor.fetchone()
      print(child)
      # sql2= 'UPDATE storingproduct SET Productserviceid=%s,orderid=%s,sku=%s,category=%s,name=%s,description=%s,status=%s,unitprice=%s,peices=%s,cost=%s,taxable=%s,priceminuscost=%s,serviceornot=%s,stock=%s,stocklimit=%s,warehouse=%s,privatenote=%s'
      # val1=(child[0],sctxt,child[2],child[3],child[4],child[5],child[6],child[7],child[8],child[9],child[10],child[11],child[12],child[13],child[14],child[15],child[16])
      # fbcursor.execute(sql2,val1,)
      # fbilldb.commit()

    sql3='UPDATE invoice SET invoiceid=%s,invodate=%s,duedate=%s,businessname=%s,status=%s,extracostname=%s,extracost=%s,template=%s,salesper=%s,discourate=%s,tax1=%s,category=%s,businessaddress=%s,shipname=%s,shipaddress=%s,cpemail=%s,cpmobileforsms=%s, recurring_period=%s, recurring_period_month=%s, next_invoice=%s, stop_recurring=%s WHERE invoiceid=%s'
    val2=(ordrid,orddatein,ordduein,cmbodto,bc,extracstnme,extracst,tplts,slzprzn,discountrte,taax,ctgryy,addrsfrm,sptto,adrsto,emlfrm,smsfrm,recurring_period,recurring_period_month,next_invoice,stop_invoice,idorder)
    fbcursor.execute(sql3,val2,)
    fbilldb.commit()

    sqlup='UPDATE storingproduct SET invoiceid=%s WHERE invoiceid=%s'
    valup=(ordrid,idorder,)
    fbcursor.execute(sqlup,valup,)
    fbilldb.commit()

    for record in invotree.get_children():
      invotree.delete(record)
    fbcursor.execute("select *  from invoice")
    pandsdata = fbcursor.fetchall()
    countp = 0
    for i in pandsdata:
      invotree.insert(parent='', index='end', iid=i, text='', values=('',i[0], i[2], i[3], i[18], i[4], i[5], i[6], i[7], i[8], i[9], i[10]))
    countp += 1
    ttlprzinptinv=priceco0.cget("text")
    ratediscntinv=dscntrte.get()
    xtaxinv=taxx.get()
    cstxtrainv=extra_cost.get()
    print(ttlprzinptinv,ratediscntinv,xtaxinv,cstxtrainv)

    isdd=round(int(ratediscntinv),3)
    pidd=ttlprzinptinv
    p=round(pidd, 4)
    dsctedd=(isdd*pidd)/100
    dscdd=round(dsctedd, 4)
    discount=Label(summaryfrme, text=str(isdd)+"% Discount").place(x=0 ,y=0)
    discount1=Label(summaryfrme,text='Rs. '+str(dscdd))
    discount1.place(x=130 ,y=0)

    sbtotlhee=p-dscdd
    subtotl=round(sbtotlhee, 4)
    sub=Label(summaryfrme, text="Subtotal").place(x=0 ,y=21)
    sub100=Label(summaryfrme, text='Rs. '+str(subtotl))
    sub100.place(x=130 ,y=21)

    taxval91=int(xtaxinv)
    tax1dsplay=(taxval91*subtotl)/100
    taxvalu=round(tax1dsplay,2)
    tax=Label(summaryfrme, text="Tax1").place(x=0 ,y=42)
    tax100=Label(summaryfrme, text='Rs. '+str(taxvalu))
    tax100.place(x=130 ,y=42)

    xtracstvaluzz=int(cstxtrainv)
    xtra1cst=round(xtracstvaluzz, 4)
    cost=Label(summaryfrme, text="Extra cost").place(x=0 ,y=63)
    cost100=Label(summaryfrme, text='Rs. '+str(xtra1cst)).place(x=130 ,y=63)

    otherttlval=subtotl+taxvalu+xtra1cst
    ot1v1=round(otherttlval, 4)
    order=Label(summaryfrme, text="Invoice total").place(x=0 ,y=84)
    order100=Label(summaryfrme, text='Rs. '+str(ot1v1)).place(x=130 ,y=84)

    itemidot = ordrid
    ordttl=ot1v1
    for record in invotree.get_children():
      invotree.delete(record)
    sqlordttl = "UPDATE invoice SET invoicetot=%s WHERE invoiceid = %s"
    valqordttl = (ordttl,itemidot, )
    fbcursor.execute(sqlordttl, valqordttl,)
    fbilldb.commit()
    fbcursor.execute('SELECT * FROM invoice')   
    j = 0
    for i in fbcursor:
     invotree.insert(parent='', index='end', iid=i, text='', values=('',i[0], i[2], i[3], i[18], i[4], i[5], i[6], i[7], i[8], i[9], i[10]))
    
     invototalinput=0
     for line in invotree.get_children():
      idsave1=invotree.item(line)['values'][9]
      invototalinput += idsave1
    j += 1
    invototalrowcol.config(text=invototalinput)

    messagebox.showinfo('Successfully Added','Successfully Added')
      
    for k in viewditree.get_children():
      pricetotl=viewditree.item(k)['values'][7]    

  firFrame=Frame(pop, bg="#f5f3f2", height=60)
  firFrame.pack(side="top", fill=X)

  w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  selectcustomer2 = Button(firFrame,compound="top", text="Select\nCustomer",relief=RAISED, image=customer,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=selectcustomer1)
  selectcustomer2.pack(side="left", pady=3, ipadx=4)


  w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  addline2= Button(firFrame,compound="top", text="Add new\nline item",relief=RAISED, image=photo,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=addnewline)
  addline2.pack(side="left", pady=3, ipadx=4)

  deleteline2= Button(firFrame,compound="top", text="Delete line\nitem",relief=RAISED, image=photo2,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=delete_prod2)
  deleteline2.pack(side="left", pady=3, ipadx=4)

  w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  # prev= Button(firFrame,compound="top", text="Preview\nInvoice",relief=RAISED, image=photo4,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=previewline)
  # prev.pack(side="left", pady=3, ipadx=4)

  prin= Button(firFrame,compound="top", text="Print \nInvoice",relief=RAISED, image=photo5,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=printsele)
  prin.pack(side="left", pady=3, ipadx=4)

  w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  mail= Button(firFrame,compound="top", text="Email\nInvoice",relief=RAISED, image=photo6,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=email_invoice_recurring)
  mail.pack(side="left", pady=3, ipadx=4)

  sms1= Button(firFrame,compound="top", text="Send SMS\nnotification",relief=RAISED, image=photo10,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=sms1)
  sms1.pack(side="left", pady=3, ipadx=4)

  w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  markinvo2= Button(firFrame,compound="top", text="Mark Invoice\n as Paid",relief=RAISED, image=mark1,bg="#f5f3f2", fg="black", height=55, bd=1, width=55)
  markinvo2.pack(side="left", pady=3, ipadx=4)

  voidinvo2= Button(firFrame,compound="top", text="Void\nInvoice",relief=RAISED, image=mark2,bg="#f5f3f2", fg="black", height=55, bd=1, width=55)
  voidinvo2.pack(side="left", pady=3, ipadx=4)

  enableinvo2= Button(firFrame,compound="top", text="Reactivate \nInvoice",relief=RAISED, image=mark2,bg="#f5f3f2", fg="black", height=55, bd=1, width=55)
  enableinvo2.pack(side="left", pady=3, ipadx=4)

  w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  calc= Button(firFrame,compound="top", text="Open\nCalculator",relief=RAISED, image=photo9,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=calcu)
  calc.pack(side="left", pady=3, ipadx=4)

  w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="right", padx=5)

  Createorder= Button(firFrame,compound="top", text="Save\nChanges",relief=RAISED, image=tick,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=updateorder)
  Createorder.pack(side="right", pady=3, ipadx=4)

  fir1Frame=Frame(pop, height=180,bg="#f5f3f2")
  fir1Frame.pack(side="top", fill=X)

    
  # fbcursor.execute('SELECT * FROM Productservice;') 
  # j = 0
  # for i in fbcursor:
  #     labelframe1.insert(parent='', index='end', iid=i, text='', values=(' ',i[0],i[4],i[5],i[7],i[8],i[10],))
  #     j += 1


  labelframe1 = LabelFrame(fir1Frame,text="Customers",font=("arial",15))
  labelframe1.place(x=10,y=5,width=640,height=160)


  def prodtreefetch1():
    itemid = cusventtree1.item(cusventtree1.focus())["values"][0]
    sql = "select * from Customer where customerid = %s"
    val = (itemid, )
    fbcursor.execute(sql, val)
    slctcstr = fbcursor.fetchone()
    cmb1.delete(0,'end')
    cmb1.insert(0, slctcstr[4])
    addrs1.delete('1.0','end')
    addrs1.insert("1.0", slctcstr[5])
    spt1.delete('1.0','end')
    spt1.insert('1.0', slctcstr[6])
    adrs.delete('1.0','end')
    adrs.insert('1.0', slctcstr[7])
    eml.delete('1.0','end')
    eml.insert('1.0', slctcstr[9])
    smsno.delete('1.0','end')
    smsno.insert('1.0', slctcstr[10])
    custselection.destroy()

##
  sql = "select businessname from Customer"
  fbcursor.execute(sql,)
  pdata = fbcursor.fetchall()
##
  itemid = invotree.item(invotree.focus())["values"][1]
  sql = "select * from Invoice where Invoiceid = %s"
  val = (itemid, )
  fbcursor.execute(sql, val)
  osdata = fbcursor.fetchone()
##


  order = Label(labelframe1, text="Invoice to").place(x=10,y=5)
  cmb1 = ttk.Combobox(labelframe1,values=pdata,width=28)
  cmb1.place(x=80,y=5)
  cmb1.delete(0,'end')
  cmb1.insert(0, osdata[18])

  address=Label(labelframe1,text="Address").place(x=10,y=30)
  # e2=scrolledtext(labelframe1,width=23).place(x=80,y=30,height=70)
  addrs1 = scrolledtext.Text(labelframe1, undo=True,width=23)
  addrs1.place(x=80,y=30,height=70)
  addrs1.delete('1.0','end')
  addrs1.insert("1.0", osdata[19])
  
  ship=Label(labelframe1,text="Ship to").place(x=342,y=5)
  #e3=Entry(labelframe1,width=30).place(x=402,y=3)
  spt1 = scrolledtext.Text(labelframe1, undo=True,width=23)
  spt1.place(x=402,y=3)
  spt1.delete('1.0','end')
  spt1.insert("1.0", osdata[20])

  address1=Label(labelframe1,text="Address").place(x=340,y=30)
  # e4=Text(labelframe1,width=23).place(x=402,y=30,height=70)
  adrs = scrolledtext.Text(labelframe1, undo=True,width=23)
  adrs.place(x=402,y=30,height=70)
  adrs.delete('1.0','end')
  adrs.insert("1.0", osdata[21])

  def changedone1():
    # shpdlt=spt1.get(osdata[17])
    spt1.delete('1.0','end')
    spt1.insert('1.0', osdata[18])
    adrs.delete('1.0','end')
    adrs.insert('1.0', osdata[19])

  btn1=Button(labelframe1,width=3,height=2,compound = LEFT,text=">>",command=changedone1).place(x=290, y=48)
  
  labelframe2 = LabelFrame(fir1Frame,text="")
  labelframe2.place(x=10,y=130,width=640,height=42)

  email=Label(labelframe2,text="Email").place(x=10,y=5)
  # e5=Entry(labelframe2,width=30).place(x=80,y=5)
  eml = scrolledtext.Text(labelframe2, undo=True,width=23)
  eml.place(x=80,y=5,height=25)
  eml.delete('1.0','end')
  eml.insert("1.0", osdata[22])


  sms=Label(labelframe2,text="SMS No.").place(x=340,y=5)
  # e6=Entry(labelframe2,width=30).place(x=402,y=5)
  smsno = scrolledtext.Text(labelframe2, undo=True,width=23)
  smsno.place(x=402,y=5,height=25)
  smsno.delete('1.0','end')
  smsno.insert("1.0", osdata[23])
    
  labelframe = LabelFrame(fir1Frame,text="Invoice",font=("arial",15))
  labelframe.place(x=652,y=5,width=290,height=170)
  order=Label(labelframe,text="Invoice#").place(x=5,y=5)
  # e1=Entry(labelframe,width=25).place(x=100,y=5,)
  sctxt = Entry(labelframe,width=20)
  sctxt.place(x=100,y=5,height=22)
  sctxt.delete(0,'end')
  sctxt.insert(0, osdata[0])


  orderdate=Label(labelframe,text="Invoice date").place(x=5,y=33)
  e2=DateEntry(labelframe,width=20)
  e2.place(x=150,y=33)
  # sctxt = scrolledtext.Text(labelframe, undo=True,width=15)
  # sctxt.place(x=150,y=33,height=22)
  e2.delete(0,'end')
  e2.insert(0, osdata[2].strftime('%d/%m/%y'))
  def duecheckinv2():
   if checkvarStatus5.get()==0:
     e3['state'] = DISABLED  
   else:
     e3['state'] = NORMAL
  

  checkvarStatus5=IntVar()
  duedate=Checkbutton(labelframe,variable = checkvarStatus5,text="Due date",onvalue =1 ,offvalue = 0, command=duecheckinv2).place(x=5,y=62)
  
  e3=DateEntry(labelframe,width=20)
  e3.place(x=150,y=62)
  # sctxt = scrolledtext.Text(labelframe, undo=True,width=15)
  # sctxt.place(x=150,y=63,height=22)
  e3.delete(0,'end')
  e3.insert(0, osdata[3].strftime('%d/%m/%y'))




  terms=Label(labelframe,text="Terms").place(x=5,y=92)
  e4=ttk.Combobox(labelframe, value="",width=25)
  e4.place(x=100,y=92)



  ref=Label(labelframe,text="Order ref#").place(x=5,y=118)
  e1=Entry(labelframe,width=27).place(x=100,y=118)

  fir2Frame=Frame(pop, height=150,width=100,bg="#f5f3f2")
  fir2Frame.pack(side="top", fill=X)
  listFrame = Frame(fir2Frame, bg="white", height=140,borderwidth=5,  relief=RIDGE)


  viewditree=ttk.Treeview(listFrame, show = "headings")
  viewditree.pack(side = 'top')
  viewditree["columns"]=["1","2","3","4","5","6","7","8"]
  viewditree.column("#0", width=40)
  viewditree.column("1", width=80)
  viewditree.column("2", width=190)
  viewditree.column("3", width=190)
  viewditree.column("4", width=80)
  viewditree.column("5", width=60)
  viewditree.column("6", width=60)
  viewditree.column("7", width=60)
  viewditree.column("8", width=80)
 
  viewditree.heading("#0")
  viewditree.heading("1",text="ID/SKU")
  viewditree.heading("2",text="Product/Service")
  viewditree.heading("3",text="Description")
  viewditree.heading("4",text="Unit Price")
  viewditree.heading("5",text="Quantity")
  viewditree.heading("6",text="Pcs/Weight")
  viewditree.heading("7",text="Tax1")
  viewditree.heading("8",text="Price")
  priceco0 = Label(listFrame,bg="#f5f3f2")
  priceco0.place(x=850,y=200,width=78,height=18)
#   priceco0 = Entry(listFrame,width=28)
  global ttlp
  ba=osdata[0]
  sql4='SELECT * FROM storingproduct WHERE invoiceid=%s'
  val10=(ba,)
  fbcursor.execute(sql4,val10)
  ttlp=0
  j = 0
  for i in fbcursor:
    viewditree.insert(parent='', index='end', iid=i, text='', values=(i[21],i[6],i[7],i[9],i[22],i[10],i[12],(i[9]*i[22])))
    ttlp+=(i[9]*i[22])
  j += 1
  priceco0.config(text=ttlp)

  # def pricetotal():
  #   fbcursor.execute('SELECT * FROM Productservice;')
  #   j = 0
  #   for i in fbcursor:
  #     pricecola=((i[7]*i[13]))
  #   j += 1

  

  viewditree.pack(fill="both", expand=1)
  listFrame.pack(side="top", fill="both", padx=5, pady=3, expand=1)
  

  # fbcursor.execute('SELECT * FROM Productservice;') 
  # j = 0
  # for i in fbcursor:
  #     vwedttree.insert(parent='', index='end', iid=i, text='', values=(i[2],i[4],i[5],i[7],i[13],i[8],i[10],(i[7]*i[13])))
  #     j += 1

  new_value = tk.StringVar()

  def edit_window_box(val):
    
    edit_window = Toplevel(root)
    edit_window.title("Edit the value or cancel")
    edit_window.geometry("400x200")
    label_edit = tk.Label(edit_window , text='Enter value to edit -', 
    font = ("Times", 12)).place(x=68,y=60)
    #create edit box
    edit_box = tk.Entry(edit_window)
    edit_box.insert(0,val)
    edit_box.place(x=200,y=63)
    #auto select edit window 
    edit_window.focus()
    
    def value_assignment(event):
        printing = edit_box.get()
        # print(printing)
        indexcolaa=int(indexcol)-1
        new_value.set(printing)
        print(indexcol)
        #only destroy will not update the value (perhaps event keeps running in background)
        #quit allows event to stop n update value in tree but does not close the window in single click 
        #rather on dbl click shuts down entire app 

        selected0 = viewditree.focus()
        valuz1= viewditree.item(selected0)["values"]
        idgettingprdt=valuz1[0]
        valuz1[indexcolaa]=printing
        print(valuz1)

        sql2z0= 'UPDATE storingproduct SET sku=%s,name=%s,description=%s,unitprice=%s,stock=%s,peices=%s,taxable=%s WHERE invoiceid=%s AND Productserviceid=%s'
        val0z1=(valuz1[0],valuz1[1],valuz1[2],valuz1[3],valuz1[4],valuz1[5],valuz1[6],osdata[0],idgettingprdt)
        # dnz=(ordrid,sql2z0,)
        print(val0z1)
        fbcursor.execute(sql2z0,val0z1)
        fbilldb.commit()

        qntsql= 'UPDATE storingproduct SET quantity=%s WHERE Productserviceid=%s'
        qntval=(valuz1[4],idgettingprdt)
        fbcursor.execute(qntsql,qntval)
        fbilldb.commit()


        fbcursor.execute("SELECT * FROM storingproduct ORDER BY invoiceid DESC LIMIT 1")
        bolo = fbcursor.fetchone()[2]
        print(bolo)
        print(osdata[0])

        if bolo==osdata[0]:        
         for record in viewditree.get_children():
          viewditree.delete(record)
         m="SELECT * FROM storingproduct  WHERE invoiceid=%s"
         i=(osdata[0],)
         fbcursor.execute(m,i)
         panrefrdata = fbcursor.fetchall()
         az=0
         countp = 0
         for i in panrefrdata:
           viewditree.insert(parent='', index='end', iid=i, text='', values=(i[4],i[6],i[7],i[9],i[22],i[10],i[12],(i[9]*i[22])))

           az+=(i[9]*i[22])
         countp += 1
         priceco0.config(text=az)
        else:
          pass

        edit_window.quit()
        edit_window.destroy()
    
    edit_window.bind('<Return>', value_assignment )
    


    B1 = tk.Button(edit_window, text=" Okay ")
    B1.bind('<Button-1>',value_assignment)
    B1.place(x=70,y=130)
    
    
    B2 = tk.Button(edit_window, text="Cancel", command = edit_window.destroy).place(x=276,y=130)
    edit_window.mainloop()
    
  #will explain
  #variable to hold col value (col clicked)
  shape1 = tk.IntVar()
  #tracks both col , row on mouse click
  def tree_click_handler(event):
      cur_item = viewditree.item(viewditree.focus())
      # print(cur_item)
      global indexcol
      indexcol = viewditree.identify_column(event.x)[1:]
      rowid = viewditree.identify_row(event.y)[1:]
      # print(indexcol)
      # print(rowid)
      #updates list
      shape1.set(indexcol)
      try:
          x,y,w,h = viewditree.bbox('I'+rowid,'#'+indexcol)
      except:pass
      #tree.tag_configure("highlight", background="yellow")
      return(indexcol)

  #code linked to event    
  viewditree.bind('<ButtonRelease-1>', tree_click_handler)

  #edit a value in a clicked cell
  def edit(event):
      try:
          selected_item = viewditree.selection()[0]
          temp = list(viewditree.item(selected_item , 'values'))
          tree_click_handler
          col_selected = int(shape1.get())-1
          edit_window_box(temp[col_selected])
          #do not run if edit window is open
          #use edit_window.mainloop() so value assign after window closes
          temp[col_selected] = new_value.get()
          viewditree.item(selected_item, values= temp)
          # prstree.insert(prstree.selection()[0])
      except: pass
  #binding allows to edit on screen double click
  viewditree.bind('<Double-Button-1>' , edit)


  fir3Frame=Frame(pop,height=200,width=700,bg="#f5f3f2")
  fir3Frame.place(x=0,y=490)

  tabStyle = ttk.Style()
  tabStyle.theme_use('default')
  tabStyle.configure('TNotebook.Tab', background="#999999", width=12, padding=5)
  myNotebook=ttk.Notebook(fir3Frame)
  invoiceFrame = Frame(myNotebook, height=200, width=800)
  recurFrame = Frame(myNotebook, height=200, width=800)
  payementFrame = Frame(myNotebook, height=200, width=800)
  headerFrame = Frame(myNotebook, height=200, width=800)
  commentFrame = Frame(myNotebook, height=200, width=800)
  termsFrame = Frame(myNotebook, height=200, width=800)
  noteFrame = Frame(myNotebook, height=200, width=800)
  documentFrame = Frame(myNotebook, height=200, width=800)
  
  myNotebook.add(invoiceFrame,compound="left", text="Invoice")
  myNotebook.add(recurFrame,compound="left", text="Recurring")
  myNotebook.add(payementFrame,compound="left", text="Payements")
  myNotebook.add(headerFrame,compound="left",  text="Header/Footer")
  myNotebook.add(commentFrame,compound="left",  text="Comments")
  myNotebook.add(termsFrame,compound="left", text="Terms")
  myNotebook.add(noteFrame,compound="left",  text="Private notes")
  myNotebook.add(documentFrame,compound="left",  text="Documents")
  myNotebook.pack(expand = 1, fill ="both")  



##
  sql = "select extracostname from invoice"
  fbcursor.execute(sql,)
  exdata = fbcursor.fetchall()  
##
  itemid = invotree.item(invotree.focus())["values"][1]
  sql = "select * from invoice where invoiceid = %s"
  val = (itemid, )
  fbcursor.execute(sql, val)
  orbtdata = fbcursor.fetchone()
##

  labelframe1 = LabelFrame(invoiceFrame,text="",font=("arial",15))
  labelframe1.place(x=1,y=1,width=800,height=170)

  cost1=Label(labelframe1,text="Extra cost name").place(x=2,y=5)
  xtracstnme=ttk.Combobox(labelframe1, value=exdata,width=20)
  xtracstnme.place(x=115,y=5)
  xtracstnme.delete(0,'end')
  xtracstnme.insert(0, orbtdata[11])


  rate=Label(labelframe1,text="Discount rate").place(x=370,y=5)
  dscntrte=Spinbox(labelframe1,width=6,  from_=0, to=100, font="italic 10")
  dscntrte.place(x=460,y=5)
  dscntrte.delete(0,'end')
  dscntrte.insert(0, orbtdata[15])


  cost2=Label(labelframe1,text="Extra cost").place(x=35,y=35)
  extra_cost=Entry(labelframe1,width=10)
  extra_cost.place(x=115,y=35)
  extra_cost.delete(0,'end')
  extra_cost.insert(0, orbtdata[12])


  tax=Label(labelframe1,text="Tax1").place(x=420,y=35)
  taxx=Entry(labelframe1,width=7)
  taxx.place(x=460,y=35)
  taxx.delete(0,'end')
  taxx.insert(0, orbtdata[16])

##
  sql = "select template from invoice"
  fbcursor.execute(sql,)
  tmpltdata = fbcursor.fetchall()  
##



  template=Label(labelframe1,text="Template").place(x=37,y=70)
  tmplte=ttk.Combobox(labelframe1, value=tmpltdata,width=25)
  tmplte.place(x=115,y=70)
  tmplte.delete(0,'end')
  tmplte.insert(0, orbtdata[13])



  sales=Label(labelframe1,text="Sales Person").place(x=25,y=100)
  salesprsn=Entry(labelframe1,width=18)
  salesprsn.place(x=115,y=100)
  salesprsn.delete(0,'end')
  salesprsn.insert(0, orbtdata[14])


  category=Label(labelframe1,text="Category").place(x=300,y=100)
  ctgry=Entry(labelframe1,width=22)
  ctgry.place(x=370,y=100)
  ctgry.delete(0,'end')
  ctgry.insert(0, orbtdata[17])
  
  statusfrme = LabelFrame(labelframe1,text="Status",font=("arial",15))
  statusfrme.place(x=540,y=0,width=160,height=160)
##
  itemid = invotree.item(invotree.focus())["values"][1]
  sql = "select status from invoice where invoiceid = %s"
  val = (itemid, )
  fbcursor.execute(sql, val)
  drftinvc = fbcursor.fetchone()
##
##
  itemid = invotree.item(invotree.focus())["values"][1]
  sql = "select emailon from invoice where invoiceid = %s"
  val = (itemid, )
  fbcursor.execute(sql, val)
  emldon = fbcursor.fetchone()
##
##
  itemid = invotree.item(invotree.focus())["values"][1]
  sql = "select printon from invoice where invoiceid = %s"
  val = (itemid, )
  fbcursor.execute(sql, val)
  prntdon = fbcursor.fetchone()
##
  draft=Label(statusfrme, text=drftinvc,font=("arial", 12, "bold"), fg="black")
  draft.place(x=50, y=3)

  on1=Label(statusfrme, text="Emailed on:").place( y=50)
  nev1=Label(statusfrme, text=emldon).place(x=100,y=50)
  on2=Label(statusfrme, text="Printed on:").place( y=90)
  nev2=Label(statusfrme, text=prntdon).place(x=98,y=90)

  def isChecked():
      if checkvarStatus6.get()==0:
        recurentry1['state'] = DISABLED 
        # recurentry2['state'] = DISABLED  
        period2['state'] = DISABLED
        #  month_var['state'] = DISABLED
      else:
          recurentry1['state'] = NORMAL
          # recurentry2['state'] = NORMAL
          period2['state'] = NORMAL

  def stopcheck():
      if checkvarStatus7.get()==0:
        recurentry2['state'] = DISABLED  
      else:
          recurentry2['state'] = NORMAL 

  # def duecheck():
  #     if checkvarStatus5.get()==0:
  #       invduedate['state'] = DISABLED  
  #     else:
  #       invduedate['state'] = NORMAL  
  
  # def dueChecked():
  #     if checkvarStatus5.get()==0:
  #       e3['state'] = DISABLED  
  #     else:
  #       e3['state'] = NORMAL



  def recalculator():  
    date_1 = e2.get_date()
    print(date_1)

    if period2.get() == "Month(s)":
      end_date = date_1 + date.timedelta(3*365/12)  
    elif period2.get() == "Day(s)":
      end_date = date_1 + date.timedelta(days=int(period1.get()))


    print(end_date)
    recurentry1.delete(0,'end')
    recurentry1.insert(0, end_date.strftime('%m/%d/%y'))
    # recurentry2.config(f"ndate: {end_date.strftime('%m/%d/%Y')}") 

  def updaterecur():# Edit recurring values into db (user)
    itemid = invotree.item(invotree.focus())["values"][1]
    recurring_period = month_var.get()
    recurring_period_month = current_var.get()
    next_invoice = recurentry1.get_date() 
    stop_invoice = recurentry2.get_date()
    sql='UPDATE invoice set recurring_period=%s,recurring_period_month=%s,next_invoice=%s,stop_recurring=%s where invoiceid=%s'
    val=(recurring_period,  recurring_period_month, next_invoice, stop_invoice, itemid)
    fbcursor.execute(sql,val)
    fbilldb.commit()

  
  #------------------------------recurring edit ---------------------------------------------
    # itemid = tree.item(tree.focus())["values"][]
    # sql = "select * from invoice where invoiceid = %s"
    # val = (itemid, )
    # fbcursor.execute(sql, val)
    # psdata = fbcursor.fetchone()

  #-----------------------------------------------------------------
  global recurentry1, recurentry2,checkvarStatus6,period2, current_var, month_var
  recureframe = LabelFrame(recurFrame,text="",font=("arial",15))
  recureframe.place(x=1,y=1,width=800,height=170)
  checkvarStatus6=IntVar()
  current_var = StringVar()
  month_var = StringVar()
  checkvarStatus6.set(0)
    
  Checkbutton(recureframe,variable = checkvarStatus6,text="Recurring", offvalue=0, onvalue=1, command=isChecked).place(x=5,y=5)
  # Checkbutton(ws, text="accept T&C", variable=cb, onvalue=1, offvalue=0, command=isChecked).pack()
  period=Label(recureframe,text="Recurring period(interval)").place(x=65,y=35)
  # period1=Entry(recureframe,width=13, textvariable=month_var)
  # period1.place(x=240,y=35)
  period1 = Spinbox(recureframe, from_=1, to=10000, font="italic 10", width=9, text="Months(s)" ,textvariable=month_var)
  period1.place(x=240,y=35)
  period1.delete(0,'end')
  period1.insert(0, osdata[24]) 
    
  # period1.delete(0,'end')
  # period1.insert(0, psdata[20])
                              
  nextinvo=Label(recureframe,text="Next Invoice").place(x=240,y=65)
  recurentry1=DateEntry(recureframe,width=20, )
  recurentry1.place(x=325,y=65)
  recurentry1['state'] = DISABLED 
  recurentry1.delete(0,'end')
  recurentry1.insert(0, osdata[26].strftime('%m/%d/%y'))
    

  recalc = Button(recureframe, text="Recalculate", command=recalculator)
  recalc.place(x=490,y=65)

  saverec= Button(recureframe, text="Save" , command=updaterecur).place(x=570,y=65)
  
  checkvarStatus7=IntVar()
  checkvarStatus7.set(0)
  stoprecur=Checkbutton(recureframe,variable = checkvarStatus7,text="Stop recurring after",onvalue =1 ,offvalue = 0, command=stopcheck).place(x=180,y=95)
  recurentry2=DateEntry(recureframe, value="",width=20)
  recurentry2.place(x=325,y=95)
  recurentry2['state'] = DISABLED 
  recurentry2.delete(0,'end')
  recurentry2.insert(0, osdata[27].strftime('%m/%d/%y'))

  def month():
    period2["values"] = ["Month(s)", "Days(s)"] 
  period2=ttk.Combobox(recureframe,width=20, 
                            values=["Month(s)", "Day(s)"],textvariable=current_var)
  # period2=Entry(recureframe,width=13, textvariable=current_var)

  period2.place(x=325,y=35)
  period2.delete(0,'end')
  period2.insert(0, osdata[25])
  period2['state'] = DISABLED 


  btn1=Button(payementFrame,height=2,width=3,text="+").place(x=5,y=10)
  btn2=Button(payementFrame,height=2,width=3,text="-").place(x=5,y=50)
  cusventtree=ttk.Treeview(payementFrame, height=5)
  cusventtree["columns"]=["1","2","3","4","5"]
  cusventtree.column("#0", width=20)
  cusventtree.column("1", width=140)
  cusventtree.column("2", width=140)
  cusventtree.column("3", width=110)
  cusventtree.column("4", width=140)
  cusventtree.column("5", width=110)
  cusventtree.heading("#0",text="", anchor=W)
  cusventtree.heading("1",text="Payement ID")
  cusventtree.heading("2",text="Payement date")
  cusventtree.heading("3",text="Paid by")
  cusventtree.heading("4",text="Description")
  cusventtree.heading("5",text="Amount")      
  cusventtree.place(x=50, y=45)


  text1=Label(headerFrame,text="Title text").place(x=50,y=5)
  e1=ttk.Combobox(headerFrame, value="",width=60).place(x=125,y=5)
  text2=Label(headerFrame,text="Page header text").place(x=2,y=45)
  e1=ttk.Combobox(headerFrame, value="",width=60).place(x=125,y=45)
  text3=Label(headerFrame,text="Footer text").place(x=35,y=85)
  e1=ttk.Combobox(headerFrame, value="",width=60).place(x=125,y=85)

  text=Label(noteFrame,text="Private notes(not shown on invoice/order/estimates)").place(x=10,y=10)
  e1=Text(noteFrame,width=100,height=7).place(x=10,y=32)

  e1=Text(termsFrame,width=100,height=9).place(x=10,y=10)

  e1=Text(commentFrame,width=100,height=9).place(x=10,y=10)

  btn1=Button(documentFrame,height=2,width=3,text="+").place(x=5,y=10)
  btn2=Button(documentFrame,height=2,width=3,text="-").place(x=5,y=50)
  text=Label(documentFrame,text="Attached documents or image files.If you attach large email then email taken long time to send").place(x=50,y=10)
  cusventtree=ttk.Treeview(documentFrame, height=5)
  cusventtree["columns"]=["1","2","3"]
  cusventtree.column("#0", width=20)
  cusventtree.column("1", width=250)
  cusventtree.column("2", width=250)
  cusventtree.column("2", width=200)
  cusventtree.heading("#0",text="", anchor=W)
  cusventtree.heading("1",text="Attach to Email")
  cusventtree.heading("2",text="Filename")
  cusventtree.heading("3",text="Filesize")  
  cusventtree.place(x=50, y=45)
  

  fir4Frame=Frame(pop,height=190,width=210,bg="#f5f3f2")
  fir4Frame.place(x=740,y=520)
  summaryfrme = LabelFrame(fir4Frame,text="Summary",font=("arial",15))
  summaryfrme.place(x=0,y=0,width=200,height=170)
  sl=orbtdata[15]
  s=round(sl, 4)
  pl=ttlp
  p=round(pl, 4)
  dscte=(orbtdata[15]*p)/100
  dsc=round(dscte, 4)
  discount=Label(summaryfrme, text=str(s)+"% Discount").place(x=0 ,y=0)
  discount1=Label(summaryfrme,text=str(dsc)+'/-')
  discount1.place(x=130 ,y=0)
  sbtotlhehe=p-dsc
  sbtotl=round(sbtotlhehe, 4)
  sub=Label(summaryfrme, text="Subtotal").place(x=0 ,y=21)
  sub1=Label(summaryfrme, text=str(sbtotl)+'/-').place(x=130 ,y=21)
  taxval9=orbtdata[16]
  taxval=round(taxval9, 4)
  tax=Label(summaryfrme, text="Tax1").place(x=0 ,y=42)
  tax1=Label(summaryfrme, text=str(taxval)+'/-').place(x=130 ,y=42)
  xtracstvalzz=orbtdata[12]
  xtracst=round(xtracstvalzz, 4)
  cost=Label(summaryfrme, text="Extra cost").place(x=0 ,y=63)
  cost=Label(summaryfrme, text=str(orbtdata[12])+'/-').place(x=130 ,y=63)

  othrttlval=(sbtotl-dsc)+taxval
  ov=round(othrttlval, 4)
  order=Label(summaryfrme, text="Invoice total").place(x=0 ,y=84)
  order1=Label(summaryfrme, text=str(ov)+'/-').place(x=130 ,y=84)
  # totalpaid='10/-'
  total=Label(summaryfrme, text="Total paid").place(x=0 ,y=105)
  total1=Label(summaryfrme, text="0.0/-").place(x=130 ,y=105)
  # paidtotal=str(totalpaid)
  # balanz=othrttlval-paidtotal
  balance=Label(summaryfrme, text="Balance").place(x=0 ,y=126)
  balance1=Label(summaryfrme, text='0.0/-').place(x=130 ,y=126)

  def calculatesummary():
    #  global discount1,sub1,tax1,cost1z,order1
    #  totalpriceinput.config(text="")
     ttlprzinptinv=priceco0.cget("text")
     ratediscntinv=dscntrte.get()
     xtaxinv=taxx.get()
     cstxtrainv=extra_cost.get()
     print(ttlprzinptinv,ratediscntinv,xtaxinv,cstxtrainv)
  
     isdd=round(int(ratediscntinv),3)
     pidd=ttlprzinptinv
     p=round(pidd, 4)
     dsctedd=(isdd*pidd)/100
     dscdd=round(dsctedd, 4)
     discount=Label(summaryfrme, text=str(isdd)+"% Discount").place(x=0 ,y=0)
     discount1=Label(summaryfrme,text='Rs. '+str(dscdd))
     discount1.place(x=130 ,y=0)
  
     sbtotlhee=p-dscdd
     subtotl=round(sbtotlhee, 4)
     sub=Label(summaryfrme, text="Subtotal").place(x=0 ,y=21)
     sub100=Label(summaryfrme, text='Rs. '+str(subtotl))
     sub100.place(x=130 ,y=21)
  
     taxval91=int(xtaxinv)
     tax1dsplay=(taxval91*subtotl)/100
     taxvalu=round(tax1dsplay,2)
     tax=Label(summaryfrme, text="Tax1").place(x=0 ,y=42)
     tax100=Label(summaryfrme, text='Rs. '+str(taxvalu))
     tax100.place(x=130 ,y=42)
  
     xtracstvaluzz=int(cstxtrainv)
     xtra1cst=round(xtracstvaluzz, 4)
     cost=Label(summaryfrme, text="Extra cost").place(x=0 ,y=63)
     cost100=Label(summaryfrme, text='Rs. '+str(xtra1cst)).place(x=130 ,y=63)
  
     otherttlval=subtotl+taxvalu+xtra1cst
     ot1v1=round(otherttlval, 4)
     order=Label(summaryfrme, text="Invoice total").place(x=0 ,y=84)
     order100=Label(summaryfrme, text='Rs. '+str(ot1v1)).place(x=130 ,y=84)
  
     itemidot = invotree.item(invotree.focus())["values"][1]
     ordttl=ot1v1
     for record in invotree.get_children():
       invotree.delete(record)
     sqlordttl = "UPDATE invoice SET invoicetot=%s WHERE invoiceid = %s"
     valqordttl = (ordttl,itemidot, )
     fbcursor.execute(sqlordttl, valqordttl,)
     fbilldb.commit()
     fbcursor.execute('SELECT * FROM invoice')   
     j = 0
     for i in fbcursor:
      invotree.insert(parent='', index='end', iid=i, text='', values=('',i[0], i[2], i[3], i[18], i[4], i[5], i[6], i[7], i[8], i[9], i[10]))
     j += 1
  

  def void_invoice2():
    for x in (selectcustomer2, addline2, deleteline2, markinvo2):
      x.config(state = 'disabled')
    for y in(cmb1,spt1,eml,smsno,e2,e3,xtracstnme,xtracst,tmplte,dscntrte,taxx):
      y.config(state = 'disabled')
    for z in (addrs1,adrs):
      z.config(state = 'disabled')


  fir5Frame=Frame(pop,height=38,width=210)
  fir5Frame.place(x=735,y=485)
  btndown=Button(fir5Frame, compound="left", text="Show summary",command=calculatesummary).place(x=75, y=0, height=35)
#   btnup=Button(fir5Frame, compound="left", text="Line Up").place(x=150, y=0)




#printselected order
  
def printsele():
  subprocess.Popen('C:\\Windows\\System32\\spoolsv.exe')
  

  def property1():
    propert=Toplevel()
    propert.title("Microsoft Print To PDF Advanced Document Settings")
    propert.geometry("670x500+240+150")

    def property2():
      propert1=Toplevel()
      propert1.title("Microsoft Print To PDF Advanced Document Settings")
      propert1.geometry("670x500+240+150")

      name=Label(propert1, text="Microsoft Print To PDF Advanced Document Settings").place(x=10, y=5)
      paper=Label(propert1, text="Paper/Output").place(x=30, y=35)
      size=Label(propert1, text="Paper size").place(x=55, y=65)
      n = StringVar()
      search = ttk.Combobox(propert1, width = 15, textvariable = n )
      search['values'] = ('letter')
      search.place(x=150,y=65)
      search.current(0)
      copy=Label(propert1, text="Copy count:").place(x=55, y=95)

      okbtn=Button(propert1,compound = LEFT,image=tick , text="Ok", width=60).place(x=460, y=450)
      canbtn=Button(propert1,compound = LEFT,image=cancel, text="Cancel", width=60).place(x=570, y=450)
      
      


    style = ttk.Style()
    style.theme_use('default')
    style.configure('TNotebook.Tab', background="#999999", padding=5)
    property_Notebook = ttk.Notebook(propert)
    property_Frame = Frame(property_Notebook, height=500, width=670)
    property_Notebook.add(property_Frame, text="Layout")
    property_Notebook.place(x=0, y=0)

    name=Label(property_Frame, text="Orientation:").place(x=10, y=5)
    n = StringVar()
    search = ttk.Combobox(property_Frame, width = 23, textvariable = n )
    search['values'] = ('Portrait')
    search.place(x=10,y=25)
    search.current(0)

    text=Text(property_Frame,width=50).place(x=250, y=5,height=350)

    btn=Button(property_Frame, text="Advanced",command=property2).place(x=550, y=380)
    btn=Button(property_Frame,compound = LEFT,image=tick  ,text="OK", width=60,).place(x=430, y=420)
    btn=Button(property_Frame,compound = LEFT,image=cancel , text="Cancel", width=60,).place(x=550, y=420)     


    
  if(False):
      messagebox.showwarning("FBilling Revelution 2020", "Customer is required, Please select customer for this invoice\nbefore printing")
  elif(False):
      messagebox.showinfo("FBilling Revelution 2020", "Print job has been completed.")
  else:
      print1=Toplevel()
      print1.title("Print")
      print1.geometry("670x400+240+150")
      
      printerframe=LabelFrame(print1, text="Printer", height=80, width=650)
      printerframe.place(x=7, y=5)      
      name=Label(printerframe, text="Name:").place(x=10, y=5)
      e1= ttk.Combobox(printerframe, width=40).place(x=70, y=5)
      where=Label(printerframe, text="Where:").place(x=10, y=30)
      printocheckvar=IntVar()
      printochkbtn=Checkbutton(printerframe,text="Print to file",variable=printocheckvar,onvalue=1,offvalue=0,height=1,width=10)
      printochkbtn.place(x=450, y=30)
      btn=Button(printerframe, text="Properties", width=10,command=property1).place(x=540, y=5)

      pageslblframe=LabelFrame(print1, text="Pages", height=140, width=320)
      pageslblframe.place(x=10, y=90)
      radvar=IntVar()
      radioall=Radiobutton(pageslblframe, text="All", variable=radvar, value="1").place(x=10, y=5)
      radiocpage=Radiobutton(pageslblframe, text="Current Page", variable=radvar, value="2").place(x=10, y=25)
      radiopages=Radiobutton(pageslblframe, text="Pages: ", variable=radvar, value="3").place(x=10, y=45)
      pagecountentry = Entry(pageslblframe, width=23).place(x=80, y=47)
      pageinfolabl=Label(pageslblframe, text="Enter page numbers and/or page ranges\nseperated by commas. For example:1,3,5-12")
      pageinfolabl.place(x=5, y=75)

      copylblframe=LabelFrame(print1, text="Copies", height=140, width=320)
      copylblframe.place(x=335, y=90)
      nolabl=Label(copylblframe, text="Number of copies").place(x=5, y=5)      
      noentry = Entry(copylblframe, width=18).place(x=130, y=5)      
      one=Frame(copylblframe, width=30, height=40, bg="black").place(x=20, y=40)     
      two=Frame(copylblframe, width=30, height=40, bg="grey").place(x=15, y=45)     
      three=Frame(copylblframe, width=30, height=40, bg="white").place(x=10, y=50)      
      four=Frame(copylblframe, width=30, height=40, bg="black").place(x=80, y=40)      
      fiv=Frame(copylblframe, width=30, height=40, bg="grey").place(x=75, y=45)      
      six=Frame(copylblframe, width=30, height=40, bg="white").place(x=70, y=50)      
      collatecheckvar=IntVar()
      collatechkbtn=Checkbutton(copylblframe,text="Collate",variable=collatecheckvar,onvalue=1,offvalue=0,height=1,width=10)
      collatechkbtn.place(x=130, y=70)

      othrlblframe=LabelFrame(print1, text="Other", height=120, width=320)
      othrlblframe.place(x=10, y=235)
      printlb=Label(othrlblframe, text="Print").place(x=5, y=0)
      dropprint = ttk.Combobox(othrlblframe, width=23).place(x=80, y=0)
      orderlb=Label(othrlblframe, text="Order").place(x=5, y=25)
      dropord = ttk.Combobox(othrlblframe, width=23).place(x=80, y=25)
      duplexlb=Label(othrlblframe, text="Duplex").place(x=5, y=50)
      droplex = ttk.Combobox(othrlblframe, width=23).place(x=80, y=50)

      prmodelblframe=LabelFrame(print1, text="Print mode", height=120, width=320)
      prmodelblframe.place(x=335, y=235)
      dropscal = ttk.Combobox(prmodelblframe, width=30).place(x=5, y=5)
      poslb=Label(prmodelblframe, text="Print on sheet").place(x=5, y=35)
      droppos = ttk.Combobox(prmodelblframe, width=10).place(x=155, y=35)

      okbtn=Button(print1,compound = LEFT,image=tick , text="Ok", width=60).place(x=460, y=370)
      canbtn=Button(print1,compound = LEFT,image=cancel, text="Cancel", width=60).place(x=570, y=370)
      


#email
      
def email_invoice():
  mailDetail=Toplevel()
  mailDetail.title("Invoice E-Mail")
  mailDetail.geometry("1080x550")
  mailDetail.resizable(False, False)
  def my_SMTP():
      if True:
          em_ser_conbtn.destroy()
          mysmtpservercon=LabelFrame(account_Frame,text="SMTP server connection(ask your ISP for your SMTP settings)", height=165, width=380)
          mysmtpservercon.place(x=610, y=110)
          lbl_hostn=Label(mysmtpservercon, text="Hostname").place(x=5, y=10)
          hostnent=Entry(mysmtpservercon, width=30).place(x=80, y=10)
          lbl_portn=Label(mysmtpservercon, text="Port").place(x=5, y=35)
          portent=Entry(mysmtpservercon, width=30).place(x=80, y=35)
          lbl_usn=Label(mysmtpservercon, text="Username").place(x=5, y=60)
          unament=Entry(mysmtpservercon, width=30).place(x=80, y=60)
          lbl_pasn=Label(mysmtpservercon, text="Password").place(x=5, y=85)
          pwdent=Entry(mysmtpservercon, width=30).place(x=80, y=85)
          ssl_chkvar=IntVar()
          ssl_chkbtn=Checkbutton(mysmtpservercon, variable=ssl_chkvar, text="This server requires a secure connection(SSL)", onvalue=1, offvalue=0)
          ssl_chkbtn.place(x=50, y=110)
          em_ser_conbtn1=Button(account_Frame, text="Test E-mail Server Connection").place(x=610, y=285)
      else:
          pass
    
  style = ttk.Style()
  style.theme_use('default')
  style.configure('TNotebook.Tab', background="#999999", padding=5)
  email_Notebook = ttk.Notebook(mailDetail)
  email_Frame = Frame(email_Notebook, height=500, width=1080)
  account_Frame = Frame(email_Notebook, height=550, width=1080)
  email_Notebook.add(email_Frame, text="E-mail")
  email_Notebook.add(account_Frame, text="Account")
  email_Notebook.place(x=0, y=0)

  messagelbframe=LabelFrame(email_Frame,text="Message", height=500, width=730)
  messagelbframe.place(x=5, y=5)
  lbl_emailtoaddr=Label(messagelbframe, text="Email to address").place(x=5, y=5)
  emailtoent=Entry(messagelbframe, width=50).place(x=120, y=5)
  sendemail_btn=Button(messagelbframe, text="Send Email", width=10, height=1,command=addacnt).place(x=600, y=10)
  lbl_carcopyto=Label(messagelbframe, text="Carbon copy to").place(x=5, y=32)
  carcopyent=Entry(messagelbframe, width=50).place(x=120, y=32)
  stopemail_btn=Button(messagelbframe, text="Stop sending", width=10, height=1).place(x=600, y=40)
  lbl_subject=Label(messagelbframe, text="Subject").place(x=5, y=59)
  subent=Entry(messagelbframe, width=50).place(x=120, y=59)

  
  style = ttk.Style()
  style.theme_use('default')
  style.configure('TNotebook.Tab', background="#999999", width=20, padding=5)
  mess_Notebook = ttk.Notebook(messagelbframe)
  emailmessage_Frame = Frame(mess_Notebook, height=350, width=710)
  htmlsourse_Frame = Frame(mess_Notebook, height=350, width=710)
  mess_Notebook.add(emailmessage_Frame, text="E-mail message")
  mess_Notebook.add(htmlsourse_Frame, text="Html sourse code")
  mess_Notebook.place(x=5, y=90)

  btn1=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=selectall).place(x=0, y=1)

  
  btn2=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=cut).place(x=36, y=1)
  btn3=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=copy).place(x=73, y=1)
  btn4=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=paste).place(x=105, y=1)
  btn5=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=undo).place(x=140, y=1)
  btn6=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=redo).place(x=175, y=1)
  btn7=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=bold).place(x=210, y=1)
  btn8=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=italics).place(x=245, y=1)
  btn9=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=underline).place(x=280, y=1)
  btn10=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=left).place(x=315, y=1)
  btn11=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=right).place(x=350, y=1)
  btn12=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=center).place(x=385, y=1)
  btn13=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=hyperlink).place(x=420, y=1)
  
  btn14=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=remove).place(x=455, y=1)


  dropcomp = ttk.Combobox(emailmessage_Frame, width=12, height=3).place(x=500, y=5)
  dropcompo = ttk.Combobox(emailmessage_Frame, width=6, height=3).place(x=600, y=5)
  mframe=Frame(emailmessage_Frame, height=350, width=710, bg="white")
  mframe.place(x=0, y=28)



  btn1=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=selectall).place(x=0, y=1)

  
  btn2=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=cut).place(x=36, y=1)
  btn3=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=copy).place(x=73, y=1)
  btn4=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=paste).place(x=105, y=1)
  mframe=Frame(htmlsourse_Frame, height=350, width=710, bg="white")
  mframe.place(x=0, y=28)

  attachlbframe=LabelFrame(email_Frame,text="Attachment(s)", height=350, width=280)
  attachlbframe.place(x=740, y=5)
  htcodeframe=Frame(attachlbframe, height=220, width=265, bg="white").place(x=5, y=5)
  lbl_btn_info=Label(attachlbframe, text="Double click on attachment to view").place(x=30, y=230)
  btn17=Button(attachlbframe, width=20, text="Add attacment file...").place(x=60, y=260)
  btn18=Button(attachlbframe, width=20, text="Remove attacment").place(x=60, y=295)
  lbl_tt_info=Label(email_Frame, text="You can create predefined invoice, order, estimate\nand payment receipt email templates under Main\nmenu/Settings/E-Mail templates tab")
  lbl_tt_info.place(x=740, y=370)

  ready_frame=Frame(mailDetail, height=20, width=1080, bg="#b3b3b3").place(x=0,y=530)
  
  sendatalbframe=LabelFrame(account_Frame,text="E-Mail(Sender data)",height=270, width=600)
  sendatalbframe.place(x=5, y=5)
  lbl_sendermail=Label(sendatalbframe, text="Your company email address").place(x=5, y=30)
  sentent=Entry(sendatalbframe, width=40).place(x=195, y=30)
  lbl_orcompanyname=Label(sendatalbframe, text="Your name or company name").place(x=5, y=60)
  nament=Entry(sendatalbframe, width=40).place(x=195, y=60)
  lbl_reply=Label(sendatalbframe, text="Reply to email address").place(x=5, y=90)
  replyent=Entry(sendatalbframe, width=40).place(x=195, y=90)
  lbl_sign=Label(sendatalbframe, text="Signature").place(x=5, y=120)
  signent=Entry(sendatalbframe,width=50).place(x=100, y=120,height=75)
  confirm_chkvar=IntVar()
  confirm_chkbtn=Checkbutton(sendatalbframe, variable=confirm_chkvar, text="Confirmation reading", onvalue=1, offvalue=0)
  confirm_chkbtn.place(x=200, y=215)
  btn18=Button(account_Frame, width=15, text="Save settings",command=savesettings).place(x=25, y=285)

  sendatalbframe=LabelFrame(account_Frame,text="SMTP Server",height=100, width=380)
  sendatalbframe.place(x=610, y=5)
  servar=IntVar()
  SMTP_rbtn=Radiobutton(sendatalbframe, text="Use the Built-In SMTP Server Settings", variable=servar, value=1)
  SMTP_rbtn.place(x=10, y=10)
  MySMTP_rbtn=Radiobutton(sendatalbframe, text="Use My Own SMTP Server Settings(Recommended)", variable=servar, value=2, command=my_SMTP)
  MySMTP_rbtn.place(x=10, y=40)
  em_ser_conbtn=Button(account_Frame, text="Test E-mail Server Connection")
  em_ser_conbtn.place(x=710, y=110)




#sms notification order
  
def sms():
  send_SMS=Toplevel()
  send_SMS.geometry("700x480+240+150")
  send_SMS.title("Send SMS notification")

  style = ttk.Style()
  style.theme_use('default')
  style.configure('TNotebook.Tab', background="#999999", padding=5)
  sms_Notebook = ttk.Notebook(send_SMS)
  SMS_Notification = Frame(sms_Notebook, height=470, width=700)
  SMS_Service_Account = Frame(sms_Notebook, height=470, width=700)
  sms_Notebook.add(SMS_Notification, text="SMS Notification")
  sms_Notebook.add(SMS_Service_Account, text="SMS Service Account")
  sms_Notebook.place(x=0, y=0)

  numlbel=Label(SMS_Notification, text="SMS number or comma seperated SMS number list(Please start each SMS number with the country code)")
  numlbel.place(x=10, y=10)
  numentry=Entry(SMS_Notification, width=92).place(x=10, y=30)
  stexbel=Label(SMS_Notification, text="SMS Text").place(x=10, y=60)
  stex=Entry(SMS_Notification, width=40).place(x=10, y=85,height=120)
  
  dclbel=Label(SMS_Notification, text="Double click to insert into text")
  dclbel.place(x=410, y=60)
  dcl=Entry(SMS_Notification, width=30)
  dcl.place(x=400, y=85,height=200)
  
  smstype=LabelFrame(SMS_Notification, text="SMS message type", width=377, height=60)
  smstype.place(x=10, y=223)
  snuvar=IntVar()
  normal_rbtn=Radiobutton(smstype, text="Normal SMS(160 chars)", variable=snuvar, value=1)
  normal_rbtn.place(x=5, y=5)
  unicode_rbtn=Radiobutton(smstype, text="Unicode SMS(70 chars)", variable=snuvar, value=2)
  unicode_rbtn.place(x=190, y=5)
  tiplbf=LabelFrame(SMS_Notification, text="Tips", width=680, height=120)
  tiplbf.place(x=10, y=290)
  tiplabl=Label(tiplbf,justify=LEFT,fg="red",  text="Always start the SMS nymber with the country code. Do not use the + sign at the beginning(example\nUS number:8455807546). Do not use any special characters in your normal SMS text. Please use the\nstndard SMS characters or the English alphabet and numbers only. Otherwise the SMS will be\nunreadable or undeliverable. If you need to enter international characters, accents,email address, or\nspecial characters to the SMS text field then choose the Unicode SMS format.")
  tiplabl.place(x=5, y=5)

  btn1=Button(SMS_Notification, width=20, text="Send SMS notification").place(x=10, y=420)
  btn2=Button(SMS_Notification, width=25, text="Confirm SMS cost before sending").place(x=280, y=420)
  btn3=Button(SMS_Notification, width=15, text="Cancel").place(x=550, y=420)
  

  smstype=LabelFrame(SMS_Service_Account, text="Select the notification service provider", width=670, height=65)
  smstype.place(x=10, y=5)
  snumvar=IntVar()
  normal_rbtn=Radiobutton(smstype,text="BULKSMS(www.bulksms.com)",variable=snumvar,value=1,)
  normal_rbtn.place(x=5, y=5)
  unicode_rbtn=Radiobutton(smstype, text="Unicode SMS(70 chars)-Recommended", variable=snumvar, value=2)
  unicode_rbtn.place(x=290, y=5)

  sms1type=LabelFrame(SMS_Service_Account, text="Your BULKSMS.COM Account", width=670, height=100)
  sms1type.place(x=10, y=80)
  name=Label(sms1type, text="Username").place(x=10, y=5)
  na=Entry(sms1type, width=20).place(x=100, y=5)
  password=Label(sms1type, text="Password").place(x=10, y=45)
  pas=Entry(sms1type, width=20).place(x=100, y=45)
  combo=Label(sms1type, text="Route").place(x=400, y=5)
  n = StringVar()
  combo1 = ttk.Combobox(sms1type, width = 20, textvariable = n ).place(x=450,y=5)
  btn1=Button(sms1type, width=10, text="Save settings").place(x=550, y=45)

  
  tiplbf=LabelFrame(SMS_Service_Account, text="Terms of service", width=680, height=250)
  tiplbf.place(x=10, y=190)
  tiplabl=Label(tiplbf,justify=LEFT,fg="red",  text="The SMS notification service is not free.This service costs you creadit.You must have your own account\nat BULKSMS.COM and you need to have sufficient creadit and an active internet connection to use\nthis feature.Please review all fields in this form for accuracy")
  tiplabl.place(x=0, y=5)
  tiplabl1=Label(tiplbf,justify=LEFT,fg="black",  text="visit www.bulksms.com website to create your own account.please make sure the BULKSMS .COM\n service works well in your country before you busy creadit")
  tiplabl1.place(x=0, y=60)
  tiplabl2=Label(tiplbf,justify=LEFT,fg="black",  text="Our SMS notification tool comes without any warranty.our software only forwards your SMS message\nthe BULKSMS API server .The BULKSMS API server will try to sent SMS message your recipient")
  tiplabl2.place(x=0, y=100)
  tiplabl3=Label(tiplbf,justify=LEFT,fg="red",  text="Please note that you access and use the SMS notification tool your own risk.F-Billing software is not\nresponsible for any type of loss or damage or undelivered SMS massage which you may as a result\nof accessing and using the SMS notification service.")
  tiplabl3.place(x=0, y=140)
  checkvar1=IntVar()
  chkbtn1=Checkbutton(tiplbf,text="I have read and agree to the terms of service above",variable=checkvar1,onvalue=1,offvalue=0).place(x=70, y=200)  



#print preview order
def printpreview():
  messagebox.showerror("F-Billing Revolution","Customer is required,please select customer for this order before printing.")




#delete invoice  
def delete_invoice():
  delmess = messagebox.askyesno("Delete Invoice", "Are you sure to delete this Invoice?")
  if delmess == True:
    itemid = invotree.item(invotree.focus())["values"][1]
    # print(itemid,)
    sql = 'DELETE FROM invoice WHERE invoiceid=%s'
    val = (itemid,)
    fbcursor.execute(sql, val)
    fbilldb.commit()
    invotree.delete(invotree.selection()[0])

    sqlstrngprdct='DELETE FROM storingproduct WHERE invoiceid=%s'
    valstpr = (itemid,)
    fbcursor.execute(sqlstrngprdct, valstpr)
    fbilldb.commit()
    for record in invotree.get_children():
      invotree.delete(record)
        
    sql = "SELECT * FROM invoice"
    fbcursor.execute(sql,)
    
    a=0
    j = 0
    for i in fbcursor:
      invotree.insert(parent='', index='end', iid=i, text='', values=('',i[0], i[2], i[3], i[18], i[4], i[5], i[6], i[7], i[8], i[9], i[10]))
      for line in invotree.get_children():
          idsave=invotree.item(line)['values'][9]
      a+=idsave
    j += 1
    invototalrowcol.config(text=a)
    # vwedttree1.delete(vwedttree1.selection()[0])
  else:
    pass

#####search invoice
def search_invoice():
  query = searchvar.get()
  selections = []
  for child in invotree.get_children():
      if query in invotree.item(child)['values']:
          print(invotree.item(child)['values'])
          selections.append(child)
  invotree.selection_set(selections)

def search():
  global searchvar  
  top = Toplevel()     
  top.title("Find Text")   
  top.geometry("600x250+390+250")
  global findwhat
  findwhat1=Label(top,text="Find What:",pady=5,padx=10).place(x=5,y=20)
  searchvar = StringVar()
  findwhat = ttk.Combobox(top, width = 40, textvariable = searchvar ).place(x=90,y=25)
  
  findin1=Label(top,text="Find in:",pady=5,padx=10).place(x=5,y=47)
  n = StringVar()
  findIN = ttk.Combobox(top, width = 30, textvariable = n )
  findIN['values'] = ('Product/Service id', ' Category', ' Active',' name',' stock',' location', ' image',' <<All>>')                       
  findIN.place(x=90,y=54)
  findIN.current(0)
  findButton = Button(top, text ="Find next",width=10,command=search_invoice).place(x=480,y=22)
  closeButton = Button(top,text ="Close",width=10).place(x=480,y=52)
  
  match1=Label(top,text="Match:",pady=5,padx=10).place(x=5,y=74)
  n = StringVar()
  match = ttk.Combobox(top, width = 23, textvariable = n )   
  match['values'] = ('From Any part',' Whole Field',' From the beginning of the field')                                   
  match.place(x=90,y=83)
  match.current(0)
  search1=Label(top,text="Search:",pady=5,padx=10).place(x=5,y=102)
  n = StringVar()
  search = ttk.Combobox(top, width = 23, textvariable = n )
  search['values'] = ('All', 'up',' Down')
  search.place(x=90,y=112)
  search.current(0)
  checkvarStatus4=IntVar()  
  Button4 = Checkbutton(top,variable = checkvarStatus4,text="Match Case",onvalue =0 ,offvalue = 1,height=3,width = 15)
  Button4.place(x=90,y=141)
  checkvarStatus5=IntVar()   
  Button5 = Checkbutton(top,variable = checkvarStatus5,text="Match Format",onvalue =0 ,offvalue = 1,height=3,width = 15)
  Button5.place(x=300,y=141)

# def search_records():
#   query = findwhat.get()
#   selections = []
#   for child in invotree.get_children():
#       if query in invotree.item(child)['values']:
#           print(invotree.item(child)['values'])
#           selections.append(child)
#   invotree.selection_set(selections)

def printpreviewinvoice():
  ws = Tk()
  ws.title('F-Billing Revolution 2022 - invoice')
  ws.maxsize(1360,740)       # Sets max size of window
  ws.minsize(1360,740)
  ws['bg']='#999999'

  style = ttk.Style(root)
  style.theme_use("clam")
  style.theme_use("default")
  # style.configure("Treeview.Heading", backgro
  # und="#ffad33")

  # tree=ttk.Treeview(master,style="mystyle.Treeview")
 
  tv = ttk.Treeview(ws, style="mystyle.Treeview", height=18, show='headings')
  # tv["show"]='headings'
  tv['columns']=('Id/sku', 'Product/Service', 'Description', 'Quantity','Unit Price','Price')
  tv.column('Id/sku', anchor=CENTER, width=100)
  tv.column('Product/Service', anchor=CENTER, width=200)
  tv.column('Description', anchor=CENTER, width=300)
  tv.column('Quantity', anchor=CENTER, width=100)
  tv.column('Unit Price', anchor=CENTER, width=100)
  tv.column('Price', anchor=CENTER, width=100)

  tv.heading('Id/sku', text='ID/SKU', anchor=CENTER,)
  tv.heading('Product/Service', text='Product/Service', anchor=CENTER)
  tv.heading('Description', text='Description', anchor=CENTER)
  tv.heading('Quantity', text='Quantity', anchor=CENTER)
  tv.heading('Unit Price', text='Unit Price', anchor=CENTER)
  tv.heading('Price', text='Price', anchor=CENTER) 

  itemid = invotree.item(invotree.focus())["values"][1]
  sql = "select * from invoice where invoiceid = %s"
  val = (itemid, )
  fbcursor.execute(sql, val)
  recurdata = fbcursor.fetchone()
  ba=recurdata[0]
  sql4='SELECT * FROM storingproduct WHERE invoiceid=%s'
  val10=(ba,)
  fbcursor.execute(sql4,val10)
  j = 0
  for i in fbcursor:
    tv.insert(parent='', index='end', iid=i, text='', values=(i[4], i[6], i[6], i[22], i[9], (i[22]*i[9])))
  j += 1

  tv.place(x=230, y=30)
# -------------------------subtree for total------------------------
  # tv1 = ttk.Treeview(ws, style="mystyle.Treeview", height=5)
  # # ttk.Style().configure("Treeview", background="#ebebe0", foreground="#ebebe0")
  # tv1.insert(parent='', index=0, iid=0, values=("vineet", "e11", 1000000.00))
  # tv1.insert(parent='', index=1, iid=1, values=("anil", "e12", 120000.00))
  # tv1.insert(parent='', index=2, iid=2, values=("ankit", "e13", 41000.00))
  # tv1.insert(parent='', index=3, iid=3, values=("Shanti", "e14", 22000.00))
  # tv1.place(x=900, y=549)
 

  
  scrollbar = Scrollbar(ws)
  scrollbar.place(x=1339, y=2, height=700)
  scrollbar.config( command=tree.yview )

  ws.mainloop()


mainFrame=Frame(tab1, relief=GROOVE, bg="#f8f8f2")
mainFrame.pack(side="top", fill=BOTH)

midFrame=Frame(mainFrame, bg="#f5f3f2", height=60)
midFrame.pack(side="top", fill=X)

w = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=(5, 2))
w = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=(0, 5))

invoiceLabel = Button(midFrame,compound="top", text="Create new\nInvoice",relief=RAISED, image=photo,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=createmaininvoice)
invoiceLabel.pack(side="left", pady=3, ipadx=4)

orderLabel = Button(midFrame,compound="top", text="View/Edit\nInvoice",relief=RAISED, image=photo1,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=edit_invoice)
orderLabel.pack(side="left")

estimateLabel = Button(midFrame,compound="top", text="Delete\nSelected",relief=RAISED, image=photo2,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=delete_invoice)
estimateLabel.pack(side="left")

w = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=5)

previewLabel = Button(midFrame,compound="top", text="Print\nSelected",relief=RAISED, image=photo4,bg="#f8f8f2", fg="black", height=55, bd=1, width=55, activebackground="red",command=printpreviewinvoice)
previewLabel.pack(side="left")

# purchaseLabel = Button(midFrame,compound="top", text="Print\nSelected",relief=RAISED, image=photo5,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=printsele)
# purchaseLabel.pack(side="left")

w = Canvas(midFrame, width=1, height=55, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=5)

expenseLabel = Button(midFrame,compound="top", text="E-mail\nInvoice",relief=RAISED, image=photo6,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=email_invoice)
expenseLabel.pack(side="left")

smsLabel = Button(midFrame,compound="top", text="Send SMS\nnotification",relief=RAISED, image=photo10,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=sms)
smsLabel.pack(side="left")

w = Canvas(midFrame, width=1, height=55, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=5)

productLabel = Button(midFrame,compound="top", text="Search\nInvoice",relief=RAISED, image=photo7,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=search)
productLabel.pack(side="left")

lbframe = LabelFrame(midFrame, height=60, width=200, bg="#f8f8f2")
lbframe.pack(side="left", padx=10, pady=0)
lbl_invdt = Label(lbframe, text="Invoice date from : ", bg="#f8f8f2")
lbl_invdt.grid(row=0, column=0, pady=5, padx=(5, 0))
lbl_invdtt = Label(lbframe, text="Invoice date to  :  ", bg="#f8f8f2")
lbl_invdtt.grid(row=1, column=0, pady=5, padx=(5, 0))


def date_range(): # Start and stop dates for range
  var1=invdt.get_date().strftime('%y/%m/%d')
  var2=invdtt.get_date().strftime('%y/%m/%d')
  for record in invotree.get_children():
    invotree.delete(record)

  sqldate='SELECT * FROM invoice WHERE invodate BETWEEN %s AND %s'
  valuz=(var1,var2,)
  fbcursor.execute(sqldate,valuz)
  filterdate=fbcursor.fetchall()
  countp = 0
  for i in filterdate:
    invotree.insert(parent='', index='end', iid=i, text='', values=('',i[0], i[2], i[3], i[18], i[4], i[5], i[6], i[7], i[8], i[9], i[10]))
  countp += 1



invdt = DateEntry(lbframe, width=15)
invdt.grid(row=0, column=1)
invdtt = DateEntry(lbframe, width=15)
invdtt.grid(row=1, column=1)
checkvar1 = IntVar()
chkbtn1 = Checkbutton(lbframe, text = "Apply filter", variable = checkvar1, onvalue = 1, offvalue = 0, height = 2, width = 8, bg="#f8f8f2", command=date_range)
chkbtn1.grid(row=0, column=2, rowspan=2, padx=(5,5))

  # ##################Refresh MySQL data to Treeview#####################
def refreshinvoice():
      for record in invotree.get_children():
          invotree.delete(record)
          count=0
      fbcursor.execute('SELECT * FROM invoice;')
      for i in fbcursor:
          if True:
              invotree.insert(parent='', index='end', iid=i, text='hello', values=('',i[0], i[2], i[3], i[18], i[4], i[5], i[6], i[7], i[8], i[9], i[10]))
          else:
              pass
      count += 1

productLabel = Button(midFrame,compound="top", text="Refresh\nInvoice list",relief=RAISED, image=photo8,fg="black", height=55, bd=1, width=55,command=refreshinvoice)
productLabel.pack(side="left")

w = Canvas(midFrame, width=1, height=55, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=5)

productLabel = Button(midFrame,compound="top", text="Hide totals\nSum",relief=RAISED, image=photo9,bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
productLabel.pack(side="left")

invoilabel = Label(mainFrame, text="Invoice(All)", font=("arial", 18), bg="#f8f8f2")
invoilabel.pack(side="left", padx=(20,0))
drop = ttk.Combobox(mainFrame, value="Hello")
drop.pack(side="right", padx=(0,10))
invoilabel = Label(mainFrame, text="Category filter", font=("arial", 15), bg="#f8f8f2")
invoilabel.pack(side="right", padx=(0,10))

# class MyApp:
#   def __init__(self, parent):
    
#     self.myParent = parent 

#     self.myContainer1 = Frame(parent) 
#     self.myContainer1.pack()
    
#     self.top_frame = Frame(self.myContainer1) 
#     self.top_frame.pack(side=TOP,
#       fill=BOTH, 
#       expand=YES,
#       )  

#     self.left_frame = Frame(self.top_frame, background="white",
#       borderwidth=5,  relief=RIDGE,
#       height=250, 
#       width=2000, 
#       )
#     self.left_frame.pack(side=LEFT,
#       fill=BOTH, 
#       expand=YES,
#       )

s = ttk.Style()
s.configure('Treeview.Heading', background='white', foreground='dark blue', State='DISABLE')


invotree=ttk.Treeview(tab1,selectmode='browse')
invotree.pack(side = 'top')
invotree["columns"]=("1","2","3","4","5","6","7","8","9","10","11","12")
invotree["show"]='headings'
invotree["height"]='15'
invotree.heading("2", text="Invoice#")
invotree.heading("3", text="Invoice date")
invotree.heading("4", text="Due date")
invotree.heading("5", text="Customer Name")
invotree.heading("6", text="Status")
invotree.heading("7", text="Emailed on")
invotree.heading("8", text="Printed on")
invotree.heading("9", text="SMS on")
invotree.heading("10", text="Invoice Total")
invotree.heading("11", text="Total Paid")
invotree.heading("12", text="Balance")
invotree.column("1", width = 35)
invotree.column("2", width = 130)
invotree.column("3", width = 110)
invotree.column("4", width = 110)
invotree.column("5", width = 180)
invotree.column("6", width = 110)
invotree.column("7", width = 130)
invotree.column("8", width = 110)
invotree.column("9", width = 110)
invotree.column("10", width = 110)
invotree.column("11", width = 110)
invotree.column("12", width = 100)
invototalrowcol = Label(tab1,bg="#f5f3f2")
invototalrowcol.place(x=1010,y=400,width=80,height=18)
invototalrowcol2 = Label(tab1,bg="#f5f3f2")
invototalrowcol2.place(x=1150,y=400,width=80,height=18)
invototalrowcol3 = Label(tab1,bg="#f5f3f2")
invototalrowcol3.place(x=1260,y=400,width=80,height=18)
def prdpicker(event):

        selected = invotree.focus()
        selected_prdct= invotree.item(selected)["values"][1]
        for record in prstree.get_children():
         prstree.delete(record)
        sqlprdct='SELECT * FROM storingproduct WHERE invoiceid=%s'
        valprdct=(selected_prdct,)
        fbcursor.execute(sqlprdct,valprdct)
        prdctsltn=fbcursor.fetchall()
        j = 0
        for i in prdctsltn:
         prstree.insert(parent='', index='end', iid=i, text='', values=(' ',i[21], i[6], i[7],i[9],i[22],i[12],(i[9]*i[22])))
        j += 1
invotree.bind('<Double-Button-1>' , prdpicker)

# invotree.bind('<Enter>', lambda event :item_selected1())
# def item_selected1(event):
#         selected = invotree.focus()
#         global valuep
#         valuep= invotree.item(selected)["values"][0]
#         print(valuep)
#         # messagebox.showinfo("",valuep)

#         sql = "SELECT * FROM productservice  WHERE productserviceid= %s"
#         i=(valuep,)
#         fbcursor.execute(sql,i)
        
#         j = 0
#         for i in fbcursor:
#          prstree.insert(parent='', index='end', iid=i, text='', values=(i[2],i[4],i[5],i[7],i[13],i[8],i[10],(i[7]*i[13])))
#         j += 1

fbcursor.execute('SELECT * FROM invoice')
invoicetotalinput=0
j = 0
for i in fbcursor:
  invotree.insert(parent='', index='end', iid=i, text='hello', values=('',i[0], i[2], i[3], i[18], i[4], i[5], i[6], i[7], i[8], i[9], i[10]))
  for line in invotree.get_children():
    idsave1=invotree.item(line)['values'][9]
    print(idsave1)
  invoicetotalinput += idsave1
  j += 1
invototalrowcol.config(text=invoicetotalinput)



inverticalbar=ttk.Scrollbar()
inverticalbar.place(x=995+350,y=143,height=300+20)
tabControl = ttk.Notebook(tab1)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 =  ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)
tabControl.add(tab1,image=invoices,compound = LEFT, text ='Invoice Items',)
tabControl.add(tab2,image=orders,compound = LEFT, text ='Private Notes')
tabControl.add(tab3,image=estimates,compound = LEFT, text ='SMS Log')
tabControl.add(tab4,image=estimates,compound = LEFT, text ='Documents')
tabControl.pack(expand = 1, fill ="both")

prstree = ttk.Treeview(tab1, columns = (1,2,3,4,5,6,7,8,), height = 15, show = "headings")
prstree.pack(side = 'top')
prstree.heading(1)
prstree.heading(2, text="Product/Service ID",)
prstree.heading(3, text="Name")
prstree.heading(4, text="Description")
prstree.heading(5, text="Price")
prstree.heading(6, text="QTY")
prstree.heading(7, text="Tax1")
prstree.heading(8, text="Line Total")   
prstree.column(1, width = 50)
prstree.column(2, width = 270) 
prstree.column(3, width = 270)
prstree.column(4, width = 300)
prstree.column(5, width = 130)
prstree.column(6, width = 100)
prstree.column(7, width = 100)
prstree.column(8, width = 150)

# fbcursor.execute('SELECT * FROM Productservice;') 
# j = 0
# for i in fbcursor:
#     prstree.insert(parent='', index='end', iid=i, text='', values=(' ',i[0],i[4],i[5],i[7],i[8],i[10],(i[7]*i[8])))
#     j += 1

note1=Text(tab2, width=220,height=10).place(x=10, y=10)
note1=Text(tab3, width=2200,height=10).place(x=10, y=10)
tree = ttk.Treeview(tab4, columns = (1,2,3), height = 15, show = "headings")
tree.pack(side = 'top')
tree.heading(1)
tree.heading(2, text="Attach to Email",)
tree.heading(3, text="Filename")
tree.column(1, width = 50)
tree.column(2, width = 290)
tree.column(3, width = 1000)
expverticalbar=ttk.Scrollbar()
expverticalbar.place(x=995+350,y=520,height=195)



def calcu():
  subprocess.Popen('C:\\Windows\\System32\\calc.exe')

# global printsele1
# def printsele1():
#   subprocess.Popen('C:\\Windows\\System32\\print.exe')

def ord_cust_reg():# Storing values into db (user)contp,cemail,ctel,cfax,cmob,scontp,scemail,sctel,scfax,ccountry,ccity
  customerid = custid.get()
  businessname = bname.get()
  businessaddress = baddress.get()
  category= cat.get()
  shipname= sname.get()
  shipaddress = saddress.get()
  contactperson= contp.get()
  cpemail = cemail.get()
  cptelno = ctel.get()
  cpfax = cfax.get()
  cpmobileforsms = cmob.get()
  shipcontactperson= scontp.get()
  shipcpemail= scemail.get()
  shipcptelno= sctel.get()
  shipcpfax = scfax.get()
  country= ccountry.get()
  city = ccity.get()
  notes= cnotes.get()
  status= checkvar1.get()
  taxexempt= checkvar2.get()

  sql='INSERT INTO Customer (customerid,businessname,businessaddress,category,status,shipname,shipaddress,contactperson,cpemail,cptelno,cpfax,cpmobileforsms,shipcontactperson,shipcpemail,shipcptelno,shipcpfax,taxexempt,country,city,notes) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)' #adding values into db
  val=(customerid,businessname,businessaddress,category,status,shipname,shipaddress,contactperson,cpemail,cptelno,cpfax,cpmobileforsms,shipcontactperson,shipcpemail,shipcptelno,shipcpfax,taxexempt,country,city,notes)
  fbcursor.execute(sql,val)
  fbilldb.commit()
  messagebox.showinfo('Registration successfull','Registration successfull')

def ord_prdt_reg():# Storing values into db (user)
  sku = codeentry.get()
  category = country.get()
  name = nameentry.get()
  description = desentry.get()
  unitprice = unitentry.get()
  peices = pcsentry.get()
  cost = costentry.get()
  priceminuscost = priceentry.get()
  stock = stockentry.get()
  stocklimit = lowentry.get()
  warehouse = wareentry.get()
  privatenote = txt.get("1.0",'end-1c')
  status = checkvarStatus.get()
  taxable = checkvarStatus.get()
  serviceornot = checkvarStatus.get()
  sql='INSERT INTO Productservice (sku,category,name,description,unitprice,peices,cost,priceminuscost,stock,stocklimit,warehouse,privatenote,status,taxable,serviceornot) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)' #adding values into db
  val=(sku,category,name,description,unitprice,peices,cost,priceminuscost,stock,stocklimit,warehouse,privatenote,status,taxable,serviceornot)
  fbcursor.execute(sql,val)
  fbilldb.commit()
  messagebox.showinfo('Registration successfull','Registration successfull')


       

def addacnt():  
   messagebox.showinfo("F-Billing Revolution 2022", "No sender email address.\nPlease fill Your company email address textfield under the Account tab.")

def savesettings():  
   messagebox.showinfo("F-Billing Revolution 2022", "Your E-mail configuration settings has been saved.")



root.mainloop()