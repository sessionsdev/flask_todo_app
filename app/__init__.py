from flask import Flask
from pony.orm import *
from .models import db
from pony.flask import Pony
from .config import Config





def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)
    Pony(app)

    with app.app_context():

        from . import routes

        db.bind(provider='mysql', host='0.0.0.0', user='root', passwd=password, db='to_do_app')
        db.generate_mapping(create_tables=True)

        return app