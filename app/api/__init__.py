from flask import Blueprint, current_app

import json

bp = Blueprint('api', __name__)


@bp.route('/echo/<string:to_echo>')
def echo(to_echo):
	response = current_app.response_class(
		response = json.dumps({"echo": to_echo}),
		status = 200,
		mimetype = "application/json"
		)
	return response