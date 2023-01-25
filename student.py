# -*- coding: utf-8 -*-

from tkinter import*
from tkinter import ttk  # cool toolkit
from PIL import Image, ImageTk  # for images  , cropping and stuff
from tkinter import messagebox  # for eeror info or warning
import mysql.connector
import cv2  # open source computer vision library more then 2000 algorithms classic and modern


class Student:
    def __init__(self, root):  # constructor + windows name +root initialized
        self.root = root
        self.width = root.winfo_screenwidth()
        self.height = root.winfo_screenheight()
        #===========variables============================
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_studentid = StringVar()
        self.var_studentname = StringVar()
        self.var_section = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

        #==========........====================== #

        # windows geometry + x,y axis points like from where there the window will start
        self.root.geometry(str(self.width)+"x"+str(self.height)+"+0+0")
        self.root.wm_iconbitmap("face.ico")
        self.root.title("face recognition app")
        self.root.state('zoomed')
        self.root.resizable(0,0)

        self.top_img_width = 512
        self.top_img_height = 142
        #images 1top
        img1 = Image.open(
            r"images\managep.jpg")
        # (W,H) ,ANTIALIAS HIGH LEVEL TO LOW LEVEL IMAGE
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
            r"images\manageg.jpg")
        # (W,H) ,ANTIALIAS HIGH LEVEL TO LOW LEVEL IMAGE
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
            r"images\manager.jpg")
        # (W,H) ,ANTIALIAS HIGH LEVEL TO LOW LEVEL IMAGE
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
            r"images\back3.jpg")
        # (W,H) ,ANTIALIAS HIGH LEVEL TO LOW LEVEL IMAGE
        img4 = img4.resize(
            (self.width, self.height-self.top_img_height), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)  # set to a variable

        #to set it on window with label
        # lable inside root , with images help
        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=self.top_img_height, width=self.width,
                     height=self.height-self.top_img_height)

        #need label title ,
        title_lbl = Label(bg_img, text="Student Record Management ", font=(
            "consolas", 29, "bold"), bg="#87cefa", fg="#030201")  # label above img ,text
        title_lbl.place(x=0, y=0, width=self.width,
                        height=45)  # can place any where

        #making the main frame optional color=#3bffe5 #f95700
        # above background image
        main_frame = Frame(bg_img, bg="#87cefa", bd=2)
        main_frame.place(x=15, y=65, width=1500, height=615)

        #left label frame

        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=(
            "consolas", 13, "bold"))  # inside mainframe+BORDER STYLE
        left_frame.place(x=10, y=10, width=740, height=590)

        #sub_left

        #images 2top#Mental-Health-847-image-775x270 ,Screenshot 2022-04-08 200013
        img_left = Image.open(
            r"images\editclip.jpg")
        # (W,H) ,ANTIALIAS HIGH LEVEL TO LOW LEVEL IMAGE
        img_left = img_left.resize((735, 130), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)  # set to a variable

        #to set it on window with label
        # lable inside left frame , with images help
        f_lbl = Label(left_frame, image=self.photoimg_left)
        f_lbl.place(x=0, y=0, width=735, height=130)

        #left label frame "current course"  + combo box usage

        current_course_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course Information ", font=(
            "consolas", 13, "bold"))  # inside mainframe+BORDER STYLE
        current_course_frame.place(x=5, y=135, width=727, height=125)

        # department
        dept_label = Label(current_course_frame, text='Department', font=(
            "consolas", 13, "bold"), bg="white")
        dept_label.grid(row=0, column=0, padx=10,
                        sticky=W)  # rows and col in grid

        dept_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=(
            "consolas", 13, "bold"), width=20, state="readonly")  # dropdownlist          #stylish in ttk
        dept_combo["values"] = ("Select Department ", "Computer Science",
                                "Information Technology", "Mechanical", "Civil", "Electrical")
        dept_combo.current(0)  # for indexing for "select deparment" to appear
        dept_combo.grid(row=0, column=1, padx=2, pady=10,
                        sticky=W)  # aage hoga +padding

        # course
        course_label = Label(current_course_frame, text='Course', font=(
            "consolas", 13, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10,
                          sticky=W)  # rows and col in grid

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=(
            "consolas", 13, "bold"), width=20, state="readonly")  # dropdownlist          #stylish in ttk
        course_combo["values"] = ("Select Course ", "Machine Learning", "Computer Networks",
                                  "Compiler Design", "Data Analytics Lab", "Skill Development Lab")
        # for indexing for "select deparment" to appear
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10,
                          sticky=W)  # aage hoga +padding

        # year
        year_label = Label(current_course_frame, text='Year',
                           font=("consolas", 13, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10,
                        sticky=W)  # rows and col in grid

        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=(
            "consolas", 13, "bold"), width=20, state="readonly")  # dropdownlist          #stylish in ttk
        year_combo["values"] = ("Select Year ", "2020-21",
                                "2021-22", "2022-23", "2023-24")
        year_combo.current(0)  # for indexing for "select deparment" to appear
        year_combo.grid(row=1, column=1, padx=2, pady=10,
                        sticky=W)  # aage hoga +padding

        # semester
        semester_label = Label(current_course_frame, text='Semester', font=(
            "consolas", 13, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10,
                            sticky=W)  # rows and col in grid

        semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_sem, font=(
            "consolas", 13, "bold"), width=20, state="readonly")  # dropdownlist          #stylish in ttk
        semester_combo["values"] = ("Select Semester ", "Spring", "Fall")
        # for indexing for "select deparment" to appear
        semester_combo.current(0)
        # aage hoga +padding +if cell is greater than widget
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        #left label frame "class student information"  + combo box usage

        class_student_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information ", font=(
            "consolas", 13, "bold"))  # below course frame+BORDER STYLE
        class_student_frame.place(x=5, y=260, width=725, height=300)

        #student id
        student_id_label = Label(class_student_frame, text='Student Id :', font=(
            "consolas", 13, "bold"), bg="white")
        student_id_label.grid(row=0, column=0, padx=10,
                              sticky=W)  # rows and col in grid

        student_id_entry = ttk.Entry(class_student_frame, textvariable=self.var_studentid, width=19, font=(
            "consolas", 13, "bold"))  # for entry field _ttk style
        student_id_entry.grid(row=0, column=1, padx=10, sticky=W)

        #student name
        student_name_label = Label(class_student_frame, text='Student Name :', font=(
            "consolas", 13, "bold"), bg="white")
        student_name_label.grid(row=0, column=2, padx=10,
                                sticky=W)  # rows and col in grid

        student_name_entry = ttk.Entry(class_student_frame, textvariable=self.var_studentname, width=19, font=(
            "consolas", 13, "bold"))  # for entry field _ttk style
        student_name_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        #student section
        student_section_label = Label(class_student_frame, text='Student Section :', font=(
            "consolas", 13, "bold"), bg="white")
        student_section_label.grid(
            row=1, column=0, padx=10, sticky=W)  # rows and col in grid

        # student_section_entry = ttk.Entry(class_student_frame, textvariable=self.var_section, width=19, font=(
        #     "consolas", 13, "bold"))  # for entry field _ttk style
        # student_section_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)
        student_section_combo = ttk.Combobox(class_student_frame, textvariable=self.var_section, font=(
            "consolas", 13, "bold"), width=17, state="readonly")  # dropdownlist          #stylish in ttk
        student_section_combo["values"] = ("Select Section ", "A", "B", "C")
        student_section_combo.current(0)
        student_section_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        #student roll no
        student_roll_label = Label(class_student_frame, text='Roll Number :', font=(
            "consolas", 13, "bold"), bg="white")
        student_roll_label.grid(row=1, column=2, padx=10,
                                sticky=W)  # rows and col in grid

        student_roll_entry = ttk.Entry(class_student_frame, textvariable=self.var_roll, width=19, font=(
            "consolas", 13, "bold"))  # for entry field _ttk style
        student_roll_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        #student gender
        student_gender_label = Label(class_student_frame, text='Gender :', font=(
            "consolas", 13, "bold"), bg="white")
        student_gender_label.grid(
            row=2, column=0, padx=10, sticky=W)  # rows and col in grid

        # student_gender_entry = ttk.Entry(class_student_frame, textvariable=self.var_gender, width=19, font=(
        #     "consolas", 13, "bold"))  # for entry field _ttk style
        # student_gender_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)
        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=(
            "consolas", 13, "bold"), width=17, state="readonly")  # dropdownlist          #stylish in ttk
        gender_combo["values"] = ("Select Gender ", "Female", "Male", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        #student dob
        student_dob_label = Label(class_student_frame, text='DoB :', font=(
            "consolas", 13, "bold"), bg="white")
        student_dob_label.grid(row=2, column=2, padx=10,
                               sticky=W)  # rows and col in grid

        student_dob_entry = ttk.Entry(class_student_frame, textvariable=self.var_dob, width=19, font=(
            "consolas", 13, "bold"))  # for entry field _ttk style
        student_dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        #student email
        student_email_label = Label(class_student_frame, text='Email Id :', font=(
            "consolas", 13, "bold"), bg="white")
        # rows and col in grid
        student_email_label.grid(row=3, column=0, padx=10, sticky=W)

        student_email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, width=19, font=(
            "consolas", 13, "bold"))  # for entry field _ttk style
        student_email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        #student phone
        student_phone_label = Label(class_student_frame, text='Phone Number :', font=(
            "consolas", 13, "bold"), bg="white")
        # rows and col in grid
        student_phone_label.grid(row=3, column=2, padx=10, sticky=W)

        student_phone_entry = ttk.Entry(class_student_frame, textvariable=self.var_phone, width=19, font=(
            "consolas", 13, "bold"))  # for entry field _ttk style
        student_phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        #student address
        student_address_label = Label(class_student_frame, text='Address :', font=(
            "consolas", 13, "bold"), bg="white")
        student_address_label.grid(
            row=4, column=0, padx=10, sticky=W)  # rows and col in grid

        student_address_entry = ttk.Entry(class_student_frame, textvariable=self.var_address, width=19, font=(
            "consolas", 13, "bold"))  # for entry field _ttk style
        student_address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        #student teacher
        student_teacher_label = Label(class_student_frame, text='Teacher :', font=(
            "consolas", 13, "bold"), bg="white")
        student_teacher_label.grid(
            row=4, column=2, padx=10, sticky=W)  # rows and col in grid

        student_teacher_entry = ttk.Entry(class_student_frame, textvariable=self.var_teacher, width=19, font=(
            "consolas", 13, "bold"))  # for entry field _ttk style
        student_teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        #radio button xchoice

        self.var_radio1 = StringVar()
        rad_btn = ttk.Radiobutton(class_student_frame, variable=self.var_radio1,
                                  text="Wanna Take Photo Sample ", value="Yes")  # select only one not both
        rad_btn.grid(row=6, column=0)

        rad_btn1 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1,
                                   text="Don't Wanna Take Photo Sample ", value="No")
        rad_btn1.grid(row=6, column=1)

        #button frame

        btn_frame = Frame(class_student_frame, bg="white", bd=2, relief=RIDGE)
        btn_frame.place(x=3, y=200, width=715, height=35)

        #save button
        save_btn = Button(btn_frame, text="Save", command=self.add_data, width=19, font=(
            "consolas", 13, "bold"), bg="black", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Update", command=self.update_data, width=18, font=(
            "consolas", 13, "bold"), bg="black", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, width=19, font=(
            "consolas", 13, "bold"), bg="black", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=19, font=(
            "consolas", 13, "bold"), bg="black", fg="white")
        reset_btn.grid(row=0, column=3)

        btn_frame1 = Frame(class_student_frame, bg="white", bd=2, relief=RIDGE)
        btn_frame1.place(x=3, y=235, width=715, height=35)

        sample_btn = Button(btn_frame1, text="Feed In Images", command=self.generate_dataset, width=38, font=(
            "consolas", 13, "bold"), bg="black", fg="white")
        sample_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame1, text="Update Images", width=39, font=(
            "consolas", 13, "bold"), bg="black", fg="white")
        update_btn.grid(row=0, column=1)

        #right label frame

        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=(
            "consolas", 13, "bold"))  # inside mainframe+BORDER STYLE
        right_frame.place(x=760, y=10, width=727, height=590)

        #images 2top#Mental-Health-847-image-775x270 ,Screenshot 2022-04-08 200013
        img_right = Image.open(
            r"images\art.jpg")
        # (W,H) ,ANTIALIAS HIGH LEVEL TO LOW LEVEL IMAGE
        img_right = img_right.resize((735, 130), Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(
            img_right)  # set to a variable

        #to set it on window with label
        # lable inside left frame , with images help
        f_lbl = Label(right_frame, image=self.photoimg_right)
        f_lbl.place(x=0, y=0, width=710, height=130)

        #search frame for searching system and table to see data fetch by database

        search_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE, text="Search System ", font=(
            "consolas", 13, "bold"))  # inside mainframe+BORDER STYLE
        search_frame.place(x=5, y=135, width=715, height=70)

        search_label = Label(search_frame, text='Search By :', font=(
            "consolas", 13, "bold"), bg="#87cefa", fg="black")
        search_label.grid(row=0, column=0, padx=10,
                          sticky=W)  # rows and col in grid

        self.cols = ("Department", "Year", "Id", "Name", "Course", "Semester", "Roll Number",
                     "Gender", "Dob", "Email", "Address", "Teacher", "Phone", "Section", "Photo")

        search_combo = ttk.Combobox(search_frame, font=(
            "consolas", 13, "bold"), width=20, state="readonly")  # dropdownlist          #stylish in ttk
        search_combo["values"] = tuple(["Select"]+list(self.cols))
        # for indexing for "select deparment" to appear
        search_combo.current(0)
        # aage hoga +padding +if cell is greater than widget
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = ttk.Entry(search_frame, width=15, font=(
            "consolas", 13, "bold"))  # for entry field _ttk style
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(search_frame, text="Search", width=10, font=(
            "consolas", 12, "bold"), bg="black", fg="white")
        search_btn.grid(row=0, column=3, padx=4)

        show_all_btn = Button(search_frame, text="Show All", width=10, font=(
            "consolas", 12, "bold"), bg="black", fg="white")
        show_all_btn.grid(row=0, column=4, padx=4)

        #table frame

        # inside mainframe+BORDER STYLE
        table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=210, width=715, height=350)

        #scroll baar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(
            table_frame, column=self.cols, xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        for i in self.cols:
            self.student_table.heading(i, text=i)
            self.student_table.column(i, width=100)

        self.student_table["show"] = "headings"
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind(
            "<ButtonRelease>", self.get_cursor)  # binding button
        self.fetch_data()

    def add_data(self):  # if no data , we are using validation  # do it for all the fields you wanna deinately take infut for
        if self.var_dep.get() == "Select Department" or self.var_studentname.get() == "" or self.var_studentid.get() == "":
            # parent for being in same window
            messagebox.showerror(
                "Error", "All Feilds Are Required", parent=self.root)
        else:
            try:                                               # HERE WE WILL SAVING DATA IN DATABASE
               # SO WHAT WE WILL DO IS CREATE DATABAS EAND A  TABLE TO STORE THE VALUES IN THAT
                connection = mysql.connector.connect(
                    host='localhost', username='root', password='password', database='facendance')
                cursor = connection.cursor()
                cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (


                    self.var_dep.get(),
                    self.var_year.get(),
                    self.var_studentid.get(),
                    self.var_studentname.get(),
                    self.var_course.get(),
                    self.var_sem.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_phone.get(),
                    self.var_section.get(),
                    self.var_radio1.get()
                ))
                # we have to call this function in button
                connection.commit()
                self.fetch_data()
                connection.close()
                messagebox.showinfo(
                    "Success", "Succesfull Operation", parent=self.root)  # cobo box issue
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To : {str(es)}", parent=self.root)

    def fetch_data(self):  # to fetch and show in our table , that delete function inside loop is for no repetition of data entres when we do it second time
        connection = mysql.connector.connect(
            host='localhost', username='root', password='password', database='facendance')
        cursor = connection.cursor()
        cursor.execute("select * from student")
        data = cursor.fetchall()
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            connection.commit()
        connection.close()
