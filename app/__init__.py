from flask import Flask

from app.views.index import blueprint as index_blueprint


def create_app(debug=False, testing=False):
    app = Flask(__name__)
    app.register_blueprint(index_blueprint)
    app.debug = debug
    app.testing = testing
    return app
