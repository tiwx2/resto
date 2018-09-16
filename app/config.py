import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	DEBUG = False

class DevelopmentConfig(Config):
	DEBUG = True
	SECRET_KEY = "S8iXFQKkOK7MgvUL2VxvN6yuOyAOTtVv"

	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(Config):
	DEBUG = False
	SECRET_KEY = os.environ.get('SECRET_KEY')

	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
	SQLALCHEMY_TRACK_MODIFICATIONS = False