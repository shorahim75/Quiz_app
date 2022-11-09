from tkinter import *
from IT_page import IT,score
from Logic_page import Logic
from MATH_page import MATH
import json
from PIL import Image,ImageTk

def register():
    registerr = Tk()
    registerr.geometry("300x450")
    registerr.title("Tkinter widgets ! ")
    registerr.config(bg='#34eb9b')
    registerr.resizable(0, 0)
    def ochir():
        if entr18.get() == '':
            label17['text'] = 'Username kiriting'
            label17['fg'] = 'red'
        elif entry1.get() == '':
            label2['text'] = 'First Name kiriting'
            label2['fg'] = 'red'
        elif entry4.get() == '':
            label3['text'] = 'Last Name kiriting'
            label3['fg'] = 'red'
        elif entry6.get() == '':
            label5['text'] = 'Phone Number kiriting'
            label5['fg'] = 'red'
        elif entry8.get() == '' or '@' not in entry8.get():
            label7['text'] = 'E-Mail kiriting'
            label7['fg'] = 'red'
        elif entry10.get() == '':
            label9['text'] = 'Password kiriting'
            label9['fg'] = 'red'
        elif entry12.get() == '':
            label11['text'] = 'Conf_password kiriting'
            label11['fg'] = 'red'
        elif entry12.get() == entry12.get():
            bio = {
                "name": entr18.get(),
                "first_name": entry1.get(),
                "last_name": entr18.get(),
                "phone_number": entr18.get(),
                "email": entr18.get(),
                "password": entr18.get(),
            }
            with open("register.json", 'w') as a:    
                  json.dump(bio,a)
            registerr.destroy()
            choose_page()
        
    label1 = Label(registerr, text="Registration", bg='#34eb9b', foreground='black', font=('Helvatica', 15, 'bold'))
    label1.pack()
    label17 = Label(registerr, text='Username', bg='#34eb9b', foreground='white', font=('Helvatica', 10, 'bold'))
    label17.pack(padx=10)
    entr18 = Entry(registerr)
    entr18.pack(padx=11)
    label2 = Label(registerr, text="First Name", bg='#34eb9b', foreground='white', font=('Helvatica', 10, 'bold'))
    label2.pack(padx=4)
    entry1 = Entry(registerr)
    entry1.pack(padx=5)
    label3 = Label(registerr, text="Last Name", bg='#34eb9b', foreground='white', font=('Helvatica', 10, 'bold'))
    label3.pack(padx=6)
    entry4 = Entry(registerr)
    entry4.pack(padx=7)
    label5 = Label(registerr, text="Phone Number", bg='#34eb9b', foreground='white', font=('Helvatica', 10, 'bold'))
    label5.pack(padx=8)
    entry6 = Entry(registerr)
    entry6.pack(padx=9)
    label7 = Label(registerr, text='E-Mail', bg='#34eb9b', foreground='white', font=('Helvatica', 10, 'bold'))
    label7.pack(padx=10)
    entry8 = Entry(registerr)
    entry8.pack(padx=11)
    label9 = Label(registerr, text='Password', bg='#34eb9b', foreground='white', font=('Helvatica', 10, 'bold'))
    label9.pack(padx=10)
    entry10 = Entry(registerr, show='*')
    entry10.pack(padx=11)
    label11 = Label(registerr, text='Conf_password', bg='#34eb9b', foreground='white', font=('Helvatica', 10, 'bold'))
    label11.pack(padx=10)
    entry12 = Entry(registerr, show='*')
    entry12.pack(padx=11)
    a = StringVar()
    a.set(0)
    radio = Radiobutton(registerr, text='Male', bg='#34eb9b',
    value='Male', variable=a)
    radio.place(x=60, y=380)
    radi1 = Radiobutton(registerr, text='Famale',bg='#34eb9b',
    variable=a, value='Famale')
    radi1.place(x=150, y=380)
    btn = Button(registerr,text="Next",font=('Helvatica',15,'normal'), command=ochir)
    btn.place(x=130, y=410)
    
    registerr.mainloop()
    
def choose_page():
    win = Tk()
    
    def page():
        win.destroy()
        Logic()
    def page2():
        win.destroy()
        IT()
    def page3():
        win.destroy()
        MATH()
    
    
        
    
    button = Button(win, text='Logical', width=10, height=5,command=page)
    button.pack()
    butto2 = Button(win, text='IT', width=10, height=5,command=page2)
    butto2.pack()
    butto3 = Button(win, text='Math', width=10, height=5,command=page3)
    butto3.pack()
    win.mainloop()



def score_page():
    root = Tk()
    root.geometry('600x500')


    frame1 = Frame(root, width=300,height=500,bg='red')
    frame1.place(x=0, y=0)

    frame2 = Frame(root, width=300,height=500,bg='green')
    frame2.place(x=300, y=0)

    rasm = Image.open('rasmmm.jpg').resize((200,200))
    image = ImageTk.PhotoImage(rasm)
    label = Label(frame1,image=image)
    label.place(x=40, y=90)

    with open('register.json','r') as a:
        w = json.load(a)

    r=30
    for k,v in w. items():
        label = Label(frame2,text=f"{k}: {v}",bg='green',fg='white')
        label.place(x=25, y=r)
        r += 30


    togri_javoblar = 0
    notogri_javoblar = 0
    for k,v in score.items():
        if v == "Tog'ri":
            togri_javoblar += 1
        else:
            notogri_javoblar += 1
        label2 = Label(frame2, text=f"Togri javoblar: {togri_javoblar}", bg='green', fg='white')
        label2.place(x=25, y=300)

        label3 = Label(frame2, text=f"Notogri javoblar: {notogri_javoblar}", bg='green', fg='white')
        label3.place(x=25, y=330)


    if togri_javoblar>=7:
        label4 = Label(frame2, text=f"Imtihon topwirildi: {notogri_javoblar}", bg='blue', fg='blue',font='bold')
        label4.place(x=45, y=360)
    else:
        label4 = Label(frame2, text=f"Imtihon topwirildi: {notogri_javoblar}", bg='green', fg='red',font='bold')
        label4.place(x=45, y=360)






    root.mainloop()

register()
score_page()






    
