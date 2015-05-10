#!/usr/bin/env python

from handler import Handler
from admin import Admin

import cookie
import hash
import inputValidation

class LoginAdmin(Handler):
	def get(self):
		if cookie.is_valid_and_secure(self, "adminId"):
			self.redirect('/admin')
		else :
			self.render("login.html", auth = False, login = None)

	def post(self):
		if cookie.is_valid_and_secure(self, "adminId"):
			self.redirect('/admin')
		else :
			login = self.request.get("login")
			password = self.request.get("password")

			params = dict(login = login)
			have_error = False

			if not login :
				params["error_login"] = "Il faut renseigner un login admin."
				have_error = True

			if not password :
				params["error_password"] = "Il faut renseigner un mot de passe."
				have_error = True

			if inputValidation.valid_username(login) and inputValidation.valid_password(password) :
				if not have_error :
					administrator = Admin.findAdminByLogin(login)
					if (not administrator) or (not hash.valid_pw(administrator.login, password, administrator.password)) :
						params["error_login"] = "Login admin ou mot de passe inconnu."
						have_error = True
			else :
				have_error = True
				params["error_login"] = "Le login admin ou le mot de passe pas bien forme."

			if have_error :
				params["auth"] = False
				params["login"] = None
				self.render("login.html", **params)
			else:
				cookie.set_secure(self, "adminId", str(administrator.key().id()))
				self.redirect('/admin',)
