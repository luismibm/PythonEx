class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def informacion(self):
        return f'Nombre: {self.nombre}, Edad: {self.edad}'

class Estudiante(Persona):
    def __init__(self, nombre, edad, nota):
        super().__init__(nombre, edad)
        self.nota = nota

    def informacion(self):
        return f'Nombre: {self.nombre}, Edad: {self.edad}, Nota: {self.nota}'

class Profesor(Persona):
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)
        self.materia = materia

    def informacion(self):
        return f'Nombre: {self.nombre}, Edad: {self.edad}, Materia: {self.materia}'

estudiante = Estudiante("Luismi", 22, 9)
profesor = Profesor("Antonio", 35, "Matemáticas")

print(estudiante.informacion())
print(profesor.informacion())