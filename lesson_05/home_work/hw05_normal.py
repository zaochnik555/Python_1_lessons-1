# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import os,hw05_easy

def change_dir(my_path):
    try:
        os.chdir(my_path)
        print(os.getcwd() + ' - текущая папка')
    except:
        print(my_path + ' - такой папки не существует')



choice="_"
while choice != "5":
    print("Меню:")
    print("1. Перейти в папку")
    print("2. Просмотреть содержимое текущей папки")
    print("3. Удалить папку")
    print("4. Создать папку")
    print("5. Выход из утилиты")
    choice = input("Введите номер нужного действия: " )
    print(choice)
    if choice == "1":
        dir_name = input ("Введите полный путь папки: ")
        change_dir(dir_name)
    elif choice == "2":
        dir_name = os.getcwd()
        hw05_easy.print_dir(dir_name)
    elif choice == "3":
        dir_name = input("Введите полный путь папки: ")
        hw05_easy.del_dir1(dir_name)
    elif choice == "4":
        dir_name = input("Введите полный путь папки: ")
        hw05_easy.create_dir(dir_name)
    elif choice == "5":
        pass
    else:
        print("Такой пункт меню отсутствует. Попробуйте снова.")










