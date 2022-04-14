from tkinter import*
from PIL import ImageTk, Image
from tkinter import messagebox,ttk
import pymysql

class ProductClass :
    def __init__(self,root):
        self.root=root
        self.root.title("Inventory Management System | Product")
        self.root.geometry("1285x642+232+137")
        self.root.resizable(False,False)
        self.root.focus_force()

        #---------- All Variables ---------->
        self.VarSearchBy = StringVar()
        self.VarSearchText = StringVar()

        self.VarProductId = StringVar()
        self.VarCategory = StringVar()
        self.VarSupplier = StringVar()

        self.CatList = []
        self.SupList = []
        self.FetchCategorySupplierDef()

        self.VarName = StringVar()
        self.VarPrice = StringVar()
        self.VarQuantity = StringVar()
        self.VarStatus = StringVar()

        #---------- Product Frame ---------->
        ProductFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        ProductFrame.place(x=10,y=10,width=560,height=625)

        #---------- Title ---------->
        title = Label(ProductFrame, text="Product Details", font=("Cambria", 20, "bold"), bg="#0f4d7d", fg="white", padx=20, bd=2)
        title.pack(side=TOP,fill=X)
        
        #---------- Content Row 1 ---------->
        LabelProductId = Label(ProductFrame, text="Product Id :-", font=("Cambria", 18), bg="white")
        LabelProductId.place(x=30,y=60)

        LabelCategory = Label(ProductFrame, text="Category :-", font=("Cambria", 18), bg="white")
        LabelCategory.place(x=30,y=120)

        LabelSupplier = Label(ProductFrame, text="Supplier :-", font=("Cambria", 18), bg="white")
        LabelSupplier.place(x=30, y=180)

        LabelProduct = Label(ProductFrame, text="Name :-", font=("Cambria", 18), bg="white")
        LabelProduct.place(x=30, y=240)

        LabelPrice = Label(ProductFrame, text="Price :-", font=("Cambria", 18), bg="white")
        LabelPrice.place(x=30, y=300)

        LabelQuantity = Label(ProductFrame, text="Quantity :-", font=("Cambria", 18), bg="white")
        LabelQuantity.place(x=30, y=360)

        LabelStatus = Label(ProductFrame, text="Status :-", font=("Cambria", 18), bg="white")
        LabelStatus.place(x=30, y=420)

        #---------- Content Row 2 ---------->
        txtProductId = Entry(ProductFrame, textvariable=self.VarProductId, font=("Cambria", 15, "bold"),bg="lightyellow").place(x=170, y=63, width=350)

        ComboCategory = ttk.Combobox(ProductFrame, textvariable=self.VarCategory, values=self.CatList, state="readonly", justify=CENTER, font=("Cambria", 15, "bold"))
        ComboCategory.place(x=170, y=120, width=350) 
        ComboCategory.current(0)

        ComboSupplier = ttk.Combobox(ProductFrame, textvariable=self.VarSupplier, values=self.SupList, state="readonly", justify=CENTER, font=("Cambria", 15, "bold"))
        ComboSupplier.place(x=170, y=180, width=350)
        ComboSupplier.current(0)

        txtName = Entry(ProductFrame, textvariable=self.VarName, font=("Cambria", 15, "bold"),bg="lightyellow").place(x=170, y=240, width=350)
        txtPrice = Entry(ProductFrame, textvariable=self.VarPrice, font=("Cambria", 15, "bold"), bg="lightyellow").place(x=170, y=300, width=350)
        txtQuantity = Entry(ProductFrame, textvariable=self.VarQuantity, font=("Cambria", 15, "bold"), bg="lightyellow").place(x=170, y=360, width=350)

        ComboStatus = ttk.Combobox(ProductFrame, textvariable=self.VarStatus, values=("Active","InActive"), state='readonly',justify=CENTER, font=("Cambria", 15, "bold"))
        ComboStatus.place(x=170, y=420, width=350)
        ComboStatus.current(0)

       #---------- Content Row 4 ---------->
        self.IconSide = PhotoImage(file="Images/side.png")
        btnSave = Button(ProductFrame, command=self.SaveDataDef, pady=5, image=self.IconSide, compound=LEFT, padx=10, anchor="w", text="Save", font=("Cambria",15,"bold"), bg="#2196f3", bd=2, relief=RIDGE, cursor="hand2").place(x=30, y=500, width=160, height=35)
        btnUpdate = Button(ProductFrame, command=self.UpdateDataDef, pady=5, image=self.IconSide, compound=LEFT, padx=10, anchor="w", text="Update", font=("Cambria",15,"bold"), bg="#4caf50", bd=2, relief=RIDGE, cursor="hand2").place(x=195, y=500, width=160, height=35)
        btnDelete = Button(ProductFrame, command=self.DeleteDataDef, pady=5, image=self.IconSide, compound=LEFT, padx=10, anchor="w", text="Delete", font=("Cambria",15,"bold"), bg="#f44336", bd=2, relief=RIDGE, cursor="hand2").place(x=360, y=500, width=160, height=35)
        btnClear = Button(ProductFrame, command=self.ClearDataDef, pady=5, image=self.IconSide, compound=LEFT, padx=10, anchor="w", text="Clear", font=("Cambria",15,"bold"), bg="#607d8b", bd=2, relief=RIDGE, cursor="hand2").place(x=195, y=560, width=160, height=35)

        #---------- Search Label Frame ---------->
        SearchFrame = LabelFrame(self.root, bd=2, relief=RIDGE, font=("Cambria", 15, "bold"), text=" Search Product ")
        SearchFrame.place(x=575, y=10, width=700, height=70)

        #---------- Options ---------->
        SearchCombo = ttk.Combobox(SearchFrame, textvariable=self.VarSearchBy, values=("<---Select--->", "PId", "Category", "Supplier", "Name"), state="readonly", justify=CENTER, font=("Cambria", 15, "bold"))
        SearchCombo.place(x=10, y=5, width=250)
        SearchCombo.current(0)

        txtSearch = Entry(SearchFrame, textvariable=self.VarSearchText, font=("Cambria",15), bg="lightyellow").place(x=270, y=4, height=30, width=260)
        btnSearch = Button(SearchFrame, command=self.SearchDataDef, text="Search", font=("Cambria",15,"bold"), bg="#4caf50", fg="white", bd=2, relief=RIDGE, cursor="hand2").place(x=540, y=3, height=30, width=150)

        #---------- Product Details Frame ---------->
        ProductDetailFrame = Frame(self.root, bd=3, relief=RIDGE)
        ProductDetailFrame.place(x=575, y=85, width=700, height=550)

        ScrollY = Scrollbar(ProductDetailFrame, orient=VERTICAL)
        ScrollY.pack(side=RIGHT, fill=Y)

        ScrollX = Scrollbar(ProductDetailFrame, orient=HORIZONTAL)
        ScrollX.pack(side=BOTTOM, fill=X)

        self.ProductTable = ttk.Treeview(ProductDetailFrame, columns=("Pid","Category","Supplier", "Name", "Price", "Quantity", "Status"),yscrollcommand=ScrollY.set, xscrollcommand=ScrollX.set)
        ScrollY.config(command=self.ProductTable.yview)
        ScrollX.config(command=self.ProductTable.xview)

        self.ProductTable.heading("Pid", text="PID")
        self.ProductTable.heading("Category", text="Category")
        self.ProductTable.heading("Supplier", text="Supplier")
        self.ProductTable.heading("Name", text="Name")
        self.ProductTable.heading("Price", text="Price")
        self.ProductTable.heading("Quantity", text="Quantity")
        self.ProductTable.heading("Status", text="Status")


        self.ProductTable["show"] = "headings"

        self.ProductTable.column("Pid", width=50)
        self.ProductTable.column("Category", width=120)
        self.ProductTable.column("Supplier", width=120)
        self.ProductTable.column("Name", width=120)
        self.ProductTable.column("Price", width=50)
        self.ProductTable.column("Quantity", width=60)
        self.ProductTable.column("Status", width=70)
        self.ProductTable.pack(fill=BOTH, expand=1)
        self.ProductTable.bind("<ButtonRelease-1>", self.GetDataDef)
        self.ShowDataDef()

    #---------- Fetch Category And Supplier ---------->
    def FetchCategorySupplierDef(self):
        con = pymysql.connect(host="localhost", user="root", password="", db="IMSDatabase")
        cur = con.cursor()
        try:
            cur.execute("select Name from Category")
            Cat = cur.fetchall()
            self.CatList.append("Empty")
            self.SupList.append("Empty")
            if len(Cat)>0:
                del self.CatList[:]
                self.CatList.append("<---Select--->")
                for i in Cat:
                    self.CatList.append(i[0])

            cur.execute("select Name from Supplier")
            Sup = cur.fetchall()
            if len(Sup)>0:
                del self.SupList[:]
                self.SupList.append("<---Select--->")
                for i in Sup:
                    self.SupList.append(i[0])

        except Exception as ex:
            messagebox.showerror("Error", f"Error Due To {str(ex)}", parent=self.root)

    #---------- Product Save Data ---------->
    def SaveDataDef(self):
        if self.VarCategory.get()=="<---Select--->" or self.VarCategory.get()=="Empty" or self.VarSupplier.get()=="<--- Select --->" or self.VarName.get()=="":
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", db="IMSDatabase")
                cur = con.cursor()
                cur.execute("select * from Product where Name=%s", (self.VarName.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error", "This Product Already Present...\nPlease Try Again With Another Name", parent=self.root)
                else:
                    cur.execute("insert into Product values(%s, %s, %s, %s, %s, %s, %s)",
                                (
                                    self.VarProductId.get(),
                                    self.VarCategory.get(),
                                    self.VarSupplier.get(),
                                    self.VarName.get(),
                                    self.VarPrice.get(),
                                    self.VarQuantity.get(),
                                    self.VarStatus.get(),
                                ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Product Added Successfully", parent=self.root)
                    self.ShowDataDef()
                    self.ClearDataDef()
            except Exception as ex:
                messagebox.showerror("Error", f"Error Due To {str(ex)}", parent=self.root)

    #---------- Product Show Data ---------->
    def ShowDataDef(self):
        try:
            con = pymysql.connect(host="localhost", user="root", password="", db="IMSDatabase")
            cur = con.cursor()
            cur.execute("select * from Product")
            Row1=cur.fetchall()
            self.ProductTable.delete(*self.ProductTable.get_children())
            for row in Row1:
                self.ProductTable.insert("", END, values=row)
            con.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error Due To {str(ex)}", parent=self.root)

    #---------- Product Get Data ---------->
    def GetDataDef(self, ev):
        f = self.ProductTable.focus()
        content = (self.ProductTable.item(f))
        row = content["values"]
        self.VarProductId.set(row[0])
        self.VarCategory.set(row[1])
        self.VarSupplier.set(row[2])
        self.VarName.set(row[3])
        self.VarPrice.set(row[4])
        self.VarQuantity.set(row[5])
        self.VarStatus.set(row[6])

    #---------- Product Update Data ---------->
    def UpdateDataDef(self):
        if self.VarProductId.get()=="":
            messagebox.showerror("Error", "Please Select Product from List", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", db="IMSDatabase")
                cur = con.cursor()
                cur.execute("select * from Product where PId=%s", (self.VarProductId.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid Product...\nPlease Try Again With Valid Id", parent=self.root)
                else:
                    cur.execute("update Product set Category=%s, Supplier=%s, Name=%s, Price=%s, Quantity=%s, Status=%s where PId=%s",
                                (
                                    self.VarCategory.get(),
                                    self.VarSupplier.get(),
                                    self.VarName.get(),
                                    self.VarPrice.get(),
                                    self.VarQuantity.get(),
                                    self.VarStatus.get(),
                                    self.VarProductId.get(),
                                ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Product Updated Successfully", parent=self.root)
                    self.ShowDataDef()
                    self.ClearDataDef()
            except Exception as ex:
                messagebox.showerror("Error", f"Error Due To {str(ex)}", parent=self.root)

    #---------- Product Delete Data ---------->
    def DeleteDataDef(self):
        con = pymysql.connect(host="localhost", user="root", password="", db="IMSDatabase")
        cur = con.cursor()
        try:
            if self.VarProductId.get()=="":
                messagebox.showerror("Error", "Please Select Product from List", parent=self.root)
            else:
                cur.execute("select * from Product where PId=%s", (self.VarProductId.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid Product...\nPlease Try Again With Valid Id", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do You Really Want to Delete ?", parent=self.root)
                    if op==True:
                        cur.execute("delete from Product where PId=%s",(self.VarProductId.get(),))
                        con.commit()
                        messagebox.showinfo("Success", "Product Deleted Successfully", parent=self.root)
                        self.ClearDataDef()
        except Exception as ex:
                messagebox.showerror("Error", f"Error Due To {str(ex)}", parent=self.root)

    #---------- Product Clear Data ---------->
    def ClearDataDef(self):
        self.VarProductId.set("")
        self.VarCategory.set("<---Select--->")
        self.VarSupplier.set("<---Select--->")
        self.VarName.set("")
        self.VarPrice.set("")
        self.VarQuantity.set("")
        self.VarStatus.set("Active")
        self.VarSearchText.set("")
        self.VarSearchBy.set("<---Select--->")
        self.ShowDataDef()
        
    #---------- Product Search Data ---------->
    def SearchDataDef(self):
        try:
            con = pymysql.connect(host="localhost", user="root", password="", db="IMSDatabase")
            cur = con.cursor()
            if self.VarSearchBy.get()=="<--- Select --->":
                messagebox.showerror("Error", "Select Search by Option Must be Required", parent=self.root)
            elif self.VarSearchText.get()=="":
                messagebox.showerror("Error", "Search Input Should be Required", parent=self.root)
            else:
                cur.execute("select * from Product where "+self.VarSearchBy.get()+" LIKE '%"+self.VarSearchText.get()+"%' " " ")
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

if __name__=="__main__":
    root=Tk()
    obj=ProductClass(root)
    root.mainloop()