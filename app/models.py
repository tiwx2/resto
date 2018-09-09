from app import db

db.Model.metadata.reflect(db.engine)

class User(db.Model):
	__table_args__ = {'extend_existing': True}
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	password_hash = db.Column(db.String(128))

	confirmed = db.Column(db.Boolean, default=False)

	def __repr__(self):
		return '[User: {} ({})]'.format(self.username, self.email)

#Check if the restaurants csv has been dumped into the database before reflecting it
if 'restaurants' in db.Model.metadata.tables:
	class Restaurant(db.Model):
		__table__ = db.Model.metadata.tables['restaurants']
		
		def __repr__(self):
			return 'Restaurant: {}]'.format(self.name)