# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Шамсутдинов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# ВыбрНиная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class People:
    def __init__(self, name, patronymic, surname):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic

    def get_full_name(self):
        return self.name + ' ' + self.patronymic + ' ' + self.surname

    def get_short_name(self):
        return '{} {}.{}.'.format(self.surname.title(), self.name[0].upper(), self.patronymic[0].upper())


# if __name__ == '__main__':  # Тестирование.
#     people1 = People('Руслан', 'Германович', 'Шамсутдинов')
#     print(people1.get_full_name())
#     print(people1.get_short_name())


class Student(People):
    def __init__(self, name, patronymic, surname, mom, dad, school_class):
        People.__init__(self, name, patronymic, surname)
        self.mom = mom
        self.dad = dad
        self.school_class = school_class


# if __name__ == '__main__':  # Тестирование.
#     st_1 = Student('Анвар', 'Владленовна', 'Купцов', 'Нина Сабирова', 'Павел Купцов', '7а')
#     st_2 = Student('Булат', 'Булатович', 'Сагадатов', 'Регина Рамазанова', 'Григорий Сагадатов', '7б')
#     st_3 = Student('Марат', 'Азаматович', 'Саакашвилли', 'Эльвира Максимова', 'Марат Саакашвилли', '7а')
#     print(Student.all_classes(st_1))


class Teacher(People):
    def __init__(self, name, patronymic, surname, subject):
        People.__init__(self, name, patronymic, surname)
        self.subject = subject


class Class_rooms:
    def __init__(self, class_room, teachers):
        self.class_room = class_room
        self.teachersdict = {t.subject: t for t in teachers}



if __name__ == '__main__':  # Тестирование.
    teachers = [Teacher('Руслан', 'Германович', 'Шамсутдинов', 'Математика'),
                Teacher('Айрат', 'Айратович', 'Саакашвилли', 'Химия'),
                Teacher('Рустам', 'Рустамович', 'Закиров', 'Правоведение'),
                Teacher('Азат', 'Азатович', 'Голубев', 'География'),
                Teacher('Вильдан', 'Маратович', 'Пахомов', 'Ботаника')]
    classes = [Class_rooms('11 А', [teachers[0], teachers[1], teachers[2]]),
               Class_rooms('11 Б', [teachers[1], teachers[3], teachers[4]]),
               Class_rooms('10 А', [teachers[3], teachers[1], teachers[0]])]
    parents = [People('Анвар', 'Владленовна', 'Купцов'),
               People('Лилия', 'Аминовна', 'Поезжалова'),
               People('Альберт', 'Алмазович', 'Платов'),
               People('Марина', 'Альбертовна', 'Кудрявцева'),
               People('Булат', 'Булатович', 'Сагадатов'),
               People('Эльвира', 'Руслановна', 'Рамазанова')]
    students = [Student('Ирек', 'ГрИрекевич', 'Купцов', parents[0], parents[1], classes[0]),
                Student('Регина', 'Кудрявцева', 'Кудрявцева', parents[2], parents[3], classes[1]),
                Student('Инновентий', 'Булатович', 'Сагадатов', parents[4], parents[5], classes[2])]
    print('Список классов в школе: ')
    for f in classes:
        print(f.class_room)

    for f in classes:
        print('Учителя, преподающие в {} классе:'.format(f.class_room))
        for teacher in classes[0].teachersdict.values():
            print(teacher.get_full_name())
    for f in classes:
        print("Ученики в классе {}:".format(f.class_room))
        for st in students:
            print(st.get_short_name())

    # for f in students:
    #     print('Список предметов ученика {}'.format(f.school_class))
    #     for teacher in classes[0].teachersdict.values():
    #         print(teacher.get_full_name())