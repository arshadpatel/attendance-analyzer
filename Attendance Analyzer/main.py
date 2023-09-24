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

        if(class_name=="CSE A"):
            attendance=[s_1,s_2,s_3,s_4,s_5,s_6,s_7,s_8,s_9,s_10]
            student_list=["20J41A0501:","20J41A0502:","20J41A0503:","20J41A0504:","20J41A0505:","20J41A0506:","20J41A0507:","20J41A0508:","20J41A0509:","20J41A0510:"]
            create_radiobuttons(student_list)

        elif(class_name=="CSE B"):
            attendance=[s_1,s_2,s_3,s_4,s_5,s_6,s_7,s_8,s_9,s_10]
            student_list=["20J41A0561:","20J41A0562:","20J41A0563:","20J41A0564:","20J41A0565:","20J41A0566:","20J41A0567:","20J41A0568:","20J41A0569:","20J41A0570:"]
            create_radiobuttons(student_list)

        elif(class_name=="CSE C"):
            attendance=[s_1,s_2,s_3,s_4,s_5,s_6,s_7,s_8,s_9,s_10]
            student_list=["20J41A05C1:","20J41A05C2:","20J41A05C3:","20J41A05C4:","20J41A05C5:","20J41A05C6:","20J41A05C7:","20J41A05C8:","20J41A05C9:","20J41A05D0:"]
            create_radiobuttons(student_list)

        else:
            attendance=[s_1,s_2,s_3,s_4,s_5,s_6,s_7,s_8,s_9,s_10]
            student_list=["20J41A05J1:","20J41A05J2:","20J41A05J3:","20J41A05J4:","20J41A05J5:","20J41A05J6:","20J41A05J7:","20J41A05J8:","20J41A05J9:","20J41A05J0:"]
            create_radiobuttons(student_list)      

        #5
        def final_click(attendance_list):
            def percentage_display(percentage_list,presentdays_list):
                third_frame.grid_forget()

                #4th frame
                fourth_frame=LabelFrame(new_window,padx=5,pady=5)
                fourth_frame.pack(padx=10,pady=10)

                heading_1=Label(fourth_frame,text="Roll Numbers",font=('Microsoft JhengHei',13,'bold'))
                heading_1.grid(row=0,column=0,pady=10,padx=3)
                for i in range(len(student_list)):
                    student=Label(fourth_frame,text=student_list[i],font=('Comic Sans MS',12))
                    student.grid(row=(i+1),column=0)

                heading_2=Label(fourth_frame,text="Days Present",font=('Microsoft JhengHei',12,'bold'))
                heading_2.grid(row=0,column=1,pady=10,padx=3)
                for i in range(1,len(presentdays_list)):
                    present=Label(fourth_frame,text=str(presentdays_list[i]),font=('Comic Sans MS',12))
                    present.grid(row=i,column=1)

                heading_3=Label(fourth_frame,text="Days Absent",font=('Microsoft JhengHei',12,'bold'))
                heading_3.grid(row=0,column=2,pady=10,padx=3)
                for i in range(1,len(presentdays_list)):
                    absent=Label(fourth_frame,text=str(presentdays_list[0]-presentdays_list[i]),font=('Comic Sans MS',12))
                    absent.grid(row=i,column=2)

                heading_4=Label(fourth_frame,text="Attendance Percentage",font=('Microsoft JhengHei',12,'bold'))
                heading_4.grid(row=0,column=3,pady=10,padx=3)
                for i in range(len(percentage_list)):
                    if(float(percentage_list[i])<70):
                        percentage_label=Label(fourth_frame,text=percentage_list[i],bg="#ff0000",font=1)
                        percentage_label.grid(row=(i+1),column=3,padx=5,pady=5)
                    elif(float(percentage_list[i])>=70 and float(percentage_list[i])<80):
                        percentage_label=Label(fourth_frame,text=percentage_list[i],bg="#ffff00",font=1)
                        percentage_label.grid(row=(i+1),column=3,padx=5,pady=5)
                    else:
                        percentage_label=Label(fourth_frame,text=percentage_list[i],bg="#3eff00",font=1)
                        percentage_label.grid(row=(i+1),column=3,padx=5,pady=5)

                #5th frame
                fifth_frame=LabelFrame(new_window)
                fifth_frame.pack()
                close_button=Button(fifth_frame,text="Close window",font=('Comic Sans MS font',10),bd=5,width=15,command=new_window.destroy)
                close_button.pack()
