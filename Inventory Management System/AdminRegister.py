from sre_parse import State
from tkinter import*
from turtle import bgcolor
from PIL import ImageTk, Image
from tkinter import messagebox,ttk
import pymysql
import os

class AdminRegisterClass :
    def __init__(self,root):
        self.root=root
        self.root.title("Inventory Management System | Admin Register")
        self.root.geometry("1285x642+120+60")
        self.root.resizable(False,False)
        self.root.focus_force()

        #---------- All Variables ---------->
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
        
        #---------- Title Image 1 ---------->
        self.FirstImage = Image.open("Images/bg.png")
        self.FirstImage = self.FirstImage.resize((250,150), Image.ANTIALIAS)
        self.FirstImage = ImageTk.PhotoImage(self.FirstImage)
        self.LabelFirstImage = Label(self.root, image=self.FirstImage, bd=0)
        self.LabelFirstImage.place(x=350, y=20)

        #---------- Title Image 2 ---------->
        self.SecondImage = Image.open("Images/menu.png")
        self.SecondImage = self.SecondImage.resize((200,150), Image.ANTIALIAS)
        self.SecondImage = ImageTk.PhotoImage(self.SecondImage)
        self.LabelSecondImage = Label(self.root, image=self.SecondImage, bd=0)
        self.LabelSecondImage.place(x=700, y=20)
        
        #---------- Title ---------->
        Title=Label(self.root, text="Wel-Come to Inventory Management System, First Time Registration", font=("Cambria", 18, "bold"), bg="#0f4d7d", fg="white", padx=20).place(x=10, y=185, width=1268, height=40)
        Title12=Label(self.root, text="Note : Email Address Should be Correct, It Will Help to Recover The Password", font=("Cambria", 15, "bold"), fg="red", padx=20).place(x=10, y=550, width=1268, height=25)

        #---------- Content Row 1 ---------->
        LabelEmpID=Label(self.root, text="Employee ID :-", font=("Cambria", 15, "bold")).place(x=10, y=250)
        LabelGender=Label(self.root, text="Gender :-", font=("Cambria", 15, "bold")).place(x=470, y=250)
        LabelContact=Label(self.root, text="Contact :-", font=("Cambria", 15, "bold")).place(x=883, y=250)
        txtEmpID=Entry(self.root, textvariable=self.VarEmpId, font=("Cambria", 15, "bold"), bg="lightyellow").place(x=150, y=250, width=300)
        GenderCombo = ttk.Combobox(self.root, textvariable=self.VarGender, values=("<--- Select --->", "Male", "Female", "Other"), state="readonly", justify=CENTER, font=("Cambria", 15, "bold"))
        GenderCombo.place(x=560, y=250, width=300)
        GenderCombo.current(0)
        txtContact=Entry(self.root, textvariable=self.VarContact, font=("Cambria", 15, "bold"), bg="lightyellow").place(x=975, y=250, width=300)

        #---------- Content Row 2 ---------->
        LabelEmpName=Label(self.root, text="Name :-", font=("Cambria", 15, "bold")).place(x=10, y=303)
        LabelDOB=Label(self.root, text="D. O. B :-", font=("Cambria", 15, "bold")).place(x=470, y=303)
        LabelDOJ=Label(self.root, text="D. O. J :-", font=("Cambria", 15, "bold")).place(x=883, y=303)
        txtEmpName=Entry(self.root, textvariable=self.VarEmpName, font=("Cambria", 15, "bold"), bg="lightyellow").place(x=150, y=303, width=300)
        txtDOB=Entry(self.root, textvariable=self.VarDOB, font=("Cambria", 15, "bold"), bg="lightyellow").place(x=560, y=303, width=300)
        txtDOJ=Entry(self.root, textvariable=self.VarDOJ, font=("Cambria", 15, "bold"), bg="lightyellow").place(x=975, y=303, width=300)

        #---------- Content Row 3 ---------->
        LabelEmail=Label(self.root, text="Email :-", font=("Cambria", 15, "bold")).place(x=10, y=355)
        LabelPassword=Label(self.root, text="Password :-", font=("Cambria", 15, "bold")).place(x=470, y=355)
        LabelUserType=Label(self.root, text="User Type :-", font=("Cambria", 15, "bold")).place(x=883, y=355)
        txtEmail=Entry(self.root, textvariable=self.VarEmail, font=("Cambria", 15, "bold"), bg="lightyellow").place(x=150, y=355, width=300)
        txtPassword=Entry(self.root, textvariable=self.VarPassword, font=("Cambria", 15, "bold"), bg="lightyellow", show="*").place(x=585, y=355, width=275)
        UserTypeCombo = ttk.Combobox(self.root, textvariable=self.VarUserType, values=("Admin", "Employee"), state=DISABLED, justify=CENTER, font=("Cambria", 15, "bold"))
        UserTypeCombo.place(x=1000, y=355, width=275)
        UserTypeCombo.current(0)

        #---------- Content Row 4 ---------->
        LabelAddress=Label(self.root, text="Address :-", font=("Cambria", 15, "bold")).place(x=10, y=410)
        LabelSalary=Label(self.root, text="Salary :-", font=("Cambria", 15, "bold")).place(x=883, y=410)
        self.txtAddress=Text(self.root, font=("Cambria", 15, "bold"), bg="lightyellow")
        self.txtAddress.place(x=150, y=410, width=710, height=40)
        txtSalary=Entry(self.root, state=DISABLED, textvariable=self.VarSalary, font=("Cambria", 15, "bold"), bg="lightyellow").place(x=975, y=410, width=300)

        #---------- Content Row 4 ---------->
        self.IconSide = PhotoImage(file="Images/side.png")
        btnRegister = Button(self.root, command=self.SaveDataDef, pady=5, image=self.IconSide, compound=LEFT, padx=10, text=" Register ", font=("Cambria",15,"bold"), bg="#2196f3", bd=2, relief=RIDGE, cursor="hand2").place(x=420, y=470, width=200, height=35)
        btnClear = Button(self.root, command=self.ClearDataDef, pady=5, image=self.IconSide, compound=LEFT, padx=10, text="Clear", font=("Cambria",15,"bold"), bg="#607d8b", bd=2, relief=RIDGE, cursor="hand2").place(x=700, y=470, width=200, height=35)
        
        self.VarSalary.set("NA")
        
    #---------- Employee Save Data ---------->
    def SaveDataDef(self):
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
                messagebox.showinfo("Success", "Record Added Successfully", parent=self.root)
                self.ClearDataDef()
                self.root.destroy()
                os.system("python Login.py")
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
        
if __name__=="__main__":
    root=Tk()
    obj=AdminRegisterClass(root)
    root.mainloop()