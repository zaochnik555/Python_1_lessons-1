#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html

"""


import sys,random

ostalos_bochonkov=90
p1=p2=15
bochonki=random.sample(range(90), 90)
nabor_bochonkov=random.sample(range(90), 30)
nabor_bochonkov_igroka=random.sample(nabor_bochonkov, 15)
nabor_bochonkov_computera=[e for e in nabor_bochonkov if not e in nabor_bochonkov_igroka]
kartochka_igroka=[nabor_bochonkov_igroka[:5], nabor_bochonkov_igroka[5:10], nabor_bochonkov_igroka[10:]]
kartochka_computera=[nabor_bochonkov_computera[:5], nabor_bochonkov_computera[5:10], nabor_bochonkov_computera[10:]]
for p1line in kartochka_igroka:
    p1line.sort()
    p1line.insert(random.randint(0, 4), ' ')
    p1line.insert(random.randint(0, 5), ' ')
    p1line.insert(random.randint(0, 6), ' ')
    p1line.insert(random.randint(0, 7), ' ')
for p2line in kartochka_computera:
    p2line.sort()
    p2line.insert(random.randint(0, 4), ' ')
    p2line.insert(random.randint(0, 5), ' ')
    p2line.insert(random.randint(0, 6), ' ')
    p2line.insert(random.randint(0, 7), ' ')


def print_kartochka(p):
    if p==0:
        print('{:-^26}'.format(' Карточка игрока'))
        for line1 in kartochka_igroka:
            for n1 in line1:
                print('{0:>2}'.format(n1), end=' ')
            print()
        print('{:-^26}\n'.format('-'))
    if p==1:
        print('{:-^26}'.format(' Карточка компьютера '))
        for line2 in kartochka_computera:
            for n2 in line2:
                print('{0:>2}'.format(n2), end=' ')
            print()
        print('{:-^26}\n'.format('-'))


def moveOfPlayer():
    a=input('Зачеркнуть цифру? (y/n): ')
    if a=='y':
        if bochonok in nabor_bochonkov_igroka:
            for l in kartochka_igroka:
                try:
                    l.insert(l.index(bochonok), 'XX')
                    l.pop(l.index(bochonok))
                except ValueError:
                    continue
            print('\nХорошо. Сделайте следующий ход')
            return 1
        else:
            print('\nИгра окончена')
            sys.exit()
    if a=='n':
        if bochonok in nabor_bochonkov_igroka:
            print('\nИгра окончена')
            sys.exit()
        else:
            print('\nХорошо. Сделайте следующий ход')


def moveOfComputer():

    if bochonok in nabor_bochonkov_computera:
        for i in kartochka_computera:
            try:
                i.insert(i.index(bochonok), 'XX')
                i.pop(i.index(bochonok))
            except ValueError:
                continue
        return 1


for bochonok in bochonki:
    ostalos_bochonkov-=1
    print('\nНовый бочонок: {} (осталось: {})\n'.format(bochonok, ostalos_bochonkov))
    print_kartochka(0)
    print_kartochka(1)
    if moveOfPlayer()==1:
        p1-=1
    if moveOfComputer()==1:
        p2-=1
    if p1==0:
        print('\nВы выйграли!')
        sys.exit()
    if p2==0:
        print('\nВы проиграли!')
        sys.exit()
    if ostalos_bochonkov==0:
        print('\nИгра окончена!')
        sys.exit()