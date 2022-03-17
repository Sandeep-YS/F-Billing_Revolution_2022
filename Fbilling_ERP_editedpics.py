
from cgitb import text
from itertools import count
from multiprocessing.sharedctypes import Value
from optparse import Values
from sre_parse import State
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter.scrolledtext as scrolledtext
from turtle import bgcolor
from unicodedata import category
from webbrowser import BackgroundBrowser
from PIL import ImageTk, Image
from tkcalendar import Calendar
from tkcalendar import DateEntry
import mysql.connector 
from tkinter import filedialog
from models import *

root=Tk()
root.geometry("1500x800")
root.state("zoomed")
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
addnew = PhotoImage(file="images/plus.png")
tick = PhotoImage(file="images/check.png")
cancel = PhotoImage(file="images/close.png")

tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3=  ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)
tab5 = ttk.Frame(tabControl)
tab6=  ttk.Frame(tabControl)
tab7 = ttk.Frame(tabControl)
tab8 = ttk.Frame(tabControl)
tab9 = ttk.Frame(tabControl)
tab10= ttk.Frame(tabControl)

  
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


# def file():
#     filename = filedialog.askopenfilename(title='open',)
#     return filename
# def file_upload():
#     f = file()
#     img = Image.open(f)
#     img = img.resize((250, 250), Image.ANTIALIAS)
#     img = ImageTk.PhotoImage(img)
#     panel = Label(tab2, image=img)
#     panel.image = img
#     panel.pack()



  

    
mainFrame=Frame(relief=GROOVE, bg="#f8f8f2")
mainFrame.pack(side="top", fill=BOTH)

midFrame=Frame(mainFrame, bg="#f5f3f2", height=60)
midFrame.pack(side="top", fill=X)



#######Expense Module###################################################

