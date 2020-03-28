import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import *
from tkinter import messagebox

#DB
import sqlite3
import csv

root=Tk()
root.title("Registertion")
root.geometry("750x450")

style=ttk.Style(root)
style.configure("lefttab.TNotebook",tabposition='wn')

conn=sqlite3.connect("data.db")
c=conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS userdata(fname TEXT,lname TEXT,email TEXT,age TEXT,dob TEXT,addr TEXT,pno REAL)')

def add_data(fname,lname,email,age,dob,addr,pno):
     c.execute('INSERT INTO userdata(fname,lname,email,age,dob,addr,pno) VALUES (?,?,?,?,?,?,?)',(fname,lname,email,age,dob,addr,pno))   
     conn.commit()

def view():
    c.execute('SELECT * FROM userdata')
    data=c.fetchall()
    for row in data:
        tree.insert("",tk.END,values=row)

def get_single_user(fname):
    c.execute('SELECT * FROM userdata WHERE fname="{}"'.format(fname))
    #data=c.fetchall()
    return c.fetchall()
def export_as_csv():
    filename=str(ef.get())
    myfilename=filename+'.csv'
    with open(myfilename,'w') as f:
        writer=csv.writer(f)
        c.execute('SELECT * FROM userdata')
        data=c.fetchall()
        writer.writerow(['fanme','lname','email','age','dob','addr','pno'])
        writer.writerows(data)
        messagebox.showinfo(title="Registeration",message='"Exported as {}"'.format(myfilename))



#tab 1
def clear_text():
    entry_fname.delete('0',END)
    entry_dob.delete('0',END)
    entry_lname.delete('0',END)
    entry_email.delete('0',END)
    entry_age.delete('0',END)
    entry_addr.delete('0',END)
    entry_pno.delete('0',END)

def add_details():
    fname=str(entry_fname.get())
    lname=str(entry_lname.get())
    age=str(entry_age.get())
    email=str(entry_email.get())
    dob=str(entry_dob.get())
    pno=str(entry_pno.get())
    addr=str(entry_addr.get())
    add_data(fname,lname,email,age,dob,addr,pno)
    result='\n First name:{},\n Last name:{},\n Email:{},\n Age:{},\n Date Of Birthday:{},\n Phone number:{},\n Address:{},'.format(fname,lname,email,age,dob,pno,addr)
    tab1_display.insert(tk.END,result)
    messagebox.showinfo(title="registration",message="submmitted to Database")

def clear_display_result():
    tab1_display.delete('1.0',END)

#tab 2
def clear_display():
    tab2_display.delete('1.0',END)
def search_single_user():
    fname=str(es.get())
    #r=get_single_user(fname)
    tab2_display.insert(tk.END,get_single_user(fname))

def clear_entry():
    es.delete("0",END)

def export_as_xls():
    filename=str(ef.get())
    myfilename=filename+'.xls'
    with open(myfilename,'w') as f:
        writer=csv.writer(f)
        c.execute('SELECT * FROM userdata')
        data=c.fetchall()
        writer.writerow(['fanme','lname','email','age','dob','addr','pno'])
        writer.writerows(data)
        messagebox.showinfo(title="Registeration",message='"Exported as {}"'.format(myfilename))


#tab layout

tab_control=ttk.Notebook(root,style="lefttab.TNotebook")

create_table()

tab1=ttk.Frame(tab_control)
tab2=ttk.Frame(tab_control)
tab3=ttk.Frame(tab_control)
tab4=ttk.Frame(tab_control)
tab5=ttk.Frame(tab_control)

tab_control.add(tab1,text=f'{"Home":^20s}')
tab_control.add(tab2,text=f'{"View":^20s}')
tab_control.add(tab3,text=f'{"Search":^20s}')
tab_control.add(tab4,text=f'{"Export":^20s}')
tab_control.add(tab5,text=f'{"About":^20s}')


tab_control.pack(expand=1,fill="both")

l1=Label(tab1,text="Registration",padx=5,pady=5)
l1.grid(row=0,column=0)
l2=Label(tab2,text="View",padx=5,pady=5)
l2.grid(row=0,column=0)
l3=Label(tab3,text="Search",padx=5,pady=5)
l3.grid(row=0,column=0)
l4=Label(tab4,text="Export",padx=5,pady=5)
l4.grid(row=0,column=0)
l5=Label(tab5,text="About",padx=5,pady=5)
l5.config(font=("times",15))
l5.grid(row=0,column=0)


