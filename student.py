from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkcalendar import Calendar, DateEntry




class Student_details:
    def __init__(self,root):
        self.root1=root
        self.root1.geometry("1200x600+0+0")
        self.root1.title("Student details")



        #============================================variables=======================================================
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_name=StringVar()
        self.var_class=StringVar()
        self.var_pid=StringVar()
        self.var_dob=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()
        self.var_ph=StringVar()
        self.var_teacher=StringVar()

    



         

        #label1
        title_lbl1=Label(text="Student Details",font=("TIMES NEW ROMAN",30,"bold"),fg="black")
        title_lbl1.place(x=0,y=0,width=1200,height=45)

        #frame
        main_frame=Frame(bd=2,bg="azure2")
        main_frame.place(x=10,y=60,width=1180,height=450)
        
        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="student details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=560,height=430)

     

        #current course information
        current_course1=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current course information",font=("times new roman",12,"bold"))
        current_course1.place(x=10,y=5,width=530,height=120)

        #department
        dep_label=Label(current_course1,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0)

        dep_combo=ttk.Combobox(current_course1,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","CMPN","IT","EXTC","MECH","ELEC")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1)

          #course
        dep_label1=Label(current_course1,text="Course",font=("times new roman",12,"bold"),bg="white")
        dep_label1.grid(row=0,column=2)

        dep_combo1=ttk.Combobox(current_course1,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly")
        dep_combo1["values"]=("Select Course","FE","SE","TE","BE")
        dep_combo1.current(0)
        dep_combo1.grid(row=0,column=3)

          #year
        dep_label2=Label(current_course1,text="Year",font=("times new roman",12,"bold"),bg="white")
        dep_label2.grid(row=1,column=0,pady=20)

        dep_combo2=ttk.Combobox(current_course1,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly")
        dep_combo2["values"]=("Select Year","2020","2021","2022","2023","2024","2025")
        dep_combo2.current(0)
        dep_combo2.grid(row=1,column=1,pady=20)

          #semester
        dep_label3=Label(current_course1,text="Semester",font=("times new roman",12,"bold"),bg="white")
        dep_label3.grid(row=1,column=2,pady=20)

        dep_combo3=ttk.Combobox(current_course1,textvariable=self.var_sem,font=("times new roman",12,"bold"),state="readonly")
        dep_combo3["values"]=("Select Semester","SEM I","SEM II","SEM III","SEM IV","SEM V","SEM VI","SEM VII","SEM VIII")
        dep_combo3.current(0)
        dep_combo3.grid(row=1,column=3,pady=20)















         #class
        
        current_course2=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="class",font=("times new roman",12,"bold"))
        current_course2.place(x=10,y=125,width=530,height=220)
        #Name
        Name_1=Label(current_course2,text="Name",font=("times new roman",12,"bold"),bg="white")
        Name_1.grid(row=0,column=0)

        Name_1=ttk.Entry(current_course2,textvariable=self.var_name,width=20,font=("times new roman",12,"bold"))
        Name_1.grid(row=0,column=1)

        #class
        Name_2=Label(current_course2,text="class",font=("times new roman",12,"bold"),bg="white")
        Name_2.grid(row=0,column=3)

        dep_combo4=ttk.Combobox(current_course2,textvariable=self.var_class,font=("times new roman",12,"bold"),state="readonly")
        dep_combo4["values"]=("Select class","A","B")
        dep_combo4.current(0)
        dep_combo4.grid(row=0,column=4,pady=20)



          #pid
        Name_3=Label(current_course2,text="PID",font=("times new roman",12,"bold"),bg="white")
        Name_3.grid(row=1,column=0)

        Name_3=ttk.Entry(current_course2,width=20,textvariable=self.var_pid,font=("times new roman",12,"bold"))
        Name_3.grid(row=1,column=1)


        #   #dob
        Name_4=Label(current_course2,text="DOB",font=("times new roman",12,"bold"),bg="white")
        Name_4.grid(row=1,column=3)

        # Name_4=ttk.Entry(current_course2,width=20,font=("times new roman",12,"bold"))
        Name_4= DateEntry(current_course2, width= 20,background= "magenta3", foreground= "white",bd=2)
        Name_4.grid(row=1,column=4)


          #gender
        gender=Label(current_course2,text="Gender",font=("times new roman",12,"bold"),bg="white")
        gender.grid(row=2,column=0)

        dep_combo5=ttk.Combobox(current_course2,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly")
        dep_combo5["values"]=("Select class","M","F","T")
        dep_combo5.current(0)
        dep_combo5.grid(row=2,column=1,pady=20)


          #email
        email=Label(current_course2,text="Email",font=("times new roman",12,"bold"),bg="white")
        email.grid(row=2,column=3)

        email=ttk.Entry(current_course2,width=20,textvariable=self.var_email,font=("times new roman",12,"bold"))
        email.grid(row=2,column=4)




        #phone no
        phone=Label(current_course2,text="Phone",font=("times new roman",12,"bold"),bg="white")
        phone.grid(row=3,column=0)

        phone=ttk.Entry(current_course2,width=20,textvariable=self.var_ph,font=("times new roman",12,"bold"))
        phone.grid(row=3,column=1)
         #teacher name
        teacher=Label(current_course2,text="Teacher :",font=("times new roman",12,"bold"),bg="white")
        teacher.grid(row=3,column=3)

        teacher=ttk.Entry(current_course2,width=20,textvariable=self.var_teacher,font=("times new roman",12,"bold"))
        teacher.grid(row=3,column=4)


        #btn-frame
        btn_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,font=("times new roman",12,"bold"))
        btn_frame.place(x=10,y=350,width=530,height=44)
        #reset button

        b=Button(btn_frame,text="RESET",cursor="hand2",width=24,font=("TIMES NEW ROMAN",14,"bold"),bg="darkblue",fg="white")
        b.grid(row=0,column=0)
        

        #  #submit
        bTN=Button(btn_frame,text="SUBMIT",cursor="hand2",width=24,font=("TIMES NEW ROMAN",14,"bold"),bg="darkblue",fg="white")
        bTN.grid(row=0,column=1)
       

            #right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="student details",font=("times new roman",12,"bold"))
        right_frame.place(x=590,y=10,width=560,height=430)
           
        #+++++++++++++++++++++++++search system++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=5,width=545,height=80)

        search_label=Label(search_frame,text="Search",font=("times new roman",12,"bold"),bg="white")
        search_label.grid(row=0,column=0)
        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="readonly")
        search_combo["values"]=("Search","Name","PID")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,pady=20)
        #=========================entry=========================================
        search_entry=ttk.Entry(search_frame,width=25,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,sticky=W)
        #===============================================================================
        #frame
        btn_frame1=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,font=("times new roman",12,"bold"))
        btn_frame1.place(x=5,y=85,width=545,height=44)

        s_btn=Button(btn_frame1,text="Search",cursor="hand2",width=25,font=("TIMES NEW ROMAN",14,"bold"),bg="darkblue",fg="white")
        s_btn.grid(row=1,column=0)
        

        #  #submit
        show_btn=Button(btn_frame1,text="Show all",cursor="hand2",width=25,font=("TIMES NEW ROMAN",14,"bold"),bg="darkblue",fg="white")
        show_btn.grid(row=1,column=1)















        #+++++++++++++++++++++details===============================================
        details_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="details",font=("times new roman",12,"bold"))
        details_frame.place(x=5,y=125,width=545,height=260)


        scroll_x=ttk.Scrollbar(details_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_frame,orient=VERTICAL)

        self.stud_details=ttk.Treeview(details_frame,columns=("dep","course","year","sem","name","class","pid","dob","gender","email","ph","teacher")) 

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.stud_details.xview)
        scroll_y.config(command=self.stud_details.yview)

        self.stud_details.heading("dep",text="Department")
        self.stud_details.heading("course",text="Course")
        self.stud_details.heading("year",text="Year")
        self.stud_details.heading("sem",text="Semester")
        self.stud_details.heading("name",text="Name")
        self.stud_details.heading("class",text="Class")
        self.stud_details.heading("pid",text="PID")
        self.stud_details.heading("dob",text="DOB")
        self.stud_details.heading("gender",text="Gender")
        self.stud_details.heading("email",text="Email")
        self.stud_details.heading("ph",text="Phone")
        self.stud_details.heading("teacher",text="Teacher")

        self.stud_details["show"]="headings"

        self.stud_details.column("dep",width=100)
        self.stud_details.column("course",width=100)
        self.stud_details.column("year",width=100)
        self.stud_details.column("sem",width=100)
        self.stud_details.column("name",width=100)
        self.stud_details.column("class",width=100)
        self.stud_details.column("pid",width=100)
        self.stud_details.column("dob",width=100)
        self.stud_details.column("gender",width=100)
        self.stud_details.column("email",width=100)
        self.stud_details.column("ph",width=100)
        self.stud_details.column("teacher",width=100)


        self.stud_details.pack(fill=BOTH,expand=1)



    #==============================functions==================================


    def add_data(self):
        pass







        

if __name__== "__main__":
    root=Tk()
    obj=Student_details(root)
    root.mainloop()





