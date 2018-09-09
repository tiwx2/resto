class Config(object):
	DEBUG = False

class DevelopmentConfig(Config):
	DEBUG = True
	SECRET_KEY = "S8iXFQKkOK7MgvUL2VxvN6yuOyAOTtVv"