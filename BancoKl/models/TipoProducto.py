from BancoKl import db

class TipoProducto(db.Model):
    __tablename__="tipo_producto"

    id_tipo_producto = db.Column(db.Integer, primary_key=True)
    nombre_tipo = db.Column(db.String(50))
    descripcion = db.Column(db.String(255))
    tasa_interes = db.Column(db.Numeric)