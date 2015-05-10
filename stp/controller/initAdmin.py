from handler import Handler
from admin import Admin

initiated = False

class InitAdmin(Handler):
	def get(self):
		global initiated
		if not initiated :
			Admin.create("admin", "admin")
			initiated = True
		self.redirect('/admin/login')