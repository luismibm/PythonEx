import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, otro_punto):
        return math.sqrt((self.x - otro_punto.x) ** 2 + (self.y - otro_punto.y) ** 2)

class Triangulo:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def perimetro(self):
        lado1 = self.p1.distancia(self.p2)
        lado2 = self.p2.distancia(self.p3)
        lado3 = self.p3.distancia(self.p1)
        return lado1 + lado2 + lado3

p1 = Punto(0, 0)
p2 = Punto(3, 0)
p3 = Punto(0, 4)
triangulo = Triangulo(p1, p2, p3)
print(f"El perímetro del triángulo es: {triangulo.perimetro()}")