def add_expense():
    window = Toplevel()  
    global expamountval,expdate,vn,cn,expdescriptionentry,expstaffentry,checkvarStatus4,cus,rebi,id_sku1,rebill_amoun,exptxt
    window.title("Add new Expense")
    p2 = PhotoImage(file = 'images/fbicon.png')
    window.iconphoto(False, p1)
 
    window.geometry("618x449+380+167")

    innerexpFrame = Frame(window, relief=GROOVE)
    innerexpFrame.pack(side="top",fill=BOTH)

    expenselabelframe = LabelFrame(innerexpFrame,text="Expense Cost",width=580,height=400)
    expenselabelframe.pack(side="top",fill=BOTH,padx=10)


    expamountval = IntVar(expenselabelframe, value='$.00')
    expamount=Label(expenselabelframe,text="Expense amount:",pady=10,padx=10)
    expamount.place(x=12,y=0)
    expamountentry = Entry(expenselabelframe,width=15,textvariable=expamountval)
    expamountentry.place(x=130,y=10)


    lbl_date=Label(expenselabelframe,text=" Date :",fg='black')
    lbl_date.place(x=380,y=10)
    
    expdate=DateEntry(expenselabelframe)
    expdate.place(x=450,y=12)

    vendor1=Label(expenselabelframe,text="Vendor:",pady=5,padx=10)
    vendor1.place(x=20,y=40)
    vn = StringVar() 
    vendor = ttk.Combobox(expenselabelframe, width = 27, textvariable = vn ) 
      
    # Adding combobox drop down list 
    vendor['values'] = ('Default') 
      
    vendor.place(x=130,y=45) 
    vendor.current(0)

    categoryexp1=Label(expenselabelframe,text="Category:",pady=5,padx=10)
    categoryexp1.place(x=330,y=40)
    cn = StringVar() 
    categorydrop = ttk.Combobox(expenselabelframe, width = 22, textvariable = cn ) 
      
    # Adding combobox drop down list 
    categorydrop['values'] = ('Default' ) 
      
    categorydrop.place(x=400,y=45) 
    categorydrop.current(0)

    

    expdescription=Label(expenselabelframe,text="Description:",pady=10,padx=10)
    expdescription.place(x=12,y=70)
    expdescriptionentry = Entry(expenselabelframe,width=70)
    expdescriptionentry.place(x=130,y=81)

    expstafftval = StringVar(expenselabelframe, value='Administrator')
    expstaff=Label(expenselabelframe,text="Staff member:",pady=10,padx=10)
    expstaff.place(x=12,y=108)
    expstaffentry = Entry(expenselabelframe,width=30,textvariable=expstafftval)
    expstaffentry.place(x=130,y=118)

    checkvarStatus4=StringVar()
   
    Button4 = Checkbutton(expenselabelframe,variable = checkvarStatus4, 
                      text="Taxable Tax1 rate", 
                      onvalue =0 ,
                      offvalue = 1,
                      height=3,
                      width = 15)

    Button4.place(x=250,y=100)

    def toggle():
      if other.get():
        ent.place(x=45,y=180)
        button51.place(x=250, y=160)
      else:
        ent.place_forget()
        button51.place_forget()
    other = BooleanVar()
    button5 = Checkbutton(expenselabelframe, text="Assign to customer (optional)", variable=other, 
    command=toggle)
    button5.place(x=40, y=160)
    cus = StringVar()
    ent=ttk.Combobox(expenselabelframe,width=30,textvariable=cus)
    def toggle():
      if rebill.get():
        id_skulabel.place(x=375,y=160)
        id_skuentry.place(x=420,y=160)
        rebill_label.place(x=335,y=180)
        rebill_entry.place(x=420, y=180)
      else:
        id_skulabel.place_forget()
        id_skuentry.place_forget()
        rebill_label.place_forget()
        rebill_entry.place_forget()
    rebill = BooleanVar()
    rebi = IntVar
    button51 = Checkbutton(expenselabelframe, text="Rebillable" ,variable=rebill, command=toggle,textvariable=rebi)
    
    id_sku1 = IntVar(expenselabelframe, value='-Expense-')
    id_skulabel=Label(expenselabelframe,text="id_sku:")
    id_skuentry = Entry(expenselabelframe,width=15,textvariable=id_sku1)

    rebill_amoun = IntVar(expenselabelframe, value='$.00')
    rebill_label=Label(expenselabelframe,text="Rebill amount:")
    rebill_entry = Entry(expenselabelframe,width=15,textvariable=rebill_amoun)
    

    #Button6 = Checkbutton(expenselabelframe, text = "Attach receipt image(optional,image will be stored to the database)")
    # Button6.place(x=40, y=200)


    exptext1=Label(expenselabelframe,text="Notes",pady=5,padx=10)
    exptext1.place(x=12,y=246)
    exptxt = scrolledtext.ScrolledText(expenselabelframe, undo=True,width=67,height=5)
    exptxt.place(x=22,y=280)

    expokButton = Button(window, text ="Ok",image=tick,width=70,compound = LEFT,command=reg_1)
    expokButton.place(x=280,y=415)

    window.mainloop()


def reg_1():# Storing values into db (user)
 
  expense_amount = expamountval.get()
  date = expdate.get_date()
  vendor = vn.get()
  catagory = cn.get()
  description = expdescriptionentry.get()
  staff_members = expstaffentry.get()
  taxable = checkvarStatus4.get()
  customer = cus.get()
  id_sku = id_sku1.get()
  notes = exptxt.get('1.0', 'end-1c')
  rebill_amount = rebill_amoun.get()
  rebillab = checkvarStatus4.get()
  sql='INSERT INTO Expenses (expense_amount,date,vendor,catagory,description,staff_members,taxable,customer,id_sku,notes,rebill_amount) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)' #adding values into db
  val=(expense_amount,date,vendor,catagory,description,staff_members,taxable,customer,id_sku,notes,rebill_amount)
  fbcursor.execute(sql,val)
  fbilldb.commit()
  messagebox.showinfo('Registration successfull','Registration successfull')
  
  
  
  
  



########################VIEW/EDIT EXPENSE#######################################################################



