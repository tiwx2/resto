from flask import Blueprint, current_app

import json

bp = Blueprint('auth', __name__)


@bp.route('/signin')
def signin():
	return "Sign in Page"


@bp.route('/signout')
def signout():
	return "Sign out Page"


@bp.route('/signup')
def signup():
	return "Sign up Page"