from modelos.cuenta_ahorro import CuentaAhorro
from modelos.cuenta_corriente import CuentaCorriente

def main():
    print("=== Bienvenido al sistema bancario ===")
    tipo = input("¿Qué tipo de cuenta desea utilizar? (ahorro/corriente): ").strip().lower()

    titular = input("Titular: ")
    dni = input("DNI del titular: ")
    fecha_nacimiento = input("Fecha de nacimiento (YYYYMMDD): ")
    saldo_inicial = float(input("Saldo inicial: "))

    if tipo == "ahorro":
        cuenta = CuentaAhorro(titular, dni, fecha_nacimiento, saldo_inicial)
    elif tipo == "corriente":
        cuenta = CuentaCorriente(titular, dni, fecha_nacimiento, saldo_inicial)
    else:
        print("Tipo de cuenta no válido.")
        return

    cuenta.mostrar_saldo()
    print(f"Edad del titular: {cuenta.obtener_edad()} años")

    deposito = float(input("Monto a depositar: "))
    cuenta.depositar(deposito)

    extraccion = float(input("Monto a extraer: "))
    try:
        cuenta.extraer(extraccion)
    except ValueError as e:
        print(f"Error al extraer: {e}")

    cuenta.mostrar_saldo()

    if tipo == "ahorro":
        interes = cuenta.calcular_interes()
        print(f"Interés generado: {interes:.2f}")

if __name__ == "__main__":
    main()