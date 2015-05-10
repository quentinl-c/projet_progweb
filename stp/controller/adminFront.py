from handler import Handler
from user import User
from TaskOffer import TaskOffer
from admin import Admin

import cookie

class AdminFront(Handler):

	def get(self):
		tasks = TaskOffer.all()
		users  = User.all()
		if cookie.is_valid_and_secure(self, "adminId") :
			adminId = cookie.read_secure(self, "adminId")
			admin = Admin.get_by_id(int(adminId))
			login = admin.login
			self.render("admin.html", auth = True, login = login, users=users, tasks=tasks)