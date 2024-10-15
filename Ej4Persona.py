class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def cumplir_años(self):
        self.edad += 1

    def saludar(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")

prueba = Persona('Luismi', 22, 'Hombre')
prueba.saludar()
prueba.cumplir_años()
prueba.saludar()