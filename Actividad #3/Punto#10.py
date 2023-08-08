class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def depositar(self, cantidad):
        if cantidad > 0:
            self.balance += cantidad
            print(f"Depósito exitoso. Nuevo balance: ${self.balance:.2f}")
        else:
            print("La cantidad de depósito debe ser mayor que cero.")

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.balance:
            self.balance -= cantidad
            print(f"Retiro exitoso. Nuevo balance: ${self.balance:.2f}")
        else:
            print("Cantidad inválida para el retiro o fondos insuficientes.")

    def aplicar_cuota_manejo(self):
        cuota = self.balance * 0.02
        self.balance -= cuota
        print(f"Cuota de manejo aplicada. Nuevo balance: ${self.balance:.2f}")


propietarios = ["Juan Perez", "Maria Lopez"]
cuenta = CuentaBancaria("114398", propietarios, 1000.0)

"""deposito = 700.0
cuenta.depositar(deposito)"""

"""retiro = 300.0
cuenta.retirar(retiro)"""

cuenta.aplicar_cuota_manejo()
