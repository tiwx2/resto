from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('app.config.DevelopmentConfig')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models

from app.api import bp as api_bp
app.register_blueprint(api_bp, url_prefix='/api')

from app.auth import bp as auth_bp
app.register_blueprint(auth_bp, url_prefix='/auth')