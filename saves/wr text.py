run = 1
num = 0
print('Для выхода введите "ех" и f для подсчёта кол-ва символов')
ans = input('Считать или записать?(r/s)')
while run == 1:
    if ans == 'r':
        f = open('my_file.txt', 'r')
        rd = f.read()
        print(rd)
        f.close()
        ans = input('Считать или записать?(r/s)')
    elif ans == 's':
        f = open('my_file.txt', 'a')
        wr = input('Что записать?')
        f.write(wr)
        f.close()
        ans = input('Считать или записать?(r/s)')
    elif ans == 'f':
        f = open('my_file.txt', 'r')
        count = input('Какой символ посчитать')
        n_of_let = len(f.read())
        f.seek(0)
        for i in range(n_of_let):
            let = f.read(1)
            if let == count:
                num += 1
        print(num)
        num = 0
        f.close()
        ans = input('Считать или записать?(r/s)')
    elif ans == 'ex':
        run = 0
    else:
        print ('Ответ не коректен попробуйте ещё раз')
        ans = input('Считать или записать?(r/s)')


