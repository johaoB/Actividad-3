class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

propietarios = ["Juan Perez", "Maria Lopez"]
cuenta = CuentaBancaria("125514", propietarios, 1000.0)
