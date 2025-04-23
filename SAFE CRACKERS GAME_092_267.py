import tkinter as tk
from tkinter.font import Font
import random
window=tk.Tk()
window.geometry("1920x1080")
window.title("SAFE CRACKERS")
window.state("zoom")
font1=Font(family="Digital-7",size=36,weight="bold")
font2=Font(family="Myriad Pro",size=16,weight="bold")
font3=Font(family="Play",size=16,weight="bold")
topiclabel=tk.Label(window,text="Enter password (not repeat digits)",bg="light yellow",font=font3)
topiclabel.pack(side="top")
txt1=tk.Entry(window,font=("Digital-7",30,'bold'),width=10,bd=10,fg="red",bg='black')
txt1.pack()
txt2=tk.Entry(window,font=("Digital-7",30,"bold"),width=10,bd=10,fg="white",bg="black")
txt2.pack()
redlabel=tk.Label(window,text=" ",bg="red",font=font3)
redlabel.place(x=0,y=400)
txt3=tk.Entry(window,font=("Digital-7",19,'bold'),width=1,bd=3,fg="red",bg='black')
txt3.place(x=20,y=400)
yellowlabel=tk.Label(window,text=" ",bg="yellow",font=font3)
yellowlabel.place(x=0,y=440)
txt4=tk.Entry(window,font=("Digital-7",19,'bold'),width=1,bd=3,fg="yellow",bg='black')
txt4.place(x=20,y=440)
greenlabel=tk.Label(window,text=" ",bg="lime",font=font3)
greenlabel.place(x=0,y=480)
txt5=tk.Entry(window,font=("Digital-7",19,'bold'),width=1,bd=3,fg="lime",bg='black')
txt5.place(x=20,y=480)
txt6=tk.Entry(window,font=("Digital-7",19,"bold"),width=3,bd=3,fg="black",bg="white")
txt6.place(x=0,y=520)
timeslabel=tk.Label(window,text="Times",bg="powder blue",font=font3)
timeslabel.place(x=50,y=520)
deslabel1=tk.Label(window,text=" ",bg="red",font=font3)
deslabel1.place(x=0,y=700)
desred=tk.Label(window,text="The number of digits that are not in the password.",bg='powder blue',font=font3)
desred.place(x=20,y=700)
deslabel2=tk.Label(window,text=" ",bg="yellow",font=font3)
deslabel2.place(x=0,y=740)
desyellow=tk.Label(window,text="The number of digits contained in the password, but in the wrong position.",bg='powder blue',font=font3)
desyellow.place(x=20,y=740)
deslabel3=tk.Label(window,text=" ",bg="lime",font=font3)
deslabel3.place(x=0,y=780)
desgreen=tk.Label(window,text="The number of digits in the password and in the correct position.",bg='powder blue',font=font3)
desgreen.place(x=20,y=780)
txt7=tk.Entry(window,font=("Digital-7",19,"bold"),width=6,bd=3,fg="black",bg="white")
txt7.place(x=50,y=560)
timeslabel=tk.Label(window,text="key",bg="powder blue",font=font3)
timeslabel.place(x=0,y=560)
window.config(background="powder blue")

i=0
def press(num):
    global i
    txt1.insert(i,num)
    i+=1
    
def delete():
    txt1.delete(0,"end")
    txt3.delete(0,"end")
    txt4.delete(0,"end")
    txt5.delete(0,"end")
c=0
def enternum():
    global txt1
    global txt2
    global s
    global n
    global g
    global y
    global gy
    global r
    global c
    txt6.delete(0,"end")
    if lv<=3 :
        a=txt1.get()
        i=0
        c+=1
        s=[]    
        while len(s)<len(n) :
            s.insert(len(s),"R")            
        while i<len(n) :
            if n[i]==a[i] :
                
                s.pop(i)
                s.insert(i,"G")

            elif a[i] in n :
                
                s.pop(i)
                s.insert(i,"Y")
            else :
                
                s.pop(i)
                s.insert(i,"R")
            i+=1
        g = str(s.count("G")) 
        txt5.insert(i,g)
        y = str(s.count("Y"))
        txt4.insert(i,y)
        r = str(s.count("R"))
        txt3.insert(i,r)
        txt2.delete(0,"end")
        txt2.insert(0,str(a))
        txt6.insert(0,c)
        return c

