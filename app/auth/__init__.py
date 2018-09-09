from flask import Blueprint, current_app, redirect, url_for, render_template, flash
from flask_login import current_user, login_user, logout_user
from app import db
from app.models import User
from app.forms import LoginForm, SignUpForm
import json

bp = Blueprint('auth', __name__)


@bp.route('/signin', methods=['GET', 'POST'])
def signin():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user is None or not user.check_password(form.password.data):
			flash('Invalid Username or Password')
			return redirect(url_for('auth.signin'))
		login_user(user, remember=form.remember_me.data)
		return redirect(url_for('index'))
	return render_template('signin.html', form=form)


@bp.route('/signout')
def signout():
	if not current_user.is_authenticated:
		return redirect(url_for('auth.login'))
	logout_user()
	flash('You have been logged out successfully!')
	return redirect(url_for('auth.signin'))


@bp.route('/signup', methods=['GET', 'POST'])
def signup():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = SignUpForm()
	if form.validate_on_submit():
		user = User(username=form.username.data, email=form.email.data)
		user.set_password(form.password.data)
		db.session.add(user)
		db.session.commit()
		flash("You have been successfully registered! You can now login")
		return redirect(url_for('auth.signin'))
	return render_template('signup.html', form=form)

