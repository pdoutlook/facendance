# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 16:18:46 2022

@author: ERA
"""

from tkinter import*
from tkinter import ttk  # cool toolkit
from PIL import Image, ImageTk  # for images  , cropping and stuff
from tkinter import messagebox  # for eeror info or warning
import mysql.connector
from tkvideo import tkvideo
from register import Register
from MAIN import Face_Recognition_System



class login_window:
     def __init__(self,root):
         self.root=root
         
         self.width = root.winfo_screenwidth()
         self.height = root.winfo_screenheight()
         self.root.geometry(str(self.width)+"x"+str(self.height)+"+0+0")
         self.root.wm_iconbitmap("face.ico")
         self.root.title("login page")
         self.root.config(background="white")
         
         self.root.state('zoomed')
         self.root.resizable(0,0)
         
         
         img = Image.open(
             r"images\logo.jpg")#x.jpg
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
         
         imglogo = Image.open( r"images\logos32.jpg")#x.jpg
         # (W,H) ,ANTIALIAS HIGH LEVEL TO LOW LEVEL IMAGE
         imglogo = imglogo.resize(
             (400, 150), Image.ANTIALIAS)
         self.photoimglogo = ImageTk.PhotoImage(imglogo)  # set to a variable

         #to set it on window with label
         # lable inside root , with images help
         bg_img = Label(self.root, image=self.photoimglogo)
         bg_img.place(x=0, y=0, width=400,
                      height=150)
         
         
         
         #================================================logo======================

         
         frame = Frame(self.root,bg="blue")  # inside mainframe+BORDER STYLE
         frame.place(x=int(self.width/2+200), y=0, width=int(self.width/2-100), height=self.height)

         
         img2 = Image.open(
            r"images\white.jpg")#x.jpg
        # (W,H) ,ANTIALIAS HIGH LEVEL TO LOW LEVEL IMAGE
         img2= img2.resize(
            (530+8,self.height-50), Image.ANTIALIAS)
         self.photoimg2 = ImageTk.PhotoImage(img2)  # set to a variable
    
        #to set it on window with label
        # lable inside root , with images help
         self.login_img = Label(self.root, image=self.photoimg2)
         self.login_img.place(x=int(self.width/2+200+17), y=10+4, width=530+8, height=self.height-50)

         img3 = Image.open(
            r"images\icon2.jpg")#x.jpg
        # (W,H) ,ANTIALIAS HIGH LEVEL TO LOW LEVEL IMAGE
         img3= img3.resize(
            (200,150), Image.ANTIALIAS)
         self.photoimg3 = ImageTk.PhotoImage(img3)  # set to a variable
    
        #to set it on window with label
        # lable inside root , with images help
         login_img2 = Label(self.login_img, image=self.photoimg3)
         login_img2.place(x=180, y=50, width=200, height=150)
         
         
         
         #=================================
         get_str = Label(self.login_img,text="Lets Get In ",font=("consolas",20,"bold"),fg="blue",bg="white")
         get_str.place(x=130, y=200-10, width=300, height=50)


       #===========================
         username_label = Label(self.login_img, text='Username :', font=(
           "consolas", 15, "bold"), bg="white")
         username_label.place(x=130, y=280)  # rows and col in grid

         self.username_entry = ttk.Entry(self.login_img, width=19, font=(
           "consolas", 15, "bold"))  # for entry field _ttk style
         self.username_entry.place(x=250, y=280)
         
         
         
         pass_label = Label(self.login_img, text='Password :', font=(
           "consolas", 15, "bold"), bg="white")
         pass_label.place(x=130, y=320)  # rows and col in grid

         self.pass_entry = ttk.Entry(self.login_img, width=19, font=(
           "consolas", 15, "bold"))  # for entry field _ttk style
         self.pass_entry.place(x=250, y=320)
         self.play_video()
         
         #===============================================login button
         
         login_button=Button(self.login_img,text="Login",command=self.login,font=("consolas",20,"bold"),bd=3,relief=RIDGE,fg="white",bg="blue",activeforeground="white",activebackground="blue")
         login_button.place(x=200,y=390,width=180,height=45)
         
         
         register_button=Button(self.login_img,text="Register",command=self.registration_page,font=("consolas",13,"bold"),bd=0,relief=RIDGE,fg="black",bg="white",activeforeground="black",activebackground="white")
         register_button.place(x=46,y=460,width=180,height=23)
         
         
         forgot_button=Button(self.login_img,text="Forgot Credentials ?",command=self.forgot_stuff,font=("consolas",13,"bold"),bd=0,relief=RIDGE,fg="black",bg="white",activeforeground="black",activebackground="white")
         forgot_button.place(x=100,y=490,width=180,height=23)
         
         
         
         
         
         
         
         
         
         
         
         
         
     def play_video(self):
        video_lable = Label(self.login_img, bg="white")
        player = tkvideo(r"images\username1.mp4", video_lable, loop=0, size=(50,50))
        video_lable.place(x=70, y=267, width=50,height=50)
        player.play()
        
        
        video_lable = Label(self.login_img, bg="white")
        player = tkvideo(r"images\pass.png", video_lable, loop=0, size=(50,50))
        video_lable.place(x=75, y=317, width=40,height=40)
        player.play()

     def login(self):
         if self.username_entry.get()=="" or self.pass_entry.get()=="":
             messagebox.showerror("Error","All Field Are Required") 
         else:
             
             #messagebox.showerror("Invalid","Invalid Username and Password Combination")
             connection = mysql.connector.connect(
                 host='localhost', username='root', password='password', database='facendance')
             cursor = connection.cursor()
             cursor.execute("select * from register where email=%s and password=%s",(
                 
                 
                 self.username_entry.get(),
                 self.pass_entry.get()              
                 ))
             row=cursor.fetchone()
             if row==None :
                 messagebox.showerror("Invalid","Invalid Username and Password Combination")
             else:
                 open_main=messagebox.askyesno("Admin","Only Admins Have Access , Are you one ?")
                 if open_main>0:
                     #messagebox.showinfo("Success","Yay ! , Welcome to Facendance {}".format(self.username_entry.get()))
                     self.princes_app()
                     
                 else:
                     if not open_main:
                         return
             connection.commit()
             connection.close()
     
    
     def princes_app(self):
         # to open a new window above the current pat one  toplevelis oused
         
         self.new_window = Toplevel(self.root)
         #to declre class
         self.app = Face_Recognition_System(self.new_window)
         #and then add command=student details in student button        
    
        
     def registration_page(self):
         # to open a new window above the current pat one  toplevelis oused
         self.new_window = Toplevel(self.root)
         #to declre class
         self.app = Register(self.new_window)
         #and then add command=student details in student button

     #==============================#============================reset=================
     
     def reset_password_checks(self):
         for widget in self.root2.winfo_children():
             widget.destroy()  
             
         forgot_stuff_label=Label(self.root2, text='Forgot Password', font=(
             "consolas", 20, "bold"), fg="blue",bg="white")
         forgot_stuff_label.place(x=0,y=0,relwidth=1)

         newpass_label = Label(self.root2, text='        New Password :', font=(
           "consolas", 15, "bold"), bg="white")
         newpass_label.place(x=20, y=80)  # rows and col in grid

         self.newpass_entry = ttk.Entry(self.root2, width=19, font=(
           "consolas", 15, "bold"))  # for entry field _ttk style
         self.newpass_entry.place(x=200+20+60, y=80,width=250)
         
         confnewpass_label = Label(self.root2, text='Confirm New Password :', font=(
           "consolas", 15, "bold"), bg="white")
         confnewpass_label.place(x=20, y=140)  # rows and col in grid

         self.confnewpass_entry = ttk.Entry(self.root2, width=19, font=(
           "consolas", 15, "bold"))  # for entry field _ttk style
         self.confnewpass_entry.place(x=200+20+60, y=140,width=250)
         def btn():
             if self.newpass_entry.get()=="" or self.confnewpass_entry.get()=="":
                 messagebox.showerror("Error","Please give the new password in both the fields",parent=self.root2)
             elif self.newpass_entry.get()!=self.confnewpass_entry.get():
                 messagebox.showerror("Error","New password and confirmed new password must be same",parent=self.root2)
             else:
                 connection = mysql.connector.connect(
                     host='localhost', username='root', password='password', database='facendance')
                 cursor = connection.cursor()
                 query=("update register set password=%s where email=%s ")
                        
                 value=(self.newpass_entry.get(),self.username_entry.get())
                 cursor.execute(query,value)
                 connection.commit()
                 connection.close()
                 messagebox.showinfo("Success","Password Successfully Changed")
                 
         reg_button=Button(self.root2,text=" Reset Password ",command=btn,font=("consolas",20,"bold"),bd=3,relief=RIDGE,fg="white",bg="blue",activeforeground="white",activebackground="blue")
         reg_button.place(x=160, y=200,width=300,height=45)
         
         
     
        
     
        
     def forgot_stuff_security(self):
         secname_label = Label(self.root2, text='Secret Phrase :', font=(
           "consolas", 15, "bold"), bg="white")
         secname_label.place(x=20, y=80) 
         self.phraname_combo = ttk.Combobox(self.root2, font=(
           "consolas", 15, "bold"), width=20, state="readonly")  # dropdownlist          #stylish in ttk
         self.phraname_combo["values"] = ("Select Secret Phrase ", "Your Secret ", "Your Pet's Name","Your Fac Ice Cream ","Your Birth Place ","Your First Ever Project ")
         # for indexing for "select deparment" to appear
         self.phraname_combo.current(0)
         self.phraname_combo.place(x=200+20, y=80,width=250)
         
         
         ansname_label = Label(self.root2, text='Answer :', font=(
           "consolas", 15, "bold"), bg="white")
         ansname_label.place(x=20+50+20+7, y=140)  # rows and col in grid

         self.ansname_entry = ttk.Entry(self.root2, width=19, font=(
           "consolas", 15, "bold"))  # for entry field _ttk style
         self.ansname_entry.place(x=200+20, y=140,width=250)
         
         def btn():
             if self.phraname_combo.get()=="Select" or self.ansname_entry.get()=="":
                 messagebox.showerror("Error","We need both Secret Phrase and Answer to it to proceed",parent=self.root2)
             else:
                 connection = mysql.connector.connect(
                     host='localhost', username='root', password='password', database='facendance')
                 cursor = connection.cursor()
                 query=("select * from register where email=%s and secret_phrase=%s and secret=%s")
                 value=(self.username_entry.get(),self.phraname_combo.get(),self.ansname_entry.get())
                 cursor.execute(query,value)
                 row=cursor.fetchone()
                 if row==None:
                     self.my_var=True
                     connection.commit()
                     connection.close()
                     messagebox.showerror("Error","The Secret Phrase and Answer to it to doesn't match , try again",parent=self.root2)
                     
                 else:
                     connection.commit()
                     connection.close()
                     self.reset_password_checks()
                     
         
         reg_button=Button(self.root2,text=" Dive In ",command=btn,font=("consolas",20,"bold"),bd=3,relief=RIDGE,fg="white",bg="blue",activeforeground="white",activebackground="blue")
         reg_button.place(x=200, y=200,width=180,height=45)
          
         
     def forgot_stuff(self):
         if self.username_entry.get()=="":
             messagebox.showerror("Error","Please Enter Email Address To Continue")
         else:
             connection = mysql.connector.connect(
                 host='localhost', username='root', password='password', database='facendance')
             cursor = connection.cursor()
             query=("select * from register where email=%s")
             value=(self.username_entry.get(),)
             cursor.execute(query,value)
             row=cursor.fetchone()
             if row==None :
                messagebox.showerror("Error","Email Not Registered , otherwise please correct it if alredy done so ")
             else:
                 connection.close()
                 self.root2=Toplevel()
                 self.root2.title("Forgot Password")
                 self.root2.geometry("600x300+670+170")
                 self.root2.configure(background="white")
                 forgot_stuff_label=Label(self.root2, text='Forgot Password', font=(
                     "consolas", 20, "bold"), fg="blue",bg="white")
                 forgot_stuff_label.place(x=0,y=0,relwidth=1)
                 
                 
                 
                 
                 #================================secret here===========================================
                 self.forgot_stuff_security()
                 
                 
                 








if __name__ == "__main__":  # to call main
    root = Tk()  # call root from toolkit
    obj = login_window(root)  # to connect with root
    root.mainloop()  # close mainloop
      