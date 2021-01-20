from flask import Flask
from db.postgresql.model import db, Bonding
from db.postgresql.postgresql_manager import PostgresqlManager

def create_app():
    postgreql_tool = PostgresqlManager()
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://dwmdwuxrbsmznj:ced17943385fa0ef9f237f025f138b0200ebd897f32a01bc7d9908023bcebf7c@ec2-52-204-113-104.compute-1.amazonaws.com:5432/dc3cnsfmu7o2u'
    with app.app_context():
        db.init_app(app)
        db.create_all()
        contratista = Bonding(description = 'Contratista')
        planta = Bonding(description = 'Planta')
        postgreql_tool.add(contratista, planta)
    return app