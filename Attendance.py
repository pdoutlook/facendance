# -*- coding: utf-8 -*-
from tkinter import*
from tkinter import ttk  # cool toolkit
from PIL import Image, ImageTk  # for images  , cropping and stuff
from tkinter import messagebox  # for eeror info or warning
import mysql.connector
import cv2  # open source computer vision library more then 2000 algorithms classic and modern
from tkvideo import tkvideo
import os 
import csv
from tkinter import filedialog


datas=[]
class attend:
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
        self.top_img_width = 512
        self.top_img_height = 265
    
        ##43B39B
        title_lbl = Label(self.root, text="Facendance Management ", font=(
            "consolas", 29, "bold"), bg="#43b39b", fg="black")  # label above img ,text
        title_lbl.place(x=0, y=self.top_img_height, width=self.width,
                        height=45)  # can place any where
        
        
        
        img4 = Image.open(
            r"images\white.jpg")
        # (W,H) ,ANTIALIAS HIGH LEVEL TO LOW LEVEL IMAGE
        img4 = img4.resize(
            (self.width, self.height-self.top_img_height), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)  # set to a variable

        #to set it on window with label
        # lable inside root , with images help
        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=self.top_img_height+45, width=self.width,
                      height=self.height-self.top_img_height-45)
        
        
        
        main_frame = Frame(bg_img, bg="#43b39b", bd=2)
        main_frame.place(x=15, y=15, width=1500, height=500)
        
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details", font=(
            "consolas", 13, "bold"))  # inside mainframe+BORDER STYLE
        left_frame.place(x=10, y=10, width=740, height=480)
        self.play_video()
        
        img_left = Image.open(r"images\attend10.png")
        # (W,H) ,ANTIALIAS HIGH LEVEL TO LOW LEVEL IMAGE
        img_left = img_left.resize((737, 150), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)  # set to a variable

        #to set it on window with label
        # lable inside left frame , with images help
        f_lbl = Label(left_frame, image=self.photoimg_left)
        f_lbl.place(x=0, y=0, width=737, height=150)
        
        left_sub_frame = Frame(left_frame, bg="white", bd=2,relief=RIDGE)
        left_sub_frame.place(x=8, y=150, width=720, height=300)
        
        
        #labels and entries
        
        #attendance id
        self.attendance_id=StringVar()
        attendance_id_label = Label(left_sub_frame, text='Attendance Id :', font=(
            "consolas", 13, "bold"), bg="white")
        attendance_id_label.grid(row=0, column=0, padx=10,pady=5,
                              sticky=W)  # rows and col in grid

        attendance_id_entry = ttk.Entry(left_sub_frame, textvariable=self.attendance_id, width=19, font=(
            "consolas", 13, "bold"))  # for entry field _ttk style
        attendance_id_entry.grid(row=0, column=1, padx=10,pady=5, sticky=W)
        
        #roll
        self.roll_id=StringVar()
        roll_id_label = Label(left_sub_frame, text='Roll No :', font=(
            "consolas", 13, "bold"), bg="white")
        roll_id_label.grid(row=0, column=2, padx=10,pady=5,
                              sticky=W)  # rows and col in grid

        roll_id_entry = ttk.Entry(left_sub_frame, textvariable=self.roll_id, width=19, font=(
            "consolas", 13, "bold"))  # for entry field _ttk style
        roll_id_entry.grid(row=0, column=3, padx=10,pady=5, sticky=W)
        
        
        
        
        
        #name
        self.name_id=StringVar()
        name_id_label = Label(left_sub_frame, text='Name :', font=(
            "consolas", 13, "bold"), bg="white")
        name_id_label.grid(row=1, column=0, padx=10,pady=5,
                              sticky=W)  # rows and col in grid

        name_id_entry = ttk.Entry(left_sub_frame, textvariable=self.name_id, width=19, font=(
            "consolas", 13, "bold"))  # for entry field _ttk style
        name_id_entry.grid(row=1, column=1,padx=10,pady=5, sticky=W)
        
        
        #department
        self.department_id=StringVar()
        department_id_label = Label(left_sub_frame, text='Department :', font=(
            "consolas", 13, "bold"), bg="white")
        department_id_label.grid(row=1, column=2, padx=10,pady=5,
                              sticky=W)  # rows and col in grid

        department_id_entry = ttk.Entry(left_sub_frame, textvariable=self.department_id, width=19, font=(
            "consolas", 13, "bold"))  # for entry field _ttk style
        department_id_entry.grid(row=1, column=3, padx=10,pady=5, sticky=W)
        
        
        # time
        self.time_id=StringVar()
        time_id_label = Label(left_sub_frame, text='Date :', font=(
            "consolas", 13, "bold"), bg="white")
        time_id_label.grid(row=2, column=0, padx=10,pady=5,
                              sticky=W)  # rows and col in grid

        time_id_entry = ttk.Entry(left_sub_frame, textvariable=self.time_id, width=19, font=(
            "consolas", 13, "bold"))  # for entry field _ttk style
        time_id_entry.grid(row=2, column=1, padx=10,pady=5, sticky=W)
        
        
        # date 
        self.date_id=StringVar()
        date_id_label = Label(left_sub_frame, text='Date :', font=(
            "consolas", 13, "bold"), bg="white")
        date_id_label.grid(row=2, column=2, padx=10,pady=5,
                              sticky=W)  # rows and col in grid

        date_id_entry = ttk.Entry(left_sub_frame, textvariable=self.date_id, width=19, font=(
            "consolas", 13, "bold"))  # for entry field _ttk style
        date_id_entry.grid(row=2, column=3, padx=10,pady=5, sticky=W)
        
        
        
        
        #attendance
        self.attendance_status=StringVar()
        attendance_status_label = Label(left_sub_frame, text='Attendance Status :', font=(
            "consolas", 13, "bold"), bg="white")
        attendance_status_label.grid(
            row=3, column=0, padx=10,pady=5, sticky=W)  # rows and col in grid

        # student_gender_entry = ttk.Entry(class_student_frame, textvariable=self.var_gender, width=19, font=(
        #     "consolas", 13, "bold"))  # for entry field _ttk style
        # student_gender_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)
        attendance_status_combo = ttk.Combobox(left_sub_frame, textvariable=self.attendance_status, font=(
            "consolas", 13, "bold"), width=17, state="readonly")  # dropdownlist          #stylish in ttk
        attendance_status_combo["values"] = ("Select Status ", "Present", "Absent")
        attendance_status_combo.current(0)
        attendance_status_combo.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        

          # #button frame

        btn_frame = Frame(left_sub_frame, bg="white", bd=2, relief=RIDGE)
        btn_frame.place(x=3, y=200, width=709, height=35)

        #save button
        save_btn = Button(btn_frame, text="Import csv",command=self.import_csv_file, width=19, font=(
            "consolas", 13, "bold"), bg="black", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Export csv",command=self.export_csv, width=18, font=(
            "consolas", 13, "bold"), bg="black", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Update", width=19, font=(
            "consolas", 13, "bold"), bg="black", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data, width=18, font=(
            "consolas", 13, "bold"), bg="black", fg="white")
        reset_btn.grid(row=0, column=3)

          # btn_frame1 = Frame(class_student_frame, bg="white", bd=2, relief=RIDGE)
          # btn_frame1.place(x=3, y=235, width=715, height=35)

          # sample_btn = Button(btn_frame1, text="Feed In Images", command=self.generate_dataset, width=38, font=(
          #     "consolas", 13, "bold"), bg="black", fg="white")
          # sample_btn.grid(row=0, column=0)

          # update_btn = Button(btn_frame1, text="Update Images", width=39, font=(
          #     "consolas", 13, "bold"), bg="black", fg="white")
          # update_btn.grid(row=0, column=1)
          
          
          
          
          
          
          
          
          
          
          
          
          



        
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details", font=(
            "consolas", 13, "bold"))  # inside mainframe+BORDER STYLE
        right_frame.place(x=760, y=10, width=727, height=480)
        
        
        # inside mainframe+BORDER STYLE
        table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=6, y=5, width=711, height=446)
        
        
        
        #=================================================scroll bar table===============================
        #scroll baar
        self.cols=["Attendance Id","Roll No.","Name","Department","Time","Date","Attendance Status"]
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.attendance_table = ttk.Treeview(
            table_frame, column=self.cols, xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.attendance_table.xview)
        scroll_y.config(command=self.attendance_table.yview)
        
        
        for i in self.cols:
            self.attendance_table.heading(i,text=i)
            self.attendance_table.column(i, width=80)
            
            
        self.attendance_table["show"] = "headings"
        self.attendance_table.pack(fill=BOTH,expand=1)
        self.attendance_table.bind(
            "<ButtonRelease>", self.get_cursor)  # binding button
        self.fetch_data(datas)
        
        #===================================fetch data=================================
    def fetch_data(self,rows):
        #first delete the childrens from the table then take data from csv file and put it in the table 
        self.attendance_table.delete(*self.attendance_table.get_children())
        for i in rows:
            self.attendance_table.insert("",END,values=i)
            
            
         #===================================import csv=================================   
    def import_csv_file(self):
        global datas
        datas.clear()
        file_name=filedialog.askopenfilename(initialdir=os.getcwd(),title="open csv",filetypes=(("CSV File","*csv"),("ALl File","*.*")),parent=self.root)
        with open(file_name) as my_file:
            csvread=csv.reader(my_file, delimiter=",")
            for i in csvread:
                datas.append(i)
            self.fetch_data(datas)
                
        #===================================export data=================================
    def export_csv(self):
        #first chech whether the table has any data or not 
        try:
            if len(datas)<1:
                messagebox.showerror("Empty Dataset ","Nothing found to export",parent=self.root)
                return FALSE
            file_name=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="open csv",filetypes=(("CSV File","*csv"),("ALl File","*.*")),parent=self.root)
            with open(file_name,mode="w",newline="") as my_file:
                csvwrite=csv.writer(my_file,delimiter=",")
                for i in datas:
                    csvwrite.writerow(i)
                messagebox.showinfo("Export ","Data Successfully Exported To "+os.path.basename(file_name))
        except Exception as es:
           messagebox.showerror(
               "Error", f"Due To : {str(es)}", parent=self.root)
        
    
    def get_cursor(self, event=""):
       cursor_focus = self.attendance_table.focus()  # cursor focussed on student table
       content = self.attendance_table.item(
           cursor_focus)  # taking content with item
       try:
           
           data = content["values"]  # values of the content
    
           self.attendance_id.set(data[0])
           self.roll_id.set(data[1])
           self.name_id.set(data[2])
           self.department_id.set(data[3])
           self.time_id.set(data[4])
           self.date_id.set(data[5])
           self.attendance_status.set(data[6])
           
           # now we have to bind get cursor with table
       except Exception as exception:
              pass
          
    def reset_data(self):
        self.attendance_id.set("")
        self.roll_id.set("")
        self.name_id.set("")
        self.department_id.set("")
        self.time_id.set("")
        self.date_id.set("")
        self.attendance_status.set("Select Status")
    
    def play_video(self):
        video_lable = Label(self.root, bg="white")
        player = tkvideo(r"images\a2.gif", video_lable, loop=1, size=(self.top_img_width, self.top_img_height))
        video_lable.place(x=0, y=0, width=self.top_img_width,height=self.top_img_height)
        player.play()
        
        
        
        video_lable = Label(self.root, bg="white")
        player = tkvideo(r"images\a3.gif", video_lable, loop=1, size=(self.top_img_width, self.top_img_height))
        video_lable.place(x=self.top_img_width, y=0,width=self.top_img_width, height=self.top_img_height)
        player.play()
        
        video_lable = Label(self.root, bg="white")
        player = tkvideo(r"images\a1.gif", video_lable, loop=1, size=(self.top_img_width, self.top_img_height))
        video_lable.place(x=self.top_img_width*2, y=0,width=self.top_img_width, height=self.top_img_height)
        player.play()
        
        # video_lable = Label(self.left_frame, bg="white")
        # player = tkvideo(r"images\attend11.png", video_lable, loop=1, size=(740, 200))
        # video_lable.place(x=0, y=0, width=740, height=200)
        # player.play()
        
        
        
        
        
        
        # img1 = Image.open(
        #     r"images\managep.jpg")
        # # (W,H) ,ANTIALIAS HIGH LEVEL TO LOW LEVEL IMAGE
        # img1 = img1.resize(
        #     (self.top_img_width, self.top_img_height), Image.ANTIALIAS)
        # self.photoimg1 = ImageTk.PhotoImage(img1)  # set to a variable

        # #to set it on window with label
        # # lable inside root , with images help  406814709
        # f_lbl = Label(self.root, image=self.photoimg1)
        # f_lbl.place(x=0, y=0, width=self.top_img_width,
        #             height=self.top_img_height)

        # #images 2top#Mental-Health-847-image-775x270 ,Screenshot 2022-04-08 200013
        # img2 = Image.open(
        #     r"images\manageg.jpg")
        # # (W,H) ,ANTIALIAS HIGH LEVEL TO LOW LEVEL IMAGE
        # img2 = img2.resize(
        #     (self.top_img_width, self.top_img_height), Image.ANTIALIAS)
        # self.photoimg2 = ImageTk.PhotoImage(img2)  # set to a variable

        # #to set it on window with label
        # # lable inside root , with images help
        # f_lbl = Label(self.root, image=self.photoimg2)
        # f_lbl.place(x=self.top_img_width, y=0,
        #             width=self.top_img_width, height=self.top_img_height)

        # #images 3top
        # img3 = Image.open(
        #     r"images\manager.jpg")
        # # (W,H) ,ANTIALIAS HIGH LEVEL TO LOW LEVEL IMAGE
        # img3 = img3.resize(
        #     (self.top_img_width, self.top_img_height), Image.ANTIALIAS)
        # self.photoimg3 = ImageTk.PhotoImage(img3)  # set to a variable


        # #to set it on window with label
        # # lable inside root , with images help
        # f_lbl = Label(self.root, image=self.photoimg3)
        # f_lbl.place(x=self.top_img_width*2, y=0,
        #             width=self.top_img_width, height=self.top_img_height)


        













if __name__ == "__main__":  # to call main
    root = Tk()  # call root from toolkit
    obj = attend(root)  # to connect with root
    root.mainloop()  # close mainloop
