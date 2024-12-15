from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/inicio_cliente')
def inicio_cliente():
    return render_template('inicio_cliente.html')

@app.route('/agendar_cita')
def agendar_cita():
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
