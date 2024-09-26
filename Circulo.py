import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    def area(self):
        print('El area es ', math.pi * self.radio**2)
    def perimetro(self):
        print('El perimetro es ', math.pi*2 * self.radio)

c = Circulo(6)
c.area()
c.perimetro()
