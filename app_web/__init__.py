from flask import Flask
#
def create_app():
    #
    from .main.controller import main_blueprint
    from .pickup.controller import pickup_blueprint
    #
    app = Flask('__name__')
    #
    app.config.from_pyfile('config.py')
    #
    app.register_blueprint(main_blueprint)
    #
    app.register_blueprint(pickup_blueprint)
    #
    return app