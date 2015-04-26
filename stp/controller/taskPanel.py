from handler import Handler
from TaskOffer import TaskOffer
from user import User
from cookie import read_secure, is_valid_and_secure

class TaskPanel(Handler):

	def get(self, id):
		task = TaskOffer.get_by_id(int(id))

		if task == None :
			self.redirect('/')
			return
		params = dict(auth = False,
			login = None,
			title = task.title,
			creator = task.creatorLogin,
			content = task.content,
			date = task.date
			)
		if is_valid_and_secure(self, "userId"):
			userId = read_secure(self, "userId")
			user = User.get_by_id(int(userId))
			params["auth"] = True
			params["login"] = user.login
		self.render("task.html", **params)
