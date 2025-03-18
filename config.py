class config:
    DEBUG = True
    TESTING = True

    #   CONFIGURACION BASE DE DATOS
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:Hellopyjs13+@localhost:3306/bancokl"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(config):
    DEBUG = False

class DevelopmentConfig(config):
    SECRET_KEY =  'dev'
    DEBUG = True
    TESTING = True