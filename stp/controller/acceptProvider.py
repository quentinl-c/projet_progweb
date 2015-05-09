from cookie import is_valid_and_secure, read_secure
from handler import Handler
from user import User
from TaskOffer import TaskOffer
from Task import Task

from google.appengine.ext import db

class AcceptProvider(Handler):
	def get(self, taskId):
		if not is_valid_and_secure(self, "userId"):
			self.redirect('/')
			return

		userId = read_secure(self, "userId")
		user = User.get_by_id(int(userId))

		task = Task.get_by_id(int(taskId))
		if task == None :
			self.redirect('/')
			return

		taskOffer = task.getTaskOffer()
		if taskOffer.creatorLogin != user.login :
			self.redirect('/')
			return

		#provider.points = provider.points + 5
		#provider.put()
		task.accepted = True
		db.put(task)
		self.redirect("/taskDashboard/" + str(task.taskOfferId))