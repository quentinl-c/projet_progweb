from google.appengine.ext import db
from user import User
from collections import namedtuple

class TaskOffer(db.Model):
	title        = db.StringProperty(required=True)
	content      = db.TextProperty(required=True)
	creatorLogin = db.StringProperty(required=True)
	creatorId = db.StringProperty(required=True)
	date         = db.DateProperty(required=True)
	private      = db.BooleanProperty(required=True)
	created      = db.DateTimeProperty(auto_now_add = True)
	address      = db.StringProperty(required=False)

	@classmethod
	def create(cls, title, content, creatorLogin, creatorId, date, private, address=None):
		taskOffer = TaskOffer(title=title, content=content, creatorLogin=creatorLogin, creatorId=creatorId, date=date, private=private, address=address)
		taskOffer.put()
		return taskOffer.key().id()

	@classmethod
	def getPublishedTasks(cls):
		return db.GqlQuery("SELECT * FROM TaskOffer WHERE private = false ORDER BY created DESC").run()

	@classmethod
	def findByCreator(cls, creatorLogin):
		return db.GqlQuery("SELECT * FROM TaskOffer WHERE creatorLogin = \'%s\'" % creatorLogin).run()

	@classmethod
	def findByTitle(cls, title):
		return db.GqlQuery("SELECT * FROM TaskOffer WHERE title = \'%s\'" % title).run()