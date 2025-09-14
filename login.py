from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import PIL
from tkinter import messagebox
import random
import time
import datetime
import mysql.connector
from bcrypt import hashpw, gensalt
from main import Face_Recognition_System
from register import Register


def main():
    win = Tk()
    app = Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        # frame=frame(self.root,bg="black")
        # frame.place(x=610,y=170,width=340,height=450)

        img1 = Image.open(r"college_image\31.jpeg")
        img1 = img1.resize((1530, 750), PIL.Image.LANCZOS)
        self.photoImg1 = ImageTk.PhotoImage(img1)
        bg_lbl = Label(self.root, image=self.photoImg1)
        bg_lbl.place(x=0, y=0, width=1530, height=750)

        title = Label(bg_lbl, text="FACIAL RECOGNITION ATTENDANCE SYSTEM", font=("times new roman", 20, "bold"), fg="white",
                      bg="black")
        title.place(x=0, y=120, width=1550, height=45)

        # =========== Project button(description)===========
        downtitle = Label(self.root, text="Note:Enter valid username and valid password", font=("times new roman", 20, "bold"), bg="black", fg="white")
        downtitle.place(x=0, y=740, width=1600, height=35)

        img10 = Image.open(r"college_image\17.jpeg")
        img10 = img10.resize((500, 120), PIL.Image.LANCZOS)
        self.photoImg10 = ImageTk.PhotoImage(img10)
        bg_lbl1 = Label(bg_lbl, image=self.photoImg10)
        bg_lbl1.place(x=0, y=0, width=500, height=120)

        img11 = Image.open(r"college_image\2.jpg")
        img11 = img11.resize((500, 120), PIL.Image.LANCZOS)
        self.photoImg11 = ImageTk.PhotoImage(img11)
        bg_lbl22 = Label(bg_lbl, image=self.photoImg11)
        bg_lbl22.place(x=500, y=0, width=500, height=120)

        img13 = Image.open(r"college_image\21.jpg")
        img13 = img13.resize((500, 120), PIL.Image.LANCZOS)
        self.photoImg13 = ImageTk.PhotoImage(img13)
        bg_lbl12 = Label(bg_lbl, image=self.photoImg13)
        bg_lbl12.place(x=1000, y=0, width=550, height=120)

        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=200, width=340, height=430)

        img1 = Image.open(r"college_image\31.jpeg")
        img1 = img1.resize((90, 90), PIL.Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg="black", borderwidth=0)
        lblimg1.place(x=730, y=200, width=90, height=90)

        get_str = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=95, y=85)

        # label
        username_lbl = Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="white", bg="black")
        username_lbl.place(x=70, y=125)

        self.txtuser = StringVar()
        username_entry = ttk.Entry(frame, textvariable=self.txtuser, font=("times new roman", 15, "bold"))
        username_entry.place(x=40, y=150, width=270)

        self.txtpass = StringVar()
        password_lbl = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password_lbl.place(x=70, y=195)

        password_entry = ttk.Entry(frame, textvariable=self.txtpass, font=("times new roman", 15, "bold"), show='*')
        password_entry.place(x=40, y=220, width=270)

        # ============= Icon Image ================
        img2 = Image.open(r"college_image\28.jpg")
        img2 = img2.resize((25, 25), PIL.Image.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg1 = Label(image=self.photoimage2, bg="black", borderwidth=0)
        lblimg1.place(x=650, y=323, width=25, height=25)

        img3 = Image.open(r"college_image\28.jpg")
        img3 = img3.resize((25, 25), PIL.Image.LANCZOS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg1 = Label(image=self.photoimage3, bg="black", borderwidth=0)
        lblimg1.place(x=650, y=395, width=25, height=25)

        # LoginButton
        loginbtn = Button(frame, text="Login", command=self.login, font=("times new roman", 15, "bold"), bd=3,
                          relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        loginbtn.place(x=110, y=270, width=120, height=35)

        # registerbutton
        registerbtn = Button(frame, text="New User Register", command=self.register_window,
                             font=("times new roman", 10, "bold"), borderwidth=0, fg="white", bg="black",
                             activeforeground="white", activebackground="black")
        registerbtn.place(x=15, y=320, width=160)

        # forgetpassbtn
        forgetbtn = Button(frame, text="Forget password", command=self.forget_password_window,
                           font=("times new roman", 10, "bold"), borderwidth=0, fg="white", bg="black",
                           activeforeground="white", activebackground="black")
        forgetbtn.place(x=10, y=340, width=160)

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def login(self):
        username = self.txtuser.get()
        password = self.txtpass.get()

        if username == "madhuri" and password == "123":
            messagebox.showinfo("Success", "Welcome to Face Recognition System", parent=self.root)
        else:
            try:
                self.authenticate_user(username, password)

            except mysql.connector.Error as e:
                messagebox.showerror("Database Error", f"An error occurred: {str(e)}")

    def authenticate_user(self, username, password):
        default_username = "harsh"
        default_password = "123"

        if username == default_username and password == default_password:
            messagebox.showinfo("Success", "Welcome to Face Recognition System", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Mypass123",
                                               database="face_recognizer", port=3307)
                my_cursor = conn.cursor()

                query = "SELECT * FROM register WHERE email = %s AND password = %s"
                values = (username, password)
                my_cursor.execute(query, values)
                row = my_cursor.fetchone()

                if row is None:
                    messagebox.showerror("Error", "Invalid Username and Password")
                else:
                    open_main = messagebox.askyesno("YesNo", "Access only admin")
                    if open_main:
                        self.new_window = Toplevel(self.root)
                        self.app = Face_Recognition_System(self.new_window)
                    else:
                        if not open_main:
                            return

                conn.commit()
                conn.close()

            except mysql.connector.Error as e:
                messagebox.showerror("Database Error", f"An error occurred: {str(e)}")

    def clear(self):
        self.txtuser.set("")
        self.txtpass.set("")

    # ========= Reset Password ================

    def reset_pass(self):
        if self.combo_security_Q.get() == "Select" or self.txt_security.get() == "" or self.txt_pas.get() == "":
            messagebox.showerror("Error", "All fields are Required", parent=self.root2)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Mypass123",
                                               database="face_recognizer", port=3307)
                my_cursor = conn.cursor()

                query = "SELECT * FROM register WHERE email=%s AND securityQ=%s AND securityA=%s"
                value = (self.txtuser.get(), self.combo_security_Q.get(), self.txt_security.get())
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                if row is None:
                    messagebox.showerror("Error", "Please select the correct security question", parent=self.root2)
                else:
                    update_query = "UPDATE register SET password=%s WHERE email=%s"
                    update_values = (self.txt_pas.get(), self.txtuser.get())
                    my_cursor.execute(update_query, update_values)

                    conn.commit()
                    messagebox.showinfo("Success", "Your password has been reset. Please login with the new password",
                                        parent=self.root2)
                    self.root2.destroy()

            except mysql.connector.Error as e:
                messagebox.showerror("Database Error", f"An error occurred: {str(e)}", parent=self.root2)

            finally:
                if conn.is_connected():
                    conn.close()

                self.txtuser.focus()

    # ============ Forget Password ================

    def forget_password_window(self):
        email = self.txtuser.get()

        if email == "":
            messagebox.showerror("Error", "Please enter the email address to reset the password")
        else:
            try:
                row = self.retrieve_user_from_database(email)

                if row is None:
                    messagebox.showerror("Error", "Please enter a valid email address")
                else:
                    self.show_reset_password_window()

            except mysql.connector.Error as e:
                messagebox.showerror("Database Error", f"An error occurred: {str(e)}")

    def retrieve_user_from_database(self, email):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="Mypass123",
                                           database="face_recognizer", port=3307)
            my_cursor = conn.cursor()

            query = "SELECT * FROM register WHERE email = %s"
            value = (email,)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            return row

        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"An error occurred: {str(e)}")

        finally:
            if conn.is_connected():
                conn.close()

    def show_reset_password_window(self):
        self.root2 = Toplevel()
        self.root2.title("Forget Password")
        self.root2.geometry("340x450+610+170")

        label_forget_password = Label(self.root2, text="Forget Password", font=("times new roman", 20, "bold"),
                                       fg="red", bg="white")
        label_forget_password.place(x=0, y=10, relwidth=1)

        label_security_question = Label(self.root2, text="Select Security Question",
                                         font=("times new roman", 15, "bold"), bg="white", fg="black")
        label_security_question.place(x=50, y=80)

        self.combo_security_Q = ttk.Combobox(self.root2, font=("times new roman", 15, "bold"), state="readonly")
        self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your mothers name", "Your pet Name")
        self.combo_security_Q.place(x=50, y=110, width=250)
        self.combo_security_Q.current(0)

        label_security_answer = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"),
                                       bg="white", fg="black")
        label_security_answer.place(x=50, y=150)

        self.txt_security = ttk.Entry(self.root2, font=("times new roman", 15, "bold"), show='*')
        self.txt_security.place(x=50, y=180, width=250)

        label_new_password = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"),
                                    bg="white", fg="black")
        label_new_password.place(x=50, y=220)

        self.txt_pas = ttk.Entry(self.root2, font=("times new roman", 15, "bold"), show='*')
        self.txt_pas.place(x=50, y=250, width=250)

        btn_reset = Button(self.root2, text="Reset", command=self.reset_pass, font=("times new roman", 15, "bold"),
                            fg="white", bg="green")
        btn_reset.place(x=120, y=290, width=100)


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        # ================ variables  ============
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_SecurityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        # ======bg image=====

        self.bg = ImageTk.PhotoImage(file=r"college_image\32.jpeg")
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # ======left image====

        self.bg1 = ImageTk.PhotoImage(file=r"college_image\10.jpeg")
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=50, y=100, width=470, height=550)

        # =======main frame=======
        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=550)

        register_lbl = Label(frame, text="REGISTER HERE", font=("timews new roman", 20, "bold"),
                              fg="darkgreen", bg="white")
        register_lbl.place(x=20, y=20)

        # =======label and entry=====

        # =====row1
        fname = Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white", fg="black")
        fname.place(x=50, y=100)

        fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15, "bold"))
        fname_entry.place(x=50, y=130, width=250)

        l_name = Label(frame, text="Last Name", font=("time new roman", 15, "bold"), bg="white", fg="black")
        l_name.place(x=370, y=100)

        self.txt_lname = ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15, "bold"))
        self.txt_lname.place(x=370, y=130, width=250)

        # ====row2
        contact = Label(frame, text="Contact No", font=("times new roman", 15, "bold"), bg="white", fg="black")
        contact.place(x=50, y=170)

        self.txt_contact = ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 15, "bold"))
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="black")
        email.place(x=370, y=170)

        self.txt_email = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15, "bold"))
        self.txt_email.place(x=370, y=200, width=250)

        # =======row3
        security_Q = Label(frame, text="Select Security Questions", font=("times new roman", 15, "bold"),
                            bg="white", fg="black")
        security_Q.place(x=50, y=240)

        self.combo_security_Q = ttk.Combobox(frame, textvariable=self.var_securityQ, font=("times new roman", 15, "bold"),
                                               state="readonly")
        self.combo_security_Q["values"] = ("Select", "", "Your village name", "Your pet Name",
                                            "The city where you born")
        self.combo_security_Q.place(x=50, y=270, width=250)
        self.combo_security_Q.current(0)

        security_A = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"),
                            bg="white", fg="black")
        security_A.place(x=370, y=240)

        self.txt_security = ttk.Entry(frame, textvariable=self.var_SecurityA, font=("times new roman", 15, "bold"))
        self.txt_security.place(x=370, y=270, width=250)

        # ==== row4 ========

        pswd = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        pswd.place(x=50, y=310)

        self.txt_pass = ttk.Entry(frame, textvariable=self.var_pass, font=("times new roman", 15, "bold"))
        self.txt_pass.place(x=50, y=340, width=250)

        confirm_pass = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white",
                              fg="black")
        confirm_pass.place(x=370, y=310)

        self.txt_confirm_pswd = ttk.Entry(frame, textvariable=self.var_confpass, font=("times new roman", 15, "bold"))
        self.txt_confirm_pswd.place(x=370, y=340, width=250)

        # ================ Checkbox ============
        self.var_check = IntVar()
        self.checkbtn = Checkbutton(frame, variable=self.var_check, text="I Agree The Terms & Conditions",
                                     font=("times new roman", 12, "bold"), onvalue=1, offvalue=0)
        self.checkbtn.place(x=50, y=380)

        # ======== buttons ==========

        img = Image.open(r"college_image\29.jpeg")
        img = img.resize((200, 55), PIL.Image.LANCZOS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame, image=self.photoimage, command=self.register_data, borderwidth=0, cursor="hand2",
                     font=("times new roman", 15, "bold"))
        b1.place(x=10, y=420, width=200)

        img1 = Image.open(r"college_image\30.jpeg")
        img1 = img1.resize((200, 100), PIL.Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b1 = Button(frame, image=self.photoimage1, command=self.register_data, borderwidth=0, cursor="hand2",
                     font=("times new roman", 15, "bold"))
        b1.place(x=330, y=420, width=200)

    # ======== Function declaration===========

    def register_data(self):
        if (
                self.var_fname.get() == ""
                or self.var_email.get() == ""
                or self.var_securityQ.get() == "Select"
                or self.var_SecurityA.get() == ""
                or self.var_pass.get() == ""
                or self.var_confpass.get() == ""
        ):
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password & Confirm Password should be same", parent=self.root)
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree our terms and condition", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="Mypass123",
                    database="face_recognizer",
                    port=3307,
                )
                my_cursor = conn.cursor()
                query = "select * from register where email=%s"
                value = (self.var_email.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                if row != None:
                    messagebox.showerror(
                        "Error", "User already exist, please try with another email"
                    )
                else:
                    

                    query = (
                        "insert into register values(NULL,%s,%s,%s,%s,%s,%s,%s)"
                    )
                    value = (
                        self.var_fname.get(),
                        self.var_lname.get(),
                        self.var_contact.get(),
                        self.var_email.get(),
                        self.var_securityQ.get(),
                        self.var_SecurityA.get(),
                        self.var_pass.get(),
                    )
                    my_cursor.execute(query, value)
                    conn.commit()
                    conn.close()
                    messagebox.showinfo(
                        "Success", "Registration Successful", parent=self.root
                    )
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error due to: {str(es)}", parent=self.root
                )


if __name__ == "__main__":
    main()
