class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    def area(self) -> int :
        print('El area es ', self.largo * self.ancho)
    def perimetro(self):
        print('El perimetro es ', 2 * (self.largo + self.ancho))
    def esCuadrado(self):
        return self.largo == self.ancho
    
r = Rectangulo(6, 6)
r.area()
r.perimetro()
print('Es cuadrado:', r.esCuadrado())

num = 1
num += 1
print(num)