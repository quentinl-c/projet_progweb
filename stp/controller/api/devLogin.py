#!/usr/bin/env python

from handler import Handler
from api import Api

import cookie
import hash
import inputValidation

class DevLogin(Handler):
	def get(self):
		if cookie.is_valid_and_secure(self, "devId"):
			self.redirect('/api/devPanel')
		else :
			self.render("devLogin.html")

	def post(self):
		if cookie.is_valid_and_secure(self, "devId"):
			self.redirect('/')
		else :
			login = self.request.get("login")
			password = self.request.get("password")

			params = dict()
			have_error = False

			if not login :
				params["error_login"] = "Il faut renseigner un login."
				have_error = True

			if not password :
				params["error_password"] = "Il faut renseigner un mot de passe."
				have_error = True

			if inputValidation.valid_username(login) and inputValidation.valid_password(password) :
				if not have_error :
					dev = Api.findByLogin(login)
					if (not dev) or (not hash.valid_pw(dev.login, password, dev.password)) :
						params["error_login"] = "Login ou mot de passe inconnu."
						have_error = True
			else :
				have_error = True
				params["error_login"] = "Le login ou le mot de passe pas bien forme."

			if have_error :
				self.render("devLogin.html", **params)
			else:
				cookie.set_secure(self, "devId", str(dev.key().id()))
				self.redirect('/api/devPanel',)
