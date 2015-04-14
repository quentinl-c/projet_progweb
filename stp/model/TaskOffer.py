from google.appengine.ext import db

class TaskOffer(db.Model):
	title = db.StringProperty(required=True)
	content = db.TextProperty(required=True)
	creatorLogin = db.StringProperty(required=True)
	date = db.DateProperty(required=True)
	private = db.BooleanProperty(required=True)
	address = db.StringProperty(required=False)

	def create(title, content, creatorLogin, date, private, address):
		taskOffer = TaskOffer(title=title, content=content, creatorLogin=creatorLogin, date=date, private=private, address=address)
		taskOffer.put()
		return taskOffer.key().id()

	def findByCreator(creatorLogin):
		return db.GqlQuery("SELECT * FROM TaskOffer WHERE name = %s" % creatorLogin)

	def findByTitle(title):
		return db.GqlQuery("SELECT * FROM TaskOffer WHERE title = %s" % title)