from flask import Flask
from flask_cors import CORS
from .db.postgresql.model import db

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config')
    app.config.from_pyfile('config.py')
    CORS(app, support_credentials=True)
    
    with app.app_context():
        from .routes import user, document, utils
        add_routes(app, user, document, utils)
        db.init_app(app)
        return app

def add_routes(app, user, document, utils):
    # User routes
    app.add_url_rule(user['login'], view_func=user['view_func_login'])
    app.add_url_rule(user['signin'], view_func=user['view_func_signin'])

    # Document routes
    app.add_url_rule(document['document'], view_func=document['view_func_document'])
    app.add_url_rule(document['search'], view_func=document['view_func_search'])

    # Utilities routes
    app.add_url_rule(utils['ch'], view_func=utils['view_func_ch'])
    app.add_url_rule(utils['re'], view_func=utils['view_func_re'])
    app.add_url_rule(utils['up'], view_func=utils['view_func_up'])