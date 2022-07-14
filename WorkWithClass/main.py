from math import sqrt

class rectangle:
    length = 0
    width = 0
    top_left_x = 0
    top_left_y = 0
    def __init__(self, lenght=0 , width=0, top_left_x=0, top_left_y=0 ):
        self.x = lenght
        self.y = width
        self.p_x = top_left_x
        self.p_y = top_left_y

        if lenght == 0:
            print("Длина не задана")
        if width == 0:
            print("Ширина не задана")
    def __str__(self):
        return "Прямоугольник с координатами (" + str(r.p_x) + ";" + str(r.p_y) + ") шириной " + str(r.x) + " и высотой " + str(r.y)
    def square(self):
        s = r.x * r.y
        return s
    def perimiter(self):
        p = (r.x + r.y) * 2
        return p
    def diagonal(self):
        k = sqrt(r.x ** 2 + r.y ** 2)
        return k

class distance:
    top_left_x = 0
    top_left_y = 0
    top_right_x = 0
    top_right_y = 0
    def __init__(self, top_left_x = 0, top_left_y = 0, top_right_x = 0, top_right_y = 0):
        self.r_x = top_right_x
        self.r_y = top_right_y
    def distance(self):
        return sqrt((f.r_x - r.p_x) ** 2 + (f.r_y - r.p_y) ** 2)

a = int(input("Введите длину: "))
b = int(input("Введите ширину: "))
c = int(input("Введите x1: "))
d = int(input("Введите y1: "))
o = int(input("Введите x2: "))
z = int(input("Введите y2: "))

f = distance(o, z)
r = rectangle(a, b, c, d)
print(r.x, r.y, r.p_x, r.p_y)
print(r)
print("Плошадь = " + str(r.square()))
print("Пириметр = " + str(r.perimiter()))
print("Диагональ = " + str(r.diagonal()))
print("Расстояние от точки до точки = " + str(f.distance()))
