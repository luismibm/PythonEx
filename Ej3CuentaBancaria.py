class CuentaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
        else:
            print("La cantidad a depositar debe ser positiva.")

    def retirar(self, cantidad):
        if cantidad > 0:
            if self.saldo >= cantidad:
                self.saldo -= cantidad
            else:
                print("Fondos insuficientes para realizar el retiro.")
        else:
            print("La cantidad a retirar debe ser positiva.")

    def consultar_saldo(self):
        return self.saldo

cuenta = CuentaBancaria(100)
cuenta.depositar(50)
print(cuenta.consultar_saldo())
cuenta.retirar(30)
print(cuenta.consultar_saldo())
cuenta.retirar(200)
print(cuenta.consultar_saldo())