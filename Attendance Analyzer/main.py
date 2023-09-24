

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from typing import Collection

#vasmsi - 1

root=Tk()
root.title("Attendance Analyzer")
root.iconbitmap("attendance.ico")

#raj - 1

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

#dev - 1

#vamsi - 2

#arshad

#raj - 3

#dev - 2

#aman - 4


submit_button=Button(first_frame_2,text="Submit",font=('Comic Sans MS font',10),bd=5,width=15,command=submit)
submit_button.pack()

exit_button=Button(root,text="Exit",width=9,command=root.quit)
exit_button.grid(row=10,column=0,pady=5)

root.mainloop()