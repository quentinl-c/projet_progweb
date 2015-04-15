#!/usr/bin/env python
import handler
import inputValidation
import user

class Register(handler.Handler):

	def get(self):
		self.render("signup.html")

	def post(self):

		self.login = self.request.get("login")
		self.email = self.request.get("email")
		self.password = self.request.get("password")
		self.confirmation = self.request.get("confirmation")

		params = dict(login = self.login,
					  email = self.email)
		have_error = False

		if not inputValidation.valid_username(self.login):
			params["error_login"] = "Le login doit etre compose de 3 a 20 chiffres, lettres "
			have_error = True

		if not inputValidation.valid_password(self.password):
			params["error_password"] = "Le mot de passe n'est pas correcte"
			have_error = True

		if self.password != self.confirmation:
			params["error_confirmation"] = "Le second mot de passe n'est pas identique au premier"
			have_error = True

		if not inputValidation.valid_email(self.email):
			params["error_email"] = "L'email n'est pas correcte"
			have_error = True

		if not have_error and user.User.findByLogin(self.login) != None :
			params["error_login"] = "Ce login existe deja"
			have_error = True

		if have_error :
			self.render("signup.html", **params)
		else:
			user.User.create(self.login, self.password, self.email)
			self.redirect("/")

