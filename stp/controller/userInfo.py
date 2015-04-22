from handler import Handler
from user import User

import cookie

class UserInfo(Handler):
	def get(self):
		if not(cookie.is_valid_and_secure(self, "userId")) :
			self.redirect('/login')

		userId = cookie.read_secure(self, "userId")
		user = User.get_by_id(int(userId))

		params = dict(login = user.login,
			email = user.email)

		params["lastName"] = user.lastName
		params["firstName"] = user.firstName
		params["phoneNumber"] = user.phoneNumber
		params["address"] = user.address
	#	params["birthDate"] = str(get_or_default(user.birthDate)) #TODO format that

		self.render("addInfo.html", auth = True, **params)