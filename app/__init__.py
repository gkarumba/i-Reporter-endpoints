from flask import Flask, Blueprint
#local imports
from instance import config
from app.api.incidents.v1 import version_one as v1
from app.api.users.v1 import user
from app.api.users.v2 import users2
from app.api.incidents.v2 import version_two as v2
from app.database.database import ReportDB 
from flask_cors import CORS

db = ReportDB()

def create_app(config_name="development_config"):
    """
    Initialize flask app instance and configure it
    """
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_object(config.CONFIGS[config_name])
    # db.start_db(app.config['DATABASE_URI'])
    CORS(app)
    db.create_tables()
    app.register_blueprint(v1)
    app.register_blueprint(user)
    app.register_blueprint(users2)
    app.register_blueprint(v2)
    return app