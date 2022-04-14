from tkinter import*
from PIL import ImageTk, Image
from tkinter import messagebox,ttk
import pymysql
import os

class SalesClass :
    def __init__(self,root):
        self.root=root
        self.root.title("Inventory Management System | Sales")
        self.root.geometry("1285x642+232+137")
        self.root.resizable(False,False)
        self.root.config(bg="white")
        self.root.focus_force()

        #---------- All Variables ---------->
        self.BillList = []
        self.VarInvoice=StringVar()
        self.VarCatName=StringVar()

        #---------- Title ---------->
        Title=Label(self.root, text="View Customer Bills", font=("Cambria", 20, "bold"), bg="#0f4d7d", fg="white", padx=20, pady=10, bd=2, relief=RIDGE).place(x=10, y=10, width=1268, height=50)
        
        #---------- Content Row 1 ---------->
        LabelInvoice=Label(self.root, text="Invoice No. :-", font=("Cambria", 15, "bold")).place(x=30, y=80)
        txtInvoice=Entry(self.root, textvariable=self.VarInvoice, font=("Cambria", 15, "bold"), bg="lightyellow").place(x=160, y=82, width=200)
        btnSearch = Button(self.root, command=self.SearchDef, text="Search", font=("Cambria",15,"bold"), bg="#2196f3", fg="white", bd=2, relief=RIDGE, cursor="hand2").place(x=370, y=80, height=30, width=120)
        btnClear = Button(self.root, command=self.ClearDef, pady=5, padx=10, text="Clear", font=("Cambria",15,"bold"), bg="#607d8b", bd=2, relief=RIDGE, cursor="hand2").place(x=500, y=80, width=120, height=30)

        #---------- Sales Frame ---------->
        SalesFrame = Frame(self.root, bd=2, relief=RIDGE)
        SalesFrame.place(x=30, y=120, width=280, height=510)

        ScrollY = Scrollbar(SalesFrame, orient=VERTICAL)
        ScrollY.pack(side=RIGHT,fill=Y)

        self.SalesList = Listbox(SalesFrame, font=("Cambria",15,"bold"), yscrollcommand=ScrollY)
        ScrollY.config(command=self.SalesList.yview)
        self.SalesList.pack(fill=BOTH, expand=1)
        self.SalesList.bind("<ButtonRelease-1>", self.GetData)

        #---------- Bill Area ---------->
        BillFrame = Frame(self.root, bd=2, relief=RIDGE)
        BillFrame.place(x=320, y=120, width=500, height=510)

        Title=Label(BillFrame, text="Customer Bill Area", font=("Cambria", 18, "bold"), bg="orange").pack(side=TOP, fill=X)

        ScrollY1 = Scrollbar(BillFrame, orient=VERTICAL)
        ScrollY1.pack(side=RIGHT,fill=Y)

        self.BillArea = Text(BillFrame, bg="lightyellow", yscrollcommand=ScrollY1)
        ScrollY.config(command=self.SalesList.yview)
        self.BillArea.pack(fill=BOTH, expand=1)
        
        #---------- Bill Area ---------->
        self.BillPhoto = Image.open("Images/cat2.jpg")
        self.BillPhoto = self.BillPhoto.resize((445,460), Image.ANTIALIAS)
        self.BillPhoto = ImageTk.PhotoImage(self.BillPhoto)

        LabelImage = Label(self.root, image=self.BillPhoto, bd=0)
        LabelImage.place(x=830, y=120)

        self.ShowTextFile()

    #---------- Bill Area ---------->
    def ShowTextFile(self):
        del self.BillList[:]
        self.SalesList.delete(0, END)
        for i in os.listdir("Bill"):
            if i.split(".")[-1]=="txt":
                self.SalesList.insert(END, i)
                self.BillList.append(i.split(".")[0])


    def GetData(self, ev):
        index_ = self.SalesList.curselection()
        FileName = self.SalesList.get(index_)
        self.BillArea.delete("1.0", END)
        FP = open(f"Bill/{FileName}", "r")
        for i in FP:
            self.BillArea.insert(END, i)
        FP.close()

    def SearchDef(self):
        if self.VarInvoice.get()=="":
            messagebox.showerror("Error", "Invoice No. Should be Required", parent =self.root)
        else:
            if self.VarInvoice.get() in self.BillList:
                FP = open(f"Bill/{self.VarInvoice.get()}.txt", "r")
                self.BillArea.delete("1.0", END)
                for i in FP:
                    self.BillArea.insert(END, i)
                FP.close()
            else:
                messagebox.showerror("Error", "Invalid Invoice No.", parent =self.root)


    def ClearDef(self):
        self.ShowTextFile()
        self.BillArea.delete("1.0", END)


        

if __name__=="__main__":
    root=Tk()
    obj=SalesClass(root)
    root.mainloop()