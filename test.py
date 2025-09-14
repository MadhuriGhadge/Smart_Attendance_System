from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import PIL
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import joblib
import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # 1st image
        img_top = Image.open(r"college_image\20.jpg")
        img_top = img_top.resize((650, 700), PIL.Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=650, height=700)

        # 2nd image
        img_bottom = Image.open(r"college_image\19.jpeg")
        img_bottom = img_bottom.resize((950, 700), PIL.Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=650, y=55, width=950, height=700)

        # Button
        b1_1 = Button(f_lbl, text="Face Recognition", cursor="hand2", command=self.recognize_faces_wrapper,
                      font=("times new roman", 18, "bold"), bg="red", fg="white")
        b1_1.place(x=365, y=620, width=200, height=40)
        
        
        proto_path = r"deploy.prototxt (1).txt"
        model_path = r"res10_300x300_ssd_iter_140000.caffemodel"
        self.net = cv2.dnn.readNetFromCaffe(proto_path, model_path)

        self.clf = cv2.face.LBPHFaceRecognizer_create()
        self.clf.read("classifier.xml")

    def mark_attendance(self, i, r, n, d):
        with open("attendance.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split(",")
                name_list.append(entry[0])
            if (i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")
                
                

    def recognize_faces_wrapper(self):
        video_cap = cv2.VideoCapture(0)
        while True:
            ret, img = video_cap.read()
            if not ret:
                print("Error capturing frame from the camera.")
                break
            self.recognize_faces(img,self.net,self.clf)

            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()

    def recognize_faces(self,img,net,clf):
        # Convert the image to grayscale for face recognition
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Use the DNN-based face detection model
        h, w = img.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(img, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))
        net.setInput(blob)
        detections = self.net.forward()

        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]

            if confidence > 0.5:
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")

                face = gray_img[startY:endY, startX:endX]

                # Predict the face using your LBPH recognizer
                if face is not None and face.any():
                    id, predict = self.clf.predict(face)
                    confidence = int((100 * (1 - predict / 300)))
                else:
                    print("No face Detected.")

                if confidence > 70:
                    cv2.rectangle(img, (startX, startY), (endX, endY), (0, 255, 0), 3)
                    
                    # Fetch details from the database
                    conn = mysql.connector.connect(host="localhost", username="root", password="Mypass123", database="face_recognizer" ,port=3307)
                    my_cursor = conn.cursor()

                    my_cursor.execute("SELECT Name FROM student WHERE Student_id=" + str(id))
                    n = my_cursor.fetchone()
                    n = '+'.join(map(str, n)) if n else ""
                

                    my_cursor.execute("SELECT Roll FROM student WHERE Student_id=" + str(id))
                    r = my_cursor.fetchone()
                    r = '+'.join(map(str, r)) if r else ""

                    my_cursor.execute("SELECT Dep FROM student WHERE Student_id=" + str(id))
                    d = my_cursor.fetchone()
                    d = '+'.join(map(str, d)) if d else ""

                    my_cursor.execute("SELECT Student_id FROM student WHERE Student_id=" + str(id))
                    i = my_cursor.fetchone()
                    i = '+'.join(map(str, i)) if i else ""
                    

                    print(i, r, n, d)

                    cv2.putText(img, f"ID:{i}", (startX, startY - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 0), 3)
                    cv2.putText(img, f"Roll:{r}", (startX, startY - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 0), 3)
                    cv2.putText(img, f"Name:{n}", (startX, startY - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 0), 3)
                    cv2.putText(img, f"Department:{d}", (startX, startY - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 0),
                                3)

                    self.mark_attendance(i, r, n, d)

                else:
                    cv2.rectangle(img, (startX, startY), (endX, endY), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (startX, startY - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8,
                                (255, 255, 255), 3)

        cv2.imshow("Face Recognition", img)

        if cv2.waitKey(1) == 13:
            self.video_cap.release()
            cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
