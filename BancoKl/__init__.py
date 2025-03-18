from flask import Flask
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#cargar configuraciones

app.config.from_object('config.DevelopmentConfig')

db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

#importar modelo clientes

from BancoKl.models.Clientes import Cliente


@app.route('/Clientes')
def mostrar_clientes():
    clientes = Cliente.query.all()  # Obtener los 50 registros
    return render_template('MostrarTabla.html', clientes=clientes)
