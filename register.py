# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 23:04:15 2022

@author: ERA
"""

from tkinter import*
from tkinter import ttk  # cool toolkit
from PIL import Image, ImageTk  # for images  , cropping and stuff
from tkinter import messagebox  # for eeror info or warning
import mysql.connector
from tkvideo import tkvideo






class Register:
    def __init__(self,root):
        self.root=root
        self.width = root.winfo_screenwidth()
        self.height = root.winfo_screenheight()
        self.root.geometry(str(self.width)+"x"+str(self.height)+"+0+0")
        self.root.wm_iconbitmap("face.ico")
        self.root.title("registration page")
        self.root.config(background="white")
        self.root.state('zoomed')
        self.root.resizable(0,0)
        #=========================variables
        self.first_name=StringVar()
        self.last_name=StringVar()
        self.contact=StringVar()
        self.email=StringVar()
        self.secret_phrase=StringVar()
        self.secret=StringVar()
        self.password=StringVar()
        self.confirm_password=StringVar()
        
        
        
        #=================================================
        img = Image.open(
            r"images\login2.png")#x.jpg
        # (W,H) ,ANTIALIAS HIGH LEVEL TO LOW LEVEL IMAGE
        img = img.resize(
            (int(self.width/2-100-100), self.height-150), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)  # set to a variable

        #to set it on window with label
        # lable inside root , with images help
        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=130, y=100, width=int(self.width/2-100-100),
                     height=self.height-150)
        
        
        #========================================logo==============================
        
        imglogo = Image.open(
            r"images\logos32.jpg")#x.jpg
        # (W,H) ,ANTIALIAS HIGH LEVEL TO LOW LEVEL IMAGE
        imglogo = imglogo.resize(
            (400, 150), Image.ANTIALIAS)
        self.photoimglogo = ImageTk.PhotoImage(imglogo)  # set to a variable

        #to set it on window with label
        # lable inside root , with images help
        bg_img = Label(self.root, image=self.photoimglogo)
        bg_img.place(x=0, y=0, width=400,
                     height=150)
         
        
        frame = Frame(self.root,bg="orange")  # inside mainframe+BORDER STYLE
        frame.place(x=650, y=150, width=int(self.width/2+100), height=self.height-300)

        
        img2 = Image.open(
           r"images\white.jpg")#x.jpg
       # (W,H) ,ANTIALIAS HIGH LEVEL TO LOW LEVEL IMAGE
        img2= img2.resize(
           (int(self.width/2+100)-40,self.height-300-40), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)  # set to a variable
   
       #to set it on window with label
       # lable inside root , with images help
        self.login_img = Label(self.root, image=self.photoimg2)
        self.login_img.place(x=650+20, y=150+20, width=int(self.width/2+100)-40, height=self.height-300-40)

        
        
        get_str = Label(self.login_img,text=" Ready To Register ! Lets Go Then ",font=("consolas",20,"bold"),fg="orange",bg="white")
        get_str.place(x=140, y=30+45, width=600, height=50)


      #===========================
        firstname_label = Label(self.login_img, text='First Name :',font=(
          "consolas", 15, "bold"), bg="white")
        firstname_label.place(x=50-30, y=100+60)  # rows and col in grid

        self.firstname_entry = ttk.Entry(self.login_img,textvariable=self.first_name ,width=19, font=(
          "consolas", 15, "bold"))  # for entry field _ttk style
        self.firstname_entry.place(x=200-30, y=100+60)
        
        
        lastname_label = Label(self.login_img, text='Last Name :', font=(
          "consolas", 15, "bold"), bg="white")
        lastname_label.place(x=450-15, y=100+60)  # rows and col in grid

        self.lastname_entry = ttk.Entry(self.login_img, textvariable=self.last_name,width=19, font=(
          "consolas", 15, "bold"))  # for entry field _ttk style
        self.lastname_entry.place(x=600-30, y=100+60)
        
        
        
        conname_label = Label(self.login_img, text='Contact No. :', font=(
          "consolas", 15, "bold"), bg="white")
        conname_label.place(x=50-30-10, y=100+60+60)  # rows and col in grid

        self.conname_entry = ttk.Entry(self.login_img, textvariable=self.contact,width=19, font=(
          "consolas", 15, "bold"))  # for entry field _ttk style
        self.conname_entry.place(x=200-30, y=100+60+60)
        
        
        emaname_label = Label(self.login_img, text='Email Id :', font=(
          "consolas", 15, "bold"), bg="white")
        emaname_label.place(x=450-15, y=100+60+60)  # rows and col in grid

        self.emaname_entry = ttk.Entry(self.login_img, textvariable=self.email,width=19, font=(
          "consolas", 15, "bold"))  # for entry field _ttk style
        self.emaname_entry.place(x=600-30, y=100+60+60)
        
        
        
    
          # rows and col in grid
          
         
        secname_label = Label(self.login_img, text='Secret Phrase :', font=(
          "consolas", 15, "bold"), bg="white")
        secname_label.place(x=50-30-10-10, y=100+60+60+60) 
          
          
        

        self.phraname_combo = ttk.Combobox(self.login_img,textvariable=self.secret_phrase, font=(
          "consolas", 15, "bold"), width=20, state="readonly")  # dropdownlist          #stylish in ttk
        self.phraname_combo["values"] = ("Select Secret Phrase ", "Your Secret ", "Your Pet's Name","Your Fac Ice Cream ","Your Birt Place ","Your First Ever Project ")
        # for indexing for "select deparment" to appear
        self.phraname_combo.current(0)
        self.phraname_combo.place(x=150+10+20, y=100+60+60+60)
        
        
        ansname_label = Label(self.login_img, text='Answer :', font=(
          "consolas", 15, "bold"), bg="white")
        ansname_label.place(x=450, y=100+60+60+60)  # rows and col in grid

        self.ansname_entry = ttk.Entry(self.login_img,textvariable=self.secret, width=19, font=(
          "consolas", 15, "bold"))  # for entry field _ttk style
        self.ansname_entry.place(x=600-30, y=100+60+60+60)
        
        
        pasname_label = Label(self.login_img, text='Password :', font=(
          "consolas", 15, "bold"), bg="white")
        pasname_label.place(x=50-30-10+10, y=100+60+120+60)  # rows and col in grid

        self.pasname_entry = ttk.Entry(self.login_img, textvariable=self.password,width=19, font=(
          "consolas", 15, "bold"))
        self.pasname_entry.place(x=200-50, y=100+60+120+60)
        
        
        confname_label = Label(self.login_img, text='Confirm Password :', font=(
          "consolas", 15, "bold"), bg="white")
        confname_label.place(x=450-55-10, y=100+60+120+60)  # rows and col in grid

        self.confname_entry = ttk.Entry(self.login_img,textvariable= self.confirm_password,width=19, font=(
          "consolas", 15, "bold"))  # for entry field _ttk style
        self.confname_entry.place(x=600-30+20+10, y=100+60+120+60) 
        
        
        #======================================================check button
        self.check=IntVar()
        checkbtn=Checkbutton(self.login_img,variable=self.check,text=" Agree to terms and conditions",fg="black",bg="orange",activeforeground="black",activebackground="orange",font=(
          "consolas", 12, "bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50-30-10+10, y=100+60+120+60+60)
        
        #==========================#=====================buttons=========================
        
        reg_button=Button(self.login_img,text=" Register ",command=self.register,font=("consolas",20,"bold"),bd=3,relief=RIDGE,fg="black",bg="orange",activeforeground="black",activebackground="orange")
        reg_button.place(x=50-30-10+10+200, y=100+60+120+60+60+60-10,width=180,height=45)
        




        login_button=Button(self.login_img,text=" Login ",command=self.back_to_login,font=("consolas",20,"bold"),bd=3,relief=RIDGE,fg="black",bg="orange",activeforeground="black",activebackground="orange")
        login_button.place(x=50-30-10+10+100+200+200, y=100+60+120+60+60+60-10,width=180,height=45)
        
       
        
       
        
       
        
        imglogs = Image.open(
           r"images\regjo.png")#x.jpg
       # (W,H) ,ANTIALIAS HIGH LEVEL TO LOW LEVEL IMAGE
        imglogs= imglogs.resize(
           (80,80), Image.ANTIALIAS)
        self.photoimglogs = ImageTk.PhotoImage(imglogs)  # set to a variable
   
       #to set it on window with label
       # lable inside root , with images help
        self.logs_img = Label(self.login_img, image=self.photoimglogs)
        self.logs_img.place(x=400, y=0, width=80, height=80)

        
        
       
        
        
        
        
        
        
    def back_to_login(self):
        self.root.destroy()
            
        
        
    def register(self):
        if self.first_name.get()==""or self.email.get()=="" or self.secret_phrase.get()=="Select Secret Phrase ":
            messagebox.showerror("Error ", "All Fields Are Required")
        elif self.password.get()!=self.confirm_password.get():
            messagebox.showerror("Error","Password and Confirmed Password must be same " )
        elif self.check.get()==0:
            messagebox.showerror("Error", "Please Agree To Terms And Conditions ")
        else:
            connection = mysql.connector.connect(
                host='localhost', username='root', password='password', database='facendance')
            cursor = connection.cursor()
            query=("select * from register where email=%s")
            value=(self.email.get(),)
            cursor.execute(query,value)
            row=cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","You Already Registered Once So Please Loging with Your Credentials ")
            else:
                cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(                    
                    self.first_name.get(),
                    self.last_name.get(),
                    self.contact.get(),
                    self.email.get(),
                    self.secret_phrase.get(),
                    self.secret.get(),
                    self.password.get()
                    
                    
                    ))
                connection.commit()
                connection.close()
                messagebox.showinfo("Suceess","Yay ! You Successfully Registered , Lets Get In ")
                
                
                
            
            
        



































if __name__ == "__main__":  # to call main
    root = Tk()  # call root from toolkit
    obj = Register(root)  # to connect with root
    root.mainloop()  # close mainloop