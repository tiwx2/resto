from app import app

from flask import current_app

@app.route('/')
@app.route('/index')
def index():
	return "Hello World!"