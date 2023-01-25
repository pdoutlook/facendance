# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 20:35:28 2022

@author: ERA
"""

from tkinter import*
from tkinter import ttk  # cool toolkit
from PIL import Image, ImageTk  # for images  , cropping and stuff
from tkinter import messagebox  # for eeror info or warning



class developer:
     def __init__(self,root):
         self.root=root
         self.width = root.winfo_screenwidth()
         self.height = root.winfo_screenheight()
         self.root.geometry(str(800)+"x"+str(600)+"+400+100")
         self.root.wm_iconbitmap("face.ico")
         self.root.title("developer")
         self.root.config(background="white")
         
         
         self.root.resizable(0,0)
         
         
         self.color="#9437fe"
         self.color2="white"
         
         
         img = Image.open(
             r"images\dev1.png")#x.jpg
         # (W,H) ,ANTIALIAS HIGH LEVEL TO LOW LEVEL IMAGE
         img = img.resize(
             (600 ,600), Image.ANTIALIAS)
         self.photo = ImageTk.PhotoImage(img)  # set to a variable

         #to set it on window with label
         # lable inside root , with images help
         bg_img = Label(self.root, image=self.photo)
         bg_img.place(x=0-100, y=0, width=600,
                      height=600)
         
         
         img2 = Image.open(
             r"images\logotrial1.jpg")#x.jpg
         # (W,H) ,ANTIALIAS HIGH LEVEL TO LOW LEVEL IMAGE
         img2 = img2.resize(
             (400 ,200), Image.ANTIALIAS)
         self.photo2 = ImageTk.PhotoImage(img2)  # set to a variable

         #to set it on window with label
         # lable inside root , with images help
         bg_img = Label(self.root, image=self.photo2)
         bg_img.place(x=400, y=100, width=400,
                      height=200)
         
         
         f_lbl = Label(self.root, bg="black")
         f_lbl.place(x=400-50-20-20-20-10,y=300+100-22-10, width=820-310, height=200-5)
         
         T = Text(self.root, height = 7, width = 47,bd=0, font=(
             "consolas", 14, "bold"),bg=self.color,fg=self.color2,padx=10,pady=10)#8c0bfc
 
                    # Create label
         
         
         help_ = """Developer : Prince Dwivedi                     Tech Used : ML and Python                      Information : This software is   developed by  Prince Dwivedi (0176CS191122 , LNCT-E) just to smoothen up the processes which involves       conventional techniques to mark presence of an individual in different settings. """
         
        # Create button for next text.
         
         T.pack()
              
         # Insert The Fact.
         #T.insert(self.root.END, help_)
         T.insert('end', help_)
         T.config(state='disabled')
         T.place(x=400-50-20-20-20, y=300+100-22)
         
         
         title_lbl = Label(self.root, text="Hi There Folks !", font=(
             "consolas", 19, "bold"), bg=self.color, fg=self.color2)  # label above img ,text #8c0bfc
         title_lbl.place(x=0, y=0, width=800,
                         height=35)





if __name__ == "__main__":  # to call main
    root = Tk()  # call root from toolkit
    obj = developer(root)  # to connect with root
    root.mainloop()  # close mainloop