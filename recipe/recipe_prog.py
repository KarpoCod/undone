#import modules

from tkinter import*
from time import*
tk=Tk()
x=tk.winfo_screenwidth()
y=tk.winfo_screenheight()
tk.geometry('{}x{}'.format(int(x*1), int(y*1)))
tk.title('Book of recipes')

#interface

main_text = Label(tk,text='Запись\чтение?',font='arial, 19')
data_path = StringVar()
vvod_entry = Entry(tk,width=30,bd=5,textvariable=data_path)
main_text.pack(expand = True, side=TOP)
vvod_entry.pack(fill=X)
#
buttonE = Button(tk, text = 'Выход', width = 50)

#variables

recipe=[]
choice=''

#func

def choice_mode(event):
    global choice
    if data_path.get() == 'запись' or 'Запись' or 'З' or 'з' or 'w' or 'W' or 'Write' or 'write' or 'Да' or 'да' or 'Д' or 'д' or 'Yes' or 'yes' or 'y' or 'Y':
        main_text.config(text='Введите название рецепта:')
        choice = 'w'
    elif data_path.get() == 'чтение' or 'Чтение' or 'ч' or 'Ч' or 'r' or 'R' or 'read' or 'Read':
        main_text.config(text='Введите название рецепта:')
        choice = 'r'
    #elif choice == 'w':
        #with open ('recipes.txt','a',encoding='utf-8') as file:
            

def exit_p(event):
    return tk.destroy()
#main code

buttonE.bind('<Button-1>', exit)
vvod_entry.focus_set()
tk.bind('<Return>', choice_mode)

tk.mainloop()
