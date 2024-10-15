class Empleado:
    def __init__(self, nombre, horas_trabajadas, salario_por_hora):
        self.nombre = nombre
        self.horas_trabajadas = horas_trabajadas
        self.salario_por_hora = salario_por_hora

    def calcular_salario(self):
        return self.horas_trabajadas * self.salario_por_hora

    def aumentar_salario(self, porcentaje):
        self.salario_por_hora += self.salario_por_hora * (porcentaje / 100)

if __name__ == "__main__":
    empleado = Empleado("Luis", 40, 15)
    print(f"Salario inicial: {empleado.calcular_salario()}")
    empleado.aumentar_salario(10)
    print(f"Salario después del aumento: {empleado.calcular_salario()}")