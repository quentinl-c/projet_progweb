from handler import Handler
from user import User

import cookie

class Front(Handler):

	def get(self):
		if cookie.is_valid_and_secure(self, "userId") :
			userId = cookie.read_secure(self, "userId")
			user = User.get_by_id(int(userId))
			login = user.login
			self.render("front.html", auth = True, login = login)
		else:
			self.render("front.html", auth = False, login = None)