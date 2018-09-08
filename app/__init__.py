from flask import Flask

app = Flask(__name__)

from app import routes
from app import config

app.config.from_object('app.config.DevelopmentConfig')

from app.api import bp as api_bp
app.register_blueprint(api_bp, url_prefix='/api')

from app.auth import bp as auth_bp
app.register_blueprint(auth_bp, url_prefix='/auth')