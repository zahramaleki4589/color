from tkinter import *
from tkinter import messagebox
from tkinter import ttk

screen = Tk()
screen.geometry("%dx%d+%d+%d" % (800, 400, 500, 200))
screen.title("ثبت نام")
userAll=[]
ListAll=[]

def OncklickAdd():
        queryAdd = txtcolor.get()
        Addtolist(queryAdd)
        loadData()
def Addtolist(value):
    if not Exist(value):
        ListAll.append(value)
        loadData()
    else:
        messagebox.showerror("تکراری", "تکراری است")

def loadData():
    for item in tbl.get_children():
        sel = (str(item),)
        tbl.delete(sel)
    for item in ListAll:
        tbl.insert('', "end", values=str(item))
def Exist(value):
    for item in ListAll:
        if item == value:
            return True
    else:
        return False
def cklickval():
    try:
        Value=listbox.get(listbox.curselection())
        print(Value)
    except:
        print("None cklick")

txtcolor=Entry(screen)
txtcolor.place(x=100,y=200)

btnAdd=Button(screen,text="افزودن",command=OncklickAdd)
btnAdd.place(x=150, y=250)
tbl=ttk.Treeview(screen,columns=("c1"),show="headings",height=100)
tbl.column("#1",width=80,anchor=E)
tbl.heading("#1", text="رنگ")
tbl.place(x=360,y=100)
listbox=Listbox(screen)
listbox.insert(1 ," ")
listbox.insert(2 ," ")
listbox.place(x=40,y=30)
listbox.delete(1)
listbox.bind("<Button-1>",cklickval)
screen.mainloop()
