from cookie import read_secure, is_valid_and_secure
from handler import Handler
from TaskOffer import TaskOffer
from Task import Task
from user import User

class RegisterForTask(Handler):

	def get(self, taskOfferId):
		if not is_valid_and_secure(self, "userId"):
			self.redirect('/login')
			return

		userId = read_secure(self, "userId")
		user = User.get_by_id(int(userId))

		tasks = Task.findByTaskOfferId(taskOfferId)
		for task in tasks :
			if task.providerLogin == user.login :
				self.redirect('/task/' + str(taskOfferId))
				return

		Task.create(int(taskOfferId), user.login, False, False)

		self.redirect("/task/"+str(taskOfferId))
