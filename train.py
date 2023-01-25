# -*- coding: utf-8 -*-



# -*- coding: utf-8 -*-

from tkinter import*
from tkinter import ttk  # cool toolkit
from PIL import Image, ImageTk  # for images  , cropping and stuff
from tkinter import messagebox  # for eeror info or warning
import mysql.connector
import cv2  # open source computer vision library more then 2000 algorithms classic and modern
from tkvideo import tkvideo
import os
import numpy as np


class Train:
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

        #need label title ,
        title_lbl = Label(self.root, text="Trainer", font=(
            "consolas", 29, "bold"), bg="#87cefa", fg="black")  # label above img ,text
        title_lbl.place(x=0, y=0, width=self.width,
                        height=45)  # can place any where

        img_top = Image.open(
            r"images\trainyourstuff.png")
        # (W,H) ,ANTIALIAS HIGH LEVEL TO LOW LEVEL IMAGE
        img_top = img_top.resize((1536, 325), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)  # set to a variable

        #to set it on window with label
        # lable inside left frame , with images help
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=47, width=1536, height=325)

        #========================video====================================#

        #=============================BUTTON====================================

        f_lbl = Label(self.root, bg="#87cefa")
        f_lbl.place(x=0, y=372, width=620, height=60)
        # for doing multiple command at once command=lambda:[funcA(), funcB(), funcC()] command=lambda:[self.play_video(),self.train_classifier()]
        b1_1 = Button(self.root, text="Train On Dataset", command=self.train_classifier, cursor="hand2", font=(
            "consolas", 18, "bold"), bg="Black", fg="white", relief=RIDGE, activebackground="red")  # hand cursor + student details text
        b1_1.place(x=620, y=372, width=300, height=60)

        f_lbl = Label(self.root, bg="#87cefa")
        f_lbl.place(x=920, y=372, width=619, height=60)

        #==========================================================================
        img_bottom = Image.open(
            r"images\neeche.jpg")
        # (W,H) ,ANTIALIAS HIGH LEVEL TO LOW LEVEL IMAGE
        img_bottom = img_bottom.resize((1536, 407+2), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(
            img_bottom)  # set to a variable

        #to set it on window with label
        # lable inside left frame , with images help
        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=432, width=1536, height=407+2)

       #========================video====================================#
        video_lable = Label(self.root, bg="black")
        player = tkvideo(r"images\nyavideo.gif", video_lable, loop=1, size=(450, 407+2))
        video_lable.place(x=540, y=432, width=450, height=407+2)
        player.play()

    # def play_video(self):
    #     video_lable=Label(self.root,bg="black")
    #     player = tkvideo("nyavideo.gif", video_lable, loop = 1, size = (450,407))
    #     video_lable.place(x=540,y=432,width=450,height=407)
    #     player.play()

    def train_classifier(self):  # now we have to train on dataset
        data_dir = ("data")
        path = [os.path.join(data_dir, file) for file in os.listdir(
            data_dir)]  # these gonna be the image set or data set
        faces = []
        ids = []
        for image in path:
            img = Image.open(image).convert('L')  # TO CONVERT INTO GRAYSCALE
            # NOW WANNA CONVERT INTO GRID X,Y WITH NUMPY
            imagenp = np.array(img, 'uint8')  # unit8 is datatype
            # the id part from the address
            id_ = int(os.path.split(image)[1].split('.')[1])

            faces.append(imagenp)
            ids.append(id_)
            cv2.imshow("Training", imagenp)  # window poop up
            cv2.waitKey(1) == 13  # pressing enter will close window
        ids = np.array(ids)  # converting to array  88% better performance
        #=====================================train ussing classifier==================================
        classifier = cv2.face.LBPHFaceRecognizer_create()
        classifier.train(faces, ids)
        classifier.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo(
            "Result", "Training On Dataset Complete", parent=self.root)


if __name__ == "__main__":  # to call main
    root = Tk()  # call root from toolkit
    obj = Train(root)  # to connect with root
    root.mainloop()  # close mainloop
