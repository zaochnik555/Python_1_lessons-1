import os,sys,shutil

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

my_path=["dir_" + str(i + 1) for  i in range(9)]

def create_dir(index):
    dir_path=os.path.join(os.getcwd(),index)
    try:
        os.mkdir(dir_path)
    except:
        print(dir_path+" - директория с таким именем в этой папке уже есть")

#создадим два варианта скрипта удаления директорий
def del_dir1(index):
    dir_path=os.path.join(os.getcwd(),index)
    try:
        os.removedirs(dir_path)
    except:
        print(dir_path+" - директории с таким именем в этой папке не существует")

def del_dir2(index):
    dir_path = os.path.join(os.getcwd(), index)
    try:
        os.rmdir(dir_path)
    except:
        print(dir_path+" - директории с таким именем в этой папке не существует")

for i in my_path:
    create_dir(i)

for i in my_path:
    del_dir1(i)

#for i in my_path:
#    del_dir2(i)


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def print_dir(my_path):
    for el in os.listdir(my_path):
        print(el)

my_path = os.getcwd()
print_dir(my_path)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
def create_copy_of_file(old_file,new_file):
    shutil.copy(old_file,new_file)

old_file = sys.argv[0]
new_file = old_file + '.copy_of_file'
create_copy_of_file(old_file,new_file)

