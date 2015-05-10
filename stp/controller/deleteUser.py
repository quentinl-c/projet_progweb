from handler import Handler
from TaskOffer import TaskOffer
from Task import Task
from user import User
from cache import frontTasks


class DeleteUser(Handler):

	def get(self, id):
		u = User.get_by_id(int(id))
		login = u.login
		u.delete()

		taskOffers = TaskOffer.findByCreator(login)
		for taskOffer in taskOffers:
			taskOffer.delete()

		tasks = Task.findByProvider(login)
		for task in tasks:
			task.delete()
		frontTasks(update = True)

		self.redirect('/admin')
