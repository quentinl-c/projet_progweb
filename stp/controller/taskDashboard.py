from handler import Handler
from user import User
from TaskOffer import TaskOffer
from Task import Task

import cookie
import inputValidation
from opt import opt

from datetime import datetime

class TaskDashboard(Handler):

	def get(self, id):
		if not cookie.is_valid_and_secure(self, "userId") :
			self.redirect('/')
			return

		task = TaskOffer.get_by_id(int(id))

		if task == None:
			self.redirect('/')
			return

		userId = cookie.read_secure(self, "userId")
		user = User.get_by_id(int(userId))

		if task.creatorLogin != user.login:
			self.redirect('/')
			return

		params = dict(auth = True, 
			login = user.login, 
			title = task.title,
			content = task.content,
			date = task.date,
			private = task.private)

		params["address"] = opt(task.address, task.address)
		params["providers"] = Task.findByTaskOfferId(int(id))

		print params["providers"]
		self.render("dashboard.html", **params)

	def post(self, id):
		if not cookie.is_valid_and_secure(self, "userId") :
			self.redirect('/')
			return

		task = TaskOffer.get_by_id(int(id))

		if task == None:
			self.redirect('/')
			return

		userId = cookie.read_secure(self, "userId")
		user = User.get_by_id(int(userId))

		if task.creatorLogin != user.login:
			self.redirect('/')
			return

		title = self.request.get("title")
		content = self.request.get("content")
		sameAd = self.request.get("sameAd")
		private = self.request.get("private")

		if sameAd:
			address = User.get_by_id(int(userId)).address
		else:
			address = self.request.get("address")

		date = self.request.get("date")

		have_error = False

		params = dict(auth = True,
			login = user.login)

		if title :
			task.title = title
		else:
			have_error = True

		if content :
			task.content = content
		else:
			have_error = True

		if address :
			task.address = address

		if private :
			task.private = True
		else :
			task.private = False

		if not date :
			params["date"] = task.date
			have_error = True
		else :
			try :
				date = datetime.strptime(date, "%Y-%m-%d")
				if datetime.today().date() > date.date() :
					params["date"] = task.date
					params["error_date"] = "La date doit etre dans le futur. [insert any reference to Back to the Future here]"
					have_error = True
				else:
					params["date"] = date
			except ValueError as e:
				params["date"] = task.date
				params["error_date"] = "La date de la tache n'est pas dans un format correct."
				have_error = True

		if not have_error :
			task.put()
			self.redirect('/task/' + str(id))
		else :
			params["global_error"] = "Erreur : vos modifications n'ont pu etre enregistrees."
			params["title"] = opt(title, task.title)
			params["content"] = opt(content, task.content)
			params["providers"] = Task.findByTaskOfferId(int(id))
			self.render("dashboard.html", **params)