#Home
fname=StringVar()
email=StringVar()
lname=StringVar()
age=IntVar()
addr=StringVar()
pno=IntVar()
dob=StringVar()
label1=Label(tab1,text="First Name",padx=5,pady=5)
label1.grid(row=1,column=0)
entry_fname=Entry(tab1,textvariable=fname,width=50)
entry_fname.grid(row=1,column=1)

label2=Label(tab1,text="Last Name",padx=5,pady=5)
label2.grid(row=2,column=0)
entry_lname=Entry(tab1,textvariable=lname,width=50)
entry_lname.grid(row=2,column=1)

label3=Label(tab1,text="Email",padx=5,pady=5)
label3.grid(row=3,column=0)
entry_email=Entry(tab1,textvariable=email,width=50)
entry_email.grid(row=3,column=1)

label4=Label(tab1,text="age",padx=5,pady=5)
label4.grid(row=4,column=0)
entry_age=Entry(tab1,textvariable=age,width=50)
entry_age.grid(row=4,column=1)

label5=Label(tab1,text="Date Of Birth",padx=5,pady=5)
label5.grid(row=5,column=0)
entry_dob=Entry(tab1,textvariable=dob,width=50)
entry_dob.grid(row=5,column=1)

label6=Label(tab1,text="Address",padx=5,pady=5)
label6.grid(row=6,column=0)
entry_addr=Entry(tab1,textvariable=addr,width=50)
entry_addr.grid(row=6,column=1)

label7=Label(tab1,text="phone number",padx=5,pady=5)
label7.grid(row=7,column=0)
entry_pno=Entry(tab1,textvariable=pno,width=50)
entry_pno.grid(row=7,column=1)

button1=Button(tab1,text="Add",width=12,bg="blue",fg="black",command=add_details)
button1.grid(row=8,column=0,padx=5,pady=5)
button2=Button(tab1,text="Clear",width=12,bg="blue",fg="black",command=clear_text)
button2.grid(row=8,column=1,padx=5,pady=5)

#display

tab1_display=ScrolledText(tab1,height=5)
tab1_display.grid(row=10,column=0,padx=5,pady=5,columnspan=3)
button3=Button(tab1,text="Clear Display",width=12,bg="blue",fg="black",command=clear_display_result)
button3.grid(row=12,column=0,padx=5,pady=5)


#view
button_view2=Button(tab2,text="view all",width=12,bg="blue",fg="white",command=view)
button_view2.grid(row=1,column=0,padx=10,pady=10)
tree=ttk.Treeview(tab2,column=("column1","column2","column3","column4","column5","column6","column7"),show="headings")
tree.heading("#1",text="First Name")
tree.heading("#2",text="Last Name")
tree.heading("#3",text="Email")
tree.heading("#4",text="Age")
tree.heading("#5",text="Date Of Birth")
tree.heading("#6",text="Address")
tree.heading("#7",text="Phone Number")
tree.grid(row=10,column=0,columnspan=2,padx=5,pady=5)

#search

ls1=Label(tab3,text="Search Name",padx=5,pady=5)
ls1.grid(column=0,row=1)
sre=StringVar()#search_raw_entry
es=Entry(tab3,textvariable=sre,width=30)
es.grid(row=1,column=1)

button_view3=Button(tab3,text="Clear Search",width=12,bg="blue",fg="white",command=clear_entry)
button_view3.grid(row=2,column=1,padx=10,pady=10)
button_view4=Button(tab3,text="Clear Result",width=12,bg="blue",fg="white",command=clear_display)
button_view4.grid(row=2,column=2,padx=10,pady=10)
button_view5=Button(tab3,text="Search",width=12,bg="blue",fg="white",command=search_single_user)
button_view5.grid(row=1,column=2,padx=10,pady=10)
tab2_display=ScrolledText(tab3,height=5)
tab2_display.grid(row=10,column=0,columnspan=3,padx=5,pady=5)

#export
label_export1=Label(tab4,text="File Name" ,padx=5,pady=5)
label_export1.grid(column=0,row=2)
fre=StringVar()#filename_raw_entry
ef=Entry(tab4,textvariable=fre,width=30)
ef.grid(row=2,column=1)
button_export3=Button(tab4,text="To CSV",width=12,bg="blue",fg="white",command=export_as_csv)
button_export3.grid(row=3,column=1,padx=10,pady=10)
button_export4=Button(tab4,text="To XLS",width=12,bg="blue",fg="white",command=export_as_xls)
button_export4.grid(row=3,column=2,padx=10,pady=10)

#About
al=Label(tab5,text="Registration software created by Venakateh T")
al.config(font=("Times",20))
al.grid(column=1,row=1)

root.mainloop()
