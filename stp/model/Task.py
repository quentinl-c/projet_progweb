from google.appengine.ext import db

from TaskOffer import TaskOffer

class Task(db.Model):
	taskOfferId = db.IntegerProperty(required=True)
	providerLogin = db.StringProperty(required=True)
	done = db.BooleanProperty(required=True)
	accepted = db.BooleanProperty(required=True)

	@classmethod
	def create(cls, taskOfferId, providerLogin, done, accepted):
		task = Task(taskOfferId=taskOfferId, providerLogin=providerLogin, done=done, accepted=accepted)
		task.put()
		return task.key().id()

	@classmethod
	def findByTaskOfferId(cls, taskOfferId):
		return db.GqlQuery("SELECT * FROM Task WHERE taskOfferId = %s" % str(taskOfferId)).get()

	@classmethod
	def findByproviderLogin(cls, providerLogin):
		tasks = db.GqlQuery("SELECT * FROM Task WHERE providerLogin = \'%s\'" % providerLogin).run()
		l = []
		for task in tasks:
			taskOffer = TaskOffer.get_by_id(int(task.taskOfferId))
			t = (taskOffer.title, task.done, task.accepted)
			l.append(t)
		return l
		
