

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from typing import Collection

#vasmsi - 1

root=Tk()
root.title("Attendance Analyzer")
root.iconbitmap("attendance.ico")

global stuff
s_1=0
s_2=0
s_3=0
s_4=0
s_5=0
s_6=0
s_7=0
s_8=0
s_9=0
s_10=0
attendance=[s_1,s_2,s_3,s_4,s_5,s_6,s_7,s_8,s_9,s_10]
date="dd/mm/yyyy"

#initial frame
first_frame=LabelFrame(root,padx=5,pady=5)
first_frame.grid(row=0,column=0,padx=10,pady=10)

first_frame_2=LabelFrame(root)
first_frame_2.grid(row=1,column=0)

login_label=Label(first_frame,text="Login ID:",font=('Comic Sans MS',12))
login_label.grid(row=0,column=0)
login_input=Entry(first_frame,borderwidth=5,width=30)
login_input.grid(row=0,column=1,padx=10,pady=10,columnspan=2)

password_label=Label(first_frame,text="Password:",font=('Comic Sans MS',12))
password_label.grid(row=1,column=0)
password_input=Entry(first_frame,borderwidth=5,width=30)
password_input.grid(row=1,column=1,padx=10,pady=10,columnspan=2)
password_input.config(show="*")

#raj - 2
Arshad M. Patel, [24-09-2023 15:44]
raj 2
def click(class_name,current_date):
    date=current_date
    if((class_name!="CSE A" and class_name!="CSE B" and class_name!="CSE C" and class_name!="CSE D") and date==""):
        messagebox.showerror("Error","Please enter date and select a class!")
    elif((class_name!="CSE A" and class_name!="CSE B" and class_name!="CSE C" and class_name!="CSE D") and date!=""):
        messagebox.showerror("Error","Please select a class!")
    elif((class_name=="CSE A" or class_name=="CSE B" or class_name=="CSE C" or class_name=="CSE D") and date==""):
        messagebox.showerror("Error","Please enter date!")
    else:
        new_window=Toplevel()
        new_window.title(class_name)
        new_window.iconbitmap("attendance.ico")

        #third frame
        third_frame=LabelFrame(new_window,padx=5,pady=5)
        third_frame.grid(row=0,column=0,padx=10,pady=10)

        #4
        def create_radiobuttons(student_list):
            for i in range(len(student_list)):
                student=Label(third_frame,text=student_list[i],font=('Comic Sans MS',12))
                student.grid(row=i,column=0)
        
            #radio button variables
            var1=IntVar()
            var2=IntVar()
            var3=IntVar()
            var4=IntVar()
            var5=IntVar()
            var6=IntVar()
            var7=IntVar()
            var8=IntVar()
            var9=IntVar()
            var10=IntVar()
        
            def add(value,row):
                if(int(value)==1):
                    attendance[row]=int(value)
                else:
                    attendance[row]=0
                

            radiobutton_1p=Radiobutton(third_frame,text="Present",font=('Comic Sans MS',12),variable=var1,value=1,command=lambda: add(var1.get(),0))
            radiobutton_1p.grid(row=0,column=1)
            radiobutton_1a=Radiobutton(third_frame,text="Absent",font=('Comic Sans MS',12),variable=var1,value=2,command=lambda: add(var1.get(),0))
            radiobutton_1a.grid(row=0,column=2)

            radiobutton_2p=Radiobutton(third_frame,text="Present",font=('Comic Sans MS',12),variable=var2,value=1,command=lambda: add(var2.get(),1))
            radiobutton_2p.grid(row=1,column=1)
            radiobutton_2a=Radiobutton(third_frame,text="Absent",font=('Comic Sans MS',12),variable=var2,value=2,command=lambda: add(var2.get(),1))
            radiobutton_2a.grid(row=1,column=2)

            radiobutton_3p=Radiobutton(third_frame,text="Present",font=('Comic Sans MS',12),variable=var3,value=1,command=lambda: add(var3.get(),2))
            radiobutton_3p.grid(row=2,column=1)
            radiobutton_3a=Radiobutton(third_frame,text="Absent",font=('Comic Sans MS',12),variable=var3,value=2,command=lambda: add(var3.get(),2))
            radiobutton_3a.grid(row=2,column=2)

            radiobutton_4p=Radiobutton(third_frame,text="Present",font=('Comic Sans MS',12),variable=var4,value=1,command=lambda: add(var4.get(),3))
            radiobutton_4p.grid(row=3,column=1)
            radiobutton_4a=Radiobutton(third_frame,text="Absent",font=('Comic Sans MS',12),variable=var4,value=2,command=lambda: add(var4.get(),3))
            radiobutton_4a.grid(row=3,column=2)

            radiobutton_5p=Radiobutton(third_frame,text="Present",font=('Comic Sans MS',12),variable=var5,value=1,command=lambda: add(var5.get(),4))
            radiobutton_5p.grid(row=4,column=1)
            radiobutton_5a=Radiobutton(third_frame,text="Absent",font=('Comic Sans MS',12),variable=var5,value=2,command=lambda: add(var5.get(),4))
            radiobutton_5a.grid(row=4,column=2)

            radiobutton_6p=Radiobutton(third_frame,text="Present",font=('Comic Sans MS',12),variable=var6,value=1,command=lambda: add(var6.get(),5))
            radiobutton_6p.grid(row=5,column=1)
            radiobutton_6a=Radiobutton(third_frame,text="Absent",font=('Comic Sans MS',12),variable=var6,value=2,command=lambda: add(var6.get(),5))
            radiobutton_6a.grid(row=5,column=2)
            radiobutton_7p=Radiobutton(third_frame,text="Present",font=('Comic Sans MS',12),variable=var7,value=1,command=lambda: add(var7.get(),6))
            radiobutton_7p.grid(row=6,column=1)
            radiobutton_7a=Radiobutton(third_frame,text="Absent",font=('Comic Sans MS',12),variable=var7,value=2,command=lambda: add(var7.get(),6))
            radiobutton_7a.grid(row=6,column=2)

            radiobutton_8p=Radiobutton(third_frame,text="Present",font=('Comic Sans MS',12),variable=var8,value=1,command=lambda: add(var8.get(),7))
            radiobutton_8p.grid(row=7,column=1)
            radiobutton_8a=Radiobutton(third_frame,text="Absent",font=('Comic Sans MS',12),variable=var8,value=2,command=lambda: add(var8.get(),7))
            radiobutton_8a.grid(row=7,column=2)

            radiobutton_9p=Radiobutton(third_frame,text="Present",font=('Comic Sans MS',12),variable=var9,value=1,command=lambda: add(var9.get(),8))
            radiobutton_9p.grid(row=8,column=1)
            radiobutton_9a=Radiobutton(third_frame,text="Absent",font=('Comic Sans MS',12),variable=var9,value=2,command=lambda: add(var9.get(),8))
            radiobutton_9a.grid(row=8,column=2)

            radiobutton_10p=Radiobutton(third_frame,text="Present",font=('Comic Sans MS',12),variable=var10,value=1,command=lambda: add(var10.get(),9))
            radiobutton_10p.grid(row=9,column=1)
            radiobutton_10a=Radiobutton(third_frame,text="Absent",font=('Comic Sans MS',12),variable=var10,value=2,command=lambda: add(var10.get(),9))
            radiobutton_10a.grid(row=9,column=2)


