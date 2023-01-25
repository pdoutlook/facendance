# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 22:47:03 2022

@author: ERA
"""


from tkinter import*
from tkinter import ttk  # cool toolkit
from PIL import Image, ImageTk  # for images  , cropping and stuff
from tkinter import messagebox  # for eeror info or warning



class helper:
     def __init__(self,root):
         self.root=root
         self.width = root.winfo_screenwidth()
         self.height = root.winfo_screenheight()
         self.root.geometry(str(800)+"x"+str(600)+"+400+100")
         self.root.wm_iconbitmap("face.ico")
         self.root.title("help")
         self.root.config(background="white")
         
         
         self.root.resizable(0,0)
         
         
         
         
         
         img = Image.open(
             r"images\help.jpg")#x.jpg
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
             r"images\newlogotrial.png")#x.jpg
         # (W,H) ,ANTIALIAS HIGH LEVEL TO LOW LEVEL IMAGE
         img2 = img2.resize(
             (400 ,200), Image.ANTIALIAS)
         self.photo2 = ImageTk.PhotoImage(img2)  # set to a variable

         #to set it on window with label
         # lable inside root , with images help
         bg_img = Label(self.root, image=self.photo2)
         bg_img.place(x=400, y=100+30, width=400,
                      height=200)
         
         
         T = Text(self.root, height = 2, width = 34,bd=0, font=(
             "consolas", 13, "bold"),bg="#32bfb9",padx=10,pady=10)
 
                    # Create label
         
         
         help_ = """Email Us : pd365000@outllook.com  Contact Us : 7440324634 """
         
        # Create button for next text.
         
         T.pack()
              
         # Insert The Fact.
         #T.insert(self.root.END, help_)
         T.insert('end', help_)
         T.config(state='disabled')
         T.place(x=400+50,y=230+100+100)
         
         
         title_lbl = Label(self.root, text="Got An Issue , Don't Worry We Are Here For You !", font=(
             "consolas", 19, "bold"), bg="#32bfb9", fg="black")  # label above img ,text
         title_lbl.place(x=0, y=0, width=800,
                         height=35)





if __name__ == "__main__":  # to call main
    root = Tk()  # call root from toolkit
    obj = helper(root)  # to connect with root
    root.mainloop()  # close mainloop