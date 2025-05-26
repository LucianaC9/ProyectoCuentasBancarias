from modelos.cuenta_bancaria import CuentaBancaria

class CuentaAhorro(CuentaBancaria):
    def __init__(self, titular, dni, fecha_nacimiento, saldo_inicial=0.0):
        super().__init__(titular, dni, fecha_nacimiento, saldo_inicial)
        self.__tasa_interes = 0.001

    def depositar(self, monto):
        if monto > 0:
            self._saldo += monto

    def extraer(self, monto):
        if monto <= self._saldo:
            self._saldo -= monto
        else:
            raise ValueError("Fondos insuficientes.")

    def calcular_interes(self):
        return self._saldo * self.__tasa_interes