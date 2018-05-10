#desktop application using tkinter and virtual env with the help of sqlite 3
from tkinter import *
import  backend

def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])
##stting the row event for the desktop application
def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)
#updating the view option,setting what to do when you click on view
def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(),Author_text.get(),year_text.get(),ISBN_text.get()):
        list1.insert(END,row)
#same like view updating the delete command
def add_command():
    backend.insert(title_text.get(),Author_text.get(),year_text.get(),ISBN_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),Author_text.get(),year_text.get(),ISBN_text.get()))
#updating the add command
def delete_command():
    backend.delete(selected_tuple[0])
#updating the delete command
def update_command():
    backend.update(selected_tuple[0],title_text.get(),Author_text.get(),year_text.get(),ISBN_text.get())
#updating the update command
window=Tk()
window.wm_title("BookStore")

l1=Label(window,text="Title")
l1.grid(row=0,column=0)

l2=Label(window,text="Author")
l2.grid(row=0,column=2)

l3=Label(window,text="year")
l3.grid(row=1,column=0)

l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)
##putting labels on the commands
title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

Author_text=StringVar()
e2=Entry(window,textvariable=Author_text)
e2.grid(row=0,column=3)

year_text=StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)
##updating the text how to show the data from the database
ISBN_text=StringVar()
e4=Entry(window,textvariable=ISBN_text)
e4.grid(row=1,column=3)

list1=Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text="view all",width=12,command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="search entry",width=12,command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="add entry",width=12,command=add_command)
b3.grid(row=4,column=3)

b4=Button(window,text="update entry",width=12,command=update_command)
b4.grid(row=5,column=3)

b5=Button(window,text="delete entry",width=12,command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window,text="close",width=12,command=window.destroy)
b6.grid(row=7,column=3)
##adding the buttons in desktop application for all the given commands or the functions

window.mainloop()
