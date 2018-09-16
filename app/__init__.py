from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os

app = Flask(__name__)

if os.environ.get('FLASK_ENV') == 'production':
	app.config.from_object('app.config.ProdConfig')
else:
	app.config.from_object('app.config.DevelopmentConfig')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'auth.signin'

from app import routes, models

from app.api import bp as api_bp
app.register_blueprint(api_bp, url_prefix='/api')

from app.auth import bp as auth_bp
app.register_blueprint(auth_bp, url_prefix='/auth')