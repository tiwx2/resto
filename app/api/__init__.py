from flask import Blueprint, current_app
from app import db
from app.models import Restaurant, User

import numpy as np

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

@bp.route('/restaurant/<int:id>')
def restaurant(id):
	restaurant = Restaurant.query.get(id)

	if restaurant==None:
		response = current_app.response_class(
		response = json.dumps({'error': 'Restaurant not found'}),
		status = 404,
		mimetype = "application/json"
		)
		return response


	response = current_app.response_class(
	response = json.dumps(restaurant.to_dict()),
	status = 200,
	mimetype = "application/json"
	)
	return response

@bp.route('/liked/<int:id>')
def liked_restaurants(id):
	user = User.query.get(id)

	liked_restaurants = user.liked_restaurants

	liked_restaurants_serializable = []

	for r in liked_restaurants:
		d = r.to_dict()
		d["distance"] = np.sqrt(np.power(user.longitude-r.longitude,2)+np.power(user.latitude-r.latitude,2))
		liked_restaurants_serializable += [d]

	response = current_app.response_class(
		response = json.dumps({"liked_restaurants": liked_restaurants_serializable}),
		status = 200,
		mimetype = "application/json"
		)
	return response