# addind here the functionality o tapping and retrieval on the form by just cliccking on a particular row

    def get_cursor(self, event=""):
       cursor_focus = self.student_table.focus()  # cursor focussed on student table
       content = self.student_table.item(
           cursor_focus)  # taking content with item
       try:
           
           data = content["values"]  # values of the content
    
           self.var_dep.set(data[0])
           self.var_year.set(data[1])
           self.var_studentid.set(data[2])
           self.var_studentname.set(data[3])
           self.var_course.set(data[4])
           self.var_sem.set(data[5])
           self.var_roll.set(data[6])
           self.var_gender.set(data[7])
           self.var_dob.set(data[8])
           self.var_email.set(data[9])
           self.var_address.set(data[10])
           self.var_teacher.set(data[11])
           self.var_phone.set(data[12])
           self.var_section.set(data[13])
           # now we have to bind get cursor with table
           self.var_radio1.set(data[14])
       except Exception as exception:
              pass
            

    #its time to update stuff
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_studentname.get() == "" or self.var_studentid.get() == "":
            # parent for being in same window
            messagebox.showerror(
                "Error", "All Feilds Are Required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno(
                    "Update", "Do you want to update details", parent=self.root)
                if Update > 0:
                    connection = mysql.connector.connect(
                        host='localhost', username='root', password='password', database='facendance')
                    cursor = connection.cursor()
                    cursor.execute("update student set Department=%s, Year=%s, Name=%s, Course=%s, Semester=%s,`Roll No`=%s,Gender=%s, DoB=%s, Email=%s, Address=%s, Teacher=%s, Phone=%s, Section=%s,`Photo Sample`=%s where `Student Id`=%s",
                                   (self.var_dep.get(),
                                    self.var_year.get(),
                                    self.var_studentname.get(),
                                    self.var_course.get(),
                                    self.var_sem.get(),
                                    self.var_roll.get(),
                                    self.var_gender.get(),
                                    self.var_dob.get(),
                                    self.var_email.get(),
                                    self.var_address.get(),
                                    self.var_teacher.get(),
                                    self.var_phone.get(),
                                    self.var_section.get(),
                                    self.var_radio1.get(),
                                    self.var_studentid.get()
                                    ))
                else:
                   if not Update:  # if no was there then the page will stay as it is
                       return
                messagebox.showinfo(
                    "Sucess", "Student details successfully updated ", parent=self.root)
                connection.commit()
                self.fetch_data()
                connection.close()
            except Exception as es:
                messagebox.showerror(
                    "Error ", f"Due to : {str(es)}", parent=self.root)

    def delete_data(self):
        if self.var_studentid.get() == "":
            messagebox.showerror(
                "Error", "Student Id is required for this operation ", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno(
                    "Delete Student Data", "Really Wanna delete it ", parent=self.root)
                if delete > 0:
                    connection = mysql.connector.connect(
                        host='localhost', username='root', password='password', database='facendance')
                    cursor = connection.cursor()
                    sql = "delete from student where `Student Id`=%s"
                    value = (self.var_studentid.get(),)
                    cursor.execute(sql, value)
                else:
                    if not delete:
                        return
                connection.commit()
                self.fetch_data()
                connection.close()
                messagebox.showinfo(
                    "Delete", "Successfully deleted student details", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Error ", f"Due to : {str(es)}", parent=self.root)

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_year.set("Select Year")
        self.var_studentid.set("")
        self.var_studentname.set("")
        self.var_course.set("Select Course")
        self.var_sem.set("Select Semester")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_phone.set("")
        self.var_section.set("Select Section")
        self.var_radio1.set("")
   # generating dataset and taking in sampples
   #the images that we wil take , we will not be inserting rather we will be matching with databases data
   #so we will be updating not inserting other wise we will get error stating already existing key
   #so we will be updating dataset to match the input with the ones already existing in database

    def generate_dataset(self):
         if self.var_dep.get() == "Select Department" or self.var_studentname.get() == "" or self.var_studentid.get() == "":
              # parent for being in same window
              messagebox.showerror(
                   "Error", "All Feilds Are Required", parent=self.root)
         else:
              try:
                     connection = mysql.connector.connect(
                          host='localhost', username='root', password='password', database='facendance')
                     cursor = connection.cursor()
                     cursor.execute("select * from student")
                     result = cursor.fetchall()
                     id = 0
                     for x in result:
                         id += 1
                     cursor.execute("update student set Department=%s, Year=%s, Name=%s, Course=%s, Semester=%s,`Roll No`=%s,Gender=%s, DoB=%s, Email=%s, Address=%s, Teacher=%s, Phone=%s, Section=%s,`Photo Sample`=%s where `Student Id`=%s",
                                     (self.var_dep.get(),
                                       self.var_year.get(),
                                       self.var_studentname.get(),
                                       self.var_course.get(),
                                       self.var_sem.get(),
                                       self.var_roll.get(),
                                       self.var_gender.get(),
                                       self.var_dob.get(),
                                       self.var_email.get(),
                                       self.var_address.get(),
                                       self.var_teacher.get(),
                                       self.var_phone.get(),
                                       self.var_section.get(),
                                       self.var_radio1.get(),
                                       self.var_studentid.get() == id+1
                                       ))
                     connection.commit()
                     self.fetch_data()
                     self.reset_data()
                     connection.close()
                      #==================har cascade ========================== face recognition ALGORITHM  ,BY
                      #========================== LOADING IN THE haarcascade_frontalface_default XML FILE from opencv
                     face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")#for object detecton

                     def face_cropped(img):
                          #first we have to convert bgr to grey
                          gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#converted to greyscale
                          faces = face_classifier.detectMultiScale(gray, 1.3,5)#scaling factor =1.3, minimum neighbour =5
                          for (x, y, w,h) in faces:
                              face_cropped = img[y:y+h, x:x+w]
                              return face_cropped
                     cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
                     img_id = 0
                     while TRUE:
                           ret, someframe = cap.read()
                           if face_cropped(someframe) is not None:
                               img_id += 1
                               face = cv2.resize(face_cropped(someframe), (450,450))
                               face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                               file_name_path = "data/user."+ \
                                   str(id)+"."+str(img_id)+".jpg"
                               cv2.imwrite(file_name_path, face)
                               cv2.putText(face, str(img_id),(50, 50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                               cv2.imshow("Cropped Face", face)

                           if cv2.waitKey(1) == 13 or int(img_id)==500:
                               break
                     cap.release()
                     cv2.destroyAllWindows()
                     messagebox.showinfo("Result", "Data Set GEneration Complete", parent=self.root)

              except Exception as es:
                    messagebox.showerror(
                         "Error ", f"Due to : {str(es)}", parent=self.root)


if __name__ == "__main__":  # to call main
    root = Tk()  # call root from toolkit
    obj = Student(root)  # to connect with root
    root.mainloop()  # close mainloop