#vamsi - 2

            def file_update(attendance):
                def list_to_dict(list1):
                    dict_data={}
                    for i in range(0,10):
                        dict_data.update({student_list[i]:list1[i]})
                    cloud_storage(dict_data)
                        
                def filecall(classfile):
                    f=open(classfile,"r")
                    l=f.readlines()
                    f.close()
                    l1=[]
                    for i in range(0,11):
                        j=l[i].strip()
                        j=int(j)
                        l1.append(j)
                    l1[0]=l1[0]+1
                    w_days=l1[0]
                    l2=[]
                    l1[0]=str(l1[0])
                    l2.append(l1[0]+"\n")
                    rajs_percentlist=[]
                    for i in range(1,11):
                        upd=attendance[i-1]+l1[i]
                        rajs_percentlist.append(upd)
                        upd=str(upd)
                        l2.append(upd+"\n")
                    f=open(classfile,"w")
                    f.writelines(l2)
                    f.close()

                    final_percent_list=[]
                    for i in range(0,10):
                        percent=(rajs_percentlist[i]/w_days)*100
                        final_percent_list.append(percent)
                    list_to_dict(attendance)
                    return final_percent_list

                if(class_name=="CSE A"):
                    classfile="csea.txt"
                    percentage_list=filecall(classfile)
                elif(class_name=="CSE B"):
                    classfile="cseb.txt"
                    percentage_list=filecall(classfile)
                elif(class_name=="CSE C"):
                    classfile="csec.txt"
                    percentage_list=filecall(classfile)
                else:
                    classfile="csed.txt"
                    percentage_list=filecall(classfile)
                better_percentagelist=["{:.2f}".format(i) for i in percentage_list]
                f=open(classfile,"r")
                l=f.readlines()
                f.close()
                l1=[]
                for i in range(0,11):
                    j=l[i].strip()
                    j=int(j)
                    l1.append(j)

                percentage_display(better_percentagelist,l1)
                
            file_update(attendance_list)

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


def submit():
    if(login_input.get()=="" and password_input.get()==""):
        messagebox.showerror("Error","Please enter Login ID and Password!")
    elif(login_input.get()=="" and password_input.get()!=""):
        messagebox.showerror("Error","Please enter Login ID!")
    elif(login_input.get()!="" and password_input.get()==""):
        messagebox.showerror("Error","Please enter Password!")
    elif(login_input.get()!="Attendance Analyzer" or password_input.get()!="MREC"):
        messagebox.showerror("Error","Your Login ID or Password is incorrect!")
    else:
        response=messagebox.showinfo("Message","logged in successfully!!")

        if(response=="ok"):
            first_frame.grid_forget()
            first_frame_2.grid_forget()

            #2nd frame
            second_frame=LabelFrame(root,padx=5,pady=5)
            second_frame.grid(row=0,column=0,padx=10,pady=10)

            date_label=Label(second_frame,text="Date:",font=('Comic Sans MS',12))
            date_label.grid(row=0,column=0)

            date_input=Entry(second_frame,borderwidth=5,width=28)
            date_input.grid(row=0,column=1,padx=10,pady=10,columnspan=2)

            class_label=Label(second_frame,text="Class:",font=('Comic Sans MS',12))
            class_label.grid(row=1,column=0)

            var1=StringVar()
            options=Combobox(second_frame,textvariable=var1,width=26)
            options['values']=("CSE A","CSE B","CSE C","CSE D")
            options.grid(row=1,column=1,columnspan=2)

            #submit frame
            submit_frame=LabelFrame(root)
            submit_frame.grid(row=1,column=0)

            submit_button=Button(submit_frame,text="Take Attendance",font=('Comic Sans MS font',10),bd=5,width=15,command=lambda: click(options.get(),date_input.get()))
            submit_button.grid(row=2,column=1)

            date_input.delete(0,END)


submit_button=Button(first_frame_2,text="Submit",font=('Comic Sans MS font',10),bd=5,width=15,command=submit)
submit_button.pack()

exit_button=Button(root,text="Exit",width=9,command=root.quit)
exit_button.grid(row=10,column=0,pady=5)

root.mainloop()
