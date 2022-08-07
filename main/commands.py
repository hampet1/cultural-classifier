from . import db


def create_db():
    """
    command for creating Postgre database on heroku
    """
    db.create_all()


def init_app(app):
    app.cli.add_command(app.cli.command()(create_db))