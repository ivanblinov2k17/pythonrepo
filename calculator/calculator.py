from tkinter import *

root = Tk()

e1 = Entry(width=20)
e2 = Entry(width=20)
plus = Button(text="+")
minus = Button(text='-')
div = Button(text='/')
mult = Button(text='*')
l = Label(bg='black', fg='white', width=20)


def plus_f(event):
    s1 = e1.get()
    s2 = e2.get()
    l['text'] = str(int(s1)+int(s2))


def minus_f(event):
    s1 = e1.get()
    s2 = e2.get()
    l['text'] = str(int(s1)-int(s2))


def div_f(event):
    s1 = e1.get()
    s2 = e2.get()
    l['text'] = str(int(s1)/int(s2))


def mult_f(event):
    s1 = e1.get()
    s2 = e2.get()
    l['text'] = str(int(s1)*int(s2))


plus.bind('<Button-1>', plus_f)
minus.bind('<Button-1>', minus_f)
div.bind('<Button-1>', div_f)
mult.bind('<Button-1>', mult_f)

e1.grid(row=1, column=1, columnspan=4)
e2.grid(row=2, column=1, columnspan=4)
plus.grid(row=3, column=1)
minus.grid(row=3, column=2)
div.grid(row=3, column=3)
mult.grid(row=3, column=4)
l.grid(row=4, column=1, columnspan=4)
root.mainloop()
