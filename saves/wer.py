spis = []
s = open('Game_Main_Save.txt', 'r')
#line = len(s.read())
#s.seek(0)
for i in s:
    p = s.read()
    print(p)
    spis.append(p)

#try:
x = int(spis[0])
y = int(spis[1])
#except IndexError:
#    x = 0
#    y = 0
key = '0'
print('start')
while key != 'ex':
    key = input('wasd-управление ех-выход ')
    if key == 'w':
        y += 1
    if key == 's':
        y -= 1
    if key == 'a':
        x -= 1
    if key == 'd':
        x += 1
    print('x=',x,'\n','y=',y)
print('GAME OVER')
ws = open('Game_Main_Save.txt', 'w')
spis = ['',x,y]
n=len(spis)
for i in range(n):
    let = str(spis[i])
    ws.write(let+"\n")

s.close()
ws.close()
