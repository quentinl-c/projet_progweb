from handler import Handler
from user import User
from TaskOffer import TaskOffer
from cache import frontTasks

import cookie

class AboutUs(Handler):

	def get(self):
		if cookie.is_valid_and_secure(self, "userId") :
			userId = cookie.read_secure(self, "userId")
			user = User.get_by_id(int(userId))
			login = user.login
			self.render("aboutUs.html", auth = True, login = login)
		else:
			self.render("aboutUs.html", auth = False, login = None)