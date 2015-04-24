from handler import Handler
from user import User
from TaskOffer import TaskOffer
from Task import Task
from opt import opt

import cookie

class Profil(Handler):

	def get(self):
		if not(cookie.is_valid_and_secure(self, "userId")) :
			self.redirect('/login')
			return

		userId = cookie.read_secure(self, "userId")
		user = User.get_by_id(int(userId))

		params = dict(login = user.login,
			email = user.email,
			points = user.points)

		params["lastName"] = opt(user.lastName, "Non renseigne(e)")
		params["firstName"] = opt(user.firstName, "Non renseigne(e)")
		params["phoneNumber"] = opt(user.phoneNumber, "Non renseigne(e)")
		params["address"] = opt(user.address, "Non renseigne(e)")
		if (user.birthDate == None):
			params["birthDate"] = "Non renseigne(e)"
		else :
			params["birthDate"] = str(user.birthDate.date())

		params["taskOffer"] = TaskOffer.findByCreator(userId)
		params["task"] = Task.findByproviderLogin(user.login) 

		self.render("profil.html", auth = True, **params)