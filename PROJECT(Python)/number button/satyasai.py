from tkinter import*
from tkinter import messagebox
def close():
    mayank.destroy()
def reset():
    e1.delete(0,"end")
def window2():
    singh=Tk()
    singh.config(background="black")
    singh.mainloop()
'''def bin2dec(bits):
    n = 0
    for b in bits:
        n = (n << 1) | (b == '1')
    return n'''

def window():
    sai=Tk()
    sai.config(background="light blue")
    sai.title("Result")
    sai.geometry("1400x500")
    w1=Frame(sai)
    w1.place()
    a=int(r.get())
    A=int(var1.get())
    B=int(var2.get())
    C=int(var3.get())
    D=int(var4.get())
    E=int(e1.get())
    if (A==0 and B==0 and C==0 and D==0) or (a!=1 and a!=2 and a!=3 and a!=4):
        sai.destroy();
        msg=messagebox.showinfo("MESSAGE BOX","Plz................   Select the option")
    l1=Label(sai,text="RESULT",borderwidth=10,relief="groove",width=94,height=1)
    l1.place(x=3,y=10,bordermode=OUTSIDE)
    l1.configure(font=("Times New Roman",20,"bold"))
    Label(sai, text="Binary", borderwidth=0, relief="flat", width=20, height=2).place(x=550, y=70,bordermode=OUTSIDE)
    Label(sai, text="Decimal", borderwidth=0, relief="flat", width=20, height=2).place(x=550, y=120,bordermode=OUTSIDE)
    Label(sai, text="Octal", borderwidth=0, relief="flat", width=20, height=2).place(x=550, y=170, bordermode=OUTSIDE)
    Label(sai, text="Hexadecimal", borderwidth=0, relief="flat", width=20, height=2).place(x=550, y=220, bordermode=OUTSIDE)
    e2=Entry(sai)
    e2.place(x=700,y=70,width=150, height=33)
    e3=Entry(sai)
    e3.place(x=700,y=120,width=150, height=33)
    e4=Entry(sai)
    e4.place(x=700,y=170,width=150, height=33)
    e5=Entry(sai)
    e5.place(x=700,y=220,width=150, height=33)
    m=Button(sai,text="Explanation",command=window2)
    m.place(x=600,y=270,width=150,height=33)
    m.config(background="dark blue",font=("Times New Roman",20,"bold"),foreground="white")
    if a==1 and A==1:
        e2.insert(0,E);
    if a==1 and B==1:
        '''e3.insert(0,bin2dec(E))'''
    if a==1 and C==1:
        z=oct(E).replace("0o","")
        e4.insert(0,z)
    if a==1 and D==1:
        x=hex(E).replace("0x","")  
        e5.insert(0,z);
    if a==2 and A==1:
        x=bin(E).replace("0b","");  
        e2.insert(0,x);
    if a==2 and B==1:  
        e3.insert(0,E);
    if a==2 and C==1:
        x=oct(E).replace("0o","");  
        e4.insert(0,x);
    if a==2 and D==1:
        x=hex(E).replace("0x","");  
        e5.insert(0,x);
    if a==3 and A==1:
        z=bin(E).replace("0b","");  
        e2.insert(0,z);
    if a==3 and B==1:
        e3.insert(0,E);
    if a==3 and C==1:
        x=oct(E).replace("0o","");  
        e4.insert(0,x);
    if a==3 and D==1:
        z=hex(E).replace("0x","");  
        e5.insert(0,z);
    if a==4 and A==1:
        z=bin(E).replace("0b","");  
        e2.insert(0,z);
    if a==4 and B==1:  
        e3.insert(0,E);
    if a==4 and C==1:
        z=oct(E).replace("0o","");  
        e4.insert(0,z);
    if a==4 and D==1:
        x=hex(E).replace("0x","");  
        e5.insert(0,x);
        
mayank=Tk()
mayank.config(background="light blue")
mayank.title("Number System Converter")
mayank.geometry("1400x700")
me=Menu(mayank)
mayank.configure(menu=me)

fl=Menu(me)
me.add_cascade(label="Info",menu=fl)
fl.add_command(label="Binary Number System")
fl.add_command(label="Decimal Number System")
fl.add_command(label="Octal Number System")
fl.add_command(label="Hexadecimal Number System")
fl.add_separator()
fl.add_command(label="Exit",command=mayank.destroy)
about=Menu(me)
me.add_cascade(label="About",menu=about)
about.add_command(label="Number System Converter")
about.add_command(label="Python")

s=PhotoImage(file="ppnp.png")
k=Label(mayank,image=s)
k.place(x=0,y=0,relwidth=1,relheight=1)
l=Label(mayank,text="NUMBER CONVERTING SYSTEM",borderwidth=10,relief="groove",width=101,height=1)
l.place(x=3,y=10,bordermode=OUTSIDE)
l.configure(font=("Britannic bold",20,"bold"), foreground="black")
Label(mayank,text="Enter decimal Number  :",borderwidth=2,relief="groove",width=22,height=2).place(x=530,y=290,bordermode=OUTSIDE)
e1=Entry(mayank,bd=5)
e1.place(x=710,y=290,width=250,height=35)
r=IntVar()
Radiobutton(mayank,text="Binary",variable=r,value=1,indicatoron=0,borderwidth=2,relief="raised",bd=3,padx=20,fg="black",bg="grey",width=16).place(x=530,y=340)
Radiobutton(mayank,text="Decimal",variable=r,value=2,indicatoron=0,borderwidth=2,relief="raised",bd=3,padx=20,fg="black",bg="grey",width=16).place(x=530,y=380)
Radiobutton(mayank,text="Octal",variable=r,value=3,indicatoron=0,borderwidth=2,relief="raised",bd=3,padx=20,fg="black",bg="grey",width=16).place(x=530,y=420)
Radiobutton(mayank,text="Hexadecimal",variable=r,value=4,indicatoron=0,borderwidth=2,relief="raised",bd=3,padx=20,fg="black",bg="grey",width=16).place(x=530,y=460)
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
Checkbutton(mayank,text="Binary", variable=var1,onvalue=1,offvalue=0,borderwidth=2,relief="groove",width=20,anchor=W,padx=10).place(x=710,y=340)
Checkbutton(mayank,text="Decimal", variable=var2,onvalue=1,offvalue=0,borderwidth=2,relief="groove",width=20,anchor=W,padx=10).place(x=710,y=380)
Checkbutton(mayank,text="Octal", variable=var3,onvalue=1,offvalue=0,borderwidth=2,relief="groove",width=20,anchor=W,padx=10).place(x=710,y=420)
Checkbutton(mayank,text="Hexadecimal", variable=var4,onvalue=1,offvalue=0,borderwidth=2,relief="groove",width=20,anchor=W,padx=10).place(x=710,y=460)
c=Button(mayank,text="RESET",command=reset)
c.place(x=1050,y=300)
c.configure(background="red")
b=Button(mayank,justify = LEFT)
photo=PhotoImage(file="sub.png")
b.config(image=photo,width="200",height="40",bd=0,background="dark blue",command=window)
b.place(x=600,y=500)
ab=Button(mayank, text="BACK",command=close)
ab.config(background="red")
ab.place(x=1050,y=480)
mayank.mainloop()
