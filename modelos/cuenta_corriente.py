from modelos.cuenta_bancaria import CuentaBancaria

class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular, dni, fecha_nacimiento, saldo_inicial=0.0):
        super().__init__(titular, dni, fecha_nacimiento, saldo_inicial)
        self._limite_descubierto = -1000.0

    def depositar(self, monto):
        if monto > 0:
            self._saldo += monto

    def extraer(self, monto):
        if self._saldo - monto >= self._limite_descubierto:
            self._saldo -= monto
        else:
            raise ValueError("Fondos insuficientes: excede el límite de descubierto.")