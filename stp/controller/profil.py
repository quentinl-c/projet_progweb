from handler import Handler
from user import User
from TaskOffer import TaskOffer
from Task import Task

import cookie


class Profil(Handler):

	def get(self):
		if cookie.is_valid_and_secure(self, "userId") :
			userId = cookie.read_secure(self, "userId")
			user = User.get_by_id(int(userId))
			login = user.login

			params = dict(login = login,
				email = user.email,
				points = user.points)

			if user.lastName == None :
				params["lastName"] = "Non renseigne"
			else :
				params["lastName"] = user.name

			if user.firstName == None :
				params["firstName"] = "Non renseigne"
			else:
				params["firstName"] = user.firstName

			if user.phoneNumber == None :
				params["phoneNumber"] = "Non renseigne"
			else :
				params["phoneNumber"] = user.phoneNumber

			if user.address == None :
				params["address"] = "Non renseigne"
			else :
				params["address"] = user.address

			if user.birthDate == None :
				params["birthDate"] = "Non renseigne"
			else :
				params["birthDate"] = str(user.birthDate)


			params["taskOffer"] = TaskOffer.findByCreator(userId)

			params["task"] = Task.findByproviderLogin(login) 

			self.render("profil.html", auth = True, **params)
		else:
			self.render("front.html", auth = False, login = None)