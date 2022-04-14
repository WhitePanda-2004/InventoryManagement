from tkinter import*
from PIL import ImageTk, Image     #------ pip install pillow ----->
from tkinter import messagebox,ttk
from Employee import EmployeeClass
from Sales import SalesClass
from Supplier import SupplierClass
from Category import CategoryClass
from Product import ProductClass
from Sales import SalesClass
import time
import pymysql
import os

class Dashboard:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1520x820+0+5")
        self.root.title("Inventory Management System | Developed by Akshay Yadav")
        self.root.resizable(False,False)
        self.root.config(bg="white")
        self.root.focus_force()

        #---------- Title Label ---------->
        self.IconTitle = PhotoImage(file="Images/logo1.png")
        Title=Label(self.root, text="Inventory Management System", image=self.IconTitle, compound=LEFT, font=("Cambria", 35, "bold"), bg="#010c48", fg="white", padx=20, anchor="w").place(x=0, y=0, relwidth=1, height=70)

        #---------- Logout Button ---------->
        btnLogout = Button(self.root, command=self.Logout, text="Logout", font=("Cambria", 20, "bold"), bg="yellow", cursor="hand2").place(x=1360, y=10, height=50, width=150)

        #---------- Clock ---------->
        self.ClockLabel=Label(self.root, text="Wel-Come to Inventory Management System\t\t Date : DD-MM-YYYY\t\t Time : HH:MM:SS", font=("Cambria", 15), bg="#4d636d", fg="white")
        self.ClockLabel.place(x=0, y=70, relwidth=1, height=30)

        #---------- Left Menu Frame ---------->
        self.MenuLogo = Image.open("Images/menu.png")
        self.MenuLogo = self.MenuLogo.resize((200, 240), Image.ANTIALIAS)
        self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)

        LeftMenuFrame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        LeftMenuFrame.place(x=0, y=101, width=230, height=675)

        LabelLeftMenu = Label(LeftMenuFrame, image=self.MenuLogo)
        LabelLeftMenu.pack(side=TOP, fill=X)

        self.IconSide = PhotoImage(file="Images/side.png")
        LabelMenu = Label(LeftMenuFrame, pady=10, bd=2, relief=RIDGE, text="Menu", font=("Cambria",20), bg="#009688").pack(side=TOP, fill=X)
        btnEmployee = Button(LeftMenuFrame, command=self.EmployeeDef, pady=5, image=self.IconSide, compound=LEFT, padx=20, anchor="w", text="Employee", font=("Cambria",20,"bold"), bg="#33bbf9", bd=2, relief=RIDGE, cursor="hand2").pack(side=TOP, fill=X)
        btnSupplier = Button(LeftMenuFrame, command=self.SupplierDef, pady=5, image=self.IconSide, compound=LEFT, padx=20, anchor="w", text="Supplier", font=("Cambria",20,"bold"), bg="#ff5722", bd=2, relief=RIDGE, cursor="hand2").pack(side=TOP, fill=X)
        btnCategory = Button(LeftMenuFrame, command=self.CategoryDef, pady=5, image=self.IconSide, compound=LEFT, padx=20, anchor="w", text="Category", font=("Cambria",20,"bold"), bg="#009688", bd=2, relief=RIDGE, cursor="hand2").pack(side=TOP, fill=X)
        btnProduct = Button(LeftMenuFrame, command=self.ProductDef, pady=5, image=self.IconSide, compound=LEFT, padx=20, anchor="w", text="Product", font=("Cambria",20,"bold"), bg="#607d8b", bd=2, relief=RIDGE, cursor="hand2").pack(side=TOP, fill=X)
        btnSales = Button(LeftMenuFrame, command=self.SalesDef, pady=5, image=self.IconSide, compound=LEFT, padx=20, anchor="w", text="Sales", font=("Cambria",20,"bold"), bg="#ffc107", bd=2, relief=RIDGE, cursor="hand2").pack(side=TOP, fill=X)
        btnExit = Button(LeftMenuFrame, pady=5, image=self.IconSide, compound=LEFT, padx=20, anchor="w", text="Exit", font=("Cambria",20,"bold"), bg="Red", bd=2, relief=RIDGE, cursor="hand2").pack(side=TOP, fill=X)

        #---------- Content ---------->
        self.LabelEmployee = Label(self.root, padx=10, pady=10, bd=5, relief=RIDGE, text="Total Employee\n\n[ 0 ]", bg="#33bbf9", fg="white", font=("Cambria", 20, "bold"))
        self.LabelEmployee.place(x=300, y=150, height=180, width=300)

        self.LabelSupplier = Label(self.root, padx=10, pady=10, bd=5, relief=RIDGE, text="Total Supplier\n\n[ 0 ]", bg="#ff5722", fg="white", font=("Cambria", 20, "bold"))
        self.LabelSupplier.place(x=725, y=350, height=180, width=300)

        self.LabelCategory = Label(self.root, padx=10, pady=10, bd=5, relief=RIDGE, text="Total Category\n\n[ 0 ]", bg="#009688", fg="white", font=("Cambria", 20, "bold"))
        self.LabelCategory.place(x=1150, y=150, height=180, width=300)

        self.LabelProduct = Label(self.root, padx=10, pady=10, bd=5, relief=RIDGE, text="Total Product\n\n[ 0 ]", bg="#607d8b", fg="white", font=("Cambria", 20, "bold"))
        self.LabelProduct.place(x=300, y=550, height=180, width=300)

        self.LabelSale = Label(self.root, padx=10, pady=10, bd=5, relief=RIDGE, text="Total Sales\n\n[ 0 ]", bg="#ffc107", fg="white", font=("Cambria", 20, "bold"))
        self.LabelSale.place(x=1150, y=550, height=180, width=300)

        #---------- Footer ---------->
        FooterLabel=Label(self.root, text="IMS-Inventory Management Sysetm | Developed by Akshay Yadav\nFor Any Technical Issue Contact : 96XXXXXX48", font=("Cambria", 12), bg="#4d636d", fg="white", activebackground="#4d636d", activeforeground="white")
        FooterLabel.pack(side=BOTTOM, fill=X)

        self.UpdateContent()

    #---------- Employee ---------->
    def EmployeeDef(self):
        self.NewWindow = Toplevel(self.root)
        self.NewObj = EmployeeClass(self.NewWindow)

    #---------- Supplier ---------->
    def SupplierDef(self):
        self.NewWindow = Toplevel(self.root)
        self.NewObj1 = SupplierClass(self.NewWindow)

    #---------- Category ---------->
    def CategoryDef(self):
        self.NewWindow = Toplevel(self.root)
        self.NewObj2 = CategoryClass(self.NewWindow)

    #---------- Product ---------->
    def ProductDef(self):
        self.NewWindow = Toplevel(self.root)
        self.NewObj3 = ProductClass(self.NewWindow)

    #---------- Product ---------->
    def SalesDef(self):
        self.NewWindow = Toplevel(self.root)
        self.NewObj3 = SalesClass(self.NewWindow)

    def UpdateContent(self):
        con = pymysql.connect(host="localhost", user="root", password="", db="IMSDatabase")
        cur = con.cursor()
        try:
            cur.execute("select * from Product")
            Product = cur.fetchall()
            self.LabelProduct.config(text=f"Total Products\n\n[ {str(len(Product))} ]")

            cur.execute("select * from Supplier")
            Supplier = cur.fetchall()
            self.LabelSupplier.config(text=f"Total Suppliers\n\n[ {str(len(Supplier))} ]")

            cur.execute("select * from Category")
            Category = cur.fetchall()
            self.LabelCategory.config(text=f"Total Category\n\n[ {str(len(Category))} ]")

            cur.execute("select * from Employee")
            Employee = cur.fetchall()
            self.LabelEmployee.config(text=f"Total Employees\n\n[ {str(len(Employee))} ]")  
        
            self.LabelSale.config(text=f"Total Sales\n\n[ {str(len(os.listdir('Bill')))} ]")
            Time1 = time.strftime("%I : %M : %S")
            Date1 = time.strftime("%d - %m - %Y")
            self.ClockLabel.config(text=f"Wel-Come to Inventory Management System\t\t Date : {str(Date1)} \t\t Time : {str(Time1)}")
            self.ClockLabel.after(200, self.UpdateContent)
        except Exception as ex:
            messagebox.showerror("Error", f"Error Due To {str(ex)}", parent=self.root)

    def Logout(self):
        OP = messagebox.askyesno("Confirm", "Are You Sure You Want to Logout.", parent=self.root)
        if OP==True:
            messagebox.showinfo("Error", "You Have Been Logged Out", parent=self.root)
            self.root.destroy()
            os.system("python Login.py")


if __name__=="__main__":
    root=Tk()
    obj=Dashboard(root)
    root.mainloop()