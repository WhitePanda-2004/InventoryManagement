from tkinter import*
from PIL import ImageTk, Image
from tkinter import messagebox,ttk
import pymysql

class CategoryClass :
    def __init__(self,root):
        self.root=root
        self.root.title("Inventory Management System | Category")
        self.root.geometry("1285x642+232+137")
        self.root.resizable(False,False)
        self.root.focus_force()

        #---------- All Variables ---------->
        self.VarCatId=StringVar()
        self.VarCatName=StringVar()

        #---------- Title ---------->
        Title=Label(self.root, text="Manage Product Category", font=("Cambria", 20, "bold"), bg="#0f4d7d", fg="white", padx=20, pady=10, bd=2, relief=RIDGE).place(x=10, y=10, width=1268, height=50)

        #---------- Content Row 1 ---------->
        LabelCatName=Label(self.root, text="Enter Category Name & Id", font=("Cambria", 20, "bold")).place(x=30, y=80)
        txtCatId=Entry(self.root, textvariable=self.VarCatId, font=("Cambria", 20, "bold"), bg="lightyellow").place(x=360, y=82, width=300)
        txtCatName=Entry(self.root, textvariable=self.VarCatName, font=("Cambria", 20, "bold"), bg="lightyellow").place(x=30, y=140, width=300)
        btnAdd = Button(self.root, command=self.SaveDataDef, text="Add", font=("Cambria",20,"bold"), bg="#4caf50", fg="white", bd=2, relief=RIDGE, cursor="hand2").place(x=350, y=140, height=35, width=150)
        btnDelete = Button(self.root,command=self.DeleteDataDef, text="Delete", font=("Cambria",20,"bold"), bg="red", fg="white", bd=2, relief=RIDGE, cursor="hand2").place(x=510, y=140, height=35, width=150)

        #---------- Category Details ---------->
        CategoryFrame = Frame(self.root, bd=2, relief=RIDGE)
        CategoryFrame.place(x=10, y=190, height=440, width=660)

        YScrollBar = Scrollbar(CategoryFrame, orient=VERTICAL)
        XScrollBar = Scrollbar(CategoryFrame, orient=HORIZONTAL)

        XScrollBar.pack(side=BOTTOM, fill=X)
        YScrollBar.pack(side=RIGHT, fill=Y)

        self.CategoryTable = ttk.Treeview(CategoryFrame, columns=("CatID", "Name"), yscrollcommand=YScrollBar.set, xscrollcommand=XScrollBar.set)
        self.CategoryTable.heading("CatID", text="Category Id")
        self.CategoryTable.heading("Name", text="Category Name")
        
        self.CategoryTable["show"] = "headings"
        
        self.CategoryTable.column("CatID", width=80)
        self.CategoryTable.column("Name", width=200)
        
        self.CategoryTable.pack(fill=BOTH, expand=1)
        self.CategoryTable.bind("<ButtonRelease-1>", self.GetDataDef)

        #---------- Images 1 ---------->
        self.CatImage1 = Image.open("Images/cat.jpg")
        self.CatImage1 = self.CatImage1.resize((590,270), Image.ANTIALIAS)
        self.CatImage1 = ImageTk.PhotoImage(self.CatImage1)

        self.LabelCatImage1 = Label(self.root, image=self.CatImage1, bd=2, relief=RAISED)
        self.LabelCatImage1.place(x=682, y=70)

        #---------- Images 2 ---------->
        self.CatImage2 = Image.open("Images/category.jpg")
        self.CatImage2 = self.CatImage2.resize((590,275), Image.ANTIALIAS)
        self.CatImage2 = ImageTk.PhotoImage(self.CatImage2)

        self.LabelCatImage2 = Label(self.root, image=self.CatImage2, bd=2, relief=RAISED)
        self.LabelCatImage2.place(x=682, y=350)

        self.ShowDataDef()

    #---------- Category Save Data ---------->
    def SaveDataDef(self):
        if self.VarCatId.get()=="":
            messagebox.showerror("Error", "Category Name Should be Required", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", db="IMSDatabase")
                cur = con.cursor()
                cur.execute("select * from Category where Name=%s", (self.VarCatName.get(),))
                Cat=cur.fetchone()
                if Cat!=None:
                    messagebox.showerror("Error", "This Category Already Present...\nPlease Try Again With Valid Category Name")
                else:
                    cur.execute("insert into Category values(%s,%s)",(self.VarCatId.get(),self.VarCatName.get()))
                    con.commit()
                    messagebox.showinfo("Success", "Category Added Successfully", parent=self.root)
                    self.VarCatName.set("")
                    self.ShowDataDef()
            except Exception as ex:
                messagebox.showerror("Error", f"Error Due To {str(ex)}", parent=self.root)
    
    #---------- Category Save Data ---------->
    def ShowDataDef(self):
        try:
            con = pymysql.connect(host="localhost", user="root", password="", db="IMSDatabase")
            cur = con.cursor()
            cur.execute("select * from Category")
            Row1=cur.fetchall()
            self.CategoryTable.delete(*self.CategoryTable.get_children())
            for row in Row1:
                self.CategoryTable.insert("", END, values=row)
            con.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error Due To {str(ex)}", parent=self.root)

    #---------- Category Get Data ---------->
    def GetDataDef(self, ev):
        f = self.CategoryTable.focus()
        content = (self.CategoryTable.item(f))
        row = content["values"]
        self.VarCatId.set(row[0])
        self.VarCatName.set(row[1])


    #---------- Category Delete Data ---------->
    def DeleteDataDef(self):
        try:
            if self.VarCatId.get()=="":
                messagebox.showerror("Error", "Please Select Category Name", parent=self.root)
            else:
                con = pymysql.connect(host="localhost", user="root", password="", db="IMSDatabase")
                cur = con.cursor()
                cur.execute("select * from Category where CId=%s", (self.VarCatId.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid Category Name...\nPlease Try Again With Valid Name", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do You Really Want to Delete ?", parent=self.root)
                    if op==True:
                        cur.execute("delete from Category where CId=%s",(self.VarCatId.get(),))
                        con.commit()
                        messagebox.showinfo("Success", "Category Deleted Successfully", parent=self.root)
                        self.ShowDataDef()
                        self.VarCatId.set("")
                        self.VarCatName.set("")
        except Exception as ex:
                messagebox.showerror("Error", f"Error Due To {str(ex)}", parent=self.root)









if __name__=="__main__":
    root=Tk()
    obj=CategoryClass(root)
    root.mainloop()