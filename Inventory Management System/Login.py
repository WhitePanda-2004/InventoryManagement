from tkinter import*
import EmailPassword
from PIL import ImageTk, Image
from tkinter import messagebox,ttk
import pymysql
import os
import smtplib
import time

class LoginClass :
    def __init__(self,root):
        self.root=root
        self.root.title("Inventory Management System | Login")
        self.root.geometry("1350x700+100+60")
        self.root.config(bg="#fafafa")
        self.root.resizable(False,False)
        self.root.focus_force()

        self.OTP = ""

        #---------- All Variables ---------->
        self.VarEmployeeId = StringVar()
        self.VarPassword = StringVar()

        #---------- Images ---------->
        self.PhoneImage = PhotoImage(file="Images/phone.png")
        self.LabelPhoneImage = Label(self.root, image=self.PhoneImage, bd=0).place(x=240,y=40)

        #---------- Login Frame ---------->
        LoginFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LoginFrame.place(x=710,y=40,width=400,height=620)

        title=Label(LoginFrame,text="Login Here",font=("Cambria",30,"bold"),fg="black", bg="white").place(x=0,y=30,relwidth=1)

        LabelEmployeeId=Label(LoginFrame,text="Enter Admin | Employee Id",font=("Cambria",16,"bold"),fg="#767171", bg="white").place(x=30,y=120)
        txtEmployeeId=Entry(LoginFrame, textvariable=self.VarEmployeeId,font=("Cambria",16, "bold"),bg="#ECECEC").place(x=30,y=170,width=340,height=30)

        LabelPassword=Label(LoginFrame,text="Enter Password",font=("Cambria",16,"bold"),fg="#767171", bg="white").place(x=30,y=250)
        txtPassword=Entry(LoginFrame, textvariable=self.VarPassword,font=("Cambria",16, "bold"),bg="#ECECEC",show="*").place(x=30,y=300,width=340,height=30)

        ButtonLogin=Button(LoginFrame, command=self.LoginDef, cursor="hand2",text=" Log In ",bg="#00B0F0", activebackground="#00B0F0", fg="white", activeforeground="white" ,font=("Cambria",18, "bold"), relief=GROOVE).place(x=30,y=375,width=340,height=40)
        LabelHRow = Label(LoginFrame,bg="lightgray",font=("Cambria",16,"bold")).place(x=30, y=470, width=340, height=3)
        LabelHOr = Label(LoginFrame,text=" OR ",fg="lightgray",bg="white",font=("Cambria",16,"bold")).place(x=175, y=455)
        ButtonForget=Button(LoginFrame, command=self.ForgetWindow, cursor="hand2",text=" Forget Password ? ",bg="white", activebackground="white", fg="#00759E", activeforeground="#00759E" ,font=("Cambria",16, "bold"),bd=0).place(x=30,y=510,width=340,height=35)
        ButtonSignup=Button(LoginFrame, command=self.SignUp, cursor="hand2",text="Don't Have An Accout ? Sign Up",bg="white", activebackground="white", fg="#00759E", activeforeground="#00759E" ,font=("Cambria",16, "bold"),bd=0).place(x=30,y=565,width=340,height=35)

        #---------- Image Animation ---------->
        self.Img1 = ImageTk.PhotoImage(file="Images/im1.png")
        self.Img2 = ImageTk.PhotoImage(file="Images/im2.png")
        self.Img3 = ImageTk.PhotoImage(file="Images/im3.png")

        self.ChangeImageLabel = Label(self.root,bg="white")
        self.ChangeImageLabel.place(x=407, y=143, height=428, width=240)

        self.Animation()

    
    def SignUp(self):
        self.root.destroy()
        os.system("python AdminRegister.py")
    
    
    def Animation(self):
        self.Img = self.Img1
        self.Img1 = self.Img2
        self.Img2 = self.Img3
        self.Img3 = self.Img
        self.ChangeImageLabel.config(image=self.Img)
        self.ChangeImageLabel.after(2000,self.Animation)
    
    def LoginDef(self):
        con = pymysql.connect(host="localhost", user="root", password="", db="IMSDatabase")
        cur = con.cursor()
        try:
            if self.VarEmployeeId.get()=="" or self.VarPassword.get()=="":
                messagebox.showerror("Error","All Fields Are Required",parent=self.root)
            else:
                cur.execute("select UserType from Employee where EmpID=%s AND Password=%s",(self.VarEmployeeId.get(), self.VarPassword.get()))
                User = cur.fetchone()
                if User==None:
                    messagebox.showerror("Error","Invalid Employee Id And Password",parent=self.root)
                else:
                    if User[0]=="Admin":
                        messagebox.showinfo("Login",f"Wel-Come To Inventory Management System\nPlaese Wait To Login...\nWel-Come {self.VarEmployeeId.get()}",parent=self.root)
                        self.root.destroy()
                        os.system("python Dashboard.py")
                    else:
                        messagebox.showinfo("Login",f"Wel-Come To Inventory Management System\nPlaese Wait To Login...\nWel-Come {self.VarEmployeeId.get()}",parent=self.root)
                        self.root.destroy()
                        os.system("python Billing.py")

        except Exception as ex:
            messagebox.showerror("Error", f"Error Due To {str(ex)}", parent=self.root)


    def ForgetWindow(self):
        con = pymysql.connect(host="localhost", user="root", password="", db="IMSDatabase")
        cur = con.cursor()
        try:
            if self.VarEmployeeId.get()=="":
                messagebox.showerror("Error", "Employee Id Must Be Required", parent=self.root)
            else:
                cur.execute("select Email from Employee where EmpID=%s",(self.VarEmployeeId.get(),))
                Email = cur.fetchone()
                if Email==None:
                    messagebox.showerror("Error","Invalid Employee Id...\nPlease Try Again",parent=self.root)
                else:
                    Chk = self.SendEmail(Email[0])
                    if Chk=='f':
                        messagebox.showerror("Error", "Connection Error, Try Again",parent=self.root)
                    else:  
                        #---------- Call Send Email Function And Window ---------->
                        self.ForgetWindow1 = Toplevel(self.root)
                        self.ForgetWindow1.title("Inventory Management System | Forget Password")
                        self.ForgetWindow1.geometry("390x610+823+136")
                        self.ForgetWindow1.focus_force()
                        self.ForgetWindow1.overrideredirect(1)

                        self.VarOTP = StringVar()
                        self.VarNewPassword = StringVar()
                        self.VarConfirmPassword = StringVar()

                        titleForget=Label(self.ForgetWindow1,text="Reset Password",font=("Cambria",30,"bold"),fg="white", bg="#3f51b5").place(x=0,y=1,relwidth=1)
                        
                        LabelResel=Label(self.ForgetWindow1,text="Enter OTP Send On Registered Email",font=("Cambria",15,"bold"),fg="black").place(x=0,y=80,relwidth=1)
                        txtReset=Entry(self.ForgetWindow1, textvariable=self.VarOTP,font=("Cambria",16, "bold"),bg="lightyellow").place(x=30,y=140,width=340,height=30)
                        
                        self.ButtonReset=Button(self.ForgetWindow1, command=self.ValidateOTP, cursor="hand2",text=" SUBMIT ",bg="lightblue", activebackground="lightblue", fg="black", activeforeground="black" ,font=("Cambria",18, "bold"), relief=GROOVE)
                        self.ButtonReset.place(x=30,y=200,width=340,height=36)

                        LabelNewPassword=Label(self.ForgetWindow1,text="Please Enter New Password",font=("Cambria",16,"bold"),fg="black").place(x=0,y=290,relwidth=1)
                        txtNewPassword=Entry(self.ForgetWindow1, textvariable=self.VarNewPassword,font=("Cambria",16, "bold"),bg="lightyellow").place(x=30,y=340,width=340,height=30)
                
                        LabelConfirmPassword=Label(self.ForgetWindow1,text="Please Enter Confirm Password",font=("Cambria",16,"bold"),fg="black").place(x=0,y=410,relwidth=1)
                        txtConfirmPassword=Entry(self.ForgetWindow1, show="*", textvariable=self.VarConfirmPassword,font=("Cambria",16, "bold"),bg="lightyellow").place(x=30,y=460,width=340,height=30)
                
                        self.ButtonUpdate=Button(self.ForgetWindow1, command=self.UpadatePassword, state=DISABLED, cursor="hand2",text=" Update Password ",bg="lightblue", activebackground="lightblue", fg="black", activeforeground="black" ,font=("Cambria",18, "bold"), relief=GROOVE)
                        self.ButtonUpdate.place(x=30,y=535,width=340,height=36)
      
        except Exception as ex:
            messagebox.showerror("Error", f"Error Due To {str(ex)}", parent=self.root)


    def UpadatePassword(self):
        if self.VarNewPassword.get()=="" or self.VarConfirmPassword.get()=="":
            messagebox.showerror("Error", "Password is Required", parent=self.ForgetWindow1)
        elif self.VarNewPassword.get()!= self.VarConfirmPassword.get():
            messagebox.showerror("Error", "New Password And Confirm Password Must be Same", parent=self.ForgetWindow1)
        else:
            con = pymysql.connect(host="localhost", user="root", password="", db="IMSDatabase")
            cur = con.cursor()
            try:
                cur.execute("update Employee SET Password=%s where EmpID=%s", (self.VarConfirmPassword.get(), self.VarEmployeeId.get()))
                con.commit()
                messagebox.showinfo("Password Update","Password Reset Successfully",parent=self.ForgetWindow1)
                self.ForgetWindow1.destroy()

            except Exception as ex:
                messagebox.showerror("Error", f"Error Due To {str(ex)}", parent=self.root)


    def ValidateOTP(self):
        if int(self.OTP)==int(self.VarOTP.get()):
            self.ButtonUpdate.config(state=NORMAL)
            self.ButtonReset.config(state=DISABLED)
        else:
            messagebox.showerror("Error", "Invalid OTO\nPlease Enter Right OTP", parent=self.ForgetWindow1)
    
    
    def SendEmail(self, to_):
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        Email1 = EmailPassword.Email1
        Password = EmailPassword.Password
        s.login(Email1, Password)

        self.OTP = int(time.strftime("%H%S%M"))+int(time.strftime("%S"))
        Subj= "IMS-Inventory Management System Reset Password OTP"
        msg = f" Dear Sir / Madam,\n\n Your Reset OTP is {str(self.OTP)}.\n\n With Regards,\n IMS Team\n Thank You...!"
        msg = "Subject : {}\n\n{}".format(Subj, msg)

        s.sendmail(Email1, to_, msg)
        Chk = s.ehlo()
        if Chk[0]==250:
            return "s"
        else:
            return "f"

if __name__=="__main__":
    root=Tk()
    obj=LoginClass(root)
    root.mainloop()