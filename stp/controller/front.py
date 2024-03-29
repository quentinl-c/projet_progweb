from handler import Handler
from user import User
from TaskOffer import TaskOffer
from cache import frontTasks

import cookie

class Front(Handler):

	def get(self):
		tasks = frontTasks()
		if cookie.is_valid_and_secure(self, "userId") :
			userId = cookie.read_secure(self, "userId")
			user = User.get_by_id(int(userId))
			login = user.login
			self.render("front.html", auth = True, login = login, tasks = tasks[0:10], script="taskNavigation.js", onloadfunction="initialRequest()")
		else:
			self.render("front.html", auth = False, login = None, tasks = tasks[0:10], script="taskNavigation.js", onloadfunction="initialRequest()")