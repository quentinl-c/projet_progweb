import hash
from google.appengine.ext import db
import hashlib
import hash

class Api(db.Model):
	login    = db.StringProperty(required = True)
	password = db.StringProperty(required = True)
	email    = db.EmailProperty(required = True)
	api_key  = db.StringProperty(required = True)

	@classmethod
	def create(cls, login, password, email, api_key = None):
		newDev = Api(login=login, password=hash.make_pw_hash(login,password), email=email, api_key = hashlib.sha256(login + email).hexdigest())
		newDev.put()
		return newDev.key().id()

	@classmethod
	def findByLogin(cls, login):
		return db.GqlQuery("SELECT * FROM Api WHERE login = \'%s\'" % login).get()

	@classmethod
	def findByKey(cls, key):
		return db.GqlQuery("SELECT * FROM Api WHERE api_key = \'%s\'" % key).get()