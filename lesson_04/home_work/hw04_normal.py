import re,random

# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.
print('Задание 1')
string="mtMmEZUOmcq"
pattern="[A-Z]+"
list1=re.split(pattern,string)
print('Решение с помощью re:',list1)

list2=[]
string2=''
for el in string:
    if el<'A' or el>'Z':
        string2+=el
    else:
        if len(string2)>0:
            list2.append(string2)
            string2=''
if len(string2)>0:
    list2.append(string2)
print('Решение без помощи re:',list2)


# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа два символа в верхнем регистре.
# Т.е. из строки
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.
print('\nЗадание 2')
string="GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
string="GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
pattern="[a-z]{2}[A-Z]+[A-Z]{2}"
list1=re.findall(pattern,string)
for i in range(len(list1)):
    list1[i]=list1[i][2:len(list1[i])-2]
print('Решение с помощью re:',list1)

list2=[]
k1=k2=i=0
for el in string:
    if el<'A' or el>'Z':
        if k2>2 and k1==-1:
            list2.append(string[i-k2:i-2])
            k1=k2=0
        k1+=1
        k2=0
    else:
        if k1>=2:
            k1=-1
        elif k1!=-1:
            k1=0
        k2+=1
    i+=1

print('Решение без помощи re:',list2)

# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.
print('\nЗадание 3')
string='33799011222344555677000008889999'

f=open('text.txt','w',encoding='UTF-8')
for _ in range(2500):
    f.write(str(random.randint(0,10)))
f.close()

f=open('text.txt','r',encoding='UTF-8')
string=f.readline()
f.close()

pattern='[0]+|[1]+|[2]+|[3]+|[4]+|[5]+|[6]+|[7]+|[8]+|[9]+'
list1=[]
list2=[]
list1=re.findall(pattern,string)
res1=max(list1,key=len)
print('Решение с помощью re:',res1)

el2=res2=s=''
for el in string:
    if el!=el2:
        if len(res2)<len(s):
            res2=s
        el2=el
        s=el
    else:
        s+=el

print('Решение без помощи re:',res2)