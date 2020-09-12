from tkinter import *
import string
expression=""

class NumberSYS:
    def __init__(self):
        self.m1 = Tk()
        self.m1.title("Number System Converter")
        self.m1.wm_attributes('-fullscreen','true')

        back=PhotoImage(file="back6.png")
        bk=Label(self.m1,image=back)
        bk.place(x=0,y=0,relwidth=1,relheight=1)

        exit = Button(self.m1, justify=LEFT,bg="#f15922",activebackground="#f15922")
        ex = PhotoImage(file="icon1.png")
        exit.config(image=ex, width="30", height="30", bd=0, command=self.m1.destroy)
        exit.place(x=1300, y=20)
        py = PhotoImage(file="pylogo3.png")
        py1=Button(self.m1,bg="#f15922",activebackground="#f15922",bd=0,command=self.popupmsg)
        py1.config(image=py,width="550",height="200")
        py1.place(x=120, y=150)

        st = Button(self.m1, justify=LEFT)
        pic = PhotoImage(file="start-button.png")
        st.config(image=pic, width="380", height="110", bd=0, command=self.number1)
        st.place(x=800, y=500)

        dv = Button(self.m1, justify=LEFT)
        pic3 = PhotoImage(file="develop.png")
        dv.config(image=pic3, width="150", height="150", bd=0,bg="#f15922",activebackground="#f15922",command=self.developer)
        dv.place(x=50, y=600)

        logo = PhotoImage(file="num_logo1.png")
        lg = Label(self.m1, image=logo,bg="#005367",activebackground="#005367")
        lg.place(x=750, y=250)

        Label(self.m1,text="Version:- v1.2.1",bd=0,relief="flat",bg="#005367",activebackground="#005367").place(x=1250,y=750)
        #self.m1.resizable(width=False,height=False)
        self.m1.mainloop()

    def developer(self):
        self.m1.destroy()
        self.dev=Tk()
        self.dev.wm_attributes('-fullscreen','true')
        back1 = PhotoImage(file="back7.png")
        b2= Label(self.dev,bd=10,height=20,width=20,image=back1,relief="flat")
        b2.place(x=0, y=0,relwidth=1,relheight=1)
        back = PhotoImage(file="back.png")
        B1 = Button(self.dev, image=back,bd=0,relief="flat",bg="#005367",activebackground="#005367",command=self.des_dev)
        B1.place(x=20, y=80)
        Label(self.dev,relief="solid",width=162,height=48,bg="#005367").place(x=200,y=30)
        Label(self.dev, relief="solid", width=160, height=47).place(x=205, y=38)
        Label(self.dev, relief="solid", width=157, height=22).place(x=215, y=48)
        me=PhotoImage(file="me1.png")
        me1= PhotoImage(file="me2.png")
        Label(self.dev,image=me,relief="solid", width=250, height=300).place(x=225, y=57)
        Label(self.dev, relief="solid", width=157, height=22).place(x=215, y=400)
        Label(self.dev,image=me1, relief="solid", width=250, height=300).place(x=225, y=409)
        mayank='''Name: Mayank Singh
        
Roll no: 52         Reg No: 11701562

Section: K17AP

E mail: mayank.bbs1998@gmail.com'''
        satya='''Name: Satya Sai Dirisala
        
Roll no: 53         Reg No: 11700960

Section: K17AP

E mail: satyasai272@gmail.com'''
        Label(self.dev,justify=LEFT,text=mayank, relief="flat", width=34, height=10,font=("Times New Roman", 20)).place(x=500, y=57)
        Label(self.dev, justify=LEFT, text=satya, relief="flat", width=30, height=10, font=("Times New Roman", 20)).place(x=500, y=409)
        self.dev.mainloop()

    def popupmsg(self):
        self.m1.destroy()
        self.popup = Tk()
        self.popup.wm_attributes('-fullscreen', 'true')
        #popup.geometry("700x900")
        self.popup.wm_title("!")
        back1 = PhotoImage(file="back6.png")
        b1 = Label(self.popup, bd=10, height=20, width=20, image=back1)
        b1.place(x=0, y=0, relwidth=1, relheight=1)
        NORM_FONT = ("Verdana", 12)
        msg='''Python is an interpreted high-level programming language for general-purpose 
programming. Created by Guido van Rossum and first released in 1991, 
Python has a design philosophy that emphasizes code readability, notably 
using significant whitespace. It provides constructs that enable clear 
programming on both small and large scales. In July 2018, Van Rossum stepped
down as the leader in the language community after 30 years.

Python features a dynamic type system and automatic memory management. It 
supports multiple programming paradigms, including object-oriented, imperative,
functional and procedural, and has a large and comprehensive standard library.

Python interpreters are available for many operating systems. CPython, the 
reference implementation of Python, is open source software and has a 
community-based development model, as do nearly all of Python's other 
implementations. Python and CPython are managed by the non-profit Python 
Software Foundation.'''
        Label(self.popup,text="ABOUT",font=("Arial",28),bg="#f15922",activebackground="#f15922").place(x=545,y=10)
        Label(self.popup,text="PYTHON",font=("Arial",28),bg="#005367",activebackground="#005367").place(x=690,y=10)
        Label(self.popup,justify=LEFT, text=msg, font=NORM_FONT,width=67,relief="flat",height=20,bg="#f15922",activebackground="#f15922").place(x=5,y=100)
        back=PhotoImage(file="back.png")
        B1 =Button(self.popup,image=back,bd=0, text="Okay",relief="flat",bg="#f15922",activebackground="#f15922",command=self.des_popup,font=NORM_FONT)
        B1.place(x=540,y=600)
        py=PhotoImage(file="pylogo2.png")
        py1=Label(self.popup,height=250, width=250, image=py,bg="#f15922",activebackground="#f15922").place(x=80,y=500)
        img = PhotoImage(file="Capture.png")
        img1 = Button(self.popup,relief="flat",bd=0)
        img1.config(image=img, width="270", height="490")
        img1.place(x=750, y=140)
        self.popup.mainloop()

    def des_popup(self):
        self.popup.destroy()
        NumberSYS()
    def des_dev(self):
        self.dev.destroy()
        NumberSYS()

    def number1(self):
        self.m1.destroy()
        self.number()
    def number(self):
        global expression
        expression=""
        #self.m1.destroy()
        self.m2 = Tk()
        self.m2.title("Number System Converter")
        self.m2.wm_attributes('-fullscreen','true')
        back = PhotoImage(file="back7.png")
        bk = Label(self.m2, image=back)
        bk.place(x=0, y=0, relwidth=1, relheight=1)

        exit = Button(self.m2, justify=LEFT,bg="#f15922",activebackground="#f15922")
        ex = PhotoImage(file="icon1.png")
        exit.config(image=ex, width="30", height="30", bd=0, command=self.m2.destroy)
        exit.place(x=1300, y=20)

        home = Button(self.m2, justify=LEFT, bg="#005367", activebackground="#005367",command=self.home1)
        h1 = PhotoImage(file="home.png")
        home.config(image=h1, width="130", height="130", bd=0)
        home.place(x=20, y=80)
        def help():
            help1='''Click on the arrow run button
from one of the following to start
converting from one number system to
another For Converting Binary number
system to another click on the arrow 
run button to start converting same 
for rest of other. After clicking you
will goto new window where you can 
convert number system to other forms 

For input just click on the buttons 
on which value are printed and it will
give the input and conversion will take 
place along with it.'''

            lb=Label(self.m2, bg="#005367",height="500",width="60")
            lb.place(x=170,y=0)
            lb1=Label(self.m2,text=help1,height="20",width="33",justify=LEFT,fg="white",font=("Verdana", 14), bg="#005367")
            lb1.place(x=175,y=60)
            def lb_dest():
                lb.destroy()
                lb1.destroy()
                exit1.destroy()

            exit1 = Button(self.m2,text="X",fg="white",font=(20),justify=CENTER, bg="#f15922",bd=0, activebackground="#f15922",command=lb_dest,height="1",width="2",relief="flat")
            exit1.place(x=550, y=20)



        hp = Button(self.m2, justify=LEFT, bg="#005367", activebackground="#005367",command=help)
        pic1 = PhotoImage(file="help1.png")
        hp.config(image=pic1, width="130", height="130", bd=0)
        hp.place(x=20, y=280)


        Label(self.m2, text="Binary to Others", borderwidth=0, relief="groove", width=30, height=2,font='Arial,10',bg="black",fg="white").place(x=450, y=200,bordermode=OUTSIDE)

        Label(self.m2, text="Decimal to Others", borderwidth=0, relief="groove", width=30, height=2,font='Arial,10',bg="black",fg="white").place(x=450, y=270,
                                                                                                           bordermode=OUTSIDE)
        Label(self.m2, text="Octal to Others", borderwidth=0, relief="groove", width=30, height=2,font='Arial,10',bg="black",fg="white").place(x=450, y=340,
                                                                                                           bordermode=OUTSIDE)
        Label(self.m2, text="Hexadecimal to Others", borderwidth=0, relief="groove", width=30, height=2,font='Arial,10',bg="black",fg="white").place(x=450, y=410,
                                                                                                           bordermode=OUTSIDE)
        run1 = Button(self.m2, justify=LEFT,command=self.binary,relief="groove",bg="#f15922",activebackground="#f15922")
        r1 = PhotoImage(file="next.png")
        run1.config(image=r1, width="40", height="40", bd=0)
        run1.place(x=750, y=199)

        run2 = Button(self.m2, justify=LEFT,command=self.decimal,relief="groove",bg="#f15922",activebackground="#f15922")
        r2 = PhotoImage(file="next.png")
        run2.config(image=r2, width="40", height="40", bd=0)
        run2.place(x=750, y=269)

        run3 = Button(self.m2, justify=LEFT,command=self.octal,relief="groove",bg="#f15922",activebackground="#f15922")
        r3 = PhotoImage(file="next.png")
        run3.config(image=r3, width="40", height="40", bd=0)
        run3.place(x=750, y=339)

        run4 = Button(self.m2, justify=LEFT,command=self.hexadecimal,relief="groove",bg="#f15922",activebackground="#f15922")
        r4 = PhotoImage(file="next.png")
        run4.config(image=r4, width="40", height="40", bd=0)
        run4.place(x=750, y=409)

        Label(self.m2, text="Version:- v1.2.1", bd=0, relief="flat", bg="#f15922", activebackground="#f15922").place(
            x=1250, y=750)
        self.m2.mainloop()

    def binary(self):
        self.m2.destroy()
        global expression
        self.m3 = Tk()
        self.m3.title("Binary Number System Converter")
        #self.m3.geometry("400x500")
        self.m3.wm_attributes('-fullscreen','true')
        bin_bk = PhotoImage(file="back7.png")
        bk2 = Label(self.m3, image=bin_bk)
        bk2.place(x=0, y=0, relwidth=1, relheight=1)

        exit = Button(self.m3, justify=LEFT,bg="#f15922",activebackground="#f15922")
        ex = PhotoImage(file="icon1.png")
        exit.config(image=ex, width="30", height="30", bd=0, command=self.m3.destroy)
        exit.place(x=1300, y=20)

        home = Button(self.m3, justify=LEFT,bg="#005367", activebackground="#005367",command=self.home2)
        h1 = PhotoImage(file="home.png")
        home.config(image=h1, width="130", height="130", bd=0)
        home.place(x=20, y=80)

        back = Button(self.m3, justify=LEFT,bg="#005367", activebackground="#005367",command=self.pre1)
        back1 = PhotoImage(file="back.png")
        back.config(image=back1, width="130", height="130", bd=0)
        back.place(x=20, y=280)

        info = Button(self.m3, justify=LEFT, bg="#005367", activebackground="#005367",command=self.bin_exp)
        info1 = PhotoImage(file="info.png")
        info.config(image=info1, width="130", height="130", bd=0)
        info.place(x=20, y=480)

        self.eq1=StringVar()
        Label(self.m3, text="Binary", borderwidth=0, relief="groove", width=20, height=3, bg="#005367",fg="white",font=("Verdana", 10)).place(x=200, y=200,bordermode=OUTSIDE)
        E=Entry(self.m3,state='disabled',justify=RIGHT,textvariable=self.eq1,font=('Arial,12'),background="black",fg="white")
        E.place(x=400, y=200, width="300", height="50")
        b0=PhotoImage(file="0.png")
        b1=PhotoImage(file="1.png")
        button1=Button(self.m3,bd=0,image=b1,height="70",width="70",bg="#f15922",activebackground="#f15922",command=lambda: self.bin_press(1)).place(x=400,y=280)
        button0=Button(self.m3,bd=0,image=b0,height="70",width="70",bg="#f15922",activebackground="#f15922",command=lambda: self.bin_press(0)).place(x=500,y=280)

        clr=PhotoImage(file="clear.png")
        clear = Button(self.m3,image=clr,command=self.bin_clear, height="70", width="70",bg="#f15922",activebackground="#f15922",bd=0).place(x=750,y=190)

        Label(self.m3, text="Decimal", borderwidth=0, relief="groove", width=20, height=3, bg="#005367",fg="white",font=("Verdana", 10)).place(x=250, y=400,bordermode=OUTSIDE)
        Label(self.m3, text="Octal", borderwidth=0, relief="groove", width=20, height=3, bg="#005367",fg="white",font=("Verdana", 10)).place(x=250, y=500,bordermode=OUTSIDE)
        Label(self.m3, text="Hexadecimal", borderwidth=0, relief="groove", width=20, height=3, bg="#005367",fg="white",font=("Verdana", 10)).place(x=250, y=600,bordermode=OUTSIDE)
        self.lbin=Label(self.m3, text="", borderwidth=0, relief="groove", width=20, height=2,font=('Arial,12'),background="black",fg="white").place(x=450, y=400, width="300", height="50",bordermode=OUTSIDE)
        self.loct=Label(self.m3, text="", borderwidth=0, relief="groove", width=20, height=2,font=('Arial,12'),background="black",fg="white").place(x=450, y=500, width="300", height="50",bordermode=OUTSIDE)
        self.lhex=Label(self.m3, text="", borderwidth=0, relief="groove", width=20, height=2,font=('Arial,12'),background="black",fg="white").place(x=450, y=600, width="300", height="50",bordermode=OUTSIDE)
        self.m3.mainloop()

    def bin_press(self,num):
        global expression
        expression=expression + str(num)
        self.eq1.set(expression)
        self.bin_dec()
        self.bin_oct()
        self.bin_hex()

    def bin_dec(self):
        global expression
        bdec=int(expression)
        self.var2, i, n = 0, 0, 0
        while (bdec !=0):
            dec = bdec % 10
            self.var2 = self.var2 + dec * pow(2, i)
            bdec = bdec // 10
            i += 1
        print(self.var2)
        self.print_bin_dec()

    def bin_oct(self):
        global expression
        boct=int(expression)
        self.var3, i, n = 0, 0, 0
        while (boct != 0):
            dec = boct % 10
            self.var3 = self.var3 + dec * pow(2, i)
            boct = boct // 10
            i += 1
        print(self.var3)
        boct1=self.var3
        self.var4=oct(boct1).lstrip("0o")
        print(self.var4)
        self.print_bin_oct()
    def bin_hex(self):
        global expression
        bhex = int(expression)
        self.var5, i, n = 0, 0, 0
        while (bhex != 0):
            dec = bhex % 10
            self.var5 = self.var5 + dec * pow(2, i)
            bhex = bhex // 10
            i += 1
        print(self.var5)
        bhex1=self.var5
        self.var6=hex(bhex1).lstrip("0x")
        print(self.var6)
        self.print_bin_hex()
    def print_bin_dec(self):
        l1 = self.var2
        self.lbin = Label(self.m3, text=l1, bd=0, relief="groove", width=30, height=2,font=('Arial,12'),background="black",fg="white").place(x=450, y=400,bordermode=OUTSIDE)
    def print_bin_oct(self):
        l2=self.var4
        self.loct=Label(self.m3,text=l2,bd=0,relief="groove",width=30,height=2,font=('Arial,12'),background="black",fg="white").place(x=450,y=500,bordermode=OUTSIDE)
    def print_bin_hex(self):
        l3=self.var6
        self.lhex=Label(self.m3,text=l3,bd=0,relief="groove",width=30,height=2,font=('Arial,12'),background="black",fg="white").place(x=450,y=600,bordermode=OUTSIDE)

    def bin_clear(self):
        global expression
        expression = ""
        self.eq1.set("")
        self.clear_bin_dec()
        self.clear_bin_oct()
        self.clear_bin_hex()
    def clear_bin_dec(self):
        self.lbin = Label(self.m3, text="", bd=0, relief="groove", width=20, height=2,font=('Arial,12'),background="black",fg="white").place(x=450, y=400,bordermode=OUTSIDE)
    def clear_bin_oct(self):
        self.loct = Label(self.m3, text="", bd=0, relief="groove", width=20, height=2,font=('Arial,12'),background="black",fg="white").place(x=450, y=500,bordermode=OUTSIDE)
    def clear_bin_hex(self):
        self.lhex = Label(self.m3, text="", bd=0, relief="groove", width=20, height=2,font=('Arial,12'),background="black",fg="white").place(x=450, y=600,bordermode=OUTSIDE)

    def bin_exp(self):
        e1 = Tk()
        e1.wm_attributes('-fullscreen', 'true')
        Label(e1,bg="#005367").place(x=0,y=0,relheight=1,relwidth=1)
        global expression
        print(expression)
        exit = Button(e1, justify=LEFT, bg="#005367", activebackground="#005367")
        cls = PhotoImage(master=e1, file="icon.png")
        exit.config(image=cls, width="30", height="30", bd=0, command=e1.destroy)
        exit.place(x=1300, y=20)
        Label(e1, text="EXPLANATION", font=("Verdana", 40),bg="#005367",fg="white").place(x=400, y=10)
        if expression=="":
            Label(e1, text="NONE", font=("Verdana", 30),bg="#005367",fg="white").place(x=10, y=100)
        else:
            ch=expression
            ch1=expression
            ex1 = int(expression)
            ex2, i, n, j, k, w, j1, k1, c = 0, 0, 0, 0, 0, 0, 0, 0, 0
            list = []
            list1=[]
            list2=[]
            list3=[]
            o1 = int(ch,2)
            while(ex1 !=0):
                dec = ex1 % 10
                exp=str(dec)
                ex2 = ex2 + dec * pow(2,i)
                ex1 = ex1 // 10
                exp3=" + "+"(" + exp + "x 2^" + str(i) +")"
                list.append(exp3)
                i += 1
            '''For Octal'''
            for j in range(3-(len(ch)%3)):
                ch="0" + ch
            oc=""
            while len(ch)>0:
                t=oct(int(ch[:3],2))
                t=t[2:]
                print(ch[:3],t)
                oca=ch[:3]+" -> "+str(t)+"   "
                list2.append(oca)
                oc += str(t)
                ch=ch[3:]
            print(oc)
            print(list2)
            '''For Hexadecimal'''
            for j1 in range(4-(len(ch1)%4)):
                ch1="0" + ch1
            hexa=""
            while len(ch1)>0:
                t1=hex(int(ch1[:4],2))
                t1=t1[2:]
                print(ch1[:4],t1)
                hea=ch1[:4]+" -> "+str(t1)+"   "
                list3.append(hea)
                hexa += str(t1)
                ch1=ch1[4:]
            print(hexa)

            list1=list[::-1]
            list2=" ".join(list2)
            list3=" ".join(list3)
            list1[0]=list1[0].lstrip(" + ")
            ex3="".join(list1)
            ex2=str(ex2)
            Label(e1,text="For Decimal",bg="#005367",fg="white", font=("Verdana", 20)).place(x=10,y=100)
            Label(e1,text=expression + " = " + ex3 + " = "+ex2,bg="#005367",fg="white", font=("Verdana", 16),wraplength=1300).place(x=10,y=150)
            Label(e1, text="For Octal",bg="#005367",fg="white", font=("Verdana", 20)).place(x=10, y=250)
            Label(e1,text=expression + " = " + list2+ " = "+oc,bg="#005367",fg="white", font=("Verdana", 16),wraplength=1300).place(x=10,y=300)
            Label(e1, text="For Hexadecimal", bg="#005367", fg="white", font=("Verdana", 20)).place(x=10, y=400)
            Label(e1,text=expression + " = " + list3+ " = "+hexa,bg="#005367",fg="white", font=("Verdana", 16),wraplength=1300).place(x=10,y=450)
        e1.resizable(width=False, height=False)
        e1.mainloop()






    def decimal(self):
        self.m2.destroy()
        self.m4 = Tk()
        self.m4.title("Decimal Number System Converter")
        self.m4.geometry("800x600")
        self.m4.wm_attributes('-fullscreen','true')
        dec_bk = PhotoImage(file="back7.png")
        bk2 = Label(self.m4, image=dec_bk)
        bk2.place(x=0, y=0, relwidth=1, relheight=1)

        exit = Button(self.m4,bg="#f15922",activebackground="#f15922")
        ex = PhotoImage(file="icon1.png")
        exit.config(image=ex, width="30", height="30", bd=0, command=self.m4.destroy)
        exit.place(x=1300, y=20)

        home = Button(self.m4, justify=LEFT,bg="#005367", activebackground="#005367",command=self.home3)
        h1 = PhotoImage(file="home.png")
        home.config(image=h1, width="130", height="130", bd=0)
        home.place(x=20, y=80)

        back = Button(self.m4, justify=LEFT,bg="#005367", activebackground="#005367",command=self.pre2)
        back1 = PhotoImage(file="back.png")
        back.config(image=back1, width="130", height="130", bd=0)
        back.place(x=20, y=280)

        info = Button(self.m4, justify=LEFT, bg="#005367", activebackground="#005367",command=self.dec_exp)
        info1 = PhotoImage(file="info.png")
        info.config(image=info1, width="130", height="130", bd=0)
        info.place(x=20, y=480)

        self.eq2 = StringVar()
        Label(self.m4, text="Decimal", borderwidth=0, relief="groove", width=20, height=3, bg="#005367",fg="white",font=("Verdana", 10)).place(x=200, y=200,
                                                                                                bordermode=OUTSIDE)
        E1 = Entry(self.m4,state='disabled', justify=RIGHT, textvariable=self.eq2, font=('Arial,12'), background="black", fg="white")
        E1.place(x=400, y=200, width="300", height="50")
        b0 = PhotoImage(file="0.png")
        b1 = PhotoImage(file="1.png")
        b2 = PhotoImage(file="2.png")
        b3 = PhotoImage(file="3.png")
        b4 = PhotoImage(file="4.png")
        b5 = PhotoImage(file="5.png")
        b6 = PhotoImage(file="6.png")
        b7 = PhotoImage(file="7.png")
        b8 = PhotoImage(file="8.png")
        b9 = PhotoImage(file="9.png")
        button1 = Button(self.m4,bd=0,image=b1, text='1',height="70",width="70",bg="#f15922",activebackground="#f15922", command=lambda: self.dec_press(1)).place(x=400, y=280)
        button2 = Button(self.m4,bd=0,image=b2, text='2',height="70",width="70",bg="#f15922",activebackground="#f15922", command=lambda: self.dec_press(2)).place(x=500, y=280)
        button3 = Button(self.m4,bd=0,image=b3, text='3',height="70",width="70",bg="#f15922",activebackground="#f15922", command=lambda: self.dec_press(3)).place(x=600, y=280)
        button4 = Button(self.m4,bd=0,image=b4, text='4',height="70",width="70",bg="#f15922",activebackground="#f15922", command=lambda: self.dec_press(4)).place(x=400, y=380)
        button5 = Button(self.m4,bd=0,image=b5, text='5',height="70",width="70",bg="#f15922",activebackground="#f15922", command=lambda: self.dec_press(5)).place(x=500, y=380)
        button6 = Button(self.m4,bd=0,image=b6, text='6',height="70",width="70",bg="#f15922",activebackground="#f15922", command=lambda: self.dec_press(6)).place(x=600, y=380)
        button7 = Button(self.m4,bd=0,image=b7, text='7',height="70",width="70",bg="#f15922",activebackground="#f15922", command=lambda: self.dec_press(7)).place(x=400, y=480)
        button8 = Button(self.m4,bd=0,image=b8, text='8',height="70",width="70",bg="#f15922",activebackground="#f15922", command=lambda: self.dec_press(8)).place(x=500, y=480)
        button9 = Button(self.m4,bd=0,image=b9, text='9',height="70",width="70",bg="#f15922",activebackground="#f15922", command=lambda: self.dec_press(9)).place(x=600, y=480)
        button0 = Button(self.m4,bd=0,image=b0, text='0',height="70",width="70",bg="#f15922",activebackground="#f15922", command=lambda: self.dec_press(0)).place(x=500, y=580)
        clr = PhotoImage(file="clear.png")
        clear = Button(self.m4, image=clr, command=self.dec_clear,bg="#f15922",activebackground="#f15922",bd=0, height="70", width="70").place(x=750, y=190)

        Label(self.m4, text="Binary", borderwidth=0, relief="groove", width=20, height=3, bg="#005367",fg="white",font=("Verdana", 10)).place(x=850, y=300,
                                                                                                 bordermode=OUTSIDE)
        Label(self.m4, text="Octal", borderwidth=0, relief="groove", width=20, height=3, bg="#005367",fg="white",font=("Verdana", 10)).place(x=850, y=400,
                                                                                               bordermode=OUTSIDE)
        Label(self.m4, text="Hexadecimal", borderwidth=0, relief="groove", width=20, height=3, bg="#005367",fg="white",font=("Verdana", 10)).place(x=850, y=500,
                                                                                                     bordermode=OUTSIDE)
        self.debin = Label(self.m4, text="", borderwidth=0, relief="groove", width=20, height=3,font=('Arial,12'),background="black",fg="white").place(x=1050, y=300, width="300", height="50",
                                                                                                      bordermode=OUTSIDE)
        self.deoct = Label(self.m4, text="", borderwidth=0, relief="groove", width=20, height=3,font=('Arial,12'),background="black",fg="white").place(x=1050, y=400, width="300", height="50",
                                                                                                      bordermode=OUTSIDE)
        self.dehex = Label(self.m4, text="", borderwidth=0, relief="groove", width=20, height=3,font=('Arial,12'),background="black",fg="white").place(x=1050, y=500, width="300", height="50",
                                                                                                      bordermode=OUTSIDE)
        self.m4.resizable(width=False,height=False)
        self.m4.mainloop()

    def dec_press(self, num):
        global expression
        expression = expression + str(num)
        self.eq2.set(expression)
        self.dec_bin()
        self.dec_oct()
        self.dec_hex()
    def dec_bin(self):
        global expression
        dbin=int(expression)
        self.dvar=0
        self.dvar=bin(dbin).lstrip("0b")
        print(self.dvar)
        self.print_dec_bin()
    def print_dec_bin(self):
        d1=self.dvar
        self.debin=Label(self.m4, text=d1, borderwidth=0, relief="groove",width=20, height=3,font=('Arial,12'),background="black",fg="white").place(x=1050, y=300, width="300", height="50",bordermode=OUTSIDE)
    def dec_clear(self):
        global expression
        expression=""
        self.eq2.set("")
        self.clear_dec_bin()
        self.clear_dec_oct()
        self.clear_dec_hex()
    def clear_dec_bin(self):
        self.debin = Label(self.m4, text="", borderwidth=0, relief="groove", width=20, height=3,font=('Arial,12'),background="black",fg="white").place(x=1050, y=300, width="300", height="50",bordermode=OUTSIDE)
    def dec_oct(self):
        global expression
        doct=int(expression)
        self.dvar2=0
        self.dvar2=oct(doct).lstrip("0o")
        print(self.dvar2)
        self.print_dec_oct()
    def print_dec_oct(self):
        d2 = self.dvar2
        self.deoct = Label(self.m4, text=d2, borderwidth=0, relief="groove", width=20, height=3,font=('Arial,12'),background="black",fg="white").place(x=1050, y=400, width="300", height="50",bordermode=OUTSIDE)
    def clear_dec_oct(self):
        self.deoct = Label(self.m4, text="", borderwidth=0, relief="groove", width=20, height=3,font=('Arial,12'),background="black",fg="white").place(x=1050, y=400, width="300", height="50",bordermode=OUTSIDE)
    def dec_hex(self):
        global expression
        dhex=int(expression)
        self.dvar3=0
        self.dvar3=hex(dhex).lstrip("0x")
        print(self.dvar3)
        self.print_dec_hex()
    def print_dec_hex(self):
        d3=self.dvar3
        self.dehex=Label(self.m4, text=d3, borderwidth=0, relief="groove", width=20, height=3,font=('Arial,12'),background="black",fg="white").place(x=1050, y=500, width="300", height="50",bordermode=OUTSIDE)
    def clear_dec_hex(self):
        self.deoct = Label(self.m4, text="", borderwidth=0, relief="groove", width=20, height=3,font=('Arial,12'),background="black",fg="white").place(x=1050, y=500, width="300", height="50",bordermode=OUTSIDE)

    def dec_exp(self):
        e1 = Tk()
        e1.wm_attributes('-fullscreen','true')
        Label(e1, bg="#005367").place(x=0, y=0, relheight=1, relwidth=1)
        global expression
        print(expression)
        list=[]
        list1=[]
        list2=[]
        exit = Button(e1, justify=LEFT, bg="#005367", activebackground="#005367")
        cls = PhotoImage(master=e1,file="icon.png")
        exit.config(image=cls, width="30", height="30", bd=0, command=e1.destroy)
        exit.place(x=1300, y=20)
        Label(e1, text="EXPLANATION", font=("Verdana", 40), bg="#005367", fg="white").place(x=400, y=10)
        if expression == "":
            Label(e1, text="NONE", font=("Verdana", 30), bg="#005367", fg="white").place(x=10, y=100)
        else:
            #For binary
            ex1=int(expression)
            ex2=ex1
            ex3=ex1
            ch=bin(ex1).lstrip("0b")
            ch1=oct(ex1).lstrip("0o")
            ch2=hex(ex1).lstrip("0x")
            i=1
            OCnum=0
            HXnum=[]
            while(ex1>1):
                t=ex1%2
                t1=" <- "+str(t)
                list.append(t1)
                ex1=ex1//2

            #For octal
            while(ex2!=0):
                OCnum=OCnum+(ex2%8)*i
                print(OCnum)
                t2=" <- "+str(OCnum)
                list1.append(t2)
                ex2=ex2//8
                print(ex2)
                i*=10

            j=0
            #For hexadecimal
            while(ex3!=0):
                temp=0
                temp=ex3%16
                if(temp<10):
                    #HXnum.append(chr(temp+48))
                    t3=" <- "+chr(temp+48)
                    HXnum.append(t3)
                    print(HXnum)
                    j=j+1
                else:
                    #HXnum.append(chr(temp+55))
                    t3=" <- "+chr(temp+55)
                    HXnum.append(t3)
                    print(HXnum)
                    j=j+1
                ex3=int(ex3/16)

           # print(list2[::-1])
            #print(list1[::-1])
            HXnum=HXnum[::-1]
            HXnum[0]=HXnum[0].lstrip(" <- ")
            hx="".join(HXnum)
            list1=list1[::-1]
            list1[0]=list1[0].lstrip(" <- ")
            oc1="".join(list1)
            #print(ex1)
            list.append(str(ex1))
            list=list[::-1]
            list[0]=list[0].lstrip(" <- ")
            ex="".join(list)
            Label(e1, text="For Binary", bg="#005367", fg="white", font=("Verdana", 20)).place(x=10, y=100)
            Label(e1, text=expression + " = " + ex+" = "+ch, bg="#005367", fg="white",font=("Verdana", 16),wraplength=1300).place(x=10, y=150)
            Label(e1, text="For Octal", bg="#005367", fg="white", font=("Verdana", 20)).place(x=10, y=250)
            Label(e1, text=expression + " = " + oc1 + " = " + ch1, bg="#005367", fg="white",font=("Verdana", 16)).place(x=10, y=300)
            Label(e1, text="For Hexadecimal", bg="#005367", fg="white", font=("Verdana", 20)).place(x=10, y=400)
            Label(e1, text=expression + " = " + hx + " = " + ch2.upper(), bg="#005367", fg="white",font=("Verdana", 16)).place(x=10, y=450)
        e1.resizable(width=False, height=False)
        e1.mainloop()

    def octal(self):
        self.m2.destroy()
        self.m5 = Tk()
        self.m5.title("Octal Number System Converter")
        self.m5.wm_attributes('-fullscreen','true')
        oct_bk = PhotoImage(file="back7.png")
        bk3 = Label(self.m5, image=oct_bk)
        bk3.place(x=0, y=0, relwidth=1, relheight=1)

        exit = Button(self.m5,bg="#f15922",activebackground="#f15922")
        ex = PhotoImage(file="icon1.png")
        exit.config(image=ex, width="30", height="30", bd=0, command=self.m5.destroy)
        exit.place(x=1300, y=20)

        home = Button(self.m5, justify=LEFT, bg="#005367", activebackground="#005367",command=self.home4)
        h1 = PhotoImage(file="home.png")
        home.config(image=h1, width="130", height="130", bd=0)
        home.place(x=20, y=80)

        back = Button(self.m5, justify=LEFT, bg="#005367", activebackground="#005367",command=self.pre3)
        back1 = PhotoImage(file="back.png")
        back.config(image=back1, width="130", height="130", bd=0)
        back.place(x=20, y=280)


        info = Button(self.m5, justify=LEFT, bg="#005367", activebackground="#005367")
        info1 = PhotoImage(file="info.png")
        info.config(image=info1, width="130", height="130", bd=0)
        info.place(x=20, y=480)


        self.eq3 = StringVar()
        Label(self.m5, text="Octal", borderwidth=0, relief="groove", width=20, height=3).place(x=200, y=200,
                                                                                                bordermode=OUTSIDE)
        E2 = Entry(self.m5,state='disabled', justify=RIGHT, textvariable=self.eq3, font=('Arial,12'), background="black", fg="white")
        E2.place(x=400, y=200, width="300", height="50")
        o0 = PhotoImage(file="0.png")
        o1 = PhotoImage(file="1.png")
        o2 = PhotoImage(file="2.png")
        o3 = PhotoImage(file="3.png")
        o4 = PhotoImage(file="4.png")
        o5 = PhotoImage(file="5.png")
        o6 = PhotoImage(file="6.png")
        o7 = PhotoImage(file="7.png")


        button1 = Button(self.m5, bd=0,image=o1, text='1',height="70",width="70",bg="#f15922",activebackground="#f15922", command=lambda: self.oct_press(1)).place(x=400, y=280)
        button2 = Button(self.m5, bd=0,image=o2, text='1',height="70",width="70",bg="#f15922",activebackground="#f15922", command=lambda: self.oct_press(2)).place(x=500, y=280)
        button3 = Button(self.m5, bd=0,image=o3, text='1',height="70",width="70",bg="#f15922",activebackground="#f15922", command=lambda: self.oct_press(3)).place(x=600, y=280)
        button4 = Button(self.m5, bd=0,image=o4, text='1',height="70",width="70",bg="#f15922",activebackground="#f15922", command=lambda: self.oct_press(4)).place(x=400, y=380)
        button5 = Button(self.m5, bd=0,image=o5, text='1',height="70",width="70",bg="#f15922",activebackground="#f15922", command=lambda: self.oct_press(5)).place(x=500, y=380)
        button6 = Button(self.m5, bd=0,image=o6, text='1',height="70",width="70",bg="#f15922",activebackground="#f15922", command=lambda: self.oct_press(6)).place(x=600, y=380)
        button7 = Button(self.m5, bd=0,image=o7, text='1',height="70",width="70",bg="#f15922",activebackground="#f15922", command=lambda: self.oct_press(7)).place(x=450, y=480)
        button0 = Button(self.m5, bd=0,image=o0, text='1',height="70",width="70",bg="#f15922",activebackground="#f15922", command=lambda: self.oct_press(0)).place(x=550, y=480)
        clr = PhotoImage(file="clear.png")
        clear = Button(self.m5, image=clr, command=self.oct_clear,bg="#f15922",activebackground="#f15922",bd=0, height="70", width="70").place(x=750, y=190)

        Label(self.m5, text="Binary", borderwidth=0, relief="groove", width=20, height=3, bg="#005367",fg="white",font=("Verdana", 10)).place(x=850, y=300,
                                                                                                 bordermode=OUTSIDE)
        Label(self.m5, text="Decimal", borderwidth=0, relief="groove", width=20, height=3, bg="#005367",fg="white",font=("Verdana", 10)).place(x=850, y=400,
                                                                                               bordermode=OUTSIDE)
        Label(self.m5, text="Hexadecimal", borderwidth=0, relief="groove", width=20, height=3, bg="#005367",fg="white",font=("Verdana", 10)).place(x=850, y=500,
                                                                                                     bordermode=OUTSIDE)
        self.ocbin = Label(self.m5, text="", borderwidth=0, relief="groove", width=20, height=3,font=('Arial,12'),background="black",fg="white").place(x=1050, y=300, width="300", height="50",bordermode=OUTSIDE)
        self.ocdec = Label(self.m5, text="", borderwidth=0, relief="groove", width=20, height=3,font=('Arial,12'),background="black",fg="white").place(x=1050, y=400, width="300", height="50",bordermode=OUTSIDE)
        self.ochex = Label(self.m5, text="", borderwidth=0, relief="groove", width=20, height=3,font=('Arial,12'),background="black",fg="white").place(x=1050, y=500, width="300", height="50",bordermode=OUTSIDE)
        self.m5.resizable(width=False,height=False)
        self.m5.mainloop()
    def oct_press(self, num):
        global expression
        expression = expression + str(num)
        self.eq3.set(expression)
        self.oct_dec()
        self.oct_bin()
        self.oct_hex()
    def oct_dec(self):
        global expression
        obin=expression
        self.ovar1=int(obin,8)
        print(self.ovar1)
        self.print_oct_dec()
    def oct_bin(self):
        global expression
        obin = expression
        obin1 = int(obin, 8)
        self.ovar2=bin(obin1).lstrip("0b")
        print(self.ovar2)
        self.print_oct_bin()
    def oct_hex(self):
        global expression
        ohex = expression
        ohex1 = int(ohex, 8)
        self.ovar3=hex(ohex1).lstrip("0x")
        print(self.ovar3)
        self.print_oct_hex()

    def print_oct_dec(self):
        o1=self.ovar1
        self.ocdec = Label(self.m5, text=o1, borderwidth=0, relief="groove", width=20, height=3, font=('Arial,12'),
                           background="black", fg="white").place(x=1050, y=400, width="300", height="50",
                                                                 bordermode=OUTSIDE)
    def print_oct_bin(self):
        o2=self.ovar2
        self.ocbin = Label(self.m5, text=o2, borderwidth=0, relief="groove", width=20, height=3, font=('Arial,12'),
                           background="black", fg="white").place(x=1050, y=300, width="300", height="50",
                                                                 bordermode=OUTSIDE)
    def print_oct_hex(self):
        o3=self.ovar3
        self.ochex = Label(self.m5, text=o3, borderwidth=0, relief="groove", width=20, height=3, font=('Arial,12'),
                           background="black", fg="white").place(x=1050, y=500, width="300", height="50",
                                                                 bordermode=OUTSIDE)

    def oct_clear(self):
        global expression
        expression=""
        self.eq3.set("")
        self.clear_oct_dec()
        self.clear_oct_bin()
        self.clear_oct_hex()
    def clear_oct_dec(self):
        self.ocdec = Label(self.m5, text="", borderwidth=0, relief="groove", width=20, height=3, font=('Arial,12'),
                           background="black", fg="white").place(x=1050, y=400, width="300", height="50",
                                                                 bordermode=OUTSIDE)
    def clear_oct_bin(self):
        self.ocbin = Label(self.m5, text="", borderwidth=0, relief="groove", width=20, height=3, font=('Arial,12'),
                           background="black", fg="white").place(x=1050, y=300, width="300", height="50",
                                                                 bordermode=OUTSIDE)
    def clear_oct_hex(self):
        self.ochex = Label(self.m5, text="", borderwidth=0, relief="groove", width=20, height=3, font=('Arial,12'),
                           background="black", fg="white").place(x=1050, y=500, width="300", height="50",
                                                                 bordermode=OUTSIDE)
    def hexadecimal(self):
        self.m2.destroy()
        self.m6 = Tk()
        self.m6.title("Hexadecimal Number System Converter")
        self.m6.wm_attributes('-fullscreen','true')
        hex_bk = PhotoImage(file="back7.png")
        bk4 = Label(self.m6, image=hex_bk)
        bk4.place(x=0, y=0, relwidth=1, relheight=1)

        exit = Button(self.m6,bg="#f15922",activebackground="#f15922")
        ex = PhotoImage(file="icon1.png")
        exit.config(image=ex, width="30", height="30", bd=0, command=self.m6.destroy)
        exit.place(x=1300, y=20)

        home = Button(self.m6, justify=LEFT, bg="#005367", activebackground="#005367",command=self.home5)
        h1 = PhotoImage(file="home.png")
        home.config(image=h1, width="130", height="130", bd=0)
        home.place(x=20, y=80)

        back = Button(self.m6, justify=LEFT, bg="#005367", activebackground="#005367",command=self.pre4)
        back1 = PhotoImage(file="back.png")
        back.config(image=back1, width="130", height="130", bd=0)
        back.place(x=20, y=280)

        info = Button(self.m6, justify=LEFT, bg="#005367", activebackground="#005367")
        info1 = PhotoImage(file="info.png")
        info.config(image=info1, width="130", height="130", bd=0)
        info.place(x=20, y=480)

        self.eq4 = StringVar()
        Label(self.m6, text="Hexadecimal", borderwidth=0, relief="groove", width=20, height=3).place(x=200, y=200,
                                                                                                bordermode=OUTSIDE)
        E3 = Entry(self.m6,state='disabled', justify=RIGHT, textvariable=self.eq4, font=('Arial,12'), background="black", fg="white")
        E3.place(x=400, y=200, width="300", height="50")

        b0 = PhotoImage(file="0.png")
        b1 = PhotoImage(file="1.png")
        b2 = PhotoImage(file="2.png")
        b3 = PhotoImage(file="3.png")
        b4 = PhotoImage(file="4.png")
        b5 = PhotoImage(file="5.png")
        b6 = PhotoImage(file="6.png")
        b7 = PhotoImage(file="7.png")
        b8 = PhotoImage(file="8.png")
        b9 = PhotoImage(file="9.png")
        bA = PhotoImage(file="A.png")
        bB = PhotoImage(file="B.png")
        bC = PhotoImage(file="C.png")
        bD = PhotoImage(file="D.png")
        bE = PhotoImage(file="E.png")
        bF = PhotoImage(file="F.png")

        button1 = Button(self.m6, bd=0,image=b1, text='1',height="70",width="70",bg="#f15922",activebackground="#f15922", command=lambda: self.hex_press(1)).place(x=300, y=280)
        button2 = Button(self.m6, bd=0,image=b2, text='1',height="70",width="70",bg="#f15922",activebackground="#f15922", command=lambda: self.hex_press(2)).place(x=400, y=280)
        button3 = Button(self.m6, bd=0,image=b3, text='1',height="70",width="70",bg="#f15922",activebackground="#f15922", command=lambda: self.hex_press(3)).place(x=500, y=280)
        button4 = Button(self.m6, bd=0,image=b4, text='1',height="70",width="70",bg="#f15922",activebackground="#f15922", command=lambda: self.hex_press(4)).place(x=600, y=280)
        button5 = Button(self.m6, bd=0,image=b5, text='1',height="70",width="70",bg="#f15922",activebackground="#f15922", command=lambda: self.hex_press(5)).place(x=300, y=380)
        button6 = Button(self.m6, bd=0,image=b6, text='1',height="70",width="70",bg="#f15922",activebackground="#f15922", command=lambda: self.hex_press(6)).place(x=400, y=380)
        button7 = Button(self.m6, bd=0,image=b7, text='1',height="70",width="70",bg="#f15922",activebackground="#f15922", command=lambda: self.hex_press(7)).place(x=500, y=380)
        button8 = Button(self.m6, bd=0,image=b8, text='1',height="70",width="70",bg="#f15922",activebackground="#f15922", command=lambda: self.hex_press(8)).place(x=600, y=380)
        button9 = Button(self.m6, bd=0,image=b9, text='1',height="70",width="70",bg="#f15922",activebackground="#f15922", command=lambda: self.hex_press(9)).place(x=300, y=480)
        buttonA = Button(self.m6, bd=0,image=bA, text='1',height="70",width="70",bg="#f15922",activebackground="#f15922", command=lambda: self.hex_press("A")).place(x=400, y=480)
        buttonB = Button(self.m6, bd=0,image=bB, text='1',height="70",width="70",bg="#f15922",activebackground="#f15922", command=lambda: self.hex_press("B")).place(x=500, y=480)
        buttonC = Button(self.m6, bd=0,image=bC, text='1',height="70",width="70",bg="#f15922",activebackground="#f15922", command=lambda: self.hex_press("C")).place(x=600, y=480)
        buttonD = Button(self.m6, bd=0,image=bD, text='1',height="70",width="70",bg="#f15922",activebackground="#f15922", command=lambda: self.hex_press("D")).place(x=300, y=580)
        buttonE = Button(self.m6, bd=0,image=bE, text='1',height="70",width="70",bg="#f15922",activebackground="#f15922", command=lambda: self.hex_press("E")).place(x=400, y=580)
        buttonF = Button(self.m6, bd=0,image=bF, text='1',height="70",width="70",bg="#f15922",activebackground="#f15922", command=lambda: self.hex_press("F")).place(x=500, y=580)
        button0 = Button(self.m6, bd=0,image=b0, text='1',height="70",width="70",bg="#f15922",activebackground="#f15922", command=lambda: self.hex_press(0)).place(x=600, y=580)

        clr = PhotoImage(file="clear.png")
        clear = Button(self.m6, image=clr, command=self.hex_clear, bg="#f15922", activebackground="#f15922", bd=0,
                       height="70", width="70").place(x=750, y=190)

        #clear = Button(self.m6, text='Clear', command=self.hex_clear, height=2, width=10).place(x=400, y=97)

        Label(self.m6, text="Binary", borderwidth=0, relief="groove", width=20, height=3, bg="#005367",fg="white",font=("Verdana", 10)).place(x=850, y=300,
                                                                                                 bordermode=OUTSIDE)
        Label(self.m6, text="Decimal", borderwidth=0, relief="groove", width=20, height=3, bg="#005367",fg="white",font=("Verdana", 10)).place(x=850, y=400,
                                                                                               bordermode=OUTSIDE)
        Label(self.m6, text="Octal", borderwidth=0, relief="groove", width=20, height=3, bg="#005367",fg="white",font=("Verdana", 10)).place(x=850, y=500,
                                                                                                     bordermode=OUTSIDE)
        self.hbin = Label(self.m6, text="", borderwidth=0, relief="groove", width=20, height=3,font=('Arial,12'),background="black",fg="white").place(x=1050, y=300,width="300",height="50",bordermode=OUTSIDE)
        self.hdec = Label(self.m6, text="", borderwidth=0, relief="groove", width=20, height=3,font=('Arial,12'),background="black",fg="white").place(x=1050, y=400,width="300",height="50",bordermode=OUTSIDE)
        self.hoct = Label(self.m6, text="", borderwidth=0, relief="groove", width=20, height=3,font=('Arial,12'),background="black",fg="white").place(x=1050, y=500,width="300",height="50",bordermode=OUTSIDE)
        self.m6.resizable(width=False,height=False)
        self.m6.mainloop()
    def hex_press(self, num):
        global expression
        expression = expression + str(num)
        self.eq4.set(expression)
        self.hex_dec()
        self.hex_bin()
        self.hex_oct()
    def hex_dec(self):
        global expression
        hbin=expression
        self.hvar1=int(hbin,16)
        print(self.hvar1)
        self.print_hex_dec()
    def hex_bin(self):
        global expression
        hbin = expression
        hbin1 = int(hbin, 16)
        self.hvar2=bin(hbin1).lstrip("0b")
        print(self.hvar2)
        self.print_hex_bin()
    def hex_oct(self):
        global expression
        hoct = expression
        hoct1 = int(hoct, 16)
        self.hvar3=oct(hoct1).lstrip("0o")
        print(self.hvar3)
        self.print_hex_oct()

    def print_hex_dec(self):
        h1=self.hvar1
        self.hdec = Label(self.m6, text=h1, borderwidth=0, relief="groove", width=20, height=3,font=('Arial,12'),background="black",fg="white").place(x=1050, y=400,width="300",height="50",bordermode=OUTSIDE)
    def print_hex_bin(self):
        h2=self.hvar2
        self.hbin=Label(self.m6, text=h2, borderwidth=0, relief="groove", width=20, height=3,font=('Arial,12'),background="black",fg="white").place(x=1050, y=300,width="300",height="50",bordermode=OUTSIDE)
    def print_hex_oct(self):
        h3=self.hvar3
        self.hoct = Label(self.m6, text=h3, borderwidth=0, relief="groove", width=20, height=3,font=('Arial,12'),background="black",fg="white").place(x=1050, y=500,width="300",height="50",bordermode=OUTSIDE)


    def hex_clear(self):
        global expression
        expression=""
        self.eq4.set("")
        self.clear_hex_dec()
        self.clear_hex_bin()
        self.clear_hex_oct()
    def clear_hex_bin(self):
        self.hbin = Label(self.m6, text="", borderwidth=0, relief="groove", width=20, height=3, font=('Arial,12'),
                          background="black", fg="white").place(x=1050, y=300, width="300", height="50",
                                                                bordermode=OUTSIDE)
    def clear_hex_dec(self):
        self.hdec = Label(self.m6, text="", borderwidth=0, relief="groove", width=20, height=3, font=('Arial,12'),
                          background="black", fg="white").place(x=1050, y=400, width="300", height="50",
                                                                bordermode=OUTSIDE)
    def clear_hex_oct(self):
        self.hoct = Label(self.m6, text="", borderwidth=0, relief="groove", width=20, height=3, font=('Arial,12'),
                          background="black", fg="white").place(x=1050, y=500, width="300", height="50",
                                                                bordermode=OUTSIDE)


    def home1(self):
        self.m2.destroy()
        NumberSYS()
    def home2(self):
        self.m3.destroy()
        NumberSYS()
    def home3(self):
        self.m4.destroy()
        NumberSYS()
    def home4(self):
        self.m5.destroy()
        NumberSYS()
    def home5(self):
        self.m6.destroy()
        NumberSYS()

    def pre1(self):
        self.m3.destroy()
        self.number()
    def pre2(self):
        self.m4.destroy()
        self.number()
    def pre3(self):
        self.m5.destroy()
        self.number()
    def pre4(self):
        self.m6.destroy()
        self.number()

NumberSYS()
