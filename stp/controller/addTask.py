#!/usr/bin/env python

from handler import Handler
from TaskOffer import TaskOffer
from user import User
from cookie import read_secure, is_valid_and_secure

from datetime import datetime

class AddTask(Handler):
	def get(self):
		if is_valid_and_secure(self, "userId") :
			self.render("addtask.html")
		else :
			self.redirect('/login')

	def post(self):
		creatorID = read_secure(self, "userId")
		if not is_valid_and_secure(self, "userId") :
			redirect('/login')
		creatorID = read_secure(self, "userId")
		title = self.request.get("title")
		comment = self.request.get("comment")
		sameAd = self.request.get("sameAd")
		if sameAd:
			address = User.get_by_id(int(creatorID)).address
		else:
			address = self.request.get("address")
			if not address:
				address = None
		date = self.request.get("date")

		params = dict(title = title,
					  comment = comment,
					  date = date,
					  address = address)
		have_error = False

		if not title :
			params["error_title"] = "La tache n'a pas de titre."
			have_error = True

		if not comment :
			params["error_comment"] = "La tache n'a pas de description."
			have_error = True

		if not date :
			params["error_date"] = "La tache n'a pas de date."
			have_error = True
		else :
			try :
				date = datetime.strptime(date, "%Y-%m-%d")
				if datetime.today().date() > date.date() :
					params["error_date"] = "La date doit etre dans le futur. [insert any reference to Back to the Future here]"
					have_error = True
			except ValueError as e:
				params["error_date"] = "La date de la tache n'est pas dans un format correct."
				have_error = True

		if have_error :
			self.render("addTask.html", **params)
		else:
			creatorLogin = User.get_by_id(int(creatorID)).login
			TaskOffer.create(title, comment, creatorLogin, date.date(), False, address)
			self.redirect('/')
