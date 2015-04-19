#!/usr/bin/env python

from handler import Handler
from TaskOffer import TaskOffer
from user import User

import datetime


class AddTask(Handler):

	def get(self):
		creatorLoginID = str(self.request.cookies.get("userId")).split('|')[0]

		if creatorLoginID == None:
			redirect('/')
		else :
			self.render("addTask.html")

	def post(self):

		self.title = self.request.get("title")
		self.comment = self.request.get("comment")
		self.sameAd = self.request.get("sameAd")
		LoginID = str(self.request.cookies.get("userId")).split('|')[0]
		if LoginID!=None:
			creatorLoginID=int(LoginID)
		if self.sameAd:
			self.address = User.get_by_id(creatorLoginID).address
		else:
			self.address = self.request.get("address")
			if self.address == "":
				self.address=None
		self.date=self.request.get("date")
		

		params = dict(title = self.title,
					  comment = self.comment,
					  date = self.date)
		have_error = False

		if self.title == "":
			params["error_title"] = "La tache n'a pas de titre."
			have_error = True

		if self.comment == "":
			params["error_comment"] = "La tache n'a pas de descripton."
			have_error = True

		if self.date == "":
			params["error_date"] = "La tache n'a pas de date."
			have_error = True
		else:
			self.date = datetime.datetime.strptime(self.request.get("date"), "%Y-%m-%d")
			#date = self.date.date().isoformat()

		if have_error :
			self.render("addTask.html", **params)
		else:
			
			if creatorLoginID != None:
				creatorLoginID=int(creatorLoginID)
				creatorLogin = User.get_by_id(creatorLoginID).login
				self.response.write(str(self.date))

				TaskOffer.create(self.title, self.comment, creatorLogin, self.date.date(), False, self.address)
			self.redirect("/")