#dev - 1

#vamsi - 2

#arshad

#raj - 3
Arshad M. Patel, [24-09-2023 15:44]
raj 2
def click(class_name,current_date):
    date=current_date
    if((class_name!="CSE A" and class_name!="CSE B" and class_name!="CSE C" and class_name!="CSE D") and date==""):
        messagebox.showerror("Error","Please enter date and select a class!")
    elif((class_name!="CSE A" and class_name!="CSE B" and class_name!="CSE C" and class_name!="CSE D") and date!=""):
        messagebox.showerror("Error","Please select a class!")
    elif((class_name=="CSE A" or class_name=="CSE B" or class_name=="CSE C" or class_name=="CSE D") and date==""):
        messagebox.showerror("Error","Please enter date!")
    else:
        new_window=Toplevel()
        new_window.title(class_name)
        new_window.iconbitmap("attendance.ico")

        #third frame
        third_frame=LabelFrame(new_window,padx=5,pady=5)
        third_frame.grid(row=0,column=0,padx=10,pady=10)

        #4
        def create_radiobuttons(student_list):
            for i in range(len(student_list)):
                student=Label(third_frame,text=student_list[i],font=('Comic Sans MS',12))
                student.grid(row=i,column=0)
        
            #radio button variables
            var1=IntVar()
            var2=IntVar()
            var3=IntVar()
            var4=IntVar()
            var5=IntVar()
            var6=IntVar()
            var7=IntVar()
            var8=IntVar()
            var9=IntVar()
            var10=IntVar()
        
            def add(value,row):
                if(int(value)==1):
                    attendance[row]=int(value)
                else:
                    attendance[row]=0
                

            radiobutton_1p=Radiobutton(third_frame,text="Present",font=('Comic Sans MS',12),variable=var1,value=1,command=lambda: add(var1.get(),0))
            radiobutton_1p.grid(row=0,column=1)
            radiobutton_1a=Radiobutton(third_frame,text="Absent",font=('Comic Sans MS',12),variable=var1,value=2,command=lambda: add(var1.get(),0))
            radiobutton_1a.grid(row=0,column=2)

            radiobutton_2p=Radiobutton(third_frame,text="Present",font=('Comic Sans MS',12),variable=var2,value=1,command=lambda: add(var2.get(),1))
            radiobutton_2p.grid(row=1,column=1)
            radiobutton_2a=Radiobutton(third_frame,text="Absent",font=('Comic Sans MS',12),variable=var2,value=2,command=lambda: add(var2.get(),1))
            radiobutton_2a.grid(row=1,column=2)

            radiobutton_3p=Radiobutton(third_frame,text="Present",font=('Comic Sans MS',12),variable=var3,value=1,command=lambda: add(var3.get(),2))
            radiobutton_3p.grid(row=2,column=1)
            radiobutton_3a=Radiobutton(third_frame,text="Absent",font=('Comic Sans MS',12),variable=var3,value=2,command=lambda: add(var3.get(),2))
            radiobutton_3a.grid(row=2,column=2)

            radiobutton_4p=Radiobutton(third_frame,text="Present",font=('Comic Sans MS',12),variable=var4,value=1,command=lambda: add(var4.get(),3))
            radiobutton_4p.grid(row=3,column=1)
            radiobutton_4a=Radiobutton(third_frame,text="Absent",font=('Comic Sans MS',12),variable=var4,value=2,command=lambda: add(var4.get(),3))
            radiobutton_4a.grid(row=3,column=2)

            radiobutton_5p=Radiobutton(third_frame,text="Present",font=('Comic Sans MS',12),variable=var5,value=1,command=lambda: add(var5.get(),4))
            radiobutton_5p.grid(row=4,column=1)
            radiobutton_5a=Radiobutton(third_frame,text="Absent",font=('Comic Sans MS',12),variable=var5,value=2,command=lambda: add(var5.get(),4))
            radiobutton_5a.grid(row=4,column=2)

            radiobutton_6p=Radiobutton(third_frame,text="Present",font=('Comic Sans MS',12),variable=var6,value=1,command=lambda: add(var6.get(),5))
            radiobutton_6p.grid(row=5,column=1)
            radiobutton_6a=Radiobutton(third_frame,text="Absent",font=('Comic Sans MS',12),variable=var6,value=2,command=lambda: add(var6.get(),5))
            radiobutton_6a.grid(row=5,column=2)


        submit_frame=LabelFrame(third_frame)
        submit_frame.grid(row=10,columnspan=3)

        submit_button=Button(submit_frame,text="Submit",font=('Comic Sans MS font',10),bd=5,width=15,command=lambda: final_click(attendance))
        submit_button.pack()

#dev - 2

#aman - 4


submit_button=Button(first_frame_2,text="Submit",font=('Comic Sans MS font',10),bd=5,width=15,command=submit)
submit_button.pack()

exit_button=Button(root,text="Exit",width=9,command=root.quit)
exit_button.grid(row=10,column=0,pady=5)

root.mainloop()
