from flask import Flask, render_template, request
from modelos.cuenta_ahorro import CuentaAhorro
from modelos.cuenta_corriente import CuentaCorriente

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    ticket = None
    error = None

    if request.method == 'POST':
        try:
            # 1. Recibir datos del formulario web
            tipo = request.form.get('tipo')
            titular = request.form.get('titular')
            dni = request.form.get('dni')
            fecha_nacimiento = request.form.get('fecha_nacimiento')
            saldo_inicial = float(request.form.get('saldo_inicial'))
            deposito = float(request.form.get('deposito'))
            extraccion = float(request.form.get('extraccion'))

            # 2. Instanciar la clase correspondiente
            if tipo == "ahorro":
                cuenta = CuentaAhorro(titular, dni, fecha_nacimiento, saldo_inicial)
            elif tipo == "corriente":
                cuenta = CuentaCorriente(titular, dni, fecha_nacimiento, saldo_inicial)

            # 3. Ejecutar las operaciones
            if deposito > 0:
                cuenta.depositar(deposito)
            
            if extraccion > 0:
                try:
                    cuenta.extraer(extraccion)
                except ValueError as e:
                    error = str(e)

            # 4. Preparar el ticket usando el método obtener_saldo()
            if not error:
                ticket = {
                    "titular": titular,
                    "edad": cuenta.obtener_edad(),
                    "tipo": "Caja de Ahorro" if tipo == "ahorro" else "Cuenta Corriente",
                    "deposito": deposito,
                    "extraccion": extraccion,
                    "saldo_final": cuenta.obtener_saldo() # <-- Aquí usamos tu método
                }
                
                if tipo == "ahorro":
                    ticket["interes"] = cuenta.calcular_interes()

        except Exception as e:
            error = f"Verifica los datos ingresados. Error: {e}"

    return render_template('index.html', ticket=ticket, error=error)

if __name__ == '__main__':
    app.run(debug=True)