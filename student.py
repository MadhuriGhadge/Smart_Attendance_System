from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import PIL
from tkinter import messagebox
import mysql.connector
import cv2
from tkinter import messagebox
import re


class Student:
  
    def __init__(self,root):
      self.root=root
      self.root.geometry("1530x790+0+0")
      self.root.title("Face Recognition System")
      
      # ================= variables =================
      self.var_dep=StringVar()
      self.var_course=StringVar()
      self.var_year=StringVar()
      self.var_semester=StringVar()
      self.var_std_id=StringVar()
      self.var_std_name=StringVar()
      self.var_div=StringVar()
      self.var_roll=StringVar()
      self.var_gender=StringVar()
      self.var_dob=StringVar()
      self.var_email=StringVar()
      self.var_phone=StringVar()
      self.var_address=StringVar()
      self.var_teacher=StringVar()
      
      
      
        # first image
      
      img=Image.open(r"images\13.jpeg")
      img=img.resize((500,130),PIL.Image.LANCZOS)
      self.photoimg=ImageTk.PhotoImage(img)      
      
      f_lbl=Label(self.root,image=self.photoimg)
      f_lbl.place(x=0,y=0,width=500,height=130)
      
      # second image
      
      img1=Image.open(r"college_image\14.jpeg")
      img1=img1.resize((500,130),PIL.Image.LANCZOS)
      self.photoimg1=ImageTk.PhotoImage(img1)      
      
      f_lbl=Label(self.root,image=self.photoimg1)
      f_lbl.place(x=500,y=0,width=500,height=130)
      
      # third image
      
      img2=Image.open(r"college_image\15.jpg")
      img2=img2.resize((500,130),PIL.Image.LANCZOS)
      self.photoimg2=ImageTk.PhotoImage(img2)      
      
      f_lbl=Label(self.root,image=self.photoimg2)
      f_lbl.place(x=1000,y=0,width=500,height=130)
      
      
      # bg image
      
      img3=Image.open(r"college_image\4.jpeg")
      img3=img3.resize((1530,710),PIL.Image.LANCZOS)
      self.photoimg3=ImageTk.PhotoImage(img3)      
      
      bg_image=Label(self.root,image=self.photoimg3)
      bg_image.place(x=0,y=150,width=1530,height=710)
      
      title_lbl=Label(bg_image,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
      title_lbl.place(x=0,y=0,width=1530,height=45)
      
      main_frame=Frame(bg_image,bd=2,bg="white")
      main_frame.place(x=5,y=55,width=1500,height=600)
      
      # left label frame
      Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
      Left_frame.place(x=10,y=10,width=760,height=580)
      
      
      img_left=Image.open(r"college_image\16.jpeg")
      img_left=img_left.resize((720,130),PIL.Image.LANCZOS)
      self.photoimg_left=ImageTk.PhotoImage(img_left)      
      
      f_lbl=Label(Left_frame,image=self.photoimg_left)
      f_lbl.place(x=5,y=0,width=720,height=130)
      
      # current course
      current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current course Information",font=("times new roman",12,"bold"))
      current_course_frame.place(x=5,y=135,width=720,height=150)
      
      # Department
      dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
      dep_label.grid(row=0,column=0,padx=10,sticky=W)
      
      dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly",width=20)
      dep_combo["values"]=("Select Department","Computer Science","Comp. Appl","CDS")
      dep_combo.current(0)
      dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
      
      # Course
      course_label=Label(current_course_frame,text="Course",font=("times new roman",13,"bold"),bg="white")
      course_label.grid(row=0,column=2,padx=10,sticky=W)
      
      course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",13,"bold"),state="readonly",width=20)
      course_combo["values"]=("Select course","Fy","Sy","Ty")
      course_combo.current(0)
      course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
      
      # Year
      year_label=Label(current_course_frame,text="Year",font=("times new roman",13,"bold"),bg="white")
      year_label.grid(row=1,column=0,padx=10,sticky=W)
      
      year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",13,"bold"),state="readonly")
      year_combo["values"]=("Select Year","2021-22","2022-23","2023-24")
      year_combo.current(0)
      year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
      
      
      # Semester
      semester_label=Label(current_course_frame,text="Semester",font=("times new roman",13,"bold"),bg="white")
      semester_label.grid(row=1,column=2,padx=10,sticky=W)
      
      semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",13,"bold"),state="readonly",width=20)
      semester_combo["values"]=("Select Semester","Semester-1","Semester-2","semester-3","semester-4","semester-5","semester-6")
      semester_combo.current(0)
      semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
      
      
      # Class Student Information
      class_Student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",13,"bold"))
      class_Student_frame.place(x=5,y=250,width=720,height=300)
      
      # Student id
      studentId_label=Label(class_Student_frame,text="StudentID:",font=("times new roman",13,"bold"),bg="white")
      studentId_label.grid(row=0,column=0,padx=10,sticky=W)
      
      studentID_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_std_id,font=("times new roman",13,"bold"))
      studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
      
      
      # student name
      studentName_label=Label(class_Student_frame,text="Student Name:",font=("times new roman",13,"bold"),bg="white")
      studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
      
      studentName_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_std_name,font=("times new roman",13,"bold"))
      studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
      
      
      # class division
      class_div_label=Label(class_Student_frame,text="Class Division:",font=("times new roman",12,"bold"),bg="white")
      class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
      
      div_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_div,font=("times new roman",13,"bold"),state="readonly")
      div_combo["values"]=("A","B","C")
      div_combo.current(0)
      div_combo.grid(row=1,column=1,padx=2,pady=5,sticky=W)
      
      # Roll No
      roll_no_label=Label(class_Student_frame,text="Roll No:",font=("times new roman",13,"bold"),bg="white")
      roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
      
      roll_no_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_roll,font=("times new roman",13,"bold"))
      roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
      
      
      # Gender
      gender_label=Label(class_Student_frame,text="Gender:",font=("times new roman",13,"bold"),bg="white")
      gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

      gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,font=("times new roman",13,"bold"),state="readonly",width=18)
      gender_combo["values"]=("Male","Female","Transgender","Other")
      gender_combo.current(0)
      gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)
      
        
      # DOB
      dob_label=Label(class_Student_frame,text="DOB:",font=("times new roman",12,"bold"),bg="white")
      dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
      
      dob_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_dob,font=("times new roman",13,"bold"))
      dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
      
      
      
      # Email
      email_label=Label(class_Student_frame,text="Email:",font=("times new roman",13,"bold"),bg="white")
      email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
      
      email_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_email,font=("times new roman",13,"bold"))
      email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
      
      
      #Phone no
      phone_label=Label(class_Student_frame,text="Phone No:",font=("times new roman",13,"bold"),bg="white")
      phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
      
      phone_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_phone,font=("times new roman",13,"bold"))
      phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
      
      
      # Address
      address_label=Label(class_Student_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
      address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
      
      address_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_address,font=("times new roman",13,"bold"))
      address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
      
      
      # Teacher name
      teacher_label=Label(class_Student_frame,text="Teacher Name:",font=("times new roman",12,"bold"),bg="white")
      teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)
      
      teacher_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_teacher,font=("times new roman",13,"bold"))
      teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
      
      
      # Radio Buttons
      radio_frame = Frame(class_Student_frame, bd=2, bg="white", relief=RIDGE)
      radio_frame.place(x=10, y=180, width=270, height=70)

      self.var_radio = StringVar()

      radiobtn1 = ttk.Radiobutton(radio_frame, variable=self.var_radio, text="Take Photo Sample", value="Yes")
      radiobtn1.grid(row=0, column=0, padx=5)

      radiobtn2 = ttk.Radiobutton(radio_frame, variable=self.var_radio, text="No Photo Sample", value="No")
      radiobtn2.grid(row=0, column=1, padx=5)
      
      
      
      
      # Buttons frame
      
      btn_frame = Frame(class_Student_frame, bd=2, relief=RIDGE, bg="white")
      btn_frame.place(x=0, y=200, width=715, height=35)

      buttons = [
          ("Save", self.add_data),
          ("Update", self.update_data),
          ("Delete", self.delete_data),
          ("Reset", self.reset_data)
      ]

      for i, (text, command) in enumerate(buttons):
          btn = Button(btn_frame, text=text, command=command, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
          btn.grid(row=0, column=i)

      btn_frame1 = Frame(class_Student_frame, bd=2, relief=RIDGE, bg="white")
      btn_frame1.place(x=0, y=235, width=715, height=35)

      photo_buttons = [
          ("Take Photo Sample", self.generate_dataset),
          ("Update Photo Sample", self.update_data)
      ]

      for i, (text, command) in enumerate(photo_buttons):
          btn = Button(btn_frame1, text=text, command=command, width=35, font=("times new roman", 13, "bold"), bg="blue", fg="white")
          btn.grid(row=0, column=i)

      # Right label frame
      RIGHT_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
      RIGHT_frame.place(x=750, y=10, width=720, height=580)

      img_right = Image.open(r"college_image/17.jpeg")
      img_right = img_right.resize((720, 130), Image.LANCZOS)
      self.photoimg_right = ImageTk.PhotoImage(img_right)

      f_lbl = Label(RIGHT_frame, image=self.photoimg_right)
      f_lbl.place(x=5, y=0, width=720, height=130)

      # Search System
      Search_frame = LabelFrame(RIGHT_frame, bd=2, bg="white", relief=RIDGE, text="Search System", font=("times new roman", 12, "bold"))
      Search_frame.place(x=5, y=135, width=710, height=70)

      search_label = Label(Search_frame, text="Search By:", font=("times new roman", 15, "bold"), bg="red", fg="white")
      search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

      self.search_combo = ttk.Combobox(Search_frame, font=("times new roman", 13, "bold"), state="readonly", width=15)
      self.search_combo["values"] = ("Select", "Roll_No", "Phone_No")
      self.search_combo.current(0)
      self.search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

      self.search_entry = ttk.Entry(Search_frame, width=15, font=("times new roman", 13, "bold"))
      self.search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

      #search_btn = Button(Search_frame, text="Search", width=12, font=("times new roman", 12, "bold"), bg="blue", fg="white")
      #search_btn.grid(row=0, column=3, padx=4)

      #show_all_btn = Button(Search_frame, text="Show All", width=12, font=("times new roman", 12, "bold"), bg="blue", fg="white")
      #show_all_btn.grid(row=0, column=4, padx=4)
      # Search Button
      search_btn = Button(Search_frame, text="Search", width=12, font=("times new roman", 12, "bold"), bg="blue", fg="white", command=self.search_data)
      search_btn.grid(row=0, column=3, padx=4)

        # Show All Button
      show_all_btn = Button(Search_frame, text="Show All", width=12, font=("times new roman", 12, "bold"), bg="blue", fg="white", command=self.show_all_data)
      show_all_btn.grid(row=0, column=4, padx=4)

      
      
      # ===============Table Frame====================
      
      
      # Table Frame
      table_frame = Frame(RIGHT_frame, bd=2, bg="white", relief="ridge")
      table_frame.place(x=5, y=210, width=720, height=330)

      scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
      scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

      self.student_table = ttk.Treeview(table_frame, column=("dep", "course", "year", "sem", "id", "name", "div", "roll", "gender", "dob", "email", "phone", "address", "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

      scroll_x.pack(side=BOTTOM, fill=X)
      scroll_y.pack(side=RIGHT, fill=Y)
      scroll_x.config(command=self.student_table.xview)
      scroll_y.config(command=self.student_table.yview)

      columns = ["dep", "course", "year", "sem", "id", "name", "div", "roll", "gender", "dob", "email", "phone", "address", "teacher", "photo"]
      headings = ["Department", "Course", "Year", "Semester", "StudentId", "Name", "Division", "Roll", "Gender", "DOB", "Email", "Phone", "Address", "Teacher", "PhotoSampleStatus"]

      for col, heading in zip(columns, headings):
          self.student_table.heading(col, text=heading)
          self.student_table.column(col, width=100)

      # Required fields with asterisks
      required_fields = [studentName_label, studentId_label, phone_label, email_label]

      for label in required_fields:
          label_text = label.cget("text")
          label.config(text=label_text, foreground="black")

          # Create an asterisk label
          asterisk_label = Label(RIGHT_frame, text=" *", foreground="red")
          asterisk_label.grid(row=label.grid_info()["row"], column=label.grid_info()["column"] + 1, sticky="W")

      # Student Name label with asterisk
      label_text = studentName_label.cget("text")
      studentName_label.config(text=label_text + " *", foreground="black")

      # Student ID label with asterisk
      label_text = studentId_label.cget("text")
      studentId_label.config(text=label_text + " *", foreground="black")

      # Phone label with asterisk
      label_text = phone_label.cget("text")
      phone_label.config(text=label_text + " *", foreground="black")

      # Email label with asterisk
      label_text = email_label.cget("text")
      email_label.config(text=label_text + " *", foreground="black")

      self.student_table.pack(fill=BOTH, expand=1)
      self.student_table.bind("<ButtonRelease>", self.get_cursor)
      self.fetch_data()

      
    def check_email(self):
      email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
      return bool(re.match(email_pattern, self.var_email.get()))
    
    def is_valid_Phone(self):
      phone_pattern = re.compile("(0|91)?[6-9][0-9]{9}")
      return bool(phone_pattern.match(self.var_phone.get()))
        
        # ============ Function declaration ============
        
    def add_data(self):
        
      if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_std_id.get()=="":
        messagebox.showerror("Error","All Fields are required",parent=self.root)
            
      elif self.check_email()==False:
        messagebox.showerror("Error","Please enter right email",parent=self.root)
            
      elif self.is_valid_Phone()==False:
        messagebox.showerror("Error","Please enter 10 digit or valid phone number ",parent=self.root)
          

      else:
        try:
          with mysql.connector.connect(host="localhost", username="root", password="Mypass123", database="face_recognizer" ,port=3307) as conn:
            my_cursor = conn.cursor()
            my_cursor.execute("""
            INSERT INTO student 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
            self.var_dep.get(),
            self.var_course.get(),
            self.var_year.get(),
            self.var_semester.get(),
            self.var_std_id.get(),
            self.var_std_name.get(),
            self.var_div.get(),
            self.var_roll.get(),
            self.var_gender.get(),
            self.var_dob.get(),
            self.var_email.get(),
            self.var_phone.get(),
            self.var_address.get(),
            self.var_teacher.get(),
            self.var_radio.get()
        ))
            conn.commit()
            self.fetch_data()
            messagebox.showinfo("Success", "Student details have been added successfully", parent=self.root)
        except Exception as es:
          messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

        
  # =========== fetch data =============
  
    def fetch_data(self):
      try:
        conn=mysql.connector.connect(host="localhost", username="root", password="Mypass123", database="face_recognizer" ,port=3307)
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
          
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
              self.student_table.insert("",END,values=i)
            conn.commit()
            
      except Exception as e:
        messagebox.showerror("Error", f"Error fetching data: {str(e)}")    
        conn.close()
        
        
      # ========= get cursor ============   
      
    def get_cursor(self,event=""):

        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        
        if data: 
          self.var_dep.set(data[0]),
          self.var_course.set(data[1]),
          self.var_year.set(data[2]),
          self.var_semester.set(data[3]),
          self.var_std_id.set(data[4]),
          self.var_std_name.set(data[5]),
          self.var_div.set(data[6]),
          self.var_roll.set(data[7]),
          self.var_gender.set(data[8]),
          self.var_dob.set(data[9]),
          self.var_email.set(data[10]),
          self.var_phone.set(data[11]),
          self.var_address.set(data[12]),
          self.var_teacher.set(data[13]),
          self.var_radio.set(data[14])
      
    # ======== update funtion===============
      
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                update = messagebox.askyesno("Update", "Do you want to update this student details", parent=self.root)
                if update:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Mypass123", database="face_recognizer" ,port=3307)
                    my_cursor = conn.cursor()
                    my_cursor.execute("""
                        UPDATE student SET 
                        Dep=%s, course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, 
                        Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s 
                        WHERE Student_id=%s
                        """, (
                        self.var_dep.get(), self.var_course.get(), self.var_year.get(), self.var_semester.get(),
                        self.var_std_name.get(), self.var_div.get(), self.var_roll.get(), self.var_gender.get(),
                        self.var_dob.get(), self.var_email.get(), self.var_phone.get(), self.var_address.get(),
                        self.var_teacher.get(), self.var_radio.get(), self.var_std_id.get()
                    ))

                    messagebox.showinfo("Success", "Student details are successfully updated", parent=self.root)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

            
        # Delete Function
              
    def delete_data(self):
      if self.var_std_id.get() == "":
          messagebox.showerror("Error", "Student ID must be required", parent=self.root)
      else:
        try:
            delete = messagebox.askyesno("Student Delete Page", "Do you want to delete this student", parent=self.root)
            if delete:
              conn = mysql.connector.connect(host="localhost", username="root", password="Mypass123", database="face_recognizer" ,port=3307)
              my_cursor = conn.cursor()
              sql = "DELETE FROM student WHERE Student_id = %s"
              val = (self.var_std_id.get(),)
              my_cursor.execute(sql, val)
              conn.commit()
              self.fetch_data()
              conn.close()
              messagebox.showinfo("Delete", "Successfully deleted student details", parent=self.root)
        except Exception as es:
              messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

      # reset
      
    def reset_data(self):
    # Clear the Treeview
      self.student_table.delete(*self.student_table.get_children())

    # Reset variable values
      self.var_dep.set("Select Department")
      self.var_course.set("Select Course")
      self.var_year.set("Select Year")
      self.var_semester.set("Select Semester")
      self.var_std_id.set("")
      self.var_std_name.set("")
      self.var_div.set("Select Division")
      self.var_roll.set("")
      self.var_gender.set("Male")
      self.var_dob.set("")
      self.var_email.set("")
      self.var_phone.set("")
      self.var_address.set("")
      self.var_teacher.set("")
      self.var_radio.set("")

        # Inside the __init__ method, after creating the buttons

    # Search Button Functionality
    def search_data(self):
        selected_criteria = self.search_combo.get()
        search_keyword = self.search_entry.get()
        
        if selected_criteria == "Select" or search_keyword == "":
            messagebox.showerror("Error", "Please select search criteria and enter search keyword", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Mypass123", database="face_recognizer", port=3307)
                my_cursor = conn.cursor()

                # Query based on selected criteria
                if selected_criteria == "Roll_No":
                    query = "SELECT * FROM student WHERE Roll LIKE %s"
                elif selected_criteria == "Phone_No":
                    query = "SELECT * FROM student WHERE Phone LIKE %s"

                # Execute the query
                my_cursor.execute(query, ('%' + search_keyword + '%',))
                data = my_cursor.fetchall()

                if len(data) != 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("", END, values=i)
                    conn.commit()
                else:
                    messagebox.showinfo("Info", "No record found", parent=self.root)

            except Exception as e:
                messagebox.showerror("Error", f"Error searching data: {str(e)}", parent=self.root)
            finally:
                conn.close()

    # Show All Button Functionality
    def show_all_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="Mypass123", database="face_recognizer", port=3307)
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM student")
            data = my_cursor.fetchall()

            if len(data) != 0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    self.student_table.insert("", END, values=i)
                conn.commit()
            else:
                messagebox.showinfo("Info", "No records found", parent=self.root)

        except Exception as e:
            messagebox.showerror("Error", f"Error fetching data: {str(e)}", parent=self.root)
        finally:
            conn.close()


        
      # ============ Generate Data set or Take Photo samples ===========
    
    def generate_dataset(self):
      if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
        messagebox.showerror("Error", "All Fields are required", parent=self.root)
      else:
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="Mypass123", database="face_recognizer" ,port=3307)
            my_cursor = conn.cursor()
            my_cursor.execute("select * from student")
            myresult = my_cursor.fetchall()
            id = 0
            for x in myresult:
                id += 1
            my_cursor.execute("""
                UPDATE student SET 
                Dep=%s, course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, 
                Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s 
                WHERE Student_id=%s
                """, (
                self.var_dep.get(), self.var_course.get(), self.var_year.get(), self.var_semester.get(),
                self.var_std_name.get(), self.var_div.get(), self.var_roll.get(), self.var_gender.get(),
                self.var_dob.get(), self.var_email.get(), self.var_phone.get(), self.var_address.get(),
                self.var_teacher.get(), self.var_radio.get(), self.var_std_id.get()
            ))
            conn.commit()
            self.fetch_data()
            self.reset_data()
            conn.close()
            
    
          # ======Load predifiend data on face frontals from opencv====
          
            face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                      
            def face_cropped(img):
                gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                faces=face_classifier.detectMultiScale(gray,1.3,5)
                    
                    # Scaling factor = 1.3
                    # Minimum Neighbour = 5
                    
                for (x,y,w,h) in faces:
                  face_cropped=img[y:y+h,x:x+w]
                  return face_cropped
                  
            cap=cv2.VideoCapture(0)
            img_id=0
            while True:
                ret,my_frame=cap.read()
                if face_cropped(my_frame) is not None:
                  img_id+=1
                  face=cv2.resize(face_cropped(my_frame),(450,450))
                  face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                  file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                  cv2.imwrite(file_name_path,face)
                  cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                  cv2.imshow("Cropped Face",face)
                      
                if cv2.waitKey(1)==13 or int(img_id)==20:
                  break
            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Result","Generating data set completed!!!")
        except Exception as es:
            messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                      
                  
        
if __name__ == "__main__" :
    root=Tk()
    obj=Student(root)
    root.mainloop()    
