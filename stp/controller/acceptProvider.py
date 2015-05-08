from handler import Handler
from user import User
from TaskOffer import TaskOffer
from Task import Task

from google.appengine.ext import db



class AcceptProvider(Handler):
	def get(self,id):
		task = Task.get_by_id(int(id))

		userss = User.findByLogin(task.providerLogin)
		userss.points = userss.points + 5
		userss.put()
		task.accepted = True
		db.put(task)
		redir = "/taskDashboard/"+ str(task.taskOfferId)
		self.redirect(redir)