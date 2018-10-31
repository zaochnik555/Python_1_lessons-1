# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [0, 1, 2, 3] --> [0, 1, 4, 9]
import random

print('Задание 1')
def getNewList(oldList):
    newList=[]
    for el in oldList:
        newList.append(el**2)

    return newList

list1=[random.randint(-10,10) for _ in range(10)]
list2=getNewList(list1)
print('Список с произвольными целыми числами:', list1)
print('Новый список:', list2)


# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
print('\nЗадание 2')
#list1=['apple','peach','raspberry','blackberry','strawberry','lemon','orange','coconut','kiwi','mandarin','pomelo','bananas',]
#list2=['grapefruit','pomelo','mango','kiwi','blueberry','apple','cherry','raspberry']
list1=['fruit'+str(random.randint(0,10)) for _ in range(random.randint(3,10))]
list2=['fruit'+str(random.randint(0,10)) for _ in range(random.randint(3,10))]
print('Первый список фруктов:',list1)
print('Второй список фруктов:',list2)
print('Список фруктов, присутствующих в обоих исходных списках:',list(set(list1)&set(list2)))

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 2
# + Элемент неотрицательный
# + Элемент не кратен 3
print('\nЗадание 3')
def createNewList(oldList):
    newList=[]
    for el in oldList:
        if el%2==0 and el>=0 and el%3!=0:
            newList.append(el)

    return newList

list1=[random.randint(-10,10) for _ in range(20)]
list2=createNewList(list1)
print('Список с произвольными целыми числами:', list1)
print('Новый список:', list2)