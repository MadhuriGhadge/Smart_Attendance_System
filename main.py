from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter
import PIL
import os
from time import strftime
from datetime import datetime
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x800+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("calibri", 35, "bold"), bg="#263D42", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # first image
        img = Image.open(r"clg_img\1.jpg")
        img = img.resize((500, 150), PIL.Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg, bg="#263D42")
        f_lbl.place(x=0, y=45, width=500, height=150)

        # second image
        img1 = Image.open(r"clg_img\2.jpg")
        img1 = img1.resize((500, 150), PIL.Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1, bg="#263D42")
        f_lbl.place(x=500, y=45, width=500, height=150)

        # third image
        img2 = Image.open(r"images\3.jpeg")
        img2 = img2.resize((500, 150), PIL.Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2, bg="#263D42")
        f_lbl.place(x=1000, y=45, width=500, height=150)

        # bg image
        img3 = Image.open(r"images\4.jpeg")
        img3 = img3.resize((1530, 710), PIL.Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_image = Label(self.root, image=self.photoimg3)
        bg_image.place(x=0, y=195, width=1530, height=710)

        title_lbl = Label(bg_image, text="FACE RECOGNITION SYSTEM SOFTWARE", font=("calibri", 35, "bold"),
                          bg="#263D42", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # =====time=======
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl = Label(title_lbl, font=('calibri', 14, 'bold'), background='#263D42', foreground='white')
        lbl.place(x=0, y=0, width=110, height=50)
        time()

        # student button
        img4 = Image.open(r"images\5.jpeg")
        img4 = img4.resize((220, 220), PIL.Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_image, image=self.photoimg4, command=self.student_details, cursor="hand2", bg="#4CAF50", fg="white")
        b1.place(x=200, y=50, width=220, height=220)

        b1_1 = Button(bg_image, text="Student Details", command=self.student_details, cursor="hand2",
                      font=("calibri", 15, "bold"), bg="#4CAF50", fg="white")
        b1_1.place(x=200, y=270, width=220, height=40)

        # Detect face button
        img5 = Image.open(r"images\6.jpeg")
        img5 = img5.resize((220, 220), PIL.Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_image, image=self.photoimg5, cursor="hand2", command=self.face_data, bg="#FFA500", fg="white")
        b1.place(x=500, y=50, width=220, height=220)

        b1_1 = Button(bg_image, text="Face Detector", cursor="hand2", command=self.face_data,
                      font=("calibri", 15, "bold"), bg="#FFA500", fg="white")
        b1_1.place(x=500, y=270, width=220, height=40)

        # Attendance face button
        img6 = Image.open(r"images\7.jpg")
        img6 = img6.resize((220, 220), PIL.Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_image, image=self.photoimg6, cursor="hand2", command=self.attendance_data, bg="black", fg="white")
        b1.place(x=800, y=50, width=220, height=220)

        b1_1 = Button(bg_image, text="Attendance", cursor="hand2", command=self.attendance_data,
                      font=("calibri", 15, "bold"), bg="darkgreen", fg="white")
        b1_1.place(x=800, y=270, width=220, height=40)

        # Help face button
        img7 = Image.open(r"images\8.jpeg")
        img7 = img7.resize((220, 220), PIL.Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_image, image=self.photoimg7, cursor="hand2", command=self.help_data, bg="#4B0082", fg="white")
        b1.place(x=1100, y=50, width=220, height=220)

        b1_1 = Button(bg_image, text="Help Desk", cursor="hand2", command=self.help_data,
                      font=("calibri", 15, "bold"), bg="#4B0082", fg="white")
        b1_1.place(x=1100, y=270, width=220, height=40)

        # Train face button
        img8 = Image.open(r"images\9.jpeg")
        img8 = img8.resize((220, 220), PIL.Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_image, image=self.photoimg8, cursor="hand2", command=self.train_data, bg="#800000", fg="white")
        b1.place(x=200, y=330, width=220, height=220)

        b1_1 = Button(bg_image, text="Train Data", cursor="hand2", command=self.train_data,
                      font=("calibri", 15, "bold"), bg="#800000", fg="white")
        b1_1.place(x=200, y=540, width=220, height=40)

        # Photos face button
        img9 = Image.open(r"images\10.jpeg")
        img9 = img9.resize((220, 220), PIL.Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_image, image=self.photoimg9, cursor="hand2", command=self.open_img, bg="#1E90FF", fg="white")
        b1.place(x=500, y=330, width=220, height=220)

        b1_1 = Button(bg_image, text="Photos", cursor="hand2", command=self.open_img,
                      font=("calibri", 15, "bold"), bg="#1E90FF", fg="white")
        b1_1.place(x=500, y=540, width=220, height=40)

        # Developer face button
        img10 = Image.open(r"images\11.jpg")
        img10 = img10.resize((220, 220), PIL.Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_image, image=self.photoimg10, cursor="hand2", command=self.developer_data, bg="#008080", fg="white")
        b1.place(x=800, y=330, width=220, height=220)

        b1_1 = Button(bg_image, text="Developer", cursor="hand2", command=self.developer_data,
                      font=("calibri", 15, "bold"), bg="#008080", fg="white")
        b1_1.place(x=800, y=540, width=220, height=40)

        # Exit face button
        img11 = Image.open(r"images\download (3).png")
        img11 = img11.resize((220, 220), PIL.Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_image, image=self.photoimg11, cursor="hand2", command=self.iExit, bg="#A52A2A", fg="white")
        b1.place(x=1100, y=330, width=220, height=220)

        b1_1 = Button(bg_image, text="Exit", cursor="hand2", command=self.iExit,
                      font=("calibri", 15, "bold"), bg="#A52A2A", fg="white")
        b1_1.place(x=1100, y=540, width=220, height=40)

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.IExit = tkinter.messagebox.askyesno("Face recognition", "Are you sure exit this project", parent=self.root)
        if self.IExit > 0:
            self.root.destroy()
        else:
            return

    # ==================Functions Buttons================
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
