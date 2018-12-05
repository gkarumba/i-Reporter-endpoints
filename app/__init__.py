from flask import Flask, Blueprint
from app import config
from app.users.v1 import user
from app.api.v1 import version_one as v1
from app.users.v1 import user
from app.users.v1.database import ReportDB

def create_app(config_option="DevConfig"):
    app = Flask(__name__)
    #app.config.from_object(config.Devconfig[config_option])
    #ReportDB.init_db(app.config['DATABASE_URI'])
    #ReportDB.create_tables()
    app.register_blueprint(v1)
    app.register_blueprint(user)
    return app