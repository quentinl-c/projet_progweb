from handler import Handler
from TaskOffer import TaskOffer
from Task import Task
from user import User
from cookie import read_secure, is_valid_and_secure

class TaskPanel(Handler):

	def get(self, taskOfferId):
		taskOffer = TaskOffer.get_by_id(int(taskOfferId))

		if taskOffer == None :
			self.redirect('/')
			return

		params = dict()

		tasks = Task.findByTaskOfferId(taskOfferId)
		if is_valid_and_secure(self, "userId"):
			userId = read_secure(self, "userId")
			user = User.get_by_id(int(userId))
			params["auth"] = True
			params["login"] = user.login

			if taskOffer.creatorLogin == user.login:
				self.redirect('/taskDashboard/' + taskOfferId)
				return

			for task in tasks :
				if task.providerLogin == user.login :
					params["doneTask"] = task.done
					params["acceptedTask"] = task.accepted
					params["taskId"] = task.key().id()
					params["isPotentialProvider"] = True
					break;
		
		params["title"] = taskOffer.title
		params["creator"] = taskOffer.creatorLogin
		params["content"] = taskOffer.content
		params["date"] = taskOffer.date
		params["address"] = taskOffer.address
		params["taskOfferId"] = taskOfferId
			
		self.render("task.html", **params)
