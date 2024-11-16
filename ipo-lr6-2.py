w = 6 
h = 5
a = 0
sum = 0
kolvo = w * h
spisok = [-15, -4, -2, -7, 0, 3, 5, 12, 9]
spisok.extend(spisok)#добавляет в конец списка 3 раза
spisok.extend(spisok)
spisok.extend(spisok)
dlina = h * w
while len(spisok) != dlina + 1:#пока ждина не равна длине + 1
    spisok.pop(dlina)#значение списка с индексом dlina
for i in range(1):#проходит i 1 раз
    for j in spisok:#проходит j по spisok
        if a == 0:
            print(j, end=' ')#написат j в конце строки
            if j % 3 != 0:
                sum+=j
        elif a % w != 0:
            print(j, end=' ')#написат j в конце строки
            if j % 3 != 0:
                sum+=j
        else:
            print(j)
            if j % 3 != 0:
                sum+=j
        a += 1
    print()
    print()
    print(sum)#выводит сумму некратных 3
