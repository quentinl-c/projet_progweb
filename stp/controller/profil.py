from handler import Handler
from user import User
from TaskOffer import TaskOffer
from Task import Task

import cookie

class Profil(Handler):

	def get(self):
		if not(cookie.is_valid_and_secure(self, "userId")) :
			self.redirect('/login')

		userId = cookie.read_secure(self, "userId")
		user = User.get_by_id(int(userId))

		params = dict(login = user.login,
			email = user.email,
			points = user.points)

		params["lastName"] = get_or_default(user.lastName)
		params["firstName"] = get_or_default(user.firstName)
		params["phoneNumber"] = get_or_default(user.phoneNumber)
		params["address"] = get_or_default(user.address)
		params["birthDate"] = str(get_or_default(user.birthDate))

		params["taskOffer"] = TaskOffer.findByCreator(userId)
		params["task"] = Task.findByproviderLogin(user.login) 

		self.render("profil.html", auth = True, **params)

def get_or_default(param) :
	if param == None :
		return "Non renseigne(e)"
	else :
		return param