from tkinter import *
import function
from function import *
import time
import random
root=Tk()
root.geometry("1600x800")
root.title("Book MAngement System")

text_input=StringVar()
large_fries = StringVar()
op=""

#frame
f1=Frame(root,height=400,width=1600,bg="Green")
f1.pack(side=TOP)
f2=Frame(root,height=500,width=500,bg="Sky blue")
f2.pack(side=RIGHT)
f3=Frame(root,height=900,width=500,bg="PowderBlue")
f3.pack(side=LEFT)

#label
lb1=Label(f1,font=("ALGERIAN",40),bg="blue",fg="yellow",bd=10,text="BMS")
lb1.grid()

name = StringVar()
author= StringVar()
book_no = StringVar()
isbn= StringVar()
l1=list()


def viewData():
    rows = function.show()
    lb5.delete(0,END)
    for row in rows:
        lb5.insert(END,row)

lb2=Label(f3,font=("arial",15),fg="black",bd=10,text="Name")
lb2.grid(row=0,column=0)
e2=Entry(f3,font=("arial",20),bd=15,justify="right",textvariable=name)
e2.grid(row=0, column=1)
lb3=Label(f3,font=("arial",15),fg="black",bd=10,text="Author")
lb3.grid(row=1,column=0)
e3=Entry(f3,font=("arial",20),bd=15,justify="right",textvariable=author)
e3.grid(row=1, column=1)


lb7=Label(f3,font=("arial",15),fg="black",bd=10,text="Number")
lb7.grid(row=0,column=2)
e7=Entry(f3,font=("arial",20),bd=15,justify="right",textvariable=book_no)
e7.grid(row=0, column=3)
llb8=Label(f3,font=("arial",15),fg="black",bd=10,text="ISBN")
llb8.grid(row=1,column=2)
e8=Entry(f3,font=("arial",20),bd=15,justify="right",textvariable=isbn)
e8.grid(row=1, column=3)
lb5=Listbox(f3,font=("arial",20),bd=15,justify="right")
lb5.insert(END,l1)
lb5.grid(row=2,columnspan=3)



#button
b1=Button(f2,padx=100,pady=15,bd=8,fg="Black",command=viewData,font=("arial",10),text="Show",bg="indigo")
b1.grid(row=0,column=0)
b2=Button(f2,padx=100,pady=15,bd=8,fg="Black",command=lambda:function.add(name.get(),author.get(),book_no.get(),isbn.get()),font =("arial",10),text="Add",bg="indigo")
b2.grid(row=1,column=0)
b3=Button(f2,padx=100,pady=15,bd=8,fg="Black",command=lambda:function.delete(name.get(),isbn.get()),font=("arial",10),text="Delete",bg="indigo")
b3.grid(row=2,column=0)
b4=Button(f2,padx=100,pady=15,bd=8,fg="Black",command=lambda:function.update(name.get(), isbn.get(), author.get()),font=("arial",10),text="Update",bg="indigo")
b4.grid(row=3,column=0)



#entry


root.mainloop()






