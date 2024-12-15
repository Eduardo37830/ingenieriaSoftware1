from flask import Flask, render_template
from controllers.transaction_controller import transaction_blueprint, admission_blueprint, personalAdmistraccion, proveedoresAdmistraccion
app = Flask(__name__)
app.register_blueprint(transaction_blueprint)
app.register_blueprint(admission_blueprint)
app.register_blueprint(personalAdmistraccion)
app.register_blueprint(proveedoresAdmistraccion)  
@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
