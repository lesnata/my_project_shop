from flask import Flask
from config import get_config
from db import db

from user import users_bp
from products import products_bp
from stores import stores_bp
from create_db import create_db


def create_app(env="DEV"):
    app = Flask(__name__)
    app.config.from_object(get_config(env))

    # db.init_app(app)
    # db.create_all(app=app)

    #хз что это за create_db
    app.register_blueprint(create_db)
    app.register_blueprint(stores_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(users_bp)

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
