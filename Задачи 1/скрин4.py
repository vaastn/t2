import random
b=random.randint(1,3)
if b==3:
    b='бумага'
if b==2:
    b='ножницы'
if b==1:
    b='камень'
a=input('сделайте ход:')
print('компьютер выбрал:  ',b)
if a==b:
    print('ничья')
else:
    if a=='бумага':
        if b=='камень':
            print('вы выиграли')
        else:
            print('вы проиграли')
    if a=='камень':
        if b=='бумага':
            print('вы проиграли')
        else:
            print('вы выиграли')
    if a=='ножницы':
        if b=='бумага':
            print('вы выиграли')
        else:
            print('вы проиграли')