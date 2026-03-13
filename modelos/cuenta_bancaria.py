from abc import ABC, abstractmethod
from datetime import datetime

class CuentaBancaria(ABC):
    def __init__(self, titular, dni, fecha_nacimiento, saldo_inicial=0.0):
        self._titular = titular
        self._dni = dni
        self._fecha_nacimiento = fecha_nacimiento
        self._saldo = saldo_inicial

    def mostrar_saldo(self):
        print(f"Saldo actual: {self._saldo:.2f}")

    @abstractmethod
    def depositar(self, monto):
        pass

    @abstractmethod
    def extraer(self, monto):
        pass

    def obtener_saldo(self):
        return self._saldo

    def obtener_edad(self):
        return self._calcular_edad()

    def _calcular_edad(self):
        try:
            nacimiento = datetime.strptime(self._fecha_nacimiento, "%Y%m%d")
            hoy = datetime.today()
            edad = hoy.year - nacimiento.year - ((hoy.month, hoy.day) < (nacimiento.month, nacimiento.day))
            return edad
        except Exception:
            return "Fecha inválida"