def amateur():   
    global s
    global n
    global lv
    global c
    c=0
    txt6.delete(0,"end")
    txt7.delete(0,"end")
    lv=1
    numbers=random.sample(range(10),4)
    n="".join(map(str,numbers))
    print(n)
    if len(n)<4 :
        x=4-len(n)
        n="0"*x+n
        return n
    return n
    return lv    

def expert():    
    global s
    global n
    global lv
    global c
    c=0
    txt6.delete(0,"end")
    txt7.delete(0,"end")
    lv=2
    numbers=random.sample(range(10),5)
    n="".join(map(str,numbers))
    print(n)
    if len(n)<5 :
        x=5-len(n)
        n="0"*x+n
        return n
    return n
    return lv    

def master():
    global s
    global n
    global lv
    global c
    c=0
    txt6.delete(0,"end")
    txt7.delete(0,"end")
    lv=3
    numbers=random.sample(range(10),6)
    n="".join(map(str,numbers))
    print(n)
    if len(n)<6 :
        x=6-len(n)
        n="0"*x+n
        return n
    return n
    return lv

def keys():
    global n
    txt7.insert(0,n)
    
btn1=tk.Button(window,padx=14,pady=14,bd=4,bg='white',command=lambda:press(1),text="1",font=font2)
btn1.place(x=675,y=160)
btn2=tk.Button(window,padx=14,pady=14,bd=4,bg='white',command=lambda:press(2),text="2",font=font2)
btn2.place(x=735,y=160)
btn3=tk.Button(window,padx=14,pady=14,bd=4,bg='white',command=lambda:press(3),text="3",font=font2)
btn3.place(x=795,y=160)
btn4=tk.Button(window,padx=14,pady=14,bd=4,bg='white',command=lambda:press(4),text="4",font=font2)
btn4.place(x=675,y=235)
btn5=tk.Button(window,padx=14,pady=14,bd=4,bg='white',command=lambda:press(5),text="5",font=font2)
btn5.place(x=735,y=235)
btn6=tk.Button(window,padx=14,pady=14,bd=4,bg='white',command=lambda:press(6),text="6",font=font2)
btn6.place(x=795,y=235)
btn7=tk.Button(window,padx=14,pady=14,bd=4,bg='white',command=lambda:press(7),text="7",font=font2)
btn7.place(x=675,y=310)
btn8=tk.Button(window,padx=14,pady=14,bd=4,bg='white',command=lambda:press(8),text="8",font=font2)
btn8.place(x=735,y=310)
btn9=tk.Button(window,padx=14,pady=14,bd=4,bg='white',command=lambda:press(9),text="9",font=font2)
btn9.place(x=795,y=310)
btn10=tk.Button(window,padx=14,pady=14,bd=4,bg='white',command=lambda:press(0),text="0",font=font2)
btn10.place(x=735,y=385)
btn11=tk.Button(window,padx=14,pady=14,bd=4,bg='white',text="#",command=delete,font=font2)
btn11.place(x=795,y=385)
btn12=tk.Button(window,padx=14,pady=14,bd=4,bg='white',text="*",command=enternum,font=font2)
btn12.place(x=677,y=385)
btn13=tk.Button(window,text="amateur(4)",fg="black",bg="light green",command=amateur,width=10,font=font3)
btn13.place(x=0,y=0)
btn14=tk.Button(window,text="expert(5)",fg="black",bg="light gray",command=expert,width=10,font=font3)
btn14.place(x=0,y=50)
btn15=tk.Button(window,text="master(6)",fg="black",bg="light blue",command=master,width=10,font=font3)
btn15.place(x=0,y=100)
btn16=tk.Button(window,text="KEYS",fg="red",bg="white",command=keys,width=10,font=font3)
btn16.place(x=0,y=150)

window.mainloop()