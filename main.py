from flask import Flask
from flask_cors import CORS
from flask_restx import Api

from app.config import Config
from app.dao.model.framework import FrameworkModel
from app.db_setup import db
from app.views.framework import framework_ns


def create_app(config_object) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config_object)
    application.app_context().push()
    return application


def configure_app(application):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(framework_ns)
    CORS(application)


# pk  name      language
# -------------------------
# 1   React     Javascript
# 2   Vue       Javascript
# 3   FastApi   Python
# 4   Laravel   PHP
# 5   Spring    Java






if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    configure_app(app)

    with app.app_context():
        db.create_all()
        db.session.add(FrameworkModel(name='React', language='Javascript'))
        db.session.add(FrameworkModel(name='Vue', language='Javascript'))
        db.session.add(FrameworkModel(name='FastApi', language='Python'))
        db.session.add(FrameworkModel(name='Laravel', language='PHP'))
        db.session.add(FrameworkModel(name='Spring', language='Java'))
        db.session.commit()

    app.run()