from tkinter import*
from PIL import ImageTk, Image
from tkinter import messagebox,ttk
import pymysql

class SupplierClass :
    def __init__(self,root):
        self.root=root
        self.root.title("Inventory Management System | Supplier")
        self.root.geometry("1285x642+232+137")
        self.root.resizable(False,False)
        self.root.focus_force()

        #---------- All Variables ---------->
        self.VarSearchBy = StringVar()
        self.VarSearchText = StringVar()

        self.VarSupInvoice = StringVar()
        self.VarSupName = StringVar()
        self.VarContact = StringVar()
        
        #---------- Search Label Frame ---------->
        SearchFrame = LabelFrame(self.root, bd=2, relief=RIDGE, font=("Cambria", 15, "bold"))
        SearchFrame.place(x=10, y=180, width=590, height=50)

        #---------- Options ---------->
        LabelSearchBy=Label(SearchFrame, text="Invoice No. :-", font=("Cambria", 15, "bold")).place(x=10, y=10)
       
        txtSearch = Entry(SearchFrame, textvariable=self.VarSearchText, font=("Cambria",15), bg="lightyellow").place(x=140, y=9, height=30, width=280)
        btnSearch = Button(SearchFrame, command=self.SearchDataDef, text="Search", font=("Cambria",15,"bold"), bg="#4caf50", fg="white", bd=2, relief=RIDGE, cursor="hand2").place(x=430, y=8, height=30, width=150)

        #---------- Title ---------->
        Title=Label(self.root, text="Supplier Details", font=("Cambria", 20, "bold"), bg="#0f4d7d", fg="white", padx=20, bd=2, relief=RIDGE).place(x=10, y=10, width=1268, height=50)

        #---------- Content Row 1 ---------->
        LabelSupInvoice=Label(self.root, text="Invoice No. :-", font=("Cambria", 15, "bold")).place(x=10, y=80)
        txtSupInvoice=Entry(self.root, textvariable=self.VarSupInvoice, font=("Cambria", 15, "bold"), bg="lightyellow").place(x=150, y=80, width=300)
        
        #---------- Content Row 2 ---------->
        LabelSupName=Label(self.root, text="Name :-", font=("Cambria", 15, "bold")).place(x=470, y=80)
        txtSupName=Entry(self.root, textvariable=self.VarSupName, font=("Cambria", 15, "bold"), bg="lightyellow").place(x=560, y=80, width=300)
       
        #---------- Content Row 3 ---------->
        LabelContact=Label(self.root, text="Contact :-", font=("Cambria", 15, "bold")).place(x=883, y=80)
        txtContact=Entry(self.root, textvariable=self.VarContact, font=("Cambria", 15, "bold"), bg="lightyellow").place(x=975, y=80, width=300)
        
        #---------- Content Row 4 ---------->
        LabelDescription=Label(self.root, text="Description :-", font=("Cambria", 15, "bold")).place(x=10, y=130)
        self.txtDescription=Text(self.root, font=("Cambria", 15, "bold"), bg="lightyellow")
        self.txtDescription.place(x=150, y=130, width=1130, height=40)

        #---------- Content Row 4 ---------->
        self.IconSide = PhotoImage(file="Images/side.png")
        btnSave = Button(self.root, command=self.SaveDataDef, pady=5, image=self.IconSide, compound=LEFT, padx=10, anchor="w", text="Save", font=("Cambria",15,"bold"), bg="#2196f3", bd=2, relief=RIDGE, cursor="hand2").place(x=610, y=185, width=150, height=35)
        btnUpdate = Button(self.root, command=self.UpdateDataDef, pady=5, image=self.IconSide, compound=LEFT, padx=10, anchor="w", text="Update", font=("Cambria",15,"bold"), bg="#4caf50", bd=2, relief=RIDGE, cursor="hand2").place(x=775, y=185, width=160, height=35)
        btnDelete = Button(self.root, command=self.DeleteDataDef, pady=5, image=self.IconSide, compound=LEFT, padx=10, anchor="w", text="Delete", font=("Cambria",15,"bold"), bg="#f44336", bd=2, relief=RIDGE, cursor="hand2").place(x=950, y=185, width=160, height=35)
        btnClear = Button(self.root, command=self.ClearDataDef, pady=5, image=self.IconSide, compound=LEFT, padx=10, anchor="w", text="Clear", font=("Cambria",15,"bold"), bg="#607d8b", bd=2, relief=RIDGE, cursor="hand2").place(x=1125, y=185, width=150, height=35)
        
        #---------- Supplier Details ---------->
        SupplierFrame = Frame(self.root, bd=2, relief=RIDGE)
        SupplierFrame.place(x=0, y=240, height=400, relwidth=1)

        YScrollBar = Scrollbar(SupplierFrame, orient=VERTICAL)
        XScrollBar = Scrollbar(SupplierFrame, orient=HORIZONTAL)

        XScrollBar.pack(side=BOTTOM, fill=X)
        YScrollBar.pack(side=RIGHT, fill=Y)

        self.SupplierTable = ttk.Treeview(SupplierFrame, columns=("Invoice", "Name", "Contact", "Description"), yscrollcommand=YScrollBar.set, xscrollcommand=XScrollBar.set)
        self.SupplierTable.heading("Invoice", text="Invoice No")
        self.SupplierTable.heading("Name", text="Name")
        self.SupplierTable.heading("Contact", text="Contact")
        self.SupplierTable.heading("Description", text="Description")
        
        self.SupplierTable["show"] = "headings"
        
        self.SupplierTable.column("Invoice", width=100)
        self.SupplierTable.column("Name", width=200)
        self.SupplierTable.column("Contact", width=100)
        self.SupplierTable.column("Description", width=300)
        
        self.SupplierTable.pack(fill=BOTH, expand=1)
        self.SupplierTable.bind("<ButtonRelease-1>", self.GetDataDef)
        
        self.ShowDataDef()

    #---------- Employee Save Data ---------->
    def SaveDataDef(self):
        if self.VarSupInvoice.get()=="":
            messagebox.showerror("Error", "Invoice Must be Required", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", db="IMSDatabase")
                cur = con.cursor()
                cur.execute("select * from Supplier where Invoice=%s", (self.VarSupInvoice.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error", "This Invoice No. Already Assigned...\nPlease Try Again With Valid Invoice No", parent=self.root)
                else:
                    cur.execute("insert into Supplier values(%s, %s, %s, %s)",
                                (
                                    self.VarSupInvoice.get(),
                                    self.VarSupName.get(),
                                    self.VarContact.get(),
                                    self.txtDescription.get("1.0", END),
                                ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Supplier Added Successfully", parent=self.root)
                    self.ShowDataDef()
                    self.ClearDataDef()
            except Exception as ex:
                messagebox.showerror("Error", f"Error Due To {str(ex)}", parent=self.root)

    #---------- Supplier Show Data ---------->
    def ShowDataDef(self):
        try:
            con = pymysql.connect(host="localhost", user="root", password="", db="IMSDatabase")
            cur = con.cursor()
            cur.execute("select * from Supplier")
            Row1=cur.fetchall()
            self.SupplierTable.delete(*self.SupplierTable.get_children())
            for row in Row1:
                self.SupplierTable.insert("", END, values=row)
            con.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error Due To {str(ex)}", parent=self.root)

    #---------- Supplier Get Data ---------->
    def GetDataDef(self, ev):
        f = self.SupplierTable.focus()
        content = (self.SupplierTable.item(f))
        row = content["values"]
        self.VarSupInvoice.set(row[0])
        self.VarSupName.set(row[1])
        self.VarContact.set(row[2])
        self.txtDescription.delete("1.0", END)
        self.txtDescription.insert(END, row[3])

    #---------- Supplier Update Data ---------->
    def UpdateDataDef(self):
        if self.VarSupInvoice.get()=="":
            messagebox.showerror("Error", "Invoice No Must Be Required", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", db="IMSDatabase")
                cur = con.cursor()
                cur.execute("select * from Supplier where Invoice=%s", (self.VarSupInvoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid Supplier Invoice No...\nPlease Try Again With Valid Invoice No", parent=self.root)
                else:
                    cur.execute("update Supplier set Name=%s, Contact=%s, Description=%s where Invoice=%s",
                                (
                                    self.VarSupName.get(),
                                    self.VarContact.get(),
                                    self.txtDescription.get("1.0", END),
                                    self.VarSupInvoice.get(),
                                ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Supplier Updated Successfully", parent=self.root)
                    self.ShowDataDef()
            except Exception as ex:
                messagebox.showerror("Error", f"Error Due To {str(ex)}", parent=self.root)

    #---------- Supplier Delete Data ---------->
    def DeleteDataDef(self):
        con = pymysql.connect(host="localhost", user="root", password="", db="IMSDatabase")
        cur = con.cursor()
        try:
            if self.VarSupInvoice.get()=="":
                messagebox.showerror("Error", "Invoice No Must Be Required", parent=self.root)
            else:
                cur.execute("select * from Supplier where Invoice=%s", (self.VarSupInvoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid Invoice No...\nPlease Try Again With Valid Id", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do You Really Want to Delete ?", parent=self.root)
                    if op==True:
                        cur.execute("delete from Supplier where Invoice=%s",(self.VarSupInvoice.get(),))
                        con.commit()
                        messagebox.showinfo("Success", "Supplier Deleted Successfully", parent=self.root)
                        self.ShowDataDef()
                        self.ClearDataDef()
        except Exception as ex:
                messagebox.showerror("Error", f"Error Due To {str(ex)}", parent=self.root)

    #---------- Supplier Clear Data ---------->
    def ClearDataDef(self):
        self.VarSupInvoice.set("")
        self.VarSupName.set("")
        self.VarContact.set("")
        self.txtDescription.delete("1.0", END)
        self.VarSearchText.set("")
        self.ShowDataDef()
        
    #---------- Supplier Search Data ---------->
    def SearchDataDef(self):
        try:
            con = pymysql.connect(host="localhost", user="root", password="", db="IMSDatabase")
            cur = con.cursor()
            if self.VarSearchText.get()=="":
                messagebox.showerror("Error", "Invoice No Should be Required", parent=self.root)
            else:
                cur.execute("select * from Supplier where Invoice=%s", (self.VarSearchText.get(),))
                Row=cur.fetchone()
                if Row!=None:
                    self.SupplierTable.delete(*self.SupplierTable.get_children())
                    self.SupplierTable.insert("", END, values=Row)
                else:
                    messagebox.showerror("Error", "No Record Found", parent=self.root)
                    con.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error Due To {str(ex)}", parent=self.root)



        

if __name__=="__main__":
    root=Tk()
    obj=SupplierClass(root)
    root.mainloop()