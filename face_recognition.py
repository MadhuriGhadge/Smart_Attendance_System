from tkinter import *
from PIL import Image, ImageTk
import PIL
import tkinter.messagebox as messagebox
import mysql.connector
from datetime import datetime
import cv2
import numpy as np

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"college_image\20.jpg")
        img_top = img_top.resize((650, 700), PIL.Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=650, height=700)

        img_bottom = Image.open(r"college_image\19.jpeg")
        img_bottom = img_bottom.resize((950, 700), PIL.Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        
        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=650, y=55, width=950, height=700)

        btn_recognition = Button(f_lbl, text="Face Recognition", cursor="hand2",
                                      command=self.face_recog, font=("times new roman", 18, "bold"),
                                      bg="red", fg="white")
        btn_recognition.place(x=365, y=620, width=200, height=40)
        
        
# ================================== Attendance ==========================================


    def mark_attendance(self, i, r, n, d, my_cursor):
        with open("attendance.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = [entry.split(",")[0] for entry in myDataList]
            if (i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.write(f"\n{i},{r},{n},{d},{dtString},{d1},Present")
                
                
# ================================== Face Recognition ===========================================
                
    def face_recog(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="Mypass123", database="face_recognizer" ,port=3307)
            my_cursor = conn.cursor()

            faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.read("classifier.xml")

            video_cap = cv2.VideoCapture(0)

            while True:
                ret, img = video_cap.read()
                img = self.recognize(img, clf, faceCascade, my_cursor, conn)
                cv2.imshow("Welcome To Face Recognition", img)

                if cv2.waitKey(1) == 13:
                    break

            video_cap.release()
            cv2.destroyAllWindows()
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error connecting to the database: {str(e)}")
        finally:
            if conn.is_connected():
                conn.close()

    def draw_boundary(self, img, classifier, scale_factor, min_neighbors, color, text, clf, my_cursor,conn):
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        features = classifier.detectMultiScale(gray_image, scale_factor, min_neighbors)

        for (x, y, w, h) in features:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
            id, predict = clf.predict(gray_image[y:y + h, x:x + w])
            confidence = int((100 * (1 - predict / 300)))
            
            

            try:
                
                my_cursor.execute("select Name from student where Student_id=%s", (id,))
                n = my_cursor.fetchone()

                my_cursor.execute("select Roll from student where Student_id=%s", (id,))
                r = my_cursor.fetchone()

                my_cursor.execute("select Dep from student where Student_id=%s", (id,))
                d = my_cursor.fetchone()

                my_cursor.execute("select Student_id from student where Student_id=%s", (id,))
                i = my_cursor.fetchone()

                if n is not None:
                    n = "+".join(map(str, n))

                if r is not None:
                    r = "+".join(map(str, r))

                if d is not None:
                    d = "+".join(map(str, d))

                if i is not None:
                    i = "+".join(map(str, i))

                if confidence > 77:
                    cv2.putText(img, f"ID:{i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 0), 3)
                    cv2.putText(img, f"Roll:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 0), 3)
                    cv2.putText(img, f"Name:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 0), 3)
                    cv2.putText(img, f"Department:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 0), 3)
                    self.mark_attendance(i, r, n, d, my_cursor)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
            except Exception as e:
                messagebox.showerror("Error", f"Error fetching data: {str(e)}")

        return img

    def recognize(self, img, clf, faceCascade, my_cursor, conn):
        img = self.draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf, my_cursor,conn)
        return img


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
