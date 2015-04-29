from handler import Handler
from TaskOffer import TaskOffer
from Task import Task
from user import User
from cookie import read_secure, is_valid_and_secure

class TaskPanel(Handler):

	def get(self, id):
		task = TaskOffer.get_by_id(int(id))

		tasks = Task.findByTaskOfferId(id)
		if is_valid_and_secure(self, "userId"):
			userId = read_secure(self, "userId")
			user = User.get_by_id(int(userId))

			accepted = False
			for t in tasks :
				if t.providerLogin == user.login :
					accepted = True

			if task == None :
				self.redirect('/')
				return
		params = dict(auth = False,
				login = None,
				title = task.title,
				creator = task.creatorLogin,
				content = task.content,
				date = task.date,
				address = task.address
				)
		if is_valid_and_secure(self, "userId"):
			userId = read_secure(self, "userId")
			user = User.get_by_id(int(userId))
			params["auth"] = True
			params["login"] = user.login
			params["accepted"] = accepted
			params["id"]=id
		self.render("task.html", **params)
