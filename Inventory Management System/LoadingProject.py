from tkinter import*
from PIL import ImageTk, Image
from tkinter import messagebox,ttk
import pymysql
import os
import time

class LoadingProject:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1300x660+120+90")
        self.root.title("Inventory Management System | Developed by Akshay Yadav")
        self.root.resizable(False,False)
        self.root.focus_force()

        # ---- Background Image ----#
        bgImage = Image.open("Images/banner.jpg")
        bgImage = bgImage.resize((1300, 645), Image.ANTIALIAS)
        self.bgImage1 = ImageTk.PhotoImage(bgImage)
        LogoButton = Label(self.root, image=self.bgImage1, border=5)
        LogoButton.place(x=0, y=40, relwidth=1, relheight=1)
        
        Title = Label(text="Wel-Come To Project Inventory Management System", font=("Cambria", 30, "bold"), bg="#323232", fg="#F70975", padx=10, pady=5).place(x=0, y=0, relwidth=1, height=70)
        
        self.progress = ttk.Progressbar(style="red.Horizontal.TProgressbar", orient=HORIZONTAL, mode="determinate")
        self.progress.place(x=1, y=638, width=1299)

        #ProgressBarStart()
        ProgressbarButton = Button(command=self.ProgressBarStart, cursor="hand2", text="Get Started", fg="white",bg="#323232", font=("Cambria", 20, "bold")).place(x=10, y=80, width=300, height=35)

    def ProgressBarStart(self):
        r = 0
        for i in range(100):
            self.progress["value"] = r
            self.root.update_idletasks()
            time.sleep(0.1)
            r = r + 1
        self.root.destroy()
        os.system("python Login.py")

if __name__=="__main__":
    root=Tk()
    obj=LoadingProject(root)
    root.mainloop()