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


propietarios = ["Juan Perez", "Maria Lopez"]
cuenta = CuentaBancaria("191424", propietarios, 1000.0)

deposito = 700.0
cuenta.depositar(deposito)