def edit_expense():
    global expamountentry,expdate,vn,cn,expdescriptionentry,expstaffentry,checkvarStatus4,cus,rebi,id_sku1,rebill_amoun,exptxt 
    # Grab record Number
    # selected = tree.focus()
    # # Grab record values
    # values = tree.item(selected, 'values')
    # # outpus to entry boxes
    # expamountentry.insert(0, values[16])
    # expdate.insert(0, values[4])
    # vn.insert(0, values[2])
    # cn.insert(0, values[3])
    # expdescriptionentry.insert(0, values[4])
    # expstaffentry.insert(0, values[5])
    # checkvarStatus4.insert(0, values[6])
    
    window1 = Toplevel()  
    
    window1.title("Edit Expense")
    p2 = PhotoImage(file = 'images/fbicon.png')
    window1.iconphoto(False, p1)
 
    window1.geometry("618x449+380+167")

    innerexpFrame = Frame(window1, relief=GROOVE)
    innerexpFrame.pack(side="top",fill=BOTH)

    expenselabelframe = LabelFrame(innerexpFrame,text="Expense Cost",width=580,height=400)
    expenselabelframe.pack(side="top",fill=BOTH,padx=10)


    expamountval = IntVar(expenselabelframe, value='$.00')
    expamount=Label(expenselabelframe,text="Expense amount:",pady=10,padx=10)
    expamount.place(x=12,y=0)
    expamountentry = Entry(expenselabelframe,width=15,textvariable=expamountval)
    expamountentry.place(x=130,y=10)

    lbl_date=Label(expenselabelframe,text=" Date :",fg='black')
    lbl_date.place(x=380,y=10)
    
    expdate=DateEntry(expenselabelframe)
    expdate.place(x=450,y=12)

    vendor1=Label(expenselabelframe,text="Vendor:",pady=5,padx=10)
    vendor1.place(x=20,y=40)
    vn = StringVar() 
    vendor = ttk.Combobox(expenselabelframe, width = 27, textvariable = vn ) 
      
    # Adding combobox drop down list 
    vendor['values'] = ('Default') 
      
    vendor.place(x=130,y=45) 
    vendor.current(0)

    categoryexp1=Label(expenselabelframe,text="Category:",pady=5,padx=10)
    categoryexp1.place(x=330,y=40)
    cn = StringVar() 
    categorydrop = ttk.Combobox(expenselabelframe, width = 22, textvariable = cn ) 
      
    # Adding combobox drop down list 
    categorydrop['values'] = ('Default') 
      
    categorydrop.place(x=400,y=45) 
    categorydrop.current(0)

    

    expdescription=Label(expenselabelframe,text="Description:",pady=10,padx=10)
    expdescription.place(x=12,y=70)
    expdescriptionentry = Entry(expenselabelframe,width=70)
    expdescriptionentry.place(x=130,y=81)

    expstafftval = StringVar(expenselabelframe, value='Administrator')
    expstaff=Label(expenselabelframe,text="Staff member:",pady=10,padx=10)
    expstaff.place(x=12,y=108)
    expstaffentry = Entry(expenselabelframe,width=30,textvariable=expstafftval)
    expstaffentry.place(x=130,y=118)

    checkvarStatus4=IntVar()
   
    Button4 = Checkbutton(expenselabelframe,variable = checkvarStatus4, 
                      text="Taxable Tax1 rate", 
                      onvalue =0 ,
                      offvalue = 1,
                      height=3,
                      width = 15)

    Button4.place(x=250,y=100)

    def toggle():
      if other.get():
        ent.place(x=45,y=180)
        button51.place(x=250, y=160)
      else:
        ent.place_forget()
        button51.place_forget()
    other = BooleanVar()
    button5 = Checkbutton(expenselabelframe, text="Assign to customer (optional)", variable=other, 
    command=toggle)
    button5.place(x=40, y=160)
    cus = StringVar()
    ent=ttk.Combobox(expenselabelframe,width=30,textvariable=cus)
    def toggle():
      if rebill.get():
        id_skulabel.place(x=375,y=160)
        id_skuentry.place(x=420,y=160)
        rebill_label.place(x=335,y=180)
        rebill_entry.place(x=420, y=180)
      else:
        id_skulabel.place_forget()
        id_skuentry.place_forget()
        rebill_label.place_forget()
        rebill_entry.place_forget()
    rebill = BooleanVar()
    rebi = IntVar
    button51 = Checkbutton(expenselabelframe, text="Rebillable" ,variable=rebill, command=toggle,textvariable=rebi)
    
    id_sku1 = IntVar(expenselabelframe, value='-Expense-')
    id_skulabel=Label(expenselabelframe,text="id_sku:")
    id_skuentry = Entry(expenselabelframe,width=15,textvariable=id_sku1)

    rebill_amoun = IntVar(expenselabelframe, value='$.00')
    rebill_label=Label(expenselabelframe,text="Rebill amount:")
    rebill_entry = Entry(expenselabelframe,width=15,textvariable=rebill_amoun)
    
    # Button6 = Checkbutton(expenselabelframe, text = "Attach receipt image(optional,image will be stored to the database)")
    # Button6.place(x=40, y=200)


    exptext1=Label(expenselabelframe,text="Notes",pady=5,padx=10)
    exptext1.place(x=12,y=246)
    exptxt = scrolledtext.ScrolledText(expenselabelframe, undo=True,width=67,height=50)
    exptxt.place(x=22,y=280)

    expokButton = Button(window1, text ="Ok",image=tick,width=70,compound = LEFT)
    expokButton.place(x=280,y=415)

    
    

    window1.mainloop()


