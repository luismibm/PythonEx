class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Se han depositado {cantidad}€. Saldo actual: {self.saldo}€.")

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Se han retirado {cantidad}€. Saldo actual: {self.saldo}€.")
        else:
            print("No hay suficiente dinero en la cuenta.")

    def mostrar_saldo(self):
        print(f"Saldo actual: {self.saldo}€.")

cuenta = CuentaBancaria("Luis", 100)
cuenta.depositar(50)
cuenta.retirar(30)
cuenta.mostrar_saldo()
cuenta.retirar(150)