# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math

class Treug:
    def __init__(self,x1,y1,x2,y2,x3,y3):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        self.x3=x3
        self.y3=y3

    @staticmethod
    def length(x1,y1,x2,y2):
        return math.sqrt(math.pow((x2-x1),2)+math.pow((y2-y1),2))

    @property
    def ploschad(self):
        len1=self.length(self.x1, self.y1, self.x2, self.y2)
        len2=self.length(self.x3, self.y3, self.x2, self.y2)
        len3=self.length(self.x1, self.y1, self.x3, self.y3)
        p=(len1+len2+len3)/2
        return math.sqrt(p*(p-len1)*(p-len2)*(p-len3))

    @property
    def vysota(self):
        return self.ploschad/(self.length(self.x1, self.y1, self.x2, self.y2)/2)

    @property
    def perimetr(self):
        return self.length(self.x1, self.y1, self.x2, self.y2) +\
            self.length(self.x3, self.y3, self.x2, self.y2) + \
            self.length(self.x1, self.y1, self.x3, self.y3)



print('Задание 1')
treug1=Treug(5,6,18,7,11,13)
print('Периметр треугольника: {}'.format(treug1.perimetr))
print('Площадь треугольника: {}'.format(treug1.ploschad))
print('Высота треугольника: {}'.format(treug1.vysota))

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
class Trapecia:
    def __init__(self,x1,y1,x2,y2,x3,y3,x4,y4):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        self.x3=x3
        self.y3=y3
        self.x4=x4
        self.y4=y4

        def length(x1,y1,x2,y2):
            return math.sqrt(math.pow((x2-x1),2)+math.pow((y2-y1),2))

        self.AB = length(self.x1, self.y1, self.x2, self.y2)
        self.BC = length(self.x2, self.y2, self.x3, self.y3)
        self.CD = length(self.x3, self.y3, self.x4, self.y4)
        self.DA = length(self.x4, self.y4, self.x1, self.y1)
        self.diag_AC = length(self.x3, self.y3, self.x1, self.y1)
        self.diag_BD = length(self.x2, self.y2, self.x4, self.y4)
        self.perimeter = self.AB + self.BC + self.CD + self.DA

    def ploschad2(self,len1,len2,len3):
        p=(len1+len2+len3)/2
        return math.sqrt(p*(p-len1)*(p-len2)*(p-len3))

    @staticmethod
    def length(x1,y1,x2,y2):
        return math.sqrt(math.pow((x2-x1),2)+math.pow((y2-y1),2))

    @property
    def ploschad(self,x1,y1,x2,y2,x3,y3):
        len1=self.length(x1, y1, x2, y2)
        len2=self.length(x3, y3, x2, y2)
        len3=self.length(x1, y1, x3, y3)
        p=(len1+len2+len3)/2
        return math.sqrt(p*(p-len1)*(p-len2)*(p-len3))

    @property
    def perimetr(self):
        return self.length(self.x1, self.y1, self.x2, self.y2) + \
            self.length(self.x2, self.y2, self.x3, self.y3) + \
            self.length(self.x3, self.y3, self.x4, self.y4) + \
            self.length(self.x4, self.y4, self.x1, self.y1)



    # трапеция это два треугольника. Площадь трапеции - это сумма площадей
    # двух треугольников
    @property
    def getPloschad(self):
        self.area = self.ploschad2(self.AB, self.diag_BD, self.DA) \
                    + self.ploschad2(self.diag_BD, self.BC, self.CD)
        return self.area

    def isTrapeciaRavnobocha(self):
        return self.diag_AC == self.diag_BD

print('/nЗадание 2')
trap1=Trapecia(5,6,18,7,11,13,7,12)
print('Периметр трапеции: {}'.format(trap1.perimetr))
print('Площадь трапеции: {}'.format(trap1.getPloschad))
print('Равнобочна ли трапеция: {}'.format(trap1.isTrapeciaRavnobocha()))