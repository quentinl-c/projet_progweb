from handler import Handler
from TaskOffer import TaskOffer
from Task import Task


class DeleteTask(Handler):

	def get(self, id):
		tasks = Task.findByTaskOfferId(int(id))

		for t in tasks:
			t.delete()

		taskOffer = TaskOffer.get_by_id(int(id))
		taskOffer.delete()

		self.redirect('/admin')
