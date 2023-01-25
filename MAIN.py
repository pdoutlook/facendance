# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 20:05:12 2022

@author: ERA
"""

from tkinter import*
from tkinter import ttk  # cool toolkit
from PIL import Image, ImageTk  # for images  , cropping and stuff
import tkinter
from student import Student
from train import Train
from recognition import Recognition
from Attendance import attend
from developer import developer
from helper import helper
from datetime import datetime
from time import strftime

import os


class Face_Recognition_System:
    def __init__(self, root):  # constructor + windows name +root initialized
        self.root = root
        self.width = root.winfo_screenwidth()
        self.height = root.winfo_screenheight()

        # windows geometry + x,y axis points like from where there the window will start
        self.root.geometry(str(self.width)+"x"+str(self.height)+"+0+0")
        self.root.wm_iconbitmap("face.ico")
        self.root.state('zoomed')
        self.root.resizable(0,0)
        self.root.title("face recognition app")
        
        self.top_img_width = 512
        self.top_img_height = 143
        #images 1top
        img1 = Image.open(
            r"images\SET2.png")#black.jpg,q.png
        # (W,H) ,ANTIALIAS HIGH LEVEL TO LOW LEVEL IMAGE 406814709.jpg
        img1 = img1.resize(
            (self.top_img_width, self.top_img_height), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)  # set to a variable

        #to set it on window with label
        # lable inside root , with images help  406814709
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=self.top_img_width,
                    height=self.top_img_height)

        #images 2top#Mental-Health-847-image-775x270 ,Screenshot 2022-04-08 200013
        img2 = Image.open(
            r"images\SET12.png")#newone.jpg,logos82.png
        # (W,H) ,ANTIALIAS HIGH LEVEL TO LOW LEVEL IMAGE fr-1200.png
        img2 = img2.resize(
            (self.top_img_width, self.top_img_height), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)  # set to a variable

        #to set it on window with label
        # lable inside root , with images help
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=self.top_img_width, y=0,
                    width=self.top_img_width, height=self.top_img_height)

        #images 3top
        img3 = Image.open(
            r"images\SET3.png")#black,r.png
        # (W,H) ,ANTIALIAS HIGH LEVEL TO LOW LEVEL IMAGE Screenshot 2022-04-08 195804.jpg
        img3 = img3.resize(
            (self.top_img_width, self.top_img_height), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)  # set to a variable

        #to set it on window with label
        # lable inside root , with images help
        f_lbl = Label(self.root, image=self.photoimg3)
        f_lbl.place(x=self.top_img_width*2, y=0,
                    width=self.top_img_width, height=self.top_img_height)
        
        #background 4image
        img4 = Image.open(
            r"images\black.jpg")#x.jpg , b.png ,col4
        # (W,H) ,ANTIALIAS HIGH LEVEL TO LOW LEVEL IMAGE
        img4 = img4.resize(
            (self.width, self.height-self.top_img_height), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)  # set to a variable

        #to set it on window with label
        # lable inside root , with images help
        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=self.top_img_height, width=self.width,
                     height=self.height-self.top_img_height-5)
        self.color = "grey"
        self.color1="white"
        
        
        # extra for time 
        try:
            
            def time():
                string=strftime('%H:%M:%S %p')#current time  string
                self.time_label.config(text=string)#put sting in label
                self.time_label.after(1000,time)#after 1000 millisecond 
            self.time_label=Label(bg_img,font=(
                "consolas", 16, "bold"),background="black",foreground="white")
            self.time_label.place(x=1400-50,y=500+100+40,height=50)
            time()
        except Exception as es:
            pass
        
        
        
    
        #need label title ,
        title_lbl = Label(bg_img, text=" Hi There 👌 ",bd=5, font=(
            "consolas", 30, "bold"), bg=self.color, fg=self.color1)  # label above img ,text
        title_lbl.place(x=0-5, y=0-2, width=self.width+10,
                        height=45)  # can place any where  #ffd000

        #making image button

        

        #student button
        img5 = Image.open(
            r"images\student.jpg")
        # (W,H) ,ANTIALIAS HIGH LEVEL TO LOW LEVEL IMAGE
        img5 = img5.resize((220, 220), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)  # set to a variable

        #convert into button
        b1 = Button(bg_img, image=self.photoimg5,
                    command=self.student_details, cursor="hand2")  # hand cursor
        b1.place(x=200, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Student Details ", command=self.student_details, cursor="hand2", font=(
            "consolas", 16, "bold"), bg=self.color, fg=self.color1)  # hand cursor + student details text
        b1_1.place(x=200, y=300, width=220, height=40)

        #detect face button
        img6 = Image.open(
            r"images\DETECTOR.jpg")
        # (W,H) ,ANTIALIAS HIGH LEVEL TO LOW LEVEL IMAGE
        img6 = img6.resize((220, 220), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)  # set to a variable

        #convert into button
        b1 = Button(bg_img, image=self.photoimg6, command=self.detection_page,
                    cursor="hand2")  # hand cursor
        b1.place(x=500, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Detector", command=self.detection_page,cursor="hand2", font=(
            "consolas", 16, "bold"), bg=self.color, fg=self.color1)  # hand cursor + student details text
        b1_1.place(x=500, y=300, width=220, height=40)

        #attendance button
        img7 = Image.open(
            r"images\26308533.jpg")
        # (W,H) ,ANTIALIAS HIGH LEVEL TO LOW LEVEL IMAGE
        img7 = img7.resize((220, 220), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)  # set to a variable

        #convert into button
        b1 = Button(bg_img, image=self.photoimg7,command=self.attend_page,
                    cursor="hand2")  # hand cursor
        b1.place(x=800, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Attendance", cursor="hand2",command=self.attend_page, font=(
            "consolas", 16, "bold"), bg=self.color, fg=self.color1)  # hand cursor + student details text
        b1_1.place(x=800, y=300, width=220, height=40)

        #help button
        img8 = Image.open(
            r"images\image_processing20200302-32596-w6sd9f.png")
        # (W,H) ,ANTIALIAS HIGH LEVEL TO LOW LEVEL IMAGE
        img8 = img8.resize((220, 220), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)  # set to a variable

        #convert into button
        b1 = Button(bg_img, image=self.photoimg8,command=self.helper_page,
                    cursor="hand2")  # hand cursor
        b1.place(x=1100, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text=" Need Help ",command=self.helper_page, cursor="hand2", font=(
            "consolas", 16, "bold"), bg=self.color, fg=self.color1)  # hand cursor + student details text
        b1_1.place(x=1100, y=300, width=220, height=40)

        #trainer  button
        img9 = Image.open(
            r"images\BACK.jpg")
        # (W,H) ,ANTIALIAS HIGH LEVEL TO LOW LEVEL IMAGE
        img9 = img9.resize((220, 220), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)  # set to a variable

        #convert into button
        b1 = Button(bg_img, image=self.photoimg9,command=self.train_page,
                    cursor="hand2")  # hand cursor
        b1.place(x=200, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Trainer",command=self.train_page,cursor="hand2", font=(
            "consolas", 16, "bold"), bg=self.color, fg=self.color1)  # hand cursor + student details text   , command=self.train_page
        b1_1.place(x=200, y=580, width=220, height=40)

        #photos  button
        img10 = Image.open(
            r"images\yiyiyi.jpg")
        # (W,H) ,ANTIALIAS HIGH LEVEL TO LOW LEVEL IMAGE
        img10 = img10.resize((220, 220), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)  # set to a variable

        #convert into button
        b1 = Button(bg_img, image=self.photoimg10,
                    cursor="hand2", command=self.open_image)  # hand cursor
        b1.place(x=500, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Face n Photo", cursor="hand2", command=self.open_image, font=(
            "consolas", 16, "bold"), bg=self.color, fg=self.color1)  # hand cursor + student details text
        b1_1.place(x=500, y=580, width=220, height=40)

        #developer  button
        img11 = Image.open(
            r"images\a27d0482706813.5d25c65b77635.jpg")
        # (W,H) ,ANTIALIAS HIGH LEVEL TO LOW LEVEL IMAGE
        img11 = img11.resize((220, 220), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)  # set to a variable

        #convert into button
        b1 = Button(bg_img, image=self.photoimg11,command=self.developer_page,
                    cursor="hand2")  # hand cursor
        b1.place(x=800, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Developer",command=self.developer_page, cursor="hand2", font=(
            "consolas", 16, "bold"), bg=self.color, fg=self.color1)  # hand cursor + student details text
        b1_1.place(x=800, y=580, width=220, height=40)

        #exit  button
        img12 = Image.open(
            r"images\student3.jpg")
        # (W,H) ,ANTIALIAS HIGH LEVEL TO LOW LEVEL IMAGE
        img12 = img12.resize((220, 220), Image.ANTIALIAS)
        self.photoimg12 = ImageTk.PhotoImage(img12)  # set to a variable

        #convert into button
        b1 = Button(bg_img, image=self.photoimg12,command=self.exit_,
                    cursor="hand2")  # hand cursor
        b1.place(x=1100, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Exit",command=self.exit_, cursor="hand2", font=(
            "consolas", 16, "bold"), bg=self.color, fg=self.color1)  # hand cursor + student details text
        b1_1.place(x=1100, y=580, width=220, height=40)

    def open_image(self):  # for showing up images with the help of photo button
        os.startfile("data")

    # =================================functionbutton========================
    def student_details(self):
        # to open a new window above the current pat one  toplevelis oused
        self.new_window = Toplevel(self.root)
        #to declre class
        self.app = Student(self.new_window)
        #and then add command=student details in student button
        
    def train_page(self):
        # to open a new window above the current pat one  toplevelis oused
        self.new_window = Toplevel(self.root)
        #to declre class
        self.app = Train(self.new_window)
        #and then add command=student details in student button
    
    def detection_page(self):
        # to open a new window above the current pat one  toplevelis oused
        self.new_window = Toplevel(self.root)
        #to declre class
        self.app = Recognition(self.new_window)
        #and then add command=student details in student button
        
        
        
    def attend_page(self):
        # to open a new window above the current pat one  toplevelis oused
        self.new_window = Toplevel(self.root)
        #to declre class
        self.app = attend(self.new_window)
        #and then add command=student details in student button
        
    def developer_page(self):
        # to open a new window above the current pat one  toplevelis oused
        self.new_window = Toplevel(self.root)
        #to declre class
        self.app = developer(self.new_window)
        #and then add command=student details in student button
    
    def helper_page(self):
        # to open a new window above the current pat one  toplevelis oused
        self.new_window = Toplevel(self.root)
        #to declre class
        self.app = helper(self.new_window)
        #and then add command=student details in student button
    
    def exit_(self):
        self.exit_page=tkinter.messagebox.askyesno("Exit Box", "So you really wanna go ",parent=self.root)
        if self.exit_page>0:
            self.root.destroy()
        else:
            return
    
    


if __name__ == "__main__":  # to call main
    root = Tk()  # call root from toolkit
    obj = Face_Recognition_System(root)  # to connect with root
    root.mainloop()  # close mainloop
