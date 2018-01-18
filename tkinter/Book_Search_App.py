"""
when you run frontend.py code it executes the backend code also because backend is imported in this code.
"""
from tkinter import*
import backend
window = Tk()

def get_selected_row(event):  # View all functionality (Fill selected information from listbox in entry box)
    global selected_tuple
    index=listBox.curselection()[0] #To query the selection, use curselection method. It produces tuple of index
    selected_tuple= listBox.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])
def listbtn_call():
    listBox.delete(0,END) #every time you press the view all button it clears the Listbox first and then show the data available backend view()
    for row in backend.view(): # backend.view() returns list
        listBox.insert(END,row) #END insert each next fetched row at end
def search_call():
    listBox.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()): # if user type a name get() convert entry to string.
        listBox.insert(END,row)
def insert_call():
    backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    listBox.delete(0,END)
    listBox.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))#enter the values at the end of the list
def update_call():
    backend.update(selected_tuple[0],selected_tuple[1],selected_tuple[2],selected_tuple[3],selected_tuple[4])

def delete_call():
    backend.delete(selected_tuple[0])

l1 = Label(window,text="Title")
l1.grid(row=0, column=0)
l2 = Label(window,text="Year")
l2.grid(row=1, column=0)
l3 = Label(window,text="Author")
l3.grid(row=0, column=2)
l4 = Label(window,text="ISBN")
l4.grid(row=1, column=2)

title_text = StringVar()
e1 = Entry(window,textvariable=title_text)
e1.grid(row=0, column=1)
author_text = StringVar()
e2 = Entry(window,textvariable=author_text)
e2.grid(row=0, column=3)
year_text = StringVar()
e3 = Entry(window,textvariable=year_text)
e3.grid(row=1, column=1)
isbn_text = StringVar()
e4 = Entry(window,textvariable=isbn_text)
e4.grid(row=1, column=3)

listBox = Listbox(window,height=6,width=50)
listBox.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=10)

listBox.bind('<<ListboxSelect>>', get_selected_row) #bind use to bind a function to a widget event. widget_name(event_type, function_name)
# get_selected_row returns list of selected row
listBox.configure(yscrollcommand=sb1.set) #yscrollcommand allow the user to scroll the listbox vertically,
sb1.configure(command=listBox.yview) #yview is to make the listbox vertically scrollable

b1=Button(window, text="View all", width=12, command=listbtn_call)
b1.grid(row=2, column=3)
b2=Button(window, text="Search History", width=12, command=search_call)
b2.grid(row=3, column=3)
b3=Button(window, text="Add Entry", width=12, command=insert_call)
b3.grid(row=4, column=3)
b4=Button(window, text="Update", width=12, command=update_call)
b4.grid(row=5, column=3)
b5=Button(window, text="Delete", width=12, command=delete_call)
b5.grid(row=6, column=3)
b6=Button(window, text="Close", width=12)
b6.grid(row=7, column=3)

window.mainloop()