def edit_expense():
  itemid = tree.item(tree.focus())["values"][0]
  print(itemid)
  sql = 'SELECT * FROM Expenses WHERE expensesid=%s'
  val = (itemid,)
  fbcursor.execute(sql, val)
  fbilldb.commit()
  #selrow = tree.selection()[0]
  tree.delete(tree.selection()[0])
  
  
  


######################## DELETE EXPENSE #######################################################################


def delete_expense():
  delmess = messagebox.askyesno("Delete Expense", "Are you sure to delete this Expense?")
  if delmess == True:
    itemid = tree.item(tree.focus())["values"][0]
    print(itemid)
    sql = 'DELETE FROM Expenses WHERE expensesid=%s'
    val = (itemid,)
    fbcursor.execute(sql, val)
    fbilldb.commit()
    #selrow = tree.selection()[0]
    tree.delete(tree.selection()[0])
  else:
    pass


######################## SEARCH EXPENSE ######################################################################
    

def search_expense():
    top = Toplevel()  
    
    top.title("Find Text")
    
    
    top.geometry("520x200+390+250")
    findwhat1=Label(top,text="Find What:",pady=5,padx=10)
    findwhat1.place(x=5,y=20)
    n = StringVar() 
    findwhat = ttk.Combobox(top, width = 50, textvariable = n ) 
      
    # Adding combobox drop down list 
    
    findwhat.place(x=80,y=25) 
    

    findButton = Button(top, text ="Find next",width=10)
    findButton.place(x=420,y=20)

    findin1=Label(top,text="Find in:",pady=5,padx=10)
    findin1.place(x=5,y=47)
    n = StringVar() 
    findIN = ttk.Combobox(top, width = 37, textvariable = n ) 
      
    # Adding combobox drop down list 
    findIN['values'] = ('Client',  
                              ' Date', 
                              ' Category', 
                              ' Vendor', 
                              ' Staff Member', 
                              ' Description', 
                              ' Rebillable',
                              'Invoiced',
                              'Image',
                              'Rebill Amount',
                              'Amount',
                        
                              ' <<All>>') 
      
    findIN.place(x=80,y=54) 
    findIN.current(0)

    closeButton = Button(top, text ="Close",width=10)
    closeButton.place(x=420,y=50)

    match1=Label(top,text="Match:",pady=5,padx=10)
    match1.place(x=5,y=74)
    n = StringVar() 
    match = ttk.Combobox(top, width = 27, textvariable = n ) 
      
    # Adding combobox drop down list 
    match['values'] = ('From Any part of the field',' Whole Field',  
                              ' From the beginning of the field')
      
    match.place(x=80,y=83) 
    match.current(0)

    search1=Label(top,text="Search:",pady=5,padx=10)
    search1.place(x=5,y=102)
    n = StringVar() 
    search = ttk.Combobox(top, width = 27, textvariable = n ) 
      
    # Adding combobox drop down list 
    search['values'] = ('All', 'up', 
                              ' Down')
      
    search.place(x=80,y=112) 
    search.current(0)


    checkvarStatus4=IntVar()
   
    Button4 = Checkbutton(top,variable = checkvarStatus4, 
                      text="Match Case", 
                      onvalue =0 ,
                      offvalue = 1,
                      height=3,
                      width = 15)

    Button4.place(x=60,y=141)

    checkvarStatus5=IntVar()
   
    Button5 = Checkbutton(top,variable = checkvarStatus5, 
                      text="Match Format", 
                      onvalue =0 ,
                      offvalue = 1,
                      height=3,
                      width = 15)

    Button5.place(x=270,y=141)





    top.mainloop()




