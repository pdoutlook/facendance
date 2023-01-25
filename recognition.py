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
from time import strftime
from datetime import datetime


class Recognition:
    def __init__(self, root):  # constructor + windows name +root initialized
        self.root = root
        self.width = root.winfo_screenwidth()
        self.height = root.winfo_screenheight()


# windows geometry + x,y axis points like from where there the window will start
        self.root.geometry(str(self.width)+"x"+str(self.height)+"+0+0")
        self.root.wm_iconbitmap("face.ico")
        self.root.title("face recognition app")
        self.root.state('zoomed')
        self.root.resizable(0,0)
        ##a4adeb ,#ff8889

        title_lbl = Label(self.root, text="Recognition", font=(
            "consolas", 29, "bold"), bg="#a4adeb", fg="black")  # label above img ,text
        title_lbl.place(x=0, y=0, width=self.width,
                        height=55)  # can place any where
        root.configure(background='white')
        self.play_video()

        b1_1 = Button(self.root, text="Face Recognition", command=self.face_recognition, cursor="hand2", font=(
            "consolas", 18, "bold"), bg="black", fg="white", relief=RIDGE, activebackground="black")  # hand cursor + student details text
        b1_1.place(x=600, y=606, width=300, height=60)

    def play_video(self):
        video_lable = Label(self.root, bg="white")
        player = tkvideo(r"images\detection.gif", video_lable, loop=1, size=(700, 550))
        video_lable.place(x=410, y=55, width=700, height=550)
        player.play()

    #===============================================================================================

    def mark_attendance(self, student_id, r, n, d):
        with open(r"attendances\attendance.csv", "r+", newline="\n") as f:
            my_data = f.readlines()
            name_list = []
            for line in my_data:
                 entry = line.split((","))
                 name_list.append(entry[0])
            if ((student_id not in name_list)) and ((r not in name_list)) and ((n not in name_list)) and ((d not in name_list)):
                 now = datetime.now()
                 d1 = now.strftime("%d/%m/%Y")
                 dtString = now.strftime("%H:%M:%S")
                 f.writelines(
                     f"\n{student_id},{r},{n},{d},{dtString},{d1},Present")

    #========================================RECOGNITION   C:\Users\ERA\Documents\MINOR FACENDANCE\advanced_attendance_princedwivedi_0176cs191122

    def face_recognition(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbour, color,text,clf):
            grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(
                grey_img, scaleFactor, minNeighbour)
            coords = []
            for(x, y, w, h) in features:
                cv2.rectangle(img, (x, w), (x+w, y+h),(0,255,0),3)
                id_, predict = clf.predict(grey_img[y:y+h, x:x+w])
                #use confidence by  root(( hist1-hist2 )square)  low confidence is good
                confidence = int((100*(1-predict/300)))

                connection = mysql.connector.connect(
                    host='localhost', username='root', password='password', database='facendance')
                cursor = connection.cursor()
                cursor.execute(
                    "select Name from student where `Student Id`="+str(id_))
                n = cursor.fetchone()
                n = "+".join(n)

                cursor.execute(
                    "select `Roll No` from student where `Student Id`="+str(id_))
                r = cursor.fetchone()
                r = "+".join(r)

                cursor.execute(
                    "select Department from student where `Student Id`="+str(id_))
                d = cursor.fetchone()
                d = "+".join(d)

                cursor.execute(
                    "select `Student Id` from student where `Student Id`="+str(id_))
                student_id = cursor.fetchone()
                student_id = "+".join(student_id)

                if confidence >77:
                   cv2.putText(img, f"Id. :{student_id}", (x, y-85), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255),3)
                   cv2.putText(img, f"Roll No. :{r}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255),3)
                   cv2.putText(img, f"Name. :{n}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255),3)
                   cv2.putText(img, f"Department. :{d}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255),3)
                   self.mark_attendance(student_id, r, n, d)
                else:
                    cv2.rectangle(img, (x, w), (x+w, y+h),(0,0,255),3)
                    cv2.putText(img, "Unknown Face", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255),3)
                coords = [x, y, w, y]
            return coords

        def recognize(img, clf, faceCascade):
            coords = draw_boundary(img, faceCascade, 1.1, 10, (255,25,255),"Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier(
            "haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)
        while TRUE:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Recognizing", img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":  # to call main
    root = Tk()  # call root from toolkit
    obj = Recognition(root)  # to connect with root
    root.mainloop()  # close mainloop
