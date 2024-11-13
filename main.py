from flask import Flask, render_template, request

app = Flask(__name__)


# Página principal con el menú
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

# Formulario del ejercicio 1 (promedio de notas y estado)
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        # Obtener los valores del formulario
        try:
            nota1 = int(request.form['nota1'])
            nota2 = int(request.form['nota2'])
            nota3 = int(request.form['nota3'])
            asistencia = int(request.form['asistencia'])

            # Calcular el promedio de las notas
            promedio = int((nota1 + nota2 + nota3) / 3)

            # Verificar el estado de aprobado o reprobado
            if promedio >= 40 and asistencia >= 75:
                estado = "Aprobado"
            else:
                estado = "Reprobado"

            # Devolver los resultados
            return render_template('ejercicio1.html', promedio=promedio, asistencia=asistencia, estado=estado)
        except ValueError:
            # Si los datos no son válidos (por ejemplo, no son números), manejar el error
            return render_template('ejercicio1.html', error="Por favor, ingresa valores numéricos válidos.")

    return render_template('ejercicio1.html')


# Formulario del ejercicio 2 (nombre más largo)
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        # Obtener los nombres del formulario
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        # Determinar el nombre más largo
        nombres = [nombre1, nombre2, nombre3]
        nombre_mas_largo = max(nombres, key=len)
        longitud = len(nombre_mas_largo)

        # Devolver los resultados
        return render_template('ejercicio2.html', nombre_mas_largo=nombre_mas_largo, longitud=longitud)

    return render_template('ejercicio2.html')


if __name__ == '__main__':
    app.run(debug=True)