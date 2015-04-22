from handler import Handler
from user import User

import cookie
import inputValidation

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

		self.render("addInfo.html", auth=True, **params)

	def post(self):
		if not(cookie.is_valid_and_secure(self, "userId")) :
			self.redirect('/login')

		userId = cookie.read_secure(self, "userId")
		user = User.get_by_id(int(userId))

		lastName = self.request.get("lastName")
		firstName = self.request.get("firstName")
		phoneNumber = self.request.get("phoneNumber")
		address = self.request.get("address")
		email = self.request.get("email")
		day = self.request.get("day")
		month = self.request.get("month")
		year = self.request.get("year")

		have_error = False

		if not inputValidation.valid_email(email):
			params["error_email"] = "L'email n'est pas correct."
			have_error = True
		else :
			user.email = email

		if lastName:
			user.lastName = lastName
		if firstName:
			user.firstName = firstName
		if phoneNumber:
			user.phoneNumber = phoneNumber
		if address:
			user.address = address
		#TODO : verify day, month and year, and if appropriate change the birthday of the user accordingly
		if not(have_error):
			user.put()
			self.redirect('/profil')
		else:
			self.render("addInfo.html", auth=True, **params)