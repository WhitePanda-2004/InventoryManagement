from tkinter import*
from PIL import ImageTk, Image
from tkinter import messagebox,ttk
import pymysql

class EmployeeClass :
    def __init__(self,root):
        self.root=root
        self.root.title("Inventory Management System | Employee")
        self.root.geometry("1285x642+232+137")
        self.root.resizable(False,False)
        self.root.focus_force()
        
        #---------- All Variables ---------->
        self.VarSearchBy = StringVar()
        self.VarSearchText = StringVar()

        self.VarEmpId = StringVar()
        self.VarGender = StringVar()
        self.VarContact = StringVar()
        self.VarEmpName = StringVar()
        self.VarDOB = StringVar()
        self.VarDOJ = StringVar()
        self.VarEmail = StringVar()
        self.VarPassword = StringVar()
        self.VarUserType = StringVar()
        self.VarSalary = StringVar()

        #---------- Search Label Frame ---------->
        SearchFrame = LabelFrame(self.root, bd=2, relief=RIDGE, font=("Cambria", 15, "bold"), text=" Search Employee ")
        SearchFrame.place(x=155, y=5, width=970, height=70)

        #---------- Options ---------->
        LabelSearchBy=Label(SearchFrame, text="Select to Search :-", font=("Cambria", 15, "bold")).place(x=10, y=5)
        SearchCombo = ttk.Combobox(SearchFrame, textvariable=self.VarSearchBy, values=("<--- Select --->", "EmpID", "Name", "Email", "Contact"), state="readonly", justify=CENTER, font=("Cambria", 15, "bold"))
        SearchCombo.place(x=180, y=5, width=300)
        SearchCombo.current(0)

        txtSearch = Entry(SearchFrame, textvariable=self.VarSearchText, font=("Cambria",15), bg="lightyellow").place(x=490, y=4, height=30, width=300)
        btnSearch = Button(SearchFrame, command=self.SearchDataDef, text="Search", font=("Cambria",15,"bold"), bg="#4caf50", fg="white", bd=2, relief=RIDGE, cursor="hand2").place(x=800, y=3, height=30, width=150)

        #---------- Title ---------->
        Title=Label(self.root, text="Employee Details", font=("Cambria", 15, "bold"), bg="#0f4d7d", fg="white", padx=20).place(x=10, y=80, width=1268)

        #---------- Content Row 1 ---------->
        LabelEmpID=Label(self.root, text="Employee ID :-", font=("Cambria", 15, "bold")).place(x=10, y=130)
        LabelGender=Label(self.root, text="Gender :-", font=("Cambria", 15, "bold")).place(x=470, y=130)
        LabelContact=Label(self.root, text="Contact :-", font=("Cambria", 15, "bold")).place(x=883, y=130)

        txtEmpID=Entry(self.root, textvariable=self.VarEmpId, font=("Cambria", 15, "bold"), bg="lightyellow").place(x=150, y=133, width=300)
        GenderCombo = ttk.Combobox(self.root, textvariable=self.VarGender, values=("<--- Select --->", "Male", "Female", "Other"), state="readonly", justify=CENTER, font=("Cambria", 15, "bold"))
        GenderCombo.place(x=560, y=133, width=300)
        GenderCombo.current(0)
        txtContact=Entry(self.root, textvariable=self.VarContact, font=("Cambria", 15, "bold"), bg="lightyellow").place(x=975, y=133, width=300)

        #---------- Content Row 2 ---------->
        LabelEmpName=Label(self.root, text="Name :-", font=("Cambria", 15, "bold")).place(x=10, y=180)
        LabelDOB=Label(self.root, text="D. O. B :-", font=("Cambria", 15, "bold")).place(x=470, y=180)
        LabelDOJ=Label(self.root, text="D. O. J :-", font=("Cambria", 15, "bold")).place(x=883, y=180)

        txtEmpName=Entry(self.root, textvariable=self.VarEmpName, font=("Cambria", 15, "bold"), bg="lightyellow").place(x=150, y=183, width=300)
        txtDOB=Entry(self.root, textvariable=self.VarDOB, font=("Cambria", 15, "bold"), bg="lightyellow").place(x=560, y=183, width=300)
        txtDOJ=Entry(self.root, textvariable=self.VarDOJ, font=("Cambria", 15, "bold"), bg="lightyellow").place(x=975, y=183, width=300)

        #---------- Content Row 3 ---------->
        LabelEmail=Label(self.root, text="Email :-", font=("Cambria", 15, "bold")).place(x=10, y=230)
        LabelPassword=Label(self.root, text="Password :-", font=("Cambria", 15, "bold")).place(x=470, y=230)
        LabelUserType=Label(self.root, text="User Type :-", font=("Cambria", 15, "bold")).place(x=883, y=230)

        txtEmail=Entry(self.root, textvariable=self.VarEmail, font=("Cambria", 15, "bold"), bg="lightyellow").place(x=150, y=230, width=300)
        txtPassword=Entry(self.root, textvariable=self.VarPassword, font=("Cambria", 15, "bold"), bg="lightyellow", show="*").place(x=585, y=230, width=275)
        UserTypeCombo = ttk.Combobox(self.root, textvariable=self.VarUserType, values=("Admin", "Employee"), state="readonly", justify=CENTER, font=("Cambria", 15, "bold"))
        UserTypeCombo.place(x=1000, y=230, width=275)
        UserTypeCombo.current(0)

        #---------- Content Row 4 ---------->
        LabelAddress=Label(self.root, text="Address :-", font=("Cambria", 15, "bold")).place(x=10, y=280)
        LabelSalary=Label(self.root, text="Salary :-", font=("Cambria", 15, "bold")).place(x=883, y=280)

        self.txtAddress=Text(self.root, font=("Cambria", 15, "bold"), bg="lightyellow")
        self.txtAddress.place(x=150, y=280, width=710, height=40)
        txtSalary=Entry(self.root, textvariable=self.VarSalary, font=("Cambria", 15, "bold"), bg="lightyellow").place(x=975, y=280, width=300)

        #---------- Content Row 4 ---------->
        self.IconSide = PhotoImage(file="Images/side.png")
        btnSave = Button(self.root, command=self.SaveDataDef, pady=5, image=self.IconSide, compound=LEFT, padx=10, anchor="w", text="Save", font=("Cambria",15,"bold"), bg="#2196f3", bd=2, relief=RIDGE, cursor="hand2").place(x=610, y=325, width=150, height=35)
        btnUpdate = Button(self.root, command=self.UpdateDataDef, pady=5, image=self.IconSide, compound=LEFT, padx=10, anchor="w", text="Update", font=("Cambria",15,"bold"), bg="#4caf50", bd=2, relief=RIDGE, cursor="hand2").place(x=775, y=325, width=160, height=35)
        btnDelete = Button(self.root, command=self.DeleteDataDef, pady=5, image=self.IconSide, compound=LEFT, padx=10, anchor="w", text="Delete", font=("Cambria",15,"bold"), bg="#f44336", bd=2, relief=RIDGE, cursor="hand2").place(x=950, y=325, width=160, height=35)
        btnClear = Button(self.root, command=self.ClearDataDef, pady=5, image=self.IconSide, compound=LEFT, padx=10, anchor="w", text="Clear", font=("Cambria",15,"bold"), bg="#607d8b", bd=2, relief=RIDGE, cursor="hand2").place(x=1125, y=325, width=150, height=35)
        
        #---------- Employee Details ---------->
        EmployeeFrame = Frame(self.root, bd=2, relief=RIDGE)
        EmployeeFrame.place(x=0, y=370, height=270, relwidth=1)

        ScrollY = Scrollbar(EmployeeFrame, orient=VERTICAL)
        ScrollY.pack(side=RIGHT, fill=Y)

        ScrollX = Scrollbar(EmployeeFrame, orient=HORIZONTAL)
        ScrollX.pack(side=BOTTOM, fill=X)

        self.EmployeeTable = ttk.Treeview(EmployeeFrame, columns=("EmpID", "Name", "Email", "Gender", "Contact", "DOB", "DOJ", "Password", "UserType", "Address", "Salary"), yscrollcommand=ScrollY.set, xscrollcommand=ScrollX.set)
        ScrollY.config(command=self.EmployeeTable.yview)
        ScrollX.config(command=self.EmployeeTable.xview)

        self.EmployeeTable.heading("EmpID", text="Emp ID")
        self.EmployeeTable.heading("Name", text="Name")
        self.EmployeeTable.heading("Email", text="Email")
        self.EmployeeTable.heading("Gender", text="Gender")
        self.EmployeeTable.heading("Contact", text="Contact")
        self.EmployeeTable.heading("DOB", text="D.O.B")
        self.EmployeeTable.heading("DOJ", text="D.O.J")
        self.EmployeeTable.heading("Password", text="Password")
        self.EmployeeTable.heading("UserType", text="User Type")
        self.EmployeeTable.heading("Address", text="Address")
        self.EmployeeTable.heading("Salary", text="Salary")

        self.EmployeeTable["show"] = "headings"
        
        self.EmployeeTable.column("EmpID", width=40)
        self.EmployeeTable.column("Name", width=130)
        self.EmployeeTable.column("Email", width=150)
        self.EmployeeTable.column("Gender", width=40)
        self.EmployeeTable.column("Contact", width=50)
        self.EmployeeTable.column("DOB", width=50)
        self.EmployeeTable.column("DOJ", width=50)
        self.EmployeeTable.column("Password", width=100)
        self.EmployeeTable.column("UserType", width=50)
        self.EmployeeTable.column("Address", width=200)
        self.EmployeeTable.column("Salary", width=100)
        self.EmployeeTable.pack(fill=BOTH, expand=1)
        self.EmployeeTable.bind("<ButtonRelease-1>", self.GetDataDef)
        self.ShowDataDef()

    #---------- Employee Save Data ---------->
    def SaveDataDef(self):
        if self.VarEmpId.get()=="" or self.VarEmpName.get()=="" or self.VarEmail.get()=="" or self.VarGender.get()=="" or self.VarContact.get()=="" or self.VarPassword.get()=="" :
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", db="IMSDatabase")
                cur = con.cursor()
                cur.execute("select * from Employee where EmpId=%s", (self.VarEmpId.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error", "This Employee Id Already Assigned...\nPlease Try Again With Another Id", parent=self.root)
                else:
                    cur.execute("insert into Employee values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                                (
                                    self.VarEmpId.get(),
                                    self.VarEmpName.get(),
                                    self.VarEmail.get(),
                                    self.VarGender.get(),
                                    self.VarContact.get(),
                                    self.VarDOB.get(),
                                    self.VarDOJ.get(),
                                    self.VarPassword.get(),
                                    self.VarUserType.get(),
                                    self.txtAddress.get("1.0", END),
                                    self.VarSalary.get(),
                                ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Employee Added Successfully", parent=self.root)
                    self.ShowDataDef()
                    self.ClearDataDef()
            except Exception as ex:
                messagebox.showerror("Error", f"Error Due To {str(ex)}", parent=self.root)

    #---------- Employee Show Data ---------->
    def ShowDataDef(self):
        try:
            con = pymysql.connect(host="localhost", user="root", password="", db="IMSDatabase")
            cur = con.cursor()
            cur.execute("select * from Employee")
            Row1=cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in Row1:
                self.EmployeeTable.insert("", END, values=row)
            con.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error Due To {str(ex)}", parent=self.root)

    #---------- Employee Get Data ---------->
    def GetDataDef(self, ev):
        f = self.EmployeeTable.focus()
        content = (self.EmployeeTable.item(f))
        row = content["values"]
        self.VarEmpId.set(row[0])
        self.VarEmpName.set(row[1])
        self.VarEmail.set(row[2])
        self.VarGender.set(row[3])
        self.VarContact.set(row[4])
        self.VarDOB.set(row[5])
        self.VarDOJ.set(row[6])
        self.VarPassword.set(row[7])
        self.VarUserType.set(row[8])
        self.txtAddress.delete("1.0", END)
        self.txtAddress.insert(END, row[9])
        self.VarSalary.set(row[10])

    #---------- Employee Update Data ---------->
    def UpdateDataDef(self):
        if self.VarEmpId.get()=="":
            messagebox.showerror("Error", "Employee Id Must Be Required", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", db="IMSDatabase")
                cur = con.cursor()
                cur.execute("select * from Employee where EmpId=%s", (self.VarEmpId.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid Employee Id...\nPlease Try Again With Valid Id", parent=self.root)
                else:
                    cur.execute("update Employee set Name=%s, Email=%s, Gender=%s, Contact=%s, DOB=%s, DOJ=%s, Password=%s, UserType=%s, Address=%s, Salary=%s where EmpID=%s",
                                (
                                    self.VarEmpName.get(),
                                    self.VarEmail.get(),
                                    self.VarGender.get(),
                                    self.VarContact.get(),
                                    self.VarDOB.get(),
                                    self.VarDOJ.get(),
                                    self.VarPassword.get(),
                                    self.VarUserType.get(),
                                    self.txtAddress.get("1.0", END),
                                    self.VarSalary.get(),
                                    self.VarEmpId.get(),
                                ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Employee Updated Successfully", parent=self.root)
                    self.ClearDataDef()
                    self.ShowDataDef()

            except Exception as ex:
                messagebox.showerror("Error", f"Error Due To {str(ex)}", parent=self.root)

    #---------- Employee Delete Data ---------->
    def DeleteDataDef(self):
        con = pymysql.connect(host="localhost", user="root", password="", db="IMSDatabase")
        cur = con.cursor()
        try:
            if self.VarEmpId.get()=="":
                messagebox.showerror("Error", "Employee Id Must Be Required", parent=self.root)
            else:
                cur.execute("select * from Employee where EmpId=%s", (self.VarEmpId.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid Employee Id...\nPlease Try Again With Valid Id", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do You Really Want to Delete ?", parent=self.root)
                    if op==True:
                        cur.execute("delete from Employee where EmpId=%s",(self.VarEmpId.get(),))
                        con.commit()
                        messagebox.showinfo("Success", "Employee Deleted Successfully", parent=self.root)
                        self.ClearDataDef()
        except Exception as ex:
                messagebox.showerror("Error", f"Error Due To {str(ex)}", parent=self.root)

    #---------- Employee Clear Data ---------->
    def ClearDataDef(self):
        self.VarEmpId.set("")
        self.VarEmpName.set("")
        self.VarEmail.set("")
        self.VarGender.set("<--- Select --->")
        self.VarContact.set("")
        self.VarDOB.set("")
        self.VarDOJ.set("")
        self.VarPassword.set("")
        self.VarUserType.set("Admin")
        self.txtAddress.delete("1.0", END)
        self.VarSalary.set("")
        self.VarSearchText.set("")
        self.VarSearchBy.set("<--- Select --->")
        self.ShowDataDef()
        
    #---------- Employee Search Data ---------->
    def SearchDataDef(self):
        try:
            con = pymysql.connect(host="localhost", user="root", password="", db="IMSDatabase")
            cur = con.cursor()
            if self.VarSearchBy.get()=="<--- Select --->":
                messagebox.showerror("Error", "Select Search by Option Must be Required", parent=self.root)
            elif self.VarSearchText.get()=="":
                messagebox.showerror("Error", "Search Input Should be Required", parent=self.root)
            else:
                cur.execute("select * from Employee where "+self.VarSearchBy.get()+" LIKE '%"+self.VarSearchText.get()+"%' " " ")
                Row1=cur.fetchall()
                if len(Row1)!=0:
                    self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                    for row in Row1:
                        self.EmployeeTable.insert("", END, values=row)
                else:
                    messagebox.showerror("Error", "No Record Found", parent=self.root)
                    con.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error Due To {str(ex)}", parent=self.root)

if __name__=="__main__":
    root=Tk()
    obj=EmployeeClass(root)
    root.mainloop()