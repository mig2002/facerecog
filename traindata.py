from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from detectface import detect
from move import moveq




class train_data:
    def __init__(self,root):
        self.root=root
        self.root.geometry("300x300")
        self.root.title("collect sampele")

      

         #take photo
        t_b1=Button(self.root,text="Take Photo",cursor="hand2",command=self.take_photo,font=("TIMES NEW ROMAN",14,"bold"),bg="darkblue",fg="white")
        t_b1.place(x=50,y=50,width=200,height=40)

         #choose from gallery
        t_b1=Button(self.root,text="Gallery",cursor="hand2",command=self.gallery,font=("TIMES NEW ROMAN",14,"bold"),bg="darkblue",fg="white")
        t_b1.place(x=50,y=150,width=200,height=40)



    def take_photo(self):
        self.new_windowq=Toplevel(self.root)
        self.appq=detect(self.new_windowq)
    #gallery
    def gallery(self):
        self.new_windoww=Toplevel(self.root)
        self.appw=moveq(self.new_windoww)
    



     


if __name__== "__main__":
    root=Tk()
    obj=train_data(root)
    root.mainloop()
