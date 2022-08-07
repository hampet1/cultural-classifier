from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from main.config import configure_app
from flask_login import LoginManager



db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    configure_app(app)
    app.config['SQLALCHEMY_DATABASE_URI']
    db.init_app(app)




    from .views import views
    from .auth import auth
    from .maps import maps
    from .api import api

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(maps, url_prefix='/')
    app.register_blueprint(api, url_prefix='/')

    from .models import User
    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.log_in'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        """
        based on user id we're returning user object
        """
        try:
            return User.query.get(id)
        except:
            return None

    # create command for heroku to be able to create_db in Postgres based on our table
    import main.commands
    main.commands.init_app(app)


    return app


def create_database(app):
    if not path.exists('main/' + app.config['DB_NAME']):
        db.create_all(app=app)
        print('Created Database!')




# for heroku we have to import my_app to Procfile
my_app = create_app()



