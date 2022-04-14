from tkinter import*
from PIL import ImageTk, Image     #------ pip install pillow ----->
from tkinter import messagebox,ttk
import pymysql
import time
import os
import tempfile

class BillingClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1520x820+0+5")
        self.root.title("Inventory Management System | Billing")
        self.root.resizable(False,False)
        self.root.focus_force()

        #---------- All Variables ---------->
        self.CartList = []
        self.CheckPrint = 0

        self.VarSearch = StringVar()
        self.VarName = StringVar()
        self.VarContact = StringVar()

        self.VarPId = StringVar()
        self.VarPName = StringVar()
        self.VarPrice = StringVar()
        self.VarQuantity = StringVar()
        self.VarStock = StringVar()

        self.VarCalInput = StringVar()

        #---------- Title Label ---------->
        self.IconTitle = PhotoImage(file="Images/logo1.png")
        Title=Label(self.root, text="Inventory Management System", image=self.IconTitle, compound=LEFT, font=("Cambria", 35, "bold"), bg="#010c48", fg="white", padx=20, anchor="w").place(x=0, y=0, relwidth=1, height=70)

        #---------- Logout Button ---------->
        btnLogout = Button(self.root, command=self.Logout, text="Logout", font=("Cambria", 20, "bold"), bg="yellow", cursor="hand2").place(x=1360, y=10, height=50, width=150)

        #---------- Clock ---------->
        self.ClockLabel=Label(self.root, text="Wel-Come to Inventory Management System\t\t Date : DD - MM - YYYY\t\t Time : HH : MM : SS", font=("Cambria", 15), bg="#4d636d", fg="white")
        self.ClockLabel.place(x=0, y=70, relwidth=1, height=30)

        #---------- Footer ---------->
        FooterLabel=Label(self.root, text="IMS-Inventory Management Sysetm | Developed by Akshay Yadav\nFor Any Technical Issue Contact : 96XXXXXX48", font=("Cambria", 12), bg="#4d636d", fg="white", activebackground="#4d636d", activeforeground="white")
        FooterLabel.pack(side=BOTTOM, fill=X)

        #---------- Product Frame ---------->
        ProductFrame1 = Frame(self.root, bd=2, relief=RIDGE)
        ProductFrame1.place(x=2, y=105, width=440, height=670)

        ProductTitle=Label(ProductFrame1, text="All Products", font=("Cambria", 20, "bold"), bg="#262626", fg="orange").pack(side=TOP, fill=X)

        #---------- Product Search Frame ---------->
        ProductFrame2 = Frame(ProductFrame1, bd=2, relief=RIDGE)
        ProductFrame2.place(x=0, y=40, width=435, height=90)      

        LabelSearch=Label(ProductFrame2, text="Search Product | By Name :-", font=("Cambria", 15, "bold"), fg="green").place(x=2, y=8)
        LabelProductName=Label(ProductFrame2, text="Product Name :-", font=("Cambria", 15, "bold"), fg="green").place(x=2, y=50)
        txtSearch=Entry(ProductFrame2, textvariable=self.VarSearch, font=("Cambria", 15, "bold"), bg="lightyellow").place(x=155, y=53, width=150, height=25)
        btnSearch = Button(ProductFrame2, command=self.SearchDataDef, text="Search", font=("Cambria",15,"bold"), bg="#4caf50", fg="white", bd=2, relief=RIDGE, cursor="hand2").place(x=308, y=52, height=25, width=120)
        btnShowAll = Button(ProductFrame2, command=self.ShowDataDef, text="Show All", font=("Cambria",15,"bold"), bg="#083531", fg="white", bd=2, relief=RIDGE, cursor="hand2").place(x=277, y=10, height=30, width=150)
 
        #---------- Product Details Frame ---------->
        ProductFrame3 = Frame(ProductFrame1, bd=3, relief=RIDGE)
        ProductFrame3.place(x=0, y=130, width=436, height=508)

        ScrollY = Scrollbar(ProductFrame3, orient=VERTICAL)
        ScrollY.pack(side=RIGHT, fill=Y)

        ScrollX = Scrollbar(ProductFrame3, orient=HORIZONTAL)
        ScrollX.pack(side=BOTTOM, fill=X)

        self.ProductTable = ttk.Treeview(ProductFrame3, columns=("PId","Name", "Price", "Quantity", "Status"),yscrollcommand=ScrollY.set, xscrollcommand=ScrollX.set)
        ScrollY.config(command=self.ProductTable.yview)
        ScrollX.config(command=self.ProductTable.xview)

        self.ProductTable.heading("PId", text="PID")
        self.ProductTable.heading("Name", text="Name")
        self.ProductTable.heading("Price", text="Price")
        self.ProductTable.heading("Quantity", text="QTY")
        self.ProductTable.heading("Status", text="Status")

        self.ProductTable["show"] = "headings"

        self.ProductTable.column("PId", width=30)
        self.ProductTable.column("Name", width=120)
        self.ProductTable.column("Price", width=60)
        self.ProductTable.column("Quantity", width=30)
        self.ProductTable.column("Status", width=50)
        self.ProductTable.pack(fill=BOTH, expand=1)
        self.ProductTable.bind("<ButtonRelease-1>", self.GetDataDef)
        
        LabelNote=Label(ProductFrame1, anchor="w", text="Note : Enter 0 Quantity to Remove the Product From Cart", font=("Cambria", 12, "bold"), fg="red").pack(side=BOTTOM, fill=X)

        #---------- Customer Details Frame ---------->
        CustomerFrame = Frame(self.root, bd=2, relief=RIDGE)
        CustomerFrame.place(x=445, y=105, width=540, height=80)

        CustomerTitle=Label(CustomerFrame, text="Customer Details", font=("Cambria", 15, "bold"), bg="lightgray").pack(side=TOP, fill=X)
        LabelName=Label(CustomerFrame, text="Name :-", font=("Cambria", 15, "bold")).place(x=2, y=37)
        txtName=Entry(CustomerFrame, textvariable=self.VarName, font=("Cambria", 15, "bold"), bg="lightyellow").place(x=80, y=40, width=180, height=25)

        LabelContact=Label(CustomerFrame, text="Contact No :-", font=("Cambria", 15, "bold")).place(x=260, y=37)
        txtContact=Entry(CustomerFrame, textvariable=self.VarContact, font=("Cambria", 15, "bold"), bg="lightyellow").place(x=380, y=40, width=150, height=25)
        
        #---------- Calculator Card Frame ---------->
        CalCartFrame = Frame(self.root, bd=2, relief=RIDGE)
        CalCartFrame.place(x=445, y=190, width=540, height=460)

        #---------- Images 1 ---------->
        self.CatImage1 = Image.open("Images/cat2.jpg")
        self.CatImage1 = self.CatImage1.resize((257,120), Image.ANTIALIAS)
        self.CatImage1 = ImageTk.PhotoImage(self.CatImage1)

        self.LabelCatImage1 = Label(CalCartFrame, image=self.CatImage1, bd=2, relief=RAISED)
        self.LabelCatImage1.place(x=1, y=1)

        #---------- Calculator Frame ---------->
        CalFrame = Frame(CalCartFrame, bd=6, relief=RIDGE)
        CalFrame.place(x=1, y=125, width=260, height=330)

        txtCalInput=Entry(CalFrame, justify=RIGHT, textvariable=self.VarCalInput, font=("Cambria", 16, "bold"), bg="lightyellow", width=20, bd=4, relief=GROOVE, state="readonly")
        txtCalInput.grid(row=0, columnspan=4)
        btn7 = Button(CalFrame, command=lambda:self.GetInput(7), text="7",font=("Cambria", 14, "bold"), bd=4, width=4, pady=15, cursor="hand2").grid(row=1, column=0)
        btn8 = Button(CalFrame, command=lambda:self.GetInput(8), text="8",font=("Cambria", 14, "bold"), bd=4, width=4, pady=15, cursor="hand2").grid(row=1, column=1)
        btn9 = Button(CalFrame, command=lambda:self.GetInput(9), text="9",font=("Cambria", 14, "bold"), bd=4, width=4, pady=15, cursor="hand2").grid(row=1, column=2)
        btnSum = Button(CalFrame, command=lambda:self.GetInput("+"), text="+",font=("Cambria", 14, "bold"), bd=4, width=5, pady=15, cursor="hand2").grid(row=1, column=3)

        btn4 = Button(CalFrame, command=lambda:self.GetInput(4), text="4",font=("Cambria", 14, "bold"), bd=4, width=4, pady=15, cursor="hand2").grid(row=2, column=0)
        btn5 = Button(CalFrame, command=lambda:self.GetInput(5), text="5",font=("Cambria", 14, "bold"), bd=4, width=4, pady=15, cursor="hand2").grid(row=2, column=1)
        btn6 = Button(CalFrame, command=lambda:self.GetInput(6), text="6",font=("Cambria", 14, "bold"), bd=4, width=4, pady=15, cursor="hand2").grid(row=2, column=2)
        btnSub = Button(CalFrame, command=lambda:self.GetInput("-"), text="-",font=("Cambria", 14, "bold"), bd=4, width=5, pady=15, cursor="hand2").grid(row=2, column=3)

        btn1 = Button(CalFrame, command=lambda:self.GetInput(1), text="1",font=("Cambria", 14, "bold"), bd=4, width=4, pady=15, cursor="hand2").grid(row=3, column=0)
        btn2 = Button(CalFrame, command=lambda:self.GetInput(2), text="2",font=("Cambria", 14, "bold"), bd=4, width=4, pady=15, cursor="hand2").grid(row=3, column=1)
        btn2 = Button(CalFrame, command=lambda:self.GetInput(3), text="3",font=("Cambria", 14, "bold"), bd=4, width=4, pady=15, cursor="hand2").grid(row=3, column=2)
        btnMul = Button(CalFrame, command=lambda:self.GetInput("*"), text="*",font=("Cambria", 14, "bold"), bd=4, width=5, pady=15, cursor="hand2").grid(row=3, column=3)

        btn0 = Button(CalFrame, command=lambda:self.GetInput(0), text="0",font=("Cambria", 14, "bold"), bd=4, width=4, pady=15, cursor="hand2").grid(row=4, column=0)
        btnC = Button(CalFrame, command=self.ClearCal, text="C",font=("Cambria", 14, "bold"), bd=4, width=4, pady=15, cursor="hand2").grid(row=4, column=1)
        btnEq = Button(CalFrame, command=self.PerformCal, text="=",font=("Cambria", 14, "bold"), bd=4, width=4, pady=15, cursor="hand2").grid(row=4, column=2)
        btnDiv = Button(CalFrame, command=lambda:self.GetInput("/"), text="/",font=("Cambria", 14, "bold"), bd=4, width=5, pady=15, cursor="hand2").grid(row=4, column=3)

        #---------- Card Frame ---------->
        CartFrame = Frame(CalCartFrame, bd=3, relief=RIDGE)
        CartFrame.place(x=262, y=2, width=273, height=452)

        self.CartTitle=Label(CartFrame, text="Cart       Total Product : [ 0 ]", font=("Cambria", 15, "bold"), bg="lightgray")
        self.CartTitle.pack(side=TOP, fill=X)

        ScrollY = Scrollbar(CartFrame, orient=VERTICAL)
        ScrollY.pack(side=RIGHT, fill=Y)

        ScrollX = Scrollbar(CartFrame, orient=HORIZONTAL)
        ScrollX.pack(side=BOTTOM, fill=X)

        self.CartTable = ttk.Treeview(CartFrame, columns=("PId","Name", "Price", "QTY"),yscrollcommand=ScrollY.set, xscrollcommand=ScrollX.set)
        ScrollY.config(command=self.CartTable.yview)
        ScrollX.config(command=self.CartTable.xview)

        self.CartTable.heading("PId", text="PID")
        self.CartTable.heading("Name", text="Name")
        self.CartTable.heading("Price", text="Price")
        self.CartTable.heading("QTY", text="QTY")

        self.CartTable["show"] = "headings"

        self.CartTable.column("PId", width=30)
        self.CartTable.column("Name", width=100)
        self.CartTable.column("Price", width=70)
        self.CartTable.column("QTY", width=40)
        self.CartTable.pack(fill=BOTH, expand=1)
        self.CartTable.bind("<ButtonRelease-1>", self.GetDataDef1)
        
        #---------- Add Card Widgets Frame ---------->
        AddCardWidgetsFrame = Frame(self.root, bd=2, relief=RIDGE)
        AddCardWidgetsFrame.place(x=445, y=652, width=540, height=122)
        
        LabelPName=Label(AddCardWidgetsFrame, text="Product Name :-", font=("Cambria", 15, "bold")).place(x=5, y=5)
        txtPName=Entry(AddCardWidgetsFrame, textvariable=self.VarPName, font=("Cambria", 15, "bold"), bg="lightyellow", state="readonly").place(x=5, y=40, width=180, height=25)

        LabelPPrice=Label(AddCardWidgetsFrame, text="Price Per QTY :-", font=("Cambria", 15, "bold")).place(x=190, y=5)
        txtPPrice=Entry(AddCardWidgetsFrame, textvariable=self.VarPrice, font=("Cambria", 15, "bold"), bg="lightyellow", state="readonly").place(x=190, y=40, width=160, height=25)

        LabelPQuantity=Label(AddCardWidgetsFrame, text="Quantity :-", font=("Cambria", 15, "bold")).place(x=355, y=5)
        txtPQuantity=Entry(AddCardWidgetsFrame, textvariable=self.VarQuantity, font=("Cambria", 15, "bold"), bg="lightyellow").place(x=355, y=40, width=178, height=25)

        self.LabelInStock=Label(AddCardWidgetsFrame, text="In Stock", font=("Cambria", 15, "bold"))
        self.LabelInStock.place(x=5, y=80)

        btnClearCart = Button(AddCardWidgetsFrame,command=self.ClearCartDef, text="Clear", font=("Cambria", 15, "bold"), bg="lightgray", cursor="hand2").place(x=180, y=80, width=150, height=30)
        btnAddCart = Button(AddCardWidgetsFrame, command=self.AddUpdateCartDef, text="Add | Update Card", font=("Cambria", 15, "bold"), bg="orange", cursor="hand2").place(x=340, y=80, width=190, height=30)

        #---------- Billing Area ---------->
        BillAreaFrame = Frame(self.root, bd=2, relief=RIDGE)
        BillAreaFrame.place(x=990, y=105, width=525, height=520)
        
        BillTitle=Label(BillAreaFrame, text="Customer Bill Area", font=("Cambria", 20, "bold"), bg="#f44336", fg="white").pack(side=TOP, fill=X)

        ScrollY0 = Scrollbar(BillAreaFrame, orient=VERTICAL)
        ScrollY0.pack(side=RIGHT, fill=Y)
        
        self.txtBillArea = Text(BillAreaFrame, font=("Cambria", 15, "bold"), yscrollcommand=ScrollY0.set)
        self.txtBillArea.pack(fill=BOTH, expand=1)
        ScrollY0.config(command=self.txtBillArea.yview)

        #---------- Billing Button Frame ---------->
        BillMenuFrame = Frame(self.root, bd=2, relief=RIDGE)
        BillMenuFrame.place(x=990, y=628, width=525, height=146)

        self.LabelAmount=Label(BillMenuFrame, text="Bill Amount\n[ 0 ]", font=("Cambria", 15, "bold"), bg="#3f51b5", fg="white")
        self.LabelAmount.place(x=2, y=2, width=165, height=75)
        
        self.LabelDiscount=Label(BillMenuFrame, text="Discount\n[ 5% ]", font=("Cambria", 15, "bold"), bg="#8bc34a", fg="white")
        self.LabelDiscount.place(x=171, y=2, width=165, height=75)
        
        self.LabelNetPay=Label(BillMenuFrame, text="Net Pay\n[ 0 ]", font=("Cambria", 15, "bold"), bg="#607d8b", fg="white")
        self.LabelNetPay.place(x=340, y=2, width=180, height=75)

        btnPrint=Button(BillMenuFrame, command=self.PrintBill, cursor="hand2", text="Print Bill", font=("Cambria", 15, "bold"), bg="lightgreen", fg="black")
        btnPrint.place(x=2, y=80, width=165, height=60)
        
        btnClear=Button(BillMenuFrame, command=self.ClearAllDef, cursor="hand2", text="Clear All", font=("Cambria", 15, "bold"), bg="gray", fg="white")
        btnClear.place(x=171, y=80, width=165, height=60)
        
        btnGenerate=Button(BillMenuFrame, command=self.GenerateBill, cursor="hand2", text="Generate Bill\nSave Bill", font=("Cambria", 15, "bold"), bg="#009688", fg="white")
        btnGenerate.place(x=340, y=80, width=180, height=60)

        self.ShowDataDef()
        self.UpdateClockDate()

    #---------- All Function ---------->
    def GetInput(self, Num):
        Xnum = self.VarCalInput.get()+str(Num)
        self.VarCalInput.set(Xnum)
    
    #---------- Clear Cal ---------->
    def ClearCal(self):
        self.VarCalInput.set("")

    #---------- Perform Cal ---------->
    def PerformCal(self):
        result = self.VarCalInput.get()
        self.VarCalInput.set(eval(result))

    #---------- Product Show Data ---------->
    def ShowDataDef(self):
        try:
            con = pymysql.connect(host="localhost", user="root", password="", db="IMSDatabase")
            cur = con.cursor()
            cur.execute("select PId, Name, Price, Quantity, Status from Product where Status='Active'")
            Row1=cur.fetchall()
            self.ProductTable.delete(*self.ProductTable.get_children())
            for row in Row1:
                self.ProductTable.insert("", END, values=row)
            con.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error Due To {str(ex)}", parent=self.root)

    #---------- Product Search Data ---------->
    def SearchDataDef(self):
        try:
            con = pymysql.connect(host="localhost", user="root", password="", db="IMSDatabase")
            cur = con.cursor()
            if self.VarSearch.get()=="":
                messagebox.showerror("Error", "Search Input Should be Required", parent=self.root)
            else:
                cur.execute("select PId, Name, Price, Quantity, Status from Product where Name LIKE '%"+self.VarSearch.get()+"%' and Status='Active'     " " ")
                Row1=cur.fetchall()
                if len(Row1)!=0:
                    self.ProductTable.delete(*self.ProductTable.get_children())
                    for row in Row1:
                        self.ProductTable.insert("", END, values=row)
                else:
                    messagebox.showerror("Error", "No Record Found", parent=self.root)
                    con.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error Due To {str(ex)}", parent=self.root)

    #---------- Product Get Data ---------->
    def GetDataDef(self, ev):
        f = self.ProductTable.focus()
        content = (self.ProductTable.item(f))
        row = content["values"]
        self.VarPId.set(row[0])
        self.VarPName.set(row[1])
        self.VarPrice.set(row[2])
        self.LabelInStock.config(text=f"In Stock    [  {str(row[3])}  ]")
        self.VarStock.set(row[3])
        self.VarQuantity.set("1")

    def GetDataDef1(self, ev):
        f = self.CartTable.focus()
        content = (self.CartTable.item(f))
        row = content["values"]
        self.VarPId.set(row[0])
        self.VarPName.set(row[1])
        self.VarPrice.set(row[2])
        self.VarQuantity.set(row[3])
        self.LabelInStock.config(text=f"In Stock    [  {str(row[4])}  ]")
        self.VarStock.set(row[4])

    #---------- Product Get Data ---------->
    def AddUpdateCartDef(self):
        if self.VarPId.get()=="":
            messagebox.showerror("Error", "Please Select Product From The List", parent=self.root)
        elif self.VarQuantity.get()=="": 
            messagebox.showerror("Error", "Quantity Should Be Required", parent=self.root)
        elif int(self.VarQuantity.get())>int(self.VarStock.get()):
            messagebox.showerror("Error", "Invalid Quantity", parent=self.root)
        else: 
            #CalPrice = float(int(self.VarQuantity.get())*float(self.VarPrice.get()))
            CalPrice = self.VarPrice.get()
            CartData = [self.VarPId.get(), self.VarPName.get(), CalPrice, self.VarQuantity.get(), self.VarStock.get()]

            #---------- Update Cart ---------->
            Present = "No"
            Index_ = 0
            for row in self.CartList:
                if self.VarPId.get()==row[0]:
                    Present = "Yes"
                    break
                Index_ += 1
            
            if Present=="Yes":
                OP = messagebox.askyesno("Confirm", "Product Already Present\nDo You Want To Update | Remove From The Cart List", parent=self.root)
                if OP==True:
                    if self.VarQuantity.get()=="0":
                        self.CartList.pop(Index_)
                    else:
                        #self.CartList[Index_][2]=CalPrice   #Price
                        self.CartList[Index_][3]=self.VarQuantity.get() #Quantity
            else:
                self.CartList.append(CartData)
            self.CartShowDef()
            self.BillUpdates()

    def CartShowDef(self):
        try:
            self.CartTable.delete(*self.CartTable.get_children())
            for row in self.CartList:
                self.CartTable.insert("", END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error Due To {str(ex)}", parent=self.root)

    def BillUpdates(self):
        self.BillAmount = 0
        self.NetPay = 0
        self.Discount = 0
        for row in self.CartList:
            self.BillAmount = self.BillAmount+(float(row[2])*int(row[3]))   
        self.Discount = (self.BillAmount*5)/100
        self.NetPay = self.BillAmount-self.Discount
        self.LabelAmount.config(text=f"Bill Amount\n[ Rs. {str(self.BillAmount)} ]")
        self.LabelNetPay.config(text=f"Net Pay Amount\n[ Rs. {str(self.NetPay)} ]")
        self.CartTitle.config(text=f"Cart       Total Product : [ {str(len(self.CartList))} ]")

    #---------- Generate Bill ---------->
    def GenerateBill(self):
        if self.VarName.get()=="" or self.VarContact.get()=="":
            messagebox.showerror("Error", f"Customer Details Are Required", parent=self.root)
        elif len(self.CartList)==0:
            messagebox.showerror("Error", f"Please Add Product to The Cart", parent=self.root)
        else:
            #---------- Top Bill ---------->
            self.TopBill()
            #---------- Middle Bill ---------->
            self.MiddleBill()
            #---------- Bottom Bill ---------->
            self.BottomBill()

            FP = open(f"Bill/{str(self.Invoice)}.txt", "w")
            FP.write(self.txtBillArea.get("1.0", END))
            FP.close()
            messagebox.showinfo("Saved", "Bill Has Been Generated | Saved Successfully in Backend", parent=self.root)
            self.CheckPrint = 1

    #---------- Top Bill ---------->
    def TopBill(self):
        self.Invoice = int(time.strftime("%H%M%S"))+int(time.strftime("%d%m%Y"))
        TopBillTemp = f"""{str("~"*41)}
\tIMS-Inventory Management System
\tPhone No. 96XXXXXX48\t,\tPune-411041
{str("~"*41)}
 Customer Name :\t\t{self.VarName.get()}
 Contact No. :\t\t{self.VarContact.get()}
 Bill No. :\t{str(self.Invoice)}\t\tDate :- {str(time.strftime("%d-%m-%Y"))}
{str("~"*41)}
 Product Name\t\tQuantity\tPrice
{str("~"*41)}      
        """
        self.txtBillArea.delete("1.0",END)
        self.txtBillArea.insert("1.0",TopBillTemp)

    #---------- Middle Bill ---------->
    def MiddleBill(self):
        con = pymysql.connect(host="localhost", user="root", password="", db="IMSDatabase")
        cur = con.cursor()
        try:
            for row in self.CartList:
                PId = row[0]
                Name1 = row[1]
                Quantity = int(row[4])-int(row[3])
                if int(row[3])==int(row[4]):
                    Status = "InActive"

                if int(row[3])!=int(row[4]):
                    Status = "Active"

                Price = float(row[2])*int(row[3])
                Price = str(Price)
                self.txtBillArea.insert(END,"\n"+Name1+"\t\t"+row[3]+"\tRs. "+Price+"\n")
                #---------- Update Quantity in Product Table ---------->
                cur.execute("update Product set Quantity=%s, Status=%s where PId=%s", 
                (
                    Quantity,
                    Status,
                    PId
                ))
                con.commit()
            con.close()
            self.ShowDataDef()
        except Exception as ex:
            messagebox.showerror("Error", f"Error Due To {str(ex)}", parent=self.root)

    #---------- Bottom Bill ---------->
    def BottomBill(self):
        BottomBillTemp = f"""
{str("~"*41)}
 Bill Amount :\t\tRs. {self.BillAmount}
 Discount :\t\tRs. {self.Discount}
 Net Pay Amount :\t\tRs. {self.NetPay}
{str("~"*41)} 
        """
        self.txtBillArea.insert(END,BottomBillTemp)

    #---------- Clear Cart ---------->
    def ClearCartDef(self):
        self.VarPId.set("")
        self.VarPName.set("")
        self.VarPrice.set("")
        self.VarQuantity.set("")
        self.LabelInStock.config(text=f"In Stock")
        self.VarStock.set("")
    
    def ClearAllDef(self):
        del self.CartList[:]
        self.VarName.set("")
        self.VarContact.set("")
        self.txtBillArea.delete("1.0", END)
        self.CartTitle.config(text=f"Cart       Total Product : [ 0 ]")
        self.VarSearch.set("")
        self.ClearCartDef()
        self.ShowDataDef()
        self.CartShowDef()

    def UpdateClockDate(self):
        Time1 = time.strftime("%I : %M : %S")
        Date1 = time.strftime("%d - %m - %Y")
        self.ClockLabel.config(text=f"Wel-Come to Inventory Management System\t\t Date : {str(Date1)} \t\t Time : {str(Time1)}")
        self.ClockLabel.after(200, self.UpdateClockDate)

    def PrintBill(self):
        if self.CheckPrint==1:
            messagebox.showinfo("Print", "Please Wait While Printing The Bill", parent=self.root)
            NewFile = tempfile.mktemp(".txt")
            open(NewFile, "w").write(self.txtBillArea.get("1.0",END))
            os.startfile(NewFile, "Print")
        else:
            messagebox.showerror("Print", "Please Generate Bill, To Print The Receipt", parent=self.root)

    def Logout(self):
        OP = messagebox.askyesno("Confirm", "Are You Sure You Want to Logout.", parent=self.root)
        if OP==True:
            messagebox.showinfo("Error", "You Have Been Logged Out", parent=self.root)
            self.root.destroy()
            os.system("python Login.py")

if __name__=="__main__":
    root=Tk()
    obj=BillingClass(root)
    root.mainloop()