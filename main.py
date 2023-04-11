from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from student import Student_details
from face import face
from tkinter import messagebox as mb
import os
from traindata import train_data




class face_recognition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1200x600+0+0")
        self.root.title("Attendance")




        #bg image
        img=Image.open(r"D:\miniprojectface recoginition\images\home_page.jpeg")
        img=img.resize((1200,600),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1200,height=600)
        #logo
        l_img=Image.open(r"D:\miniprojectface recoginition\images\logo.jpg")
        l_img=l_img.resize((180,100),Image.ANTIALIAS)
        self.photol_img=ImageTk.PhotoImage(l_img)

        l_img=Label(self.root,image=self.photol_img)
        l_img.place(x=500,y=100,width=180,height=100)
        #label
        title_lbl=Label(bg_img,text="STUDENT DATA BASE USING FACE RECOGNITION AND BLOCKCHAIN",font=("TIMES NEW ROMAN",25,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1200,height=45)

        #button student details
        b1=Button(bg_img,text="Student details",cursor="hand2",command=self.student_details,font=("TIMES NEW ROMAN",14,"bold"),bg="darkblue",fg="white")
        b1.place(x=200,y=250,width=200,height=40)

         #button mark attendance
        b1=Button(bg_img,text="Mark attendance",cursor="hand2",command=self.mark_attendace,font=("TIMES NEW ROMAN",14,"bold"),bg="darkblue",fg="white")
        b1.place(x=475,y=250,width=200,height=40)

        #button view attendance
        b1=Button(bg_img,text="View attendance",cursor="hand2",command=self.open_Attendance,font=("TIMES NEW ROMAN",14,"bold"),bg="darkblue",fg="white")
        b1.place(x=750,y=250,width=200,height=40)


           #button train data
        b1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("TIMES NEW ROMAN",14,"bold"),bg="darkblue",fg="white")
        b1.place(x=200,y=400,width=200,height=40)

         #button photos
        b1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("TIMES NEW ROMAN",14,"bold"),bg="darkblue",fg="white")
        b1.place(x=475,y=400,width=200,height=40)

        #button Exit
        b1=Button(bg_img,text="Exit",cursor="hand2",command=self.iexit,font=("TIMES NEW ROMAN",14,"bold"),bg="darkblue",fg="white")
        b1.place(x=750,y=400,width=200,height=40)




    #*******************buttons function******************
    #student details
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student_details(self.new_window)
    #mark attendace
    def mark_attendace(self):
        self.new_window1=Toplevel(self.root)
        self.app=face(self.new_window1)

    #exit 
    def iexit(self):
        self.iexit1=mb.askquestion('Exit Application', 'Do you really want to exit')
        if self.iexit1 == 'yes':
            self.root.destroy()
        else:
            return
        
    #open photos
    def open_img(self):
        os.startfile("image")

    #view attendance
    def open_Attendance(self):
        os.startfile("Attendance.csv")

     #student details
    def train_data(self):
        self.new_window2=Toplevel(self.root)
        self.app=train_data(self.new_window2)






if __name__== "__main__":
    root=Tk()
    obj=face_recognition_system(root)
    root.mainloop()

