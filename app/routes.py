from flask import render_template
from app import app
from flask_login import login_required, current_user

from flask import current_app

@app.route('/')
@app.route('/index')
@login_required
def index():
	user_id = current_user.id
	return render_template('index.html', user_id = user_id)

@app.route('/')
@app.route('/mylist')
@login_required
def mylist():
	user_id = current_user.id
	return render_template('mylist.html', user_id = user_id)