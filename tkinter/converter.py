from tkinter import *
top = Tk()

def converter():
    gm=float(var1.get())*1000
    text1.insert(END,gm)

    pnds=float(var1.get())*2.20462
    text2.insert(END,pnds)
    onc=float(var1.get())*35.274
    text3.insert(END,onc)
def delete():
    text1.delete(1.0,END)
    text2.delete(1.0,END)
    text3.delete(1.0,END)

label = Label(top, text="Kg", relief=RAISED, height=1, width=10)
label.grid(row=0,column=1)

var1 = StringVar()
e1 = Entry(top, textvariable=var1, relief=RAISED)
var1.set("Enter you weight")
e1.grid(row=0,column=2)

label = Label(top, textvariable="Grams", relief=RAISED, height=1, width=10)
label.grid(row=1,column=1)

text1 = Text(top, height=1, width=20)
text1.grid(row=1,column=2)

label = Label(top, textvariable="pounds", relief=RAISED, height=1, width=10)
label.grid(row=2,column=1)

text2 = Text(top, height=1, width=20)
text2.grid(row=2,column=2)

label = Label(top, text="ounces", relief=RAISED, height=1, width=10)
label.grid(row=3,column=1)

text3 = Text(top, height=1, width=20)
text3.grid(row=3,column=2)

B1=Button(top,text="Convert",command=converter)
B1.grid(row=4,column=1)
B2=Button(top,text="Clear",command=delete)
B2.grid(row=4,column=2)

top.mainloop()
