import random
rand=0
count=0
win_summ=0
num_cube1=0
num_cube2=0
ans = "да"
ex = False
class Cub():
    def __init__(self, num_wall_1, num_wall_2):       
        self.num_wall_1 = num_wall_1
        self.num_wall_2 = num_wall_2
    def win_rand(self):
        global win_summ
        win_summ = random.randint(2, self.num_wall_1+self.num_wall_2)
    def rand(self):
        global win_summ, num_cube1, num_cube2, ans, ex
        while ex == False:
            if ans == "да":
                num_cube1=random.randint(1, self.num_wall_1)
                num_cube2=random.randint(1, self.num_wall_2)
                print(num_cube1+num_cube2)
                if win_summ == num_cube1+num_cube2:
                    win_summ = random.randint(1, self.num_wall_1+self.num_wall_2)
                    ans=input("тебе повезло, продолжить?")
                else:
                    ans=input("продолжить?")
            elif ans == "нет":
                print("bay have a great time")
                ex = True
            elif ans == "перезапуск" or "reboot":
                win_summ = random.randint(1, self.num_wall_1+self.num_wall_2)
                num_cube1=random.randint(1, self.num_wall_1)
                num_cube2=random.randint(1, self.num_wall_2)
                print(num_cube1+num_cube2)
                ans=input("продолжить?")
                
fir_cub=Cub(6,7)
fir_cub.win_rand()
fir_cub.rand()
