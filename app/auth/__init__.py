from flask import Blueprint, current_app

import json

bp = Blueprint('auth', __name__)


@bp.route('/login')
def login():
	return "Login Page"