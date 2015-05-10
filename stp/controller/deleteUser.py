from handler import Handler
from user import User


class DeleteUser(Handler):

	def get(self, id):
		u = User.get_by_id(int(id))
		u.delete()
		self.redirect('/admin')
