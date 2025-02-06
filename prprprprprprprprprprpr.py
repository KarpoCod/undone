from tkinter import*
import random

tk = Tk()
tk.title('kosti')
tk.geometry('1000x500')
comp=[]
us=[]
score_us=0
score_comp=0
us_comb=['one_sch', 'two_sch', 'three_sch', 'four_sch', 'five_shc', 'six_sch', 'l_st', 'h_st', 'f', 'low_gen', 'gen']
comp_comb=['one_sch', 'two_sch', 'three_sch', 'four_sch', 'five_shc', 'six_sch', 'l_st', 'h_st', 'f', 'low_gen', 'gen']
k_1=0
k_2=0
k_3=0
k_4=0
k_5=0
costi_btn= Button(tk,text='Бросить/перебросить',font=('Times New Roman',20), relief=GROOVE, borderwidth=10)
costi_btn.pack(expand=True,side = BOTTOM)
vibili=Label(tk,text='Вы уже выбили: '+str(us)+'\n'+'Вам осталось выбить: '+str(us_comb)+'\n'+'Счет'+str(score_us)+'\n'\
             +'Компьютр уже выбил: '+str(comp)+'\n'+'Компу осталось выбить: '+str(comp_comb)+'\n'+'счет: '+str(score_comp)\
             ,font=('Times New Roman',15))
vibili.pack(side=LEFT)


def prog():
    global k_1, k_2, k_3, k_4, k_5
    k_1=random.randint(1,6)
    k_2=random.randint(1,6)
    k_3=random.randint(1,6)
    k_4=random.randint(1,6)
    k_5=random.randint(1,6)
    print(k_1,k_2,k_3,k_4,k_5)
    #if int(k_1) == int(k_2) == int(k_3) or int(k_1) == int(k_2) == int(k_4)or int(k_1) == int(k_2) == int(k_5)or\
     #  int(k_1) == int(k_4) == int(k_3) or int(k_1) == int(k_5) == int(k_3) or int(k_1) == int(k_4) == int(k_5) or\
      # int(k_4) == int(k_2) == int(k_3) or int(k_5) == int(k_2) == int(k_3):
        
    if k_1 == 1 or k_3 == 1 or k_5 == 1:
        try:
            us_comb.remove('one_sch')
            us.append('1 - школа')
        except:
            pass
    elif k_1 == 2 or k_3 == 2 or k_5 == 2:
        try:
            us_comb.remove('two_sch')
            us.append('2 - школа')
        except:
            pass
    elif k_1 == 3 or k_3 == 3 or k_5 == 3:
        try:
            us_comb.remove('three_sch')
            us.append('3 - школа')
        except:
            pass
    elif k_1 == 4 or k_3 == 4 or k_5 == 4:
        try:
            us_comb.remove('four_sch')
            us.append('4 - школа')
        except:
            pass
    elif k_1 == 5 or k_3 == 5 or k_5 == 5:
        try:
            us_comb.remove('five_sch')
            us.append('5 - школа')
        except:
            pass
    elif k_1 == 6 or k_3 == 6 or k_5 == 6:
        try:
            us_comb.remove('six_sch')
            us.append('6 - школа')
        except:
            pass

vibili.config(text='Вы уже выбили: '+str(us)+'\n'+'Вам осталось выбить: '+str(us_comb)+'\n'+'Счет'+str(score_us)+'\n'\
             +'Компьютр уже выбил: '+str(comp)+'\n'+'Компу осталось выбить: '+str(comp_comb)+'\n'+'счет: '+str(score_comp))
vibili.pack()
costi_btn.bind('<Button-1>', prog())
tk.mainloop()
