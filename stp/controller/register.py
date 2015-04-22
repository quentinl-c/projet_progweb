#!/usr/bin/env python

from handler import Handler
from user import User

import inputValidation
import cookie

class Register(Handler):

	def get(self):
		self.render("signup.html")

	def post(self):

		login = self.request.get("login")
		email = self.request.get("email")
		password = self.request.get("password")
		confirmation = self.request.get("confirmation")

		params = dict(login = login,
					  email = email)
		have_error = False

		if not inputValidation.valid_username(login):
			params["error_login"] = "Le login doit etre compose de 3 a 20 chiffres/lettres."
			have_error = True

		if not inputValidation.valid_password(password):
			params["error_password"] = "Le mot de passe n'est pas correct."
			have_error = True

		if password != confirmation:
			params["error_confirmation"] = "Le second mot de passe n'est pas identique au premier."
			have_error = True

		if not inputValidation.valid_email(email):
			params["error_email"] = "L'email n'est pas correct."
			have_error = True

		if not have_error and User.findByLogin(login) != None :
			params["error_login"] = "Ce login existe deja."
			have_error = True

		if have_error :
			self.render("signup.html", **params)
		else:
			userId = User.create(login, password, email)
			cookie.set_secure(self, "userId", str(userId))
			self.redirect("/")
