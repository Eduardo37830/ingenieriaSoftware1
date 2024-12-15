from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/inicio_cliente')
def inicio_cliente():
    return render_template('inicio_cliente.html')


if __name__ == "__main__":
    app.run(debug=True)
