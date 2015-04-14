from google.appengine.ext import db

class Task(db.Model):
	taskOfferId = db.IntegerProperty(required=True)
	providerLogin = db.StringProperty(required=True)
	done = db.BooleanProperty(required=True)
	accepted = db.BooleanProperty(required=True)

	def create(taskOfferId, providerLogin, done, accepted):
		task = Task(taskOfferId=taskOfferId, providerLogin=providerLogin, done=done, accepted=accepted)
		task.put()
		return task.key().id()

	def findByTaskOfferId(taskOfferId):
		return db.GqlQuery("SELECT * FROM Task WHERE taskOfferId = %s" % str(taskOfferId))