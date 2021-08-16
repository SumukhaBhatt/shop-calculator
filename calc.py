def sub():
    a=en1.get()
    b=en2.get()
    c=en3.get()
    if c.isdigit() and b.isdigit():
        f=open("cal.txt","a")
        f.write(a+'\t'+b+'\t'+c+"\n")
        f.close()
        en1.delete(0,END)
        en2.delete(0,END)
        en3.delete(0,END)
        en2.insert(0,1)
    else:
        messagebox.showinfo("Alert","please enetr the number ")
def file():
    try:
        f=open("cal.txt","r")
        a=f.readlines()
        s=0
        for i in range(len(a)):
            pr=int(a[i].split("\t")[-1].split("\n")[0])
            qt=int(a[i].split("\t")[1])
            s=s+pr*qt
        f.close()
        l1["text"]="Amount="+str(s)
    except:
        messagebox.showinfo("Error","Nothing is there ")
from tkinter import *
from tkinter import messagebox
ob=Tk()
ob.geometry("500x300")
ob.title("calc")
ca=Frame(ob)
ca.grid()
Label(ca,text="Enter the prduct name").grid(row=0,column=0)
en1=Entry(ca,width=20)
en1.grid(row=0,column=1)
Label(ca,text="Enter the quantity").grid(row=1,column=0)
en2=Entry(ca,width=10)
en2.grid(row=1,column=1)
Label(ca,text="Enter the price").grid(row=2,column=0)
en3=Entry(ca,width=5)
en3.grid(row=2,column=1)
en2.insert(0,1)
b1=Button(ca,text="submit",command=sub)
b1.grid(row=3,column=2)
b2=Button(ca,text="Amount",command=file)
b2.grid(row=4,column=1)
l1=Label(ca,text="Amount=0")
l1.grid(row=5,column=1)
ob.mainloop()
