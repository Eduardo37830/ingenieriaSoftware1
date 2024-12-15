from flask import Flask, render_template, request
from controllers.transaction_controller import transaction_blueprint, admission_blueprint, personalAdmistraccion, proveedoresAdmistraccion

app = Flask(__name__)
app.register_blueprint(transaction_blueprint)
app.register_blueprint(admission_blueprint)
app.register_blueprint(personalAdmistraccion)
app.register_blueprint(proveedoresAdmistraccion)  
@app.route("/")
def home():
    return render_template("index.html")

@app.route('/inicio_cliente')
def inicio_cliente():
    return render_template('inicio_cliente.html')

@app.route('/agendar_cita', methods=["GET", "POST"])
def agendar_cita():
    if request.method == "POST":
        # Capturar los datos del formulario
        fecha = request.form.get("fecha")
        hora = request.form.get("hora")
        tipo = request.form.get("tipo")
        medico = request.form.get("medico")
        
        print(f"Fecha: {fecha}, Hora: {hora}, Tipo: {tipo}, Médico: {medico}")
        
        # Mensaje de confirmación (puedes redirigir a otra página o mostrar un mensaje)
        mensaje = f"Cita agendada con éxito: Fecha: {fecha}, Hora: {hora}, Tipo: {tipo}, Médico: {medico}"
        return render_template("agendar_cita.html", mensaje=mensaje)
    
    # Si es un GET, simplemente renderiza el formulario
    return render_template('agendar_cita.html')


@app.route('/citas_agendadas')
def citas_agendadas():
    return render_template('citas_agendadas.html')

@app.route('/historial_medico')
def historial_medico():
    return render_template('historial_medico.html')

@app.route('/medicamentos')
def medicamentos():
    return render_template('medicamentos.html')

if __name__ == "__main__":
    app.run(debug=True)
