#!/usr/bin/env python

from handler import Handler
from TaskOffer import TaskOffer
from user import User
from cookie import read_secure, is_valid_and_secure
from cache import frontTasks
from datetime import datetime
import time

class AddTask(Handler):
	def get(self):
		if is_valid_and_secure(self, "userId") :
			userId = read_secure(self, "userId")
			user = User.get_by_id(int(userId))
			self.render("addTask.html", auth=True, login =user.login)
		else :
			self.redirect('/login')

	def post(self):
		if not is_valid_and_secure(self, "userId") :
			self.redirect('/login')
			return
		creatorID = read_secure(self, "userId")
		user = User.get_by_id(int(creatorID))
		title = self.request.get("title")
		comment = self.request.get("comment")
		sameAd = self.request.get("sameAd")
		if sameAd:
			address = user.address
		else:
			address = self.request.get("address")
			if not address:
				address = None
		date = self.request.get("date")

		params = dict(login = user.login,
					  auth = True,
					  title = title,
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
			author = User.get_by_id(int(creatorID))
			creatorLogin = author.login
			creatorId = str(author.key().id())
			TaskOffer.create(title, comment, creatorLogin, creatorId, date.date(), False, address)
			frontTasks(update = True)
			self.redirect('/')

