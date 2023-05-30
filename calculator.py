import tkinter
from tkinter import *

root=Tk()
root.title('basic calculator')
root.geometry('500x650')
root.resizable(False,False)
root.configure(bg='#17161b')


equation=''

def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)

def percentage():
    global equation
    e = calculate()
    label_result.config(text=e/100)
    equation = e/100


def clear():
    global equation 
    equation=''
    label_result.config(text=equation)


def calculate():
    global equation
    result=''
    if equation !='':
        try:
            result= eval(str(equation))
        except Exception as e:
            print(e)
            result='error'
            equation=''
    label_result.config(text=result)
    return result    

label_result= Label(root,width=25,height=3,text='',font=('Impact',30))
label_result.pack()



Button(root,text='c', width=5,height=1,font=('arial',30,'bold'),bd=1,fg='#fff',bg='#3697f5',command=lambda: clear()).place(x=10,y=150)
Button(root,text='/', width=4,height=1,font=('arial',30,'bold'),bd=1,fg='#fff',bg='#2E2E2E',command=lambda: show('/')).place(x=150,y=150)
Button(root,text='%', width=4,height=1,font=('arial',30,'bold'),bd=1,fg='#fff',bg='#2E2E2E',command=lambda: percentage()).place(x=265,y=150)
Button(root,text='*', width=4,height=1,font=('arial',30,'bold'),bd=1,fg='#fff',bg='#2E2E2E',command=lambda: show('*')).place(x=380,y=150)


Button(root,text='7', width=5,height=1,font=('arial',30,'bold'),bd=1,fg='#fff',bg='#2E2E2E',command=lambda: show('7')).place(x=10,y=250)
Button(root,text='8', width=4,height=1,font=('arial',30,'bold'),bd=1,fg='#fff',bg='#2E2E2E',command=lambda: show('8')).place(x=150,y=250)
Button(root,text='9', width=4,height=1,font=('arial',30,'bold'),bd=1,fg='#fff',bg='#2E2E2E',command=lambda: show('9')).place(x=265,y=250)
Button(root,text='-', width=4,height=1,font=('arial',30,'bold'),bd=1,fg='#fff',bg='#2E2E2E',command=lambda: show('-')).place(x=380,y=250)

Button(root,text='4', width=5,height=1,font=('arial',30,'bold'),bd=1,fg='#fff',bg='#2E2E2E',command=lambda: show('4')).place(x=10,y=350)
Button(root,text='5', width=4,height=1,font=('arial',30,'bold'),bd=1,fg='#fff',bg='#2E2E2E',command=lambda: show('5')).place(x=150,y=350)
Button(root,text='6', width=4,height=1,font=('arial',30,'bold'),bd=1,fg='#fff',bg='#2E2E2E',command=lambda: show('6')).place(x=265,y=350)
Button(root,text='+', width=4,height=1,font=('arial',30,'bold'),bd=1,fg='#fff',bg='#2E2E2E',command=lambda: show('+')).place(x=380,y=350)


Button(root,text='1', width=5,height=1,font=('arial',30,'bold'),bd=1,fg='#fff',bg='#2E2E2E',command=lambda: show('1')).place(x=10,y=450)
Button(root,text='2', width=4,height=1,font=('arial',30,'bold'),bd=1,fg='#fff',bg='#2E2E2E',command=lambda: show('2')).place(x=150,y=450)
Button(root,text='3', width=4,height=1,font=('arial',30,'bold'),bd=1,fg='#fff',bg='#2E2E2E',command=lambda: show('3')).place(x=265,y=450)
Button(root,text='0', width=10,height=1,font=('arial',30,'bold'),bd=1,fg='#fff',bg='#2E2E2E',command=lambda: show('0')).place(x=10,y=550)


Button(root,text='.', width=4,height=1,font=('arial',30,'bold'),bd=1,fg='#fff',bg='#2E2E2E',command=lambda: show('.')).place(x=265,y=550)
Button(root,text='=', width=4,height=3,font=('arial',30,'bold'),bd=1,fg='#fff',bg='#EEEE63',command=lambda: calculate()).place(x=380,y=450)





root.mainloop()