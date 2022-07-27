from tkinter import *
import mysql.connector
from mysql.connector import Error

conn=mysql.connector.connect(host='localhost',database='project1',user='root',password='navaneet5',port=3306)
global cursor
if conn.is_connected():
    print("connected to mySql database")

root=Tk()
root.title("Digital voting ballot")


label=Label(root,text="VOTING BALLOT",bg='orange')
label.config(font=('Aerial',20,'bold'))
label.pack(side=TOP)


   

def submit_btn():
    global var,top
    top=Toplevel(root)
    var=StringVar()
    label1=Label(top,text="VOTE TO")
    label1.config(font=('times roman',20,'bold'))
    label1.pack(side='top')
    r1=Radiobutton(top,text="SUN(Option 1)",variable=var,value=1,command=submit_it)
    r1.pack(anchor=W)
    r2=Radiobutton(top,text="TREE(Option 2)",variable=var,value=2,command=submit_it)
    r2.pack(anchor=W)
   
    
def Vote_india():
    global nameVar,IDVar
    
    frame1=Frame(root)
    frame1.pack()
    Label(frame1,text="Voter name").grid(row=0,column=0,sticky=W)
    nameVar=StringVar()
    name=Entry(frame1,textvariable=nameVar).grid(row=0,column=1,sticky=W)
    Label(frame1,text="Voter ID").grid(row=1,column=0,sticky=W)
    IDVar=StringVar()
    voterID=Entry(frame1,textvariable=IDVar).grid(row=1,column=1,sticky=W)


    frame2=Frame(root)
    frame2.pack()
    l4=Label(root,text='VOTING IS YOUR RIGHT',bg='green')
    l4.config(font=('aerial',14,'bold'))
    l4.pack()
    b1=Button(frame2,text="SUBMIT",command=submit_btn)
    b1.pack(anchor=W)

def submit_it():
    win=Toplevel(top)
    l3=Label(win,text='Congrats,You have voted!')
    l3.config(font=('Aerial',20))
    l3.pack(side=TOP)
    print('You have voted to option '+ str(var.get()))
    
    cursor=conn.cursor()
    cursor.execute('INSERT INTO vote VALUES(%s,%s,%s)',(nameVar.get(),IDVar.get(),var.get()))
    conn.commit()
    print('inserted successfully')
    cursor.close()
    conn.close()

def main():
    Vote_india();
    submit_btn()

if __name__=='__main__':
    main()

    
    
    
    
