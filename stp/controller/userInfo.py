from handler import Handler
from user import User

class UserInfo(Handler):

	def get(self):
		self.render("addInfo.html")