# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonachchi(n,m):
    a=b=1
    k=2
    while k<m:
        c=a+b
        a=b
        b=c
        k+=1
        if n<=k<=m:
            print(c)

print('Задача 1')
n=5
m=10
print('Ряд Фибоначчи с элементами с {} по {}:'.format(n,m))
fibonachchi(n,m)




# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def my_sort(my_list):
    for i in range(len(my_list)):
        for j in range(i+1,len(my_list)):
            if my_list[i]>my_list[j]:
                t=my_list[i]
                my_list[i]=my_list[j]
                my_list[j]=t
    print(my_list)

print('\nЗадача 2')
list1=[18,-6,3,8,-5,14,123,-999]
my_sort(list1)

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
def my_filter(lambda_func, list1):
    list2=[]
    for i in list1:
        if lambda_func(i):
            list2.append(i)
        else:
            continue
    return list2

print('\nЗадача 3')
print((my_filter((lambda x: x<10), list1=[18,-6,3,8,-5,14,123,-999])))



# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def is_parallelogram(x1,y1,x2,y2,x3,y3,x4,y4):
    if (y1==y4) and (y2==y3) and (abs(x1-x2)==abs(x3-x4)):
        return True
    else:
        return False

print('\nЗадача 4')
x1=0
y1=5
x2=5
y2=20
x3=25
y3=20
x4=20
y4=5
print('Являются ли точки A1({}, {}), А2({} ,{}), А3({} , {}), А4({}, {}) вершинами параллелограмма: '.format(x1,y1,x2,y2,x3,y3,x4,y4),is_parallelogram(x1,y1,x2,y2,x3,y3,x4,y4))