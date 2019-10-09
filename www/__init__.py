from flask import Flask

from www.views import test, test2, test3


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_pyfile('../config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    app.register_blueprint(test.t)
    app.register_blueprint(test2.t1)
    app.register_blueprint(test3.new_old_pow)

    return app