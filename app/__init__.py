from flask import Flask, Blueprint
from instance.config import CONFIGS
from app.users.v1 import user
from app.api.v1 import version_one as v1
from app.users.v1 import user
from app.users.v2 import users2
from app.users.v1.database import ReportDB

def create_app(config_name="development_config"):
    app = Flask(__name__)
    app.config.from_object(CONFIGS[config_name])
    #ReportDB.init_db(app.config['DATABASE_URI'])
    #ReportDB.create_tables()
    app.register_blueprint(v1)
    app.register_blueprint(user)
    app.register_blueprint(users2)
    return app