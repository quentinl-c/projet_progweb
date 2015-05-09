from cookie import read_secure, is_valid_and_secure
from handler import Handler
from TaskOffer import TaskOffer
from Task import Task
from user import User

class CancelTask(Handler):

	def get(self, taskId):
		if not is_valid_and_secure(self, "userId"):
			self.redirect('/login')
		else :
			userId = read_secure(self, "userId")
			user = User.get_by_id(int(userId))

			task = Task.get_by_id(int(taskId))
			if not task.done :
				taskOffer = TaskOffer.get_by_id(task.taskOfferId)
				if user.login == task.providerLogin :
					task.delete();
					self.redirect("/task/" + str(taskId))
					return
				elif user.login == taskOffer.creatorLogin :
					task.delete();
					self.redirect("/profil")
					return
			else :
				self.redirect("/task/" + str(taskId))
				return
			self.redirect("/")
