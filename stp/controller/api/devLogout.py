from handler import Handler

class DevLogout(Handler):
	def get(self):
		self.response.delete_cookie("devId")
		self.redirect('/api/devLogin')