######################## FRONT PAGE OF EXPENSE MODULE #######################################################################



    
expframe = Frame(tab6,relief=GROOVE)
expframe.pack(side="top", fill=BOTH)

expmidFrame=Frame(expframe, height=60)
expmidFrame.pack(side="top", fill=X)

e = Canvas(expmidFrame, width=1, height=65, bg="#b3b3b3", bd=0)
e.pack(side="left", padx=(5, 2))
e = Canvas(expmidFrame, width=1, height=65, bg="#b3b3b3", bd=0)
e.pack(side="left", padx=(0, 5))

expenseIcon = ImageTk.PhotoImage(Image.open("images/plus.png"))
expenseLabel = Button(expmidFrame,compound="top", text="Create new\nExpense",relief=RAISED,command=add_expense, image=expenseIcon,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,)
expenseLabel.pack(side="left", pady=3, ipadx=4)

expeditIcon = ImageTk.PhotoImage(Image.open("images/edit.png"))
expeditLabel = Button(expmidFrame,compound="top", text="Edit/View\nExpense",relief=RAISED, image=expeditIcon,command=edit_expense,bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
expeditLabel.pack(side="left")

expdeleteIcon = ImageTk.PhotoImage(Image.open("images/delete.png"))
expdeleteLabel = Button(expmidFrame,compound="top", text="Delete\nSelected", relief=RAISED, command=delete_expense,image=expdeleteIcon,bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
expdeleteLabel.pack(side="left")

e = Canvas(expmidFrame, width=1, height=65, bg="#b3b3b3", bd=0)
e.pack(side="left", padx=5)

expsearchIcon = ImageTk.PhotoImage(Image.open("images/research.png"))
expsearchLabel = Button(expmidFrame,compound="top", text="Search in\nExpenses",relief=RAISED,command=search_expense, image=expsearchIcon,bg="#f8f8f2", fg="black", height=55, bd=1, width=55, )
expsearchLabel.pack(side="left")


lbframe = LabelFrame(expmidFrame, height=60, width=200)
lbframe.pack(side="left", padx=10, pady=0)

lbl_expdt=Label(lbframe,text="Expense date from:",fg='black')
lbl_expdt.grid(row=0, column=0, pady=5, padx=(5, 0))

lbl_expdtt=Label(lbframe,text="Expense date to:" , fg='black')
lbl_expdtt.grid(row=1, column=0, pady=5, padx=(5, 0))

   
expdt=DateEntry(lbframe)
expdt.grid(row=0, column=1)
   
expdtt=DateEntry(lbframe)
expdtt.grid(row=1, column=1)
   
checkvar1 = IntVar()
chkbtn1 = Checkbutton(lbframe, text = "Apply filter", variable = checkvar1, onvalue = 1, offvalue = 0, height = 2, width = 8)
chkbtn1.grid(row=0, column=2, rowspan=2, padx=(5,5))


e = Canvas(midFrame, width=1, height=55, bg="#b3b3b3", bd=0)
e.pack(side="left", padx=5)

exprefreshIcon = ImageTk.PhotoImage(Image.open("images/refresh.png"))
exprefreshLabel = Button(expmidFrame,compound="top", text="Refresh\nExpense List",relief=RAISED, image=exprefreshIcon,bg="#f8f8f2", fg="black", height=55, bd=1, width=63)
exprefreshLabel.pack(side="left")

expoilabel = Label(expframe, text="Expenses (All)", font=("arial", 14))
expoilabel.place(x=8,y=66)
drop = ttk.Combobox(expframe)
drop.pack(side="right", padx=(0,10))
expcatlabel = Label(expframe, text="Category filter")
expcatlabel.pack(side="right", padx=(0,10)) 

#table 
s = ttk.Style()
s.configure('Treeview.Heading', background='white', foreground='dark blue', State='DISABLE')


tree=ttk.Treeview(tab6,selectmode='browse')
tree.place(x=10,y=92,height=580)

expverticalbar=ttk.Scrollbar(tab6,orient="vertical",command=tree.yview,)
expverticalbar.place(x=1336,y=93,height=570,)
expverticalbar.place(x=1336,y=93,height=570)
tree["columns"]=("1","2","3","4","5","6","7","8","9","10","11","12")
tree["show"]='headings'
tree.column("1",width=5,anchor='c')
tree.column("2",width=120,anchor='c')
tree.column("3",width=100,anchor='c')
tree.column("4",width=120,anchor='c')
tree.column("5",width=120,anchor='c')
tree.column("6",width=120,anchor='c')
tree.column("7",width=220,anchor='c')
tree.column("8",width=120,anchor='c')
tree.column("9",width=100,anchor='c')
tree.column("10",width=100,anchor='c')
tree.column("11",width=100,anchor='c')
tree.column("12",width=100,anchor='c')
tree.heading("2",text="Client")
tree.heading("3",text="Date")
tree.heading("4",text="Category")
tree.heading("5",text="Vendor")
tree.heading("6",text="Staff member")
tree.heading("7",text="Description")
tree.heading("8",text="Rebillable")
tree.heading("9",text="Invoiced")
tree.heading("10",text="Image")
tree.heading("11",text="Rebill Amount")
tree.heading("12",text="Amount")

fbcursor.execute('SELECT * FROM Expenses;')
j = 0
for i in fbcursor:
  tree.insert(parent='', index='end', iid=i, text='hello', values=(i[0], i[10], i[4], i[6], i[5], i[8], i[7], i[13], i[14], i[11],i[16],i[3]))
  j += 1

# def generate_recurring():  
    
#     fbcursor.execute("SELECT Recurring.recurringid, invoice.invoive_number, Recurring.next_invoice, Recurring.recurring_period, Recurring.stop_recurring, Customer.businessname, invoice.invoicetot FROM Recurring  JOIN invoice ON Recurring.invoiceid = invoice.invoiceid JOIN Customer ON Recurring.customerid = Customer.customerid")
  
#     rows = fbcursor.fetchall()    

#     for row in rows:

#         print(row) 

#         tree.insert("", ttk.END, values=row)        

#     fbilldb.close()

# def treeview():# Storing values into db (user)
#   global rebillabe,invoiced,images 
#   rebillabe = StringVar
#   invoiced = StringVar
#   images = StringVar
#   expense_amount = expamountval.get()
#   date = expdate.get_date()
#   vendor = vn.get()
#   catagory = cn.get()
#   description = expdescriptionentry.get()
#   staff_members = expstaffentry.get()
#   taxable = checkvarStatus4.get()
#   customer = cus.get()
#   id_sku = id_sku1.get()
#   notes = exptxt.get('1.0', 'end-1c')
#   rebill_amount = rebill_amoun.get()
#   rebillab = rebillabe.get()
#   invoice = invoiced.get()
#   image = images.get()

#   sql='Select * from Expenses (customer,date,catagory,vendor,staff_members,description,rebillable,invoiced,image,rebill_amount,expense_amount) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)' #adding values into db
#   val=(customer,date,catagory,vendor,staff_members,description,rebillab,invoice,image,rebill_amount,expense_amount)
#   rows = fbcursor.execute(sql,val)
#   # for i in row:
#   #   tree.insert(parent='', index='end', iid=countp, text='hello', values=('customer,date,catagory,vendor,staff_members,description,rebillab,invoice,image,rebill_amount,expense_amount', i[0], i[2]))
#   #   countp += 1
#   #   tree.place(height=580, width=1200, x=10, y=101)
#   #   tree.selection()

#   for row in rows:
#     print(row) 
#     tree.insert("", ttk.END, values=row)        
#     fbilldb.close()






root.mainloop()








