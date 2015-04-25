from handler import Handler
from user import User
import cookie
import inputValidation
from opt import opt
import hash
from datetime import datetime

class UserInfo(Handler):
	def get(self):
		if not(cookie.is_valid_and_secure(self, "userId")) :
			self.redirect('/login')
			return

		userId = cookie.read_secure(self, "userId")
		user = User.get_by_id(int(userId))

		params = dict(login = user.login,
			email = user.email)

		params["lastName"] = user.lastName
		params["firstName"] = user.firstName
		params["phoneNumber"] = user.phoneNumber
		params["address"] = user.address
		if user.birthDate != None :
			params["birthday"] = str(user.birthDate) #TODO format that
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
		date = self.request.get("birthday")
		password = self.request.get("password")
		newPassword = self.request.get("new_password")
		confirmation = self.request.get("confirmation")

		have_error = False
		date_error = False

		params = dict(login = user.login)

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
		if date :
			try :
				date = datetime.strptime(date, "%Y-%m-%d")
				if datetime.today().date() < date.date() :
					params["error_date"] = "Vous ne venez pas du futur. [insert any reference to Back to the Future here]"
					have_error = True
				else :
					user.birthDate = date
 			except ValueError as e:
 				params["error_date"] = "La date de naissance n'est pas dans un format correct."
 				have_error = True
 				date_error = True
 		if password and newPassword and confirmation:
 			if inputValidation.valid_password(password):
 				if hash.valid_pw(user.login, password, user.password) and newPassword == confirmation :
					if inputValidation.valid_password(newPassword) and inputValidation.valid_password(confirmation):
						user.password = hash.make_pw_hash(user.login,newPassword)
					else: 
						have_error = True
				else:
					have_error = True
			else :
				have_error =True

		if not(have_error):
			user.put()
			self.redirect('/profil')
		else:
			params["global_error"] = "Erreur : vos modifications n'ont pu etre enregistrees."
			params["lastName"] = opt(lastName, user.lastName)
			params["email"] = opt(email, user.email)
			params["firstName"] = opt(firstName, user.firstName)
			params["phoneNumber"] = opt(phoneNumber, user.phoneNumber)
			params["address"] = opt(address, user.address)

			if not date_error:
				params["birthday"] = str(opt(date, (opt(user.birthDate, ""))))
			
			self.render("addInfo.html", auth=True, **params)