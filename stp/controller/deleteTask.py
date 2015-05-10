from handler import Handler
from TaskOffer import TaskOffer
from Task import Task
from cache import frontTasks


class DeleteTask(Handler):

	def get(self, id):
		tasks = Task.findByTaskOfferId(int(id))

		for t in tasks:
			t.delete()

		taskOffer = TaskOffer.get_by_id(int(id))
		taskOffer.delete()
		frontTasks(True)
		self.redirect('/admin')
