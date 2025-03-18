from BancoKl import db


class Cliente(db.Model):
    __tablename__ = 'Cliente'

    id_cliente = db.Column(db.Integer, primary_key=True)
    nombre_cliente = db.Column(db.String(50))
    edad_cliente = db.Column(db.Integer)
    score_cliente = db.Column(db.Numeric)  # Si score es decimal, usamos Numeric
    pais_cliente = db.Column(db.String(50))
    tipo_persona = db.Column(db.String(50))
    correoelectronico_cliente = db.Column(db.String(50))
    telefono = db.Column(db.String(20))