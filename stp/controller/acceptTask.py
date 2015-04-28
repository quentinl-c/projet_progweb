from cookie import read_secure, is_valid_and_secure
from handler import Handler
from TaskOffer import TaskOffer
from Task import Task
from user import User

class AcceptTask(Handler):

	def get(self, id):

		if not is_valid_and_secure(self, "userId"):
			self.redirect('/')
		else :
			userId = read_secure(self, "userId")
			user = User.get_by_id(int(userId))

			Task.create(int(id), user.login, False, True)

			self.redirect("/")


