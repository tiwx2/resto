from app import db, login
from flask_login import UserMixin

from werkzeug.security import generate_password_hash, check_password_hash

db.Model.metadata.reflect(db.engine)

class User(UserMixin, db.Model):
	__table_args__ = {'extend_existing': True}
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	password_hash = db.Column(db.String(128))

	confirmed = db.Column(db.Boolean, default=False)

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

	def __repr__(self):
		return '[User: {} ({})]'.format(self.username, self.email)


@login.user_loader
def load_user(id):
	return User.query.get(int(id))

#Check if the restaurants csv has been dumped into the database before reflecting it
if 'restaurants' in db.Model.metadata.tables:
	class Restaurant(db.Model):
		__table__ = db.Model.metadata.tables['restaurants']
		
		def __repr__(self):
			return 'Restaurant: {}]'.format(self.name)