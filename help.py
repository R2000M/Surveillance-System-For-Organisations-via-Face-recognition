from tkinter import *
import tkinter.ttk as ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="HELP DISK",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=5,y=0,width=1500,height=50)


        img_top=Image.open(r"C:\Users\Jahnavi\Desktop\Face-Recognition-for-Survelliance\main_face\helpm.jpg")
        img_top=img_top.resize((1530,840),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=0,width=1580,height=840)

         # frame
        main_frame=Frame(f_lbl,bd=2)
        main_frame.place(x=300,y=200,width=500,height=400)

        #department 
        dev_label=Label(main_frame,text="Email ID:",font=("times new roman",30,"bold"),fg="blue",bg="white")
        dev_label.place(x=0,y=5)

        dev_label=Label(main_frame,text="meghareddyn@gmail.com",font=("times new roman",24,"bold"),bg="white")
        dev_label.place(x=0,y=80)

        dev_label=Label(main_frame,text="jahnaviyadav5555@gmail.com",font=("times new roman",24,"bold"),bg="white")
        dev_label.place(x=0,y=160)

        dev_label=Label(main_frame,text="rufinamariam01@gmail.com",font=("times new roman",24,"bold"),bg="white")
        dev_label.place(x=0,y=240)

        dev_label=Label(main_frame,text="msranjitham@gmail.com",font=("times new roman",24,"bold"),bg="white")
        dev_label.place(x=0,y=320)


if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()