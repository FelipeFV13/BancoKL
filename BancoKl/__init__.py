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
from BancoKl.models.TipoProducto import TipoProducto


@app.route('/Clientes')
def mostrar_clientes():
    columnas = [column.name for column in Cliente.__table__.columns]
    clientes = Cliente.query.all()
    return render_template('MostrarTabla.html', clientes=clientes, columnas =columnas)

@app.route('/Tipo_producto')
def mostrar_tipo_producto():
    columnas = [column.name for column in TipoProducto.__table__.columns]
    tipo_producto = TipoProducto.query.all()
    return render_template('MostrarTabla2.html', tipo_producto=tipo_producto, columnas =columnas)
