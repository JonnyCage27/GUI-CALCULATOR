#Code For GUI CALCULATOR
from tkinter import *
root=Tk()
root.geometry("1200x1200")
root.configure(background="black")
root.title("GUI Calculator ASHUTOSH KUMBHAR")
f3=Frame(root)
l2=Label(text="GUI Calculator By Ashutosh Kumbhar",fg="black",bg="gold",font="TrebuchetMS 20 bold ")
l2.pack(side=TOP,fill=X)
f3.pack()
def click(event):
    global screen_value
    text=event.widget.cget("text")
    print(text)
    if (text == "="):
        if (screen_value.get().isdigit()):
            value=int(screen_value.get())
        else:
            value=eval(screen.get())
        screen_value.set(value)
        screen.update()


    elif(text=="C"):
        screen_value.set("")
        screen.update()
    else:
        screen_value.set(screen_value.get()+text)
        screen.update()

screen_value=StringVar()
screen=Entry(root,textvariable=screen_value,font="TrebuchetMS 40 bold ",fg="gold",bg="black")
screen.pack(padx=50,pady=40,ipady=40,ipadx=70)

f=Frame(root,bg="black")
btn=Button(f,text="1",bg='black',fg='gold',font="TrebuchetMS 25 bold")
btn.pack(side=LEFT,padx=5,pady=5,ipadx=30,ipady=30)
btn.bind("<Button-1>",click)
btn=Button(f,text="2",fg='gold',font="TrebuchetMS 25 bold")
btn.pack(side=LEFT,padx=5,pady=5,ipadx=30,ipady=30)
btn.bind("<Button-1>",click)
btn=Button(f,text="3",fg='gold',font="TrebuchetMS 25 bold")
btn.pack(side=LEFT,padx=5,pady=5,ipadx=30,ipady=30)
btn.bind("<Button-1>",click)

btn=Button(f,text="+",fg='gold',font="TrebuchetMS 25 bold")
btn.pack(side=LEFT,padx=5,pady=5,ipadx=30,ipady=30)
btn.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="black")
btn=Button(f,text="4",fg='gold',font="TrebuchetMS 25 bold")
btn.pack(side=LEFT,padx=5,pady=5,ipadx=30,ipady=30)
btn.bind("<Button-1>",click)
btn=Button(f,text="5",fg='gold',font="TrebuchetMS 25 bold")
btn.pack(side=LEFT,padx=5,pady=5,ipadx=30,ipady=30)
btn.bind("<Button-1>",click)
btn=Button(f,text="6",fg='gold',font="TrebuchetMS 25 bold")
btn.pack(side=LEFT,padx=5,pady=5,ipadx=30,ipady=30)
btn.bind("<Button-1>",click)

btn=Button(f,text="-",fg='gold',font="TrebuchetMS 25 bold")
btn.pack(side=LEFT,padx=5,pady=5,ipadx=30,ipady=30)
btn.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="black")
btn=Button(f,text="7",fg='gold',font="TrebuchetMS 25 bold")
btn.pack(side=LEFT,padx=5,pady=5,ipadx=30,ipady=30)
btn.bind("<Button-1>",click)
btn=Button(f,text="8",fg='gold',font="TrebuchetMS 25 bold")
btn.pack(side=LEFT,padx=5,pady=5,ipadx=30,ipady=30)
btn.bind("<Button-1>",click)
btn=Button(f,text="9",fg='gold',font="TrebuchetMS 25 bold")
btn.pack(side=LEFT,padx=5,pady=5,ipadx=30,ipady=30)
btn.bind("<Button-1>",click)

btn=Button(f,text="*",fg='gold',font="TrebuchetMS 25 bold")
btn.pack(side=LEFT,padx=5,pady=5,ipadx=30,ipady=30)
btn.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="black")
btn=Button(f,text="C",fg='gold',font="TrebuchetMS 25 bold")
btn.pack(side=LEFT,padx=5,pady=5,ipadx=30,ipady=30)
btn.bind("<Button-1>",click)
btn=Button(f,text="0",fg='gold',font="TrebuchetMS 25 bold")
btn.pack(side=LEFT,padx=5,pady=5,ipadx=30,ipady=30)
btn.bind("<Button-1>",click)
btn=Button(f,text="=",fg='gold',font="TrebuchetMS 25 bold")
btn.pack(side=LEFT,padx=5,pady=5,ipadx=30,ipady=30)
btn.bind("<Button-1>",click)

btn=Button(f,text="%",fg='gold',font="TrebuchetMS 25 bold")
btn.pack(side=LEFT,padx=5,pady=5,ipadx=30,ipady=30)
btn.bind("<Button-1>",click)
f.pack()
f=Frame(root,bg="black")
btn=Button(f,text="!",fg='gold',font="TrebuchetMS 25 bold")
btn.pack(side=LEFT,padx=5,pady=5,ipadx=30,ipady=30)
btn.bind("<Button-1>",click)
btn=Button(f,text="00",fg='gold',font="TrebuchetMS 25 bold")
btn.pack(side=LEFT,padx=5,pady=5,ipadx=30,ipady=30)
btn.bind("<Button-1>",click)
btn=Button(f,text="000",fg='gold',font="TrebuchetMS 25 bold")
btn.pack(side=LEFT,padx=5,pady=5,ipadx=30,ipady=30)
btn.bind("<Button-1>",click)


btn=Button(f,text="/",fg='gold',font="TrebuchetMS 25 bold")
btn.pack(side=LEFT,padx=5,pady=5,ipadx=30,ipady=30)
btn.bind("<Button-1>",click)
f.pack()
f2=Frame(root)
l1=Label(text="Copyright : Ashutosh Kumbhar 2020",fg="black",bg="gold",font="TrebuchetMS 15 bold ")
l1.pack(side=BOTTOM,fill=X)
f2.pack(fill=X)

root.mainloop()
