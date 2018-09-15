from flask import Blueprint, current_app
from app import db
from app.models import Restaurant, User

from flask_login import login_required, current_user

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
		d["distance"] = np.round(np.sqrt(np.power(user.longitude-r.longitude,2)+np.power(user.latitude-r.latitude,2)), 1)
		liked_restaurants_serializable += [d]

	liked_restaurants_serializable.sort(key=lambda x: (x["distance"], x['id']))

	response = current_app.response_class(
		response = json.dumps({"liked_restaurants": liked_restaurants_serializable}),
		status = 200,
		mimetype = "application/json"
		)
	return response

@bp.route('/notliked/<int:id>')
def not_liked_restaurants(id):
	user = User.query.get(id)

	liked_restaurants = user.liked_restaurants

	not_liked_restaurants = list(set(Restaurant.query.all())-set(liked_restaurants))

	not_liked_restaurants_serializable = []

	for r in not_liked_restaurants:
		d = r.to_dict()
		d["distance"] = np.round(np.sqrt(np.power(user.longitude-r.longitude,2)+np.power(user.latitude-r.latitude,2)), 1)
		not_liked_restaurants_serializable += [d]

	not_liked_restaurants_serializable.sort(key=lambda x: (x["distance"], x['id']))

	response = current_app.response_class(
		response = json.dumps({"not_liked_restaurants": not_liked_restaurants_serializable}),
		status = 200,
		mimetype = "application/json"
		)
	return response

@bp.route('/like/<int:id>', methods=['POST'])
@login_required
def like_a_restaurants(id):
	user = current_user
	liked_restaurants = user.liked_restaurants
	restaurant = Restaurant.query.get(id)
	liked_restaurants += [restaurant]

	db.session.add(user)
	db.session.commit()

	response = current_app.response_class(
		response = json.dumps({"message": "user {} liked restaurant {} successfully".format(user.__repr__(), restaurant.__repr__())}),
		status = 200,
		mimetype = "application/json"
		)
	return response

@bp.route('/dislike/<int:id>', methods=['POST'])
@login_required
def dislike_a_restaurants(id):
	user = current_user
	liked_restaurants = user.liked_restaurants
	restaurant = Restaurant.query.get(id)

	if restaurant in liked_restaurants:
		liked_restaurants.remove(restaurant)

	db.session.add(user)
	db.session.commit()

	response = current_app.response_class(
		response = json.dumps({"message": "user {} disliked restaurant {} successfully".format(user.__repr__(), restaurant.__repr__())}),
		status = 200,
		mimetype = "application/json"
		)
	return response