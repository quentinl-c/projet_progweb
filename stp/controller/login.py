#!/usr/bin/env python

from handler import Handler
from user import User

import cookie
import hash
import inputValidation

class Login(Handler):
	def get(self):
		if cookie.is_valid_and_secure(self, "userId"):
			self.redirect('/')
		else :
			self.render("login.html", auth = False, login = None)

	def post(self):
		if cookie.is_valid_and_secure(self, "userId"):
			self.redirect('/')
		else :
			login = self.request.get("login")
			password = self.request.get("password")

			params = dict(login = login)
			have_error = False

			if not login :
				params["error_login"] = "Il faut renseigner un login."
				have_error = True

			if not password :
				params["error_password"] = "Il faut renseigner un mot de passe."
				have_error = True

			if inputValidation.valid_username(login) and inputValidation.valid_password(password) :
				if not have_error :
					user = User.findByLogin(login)
					if (not user) or (not hash.valid_pw(user.login, password, user.password)) :
						params["error_login"] = "Login ou mot de passe inconnu."
						have_error = True
			else :
				have_error = True
				params["error_login"] = "Le login ou le mot de passe pas bien forme."

			if have_error :
				params["auth"] = False
				params["login"] = None
				self.render("login.html", **params)
			else:
				cookie.set_secure(self, "userId", str(user.key().id()))
				self.redirect('/',)
