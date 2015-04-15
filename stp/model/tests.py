import os
import webapp2
import jinja2
from datetime import date

from google.appengine.ext import db

from users import Users
from admin import Admin
from TaskOffer import TaskOffer
from Task import Task

class MainHandler(webapp2.RequestHandler):

	

	def get(self):
		self.login="MichMichdu54"
		self.password="icicestleparadis"
		self.email="paradis@putalundi.com"
	
		#test User
		newUserID=Users.create(login=self.login,password=self.password,email=self.email)
		print newUserID
		#self.response.write("ID="+str(newUserID))
		user = Users.get_by_id(newUserID)
		print user
		self.response.write("<p>login : "+user.login +", password : "+ user.password + ", email : "+ user.email+"</p>")
		Users.deleteUser(idf=newUserID)

		#test admin
		newAdminID=Admin.create(login=self.login,password=self.password)
		a = Admin.get_by_id(newAdminID)
		self.response.write("<p>login : "+a.login +", password : "+ a.password+"</p>")

		#test taskOffer
		self.title="tondre ma pelouseeeuh"
		self.content="je veux tondre ma pelouse"
		self.creatorLogin=self.login
		self.date=date.today()
		self.private=True
		self.address="6 rue Punta Lundi"

		newTaskOfferID=TaskOffer.create(title=self.title, content=self.content, creatorLogin = self.creatorLogin, date = self.date, private = self.private, address=self.address)
		taskOf=TaskOffer.get_by_id(newTaskOfferID)
		self.response.write("<p>title : "+taskOf.title +", content : "+ taskOf.content + ", creatorLogin : "+ taskOf.creatorLogin+"</p>")
		for tasks in TaskOffer.findByTitle(self.title):
			self.response.write("<p>title : "+tasks.title +", content : "+ tasks.content + ", creatorLogin : "+ tasks.creatorLogin+"</p>")


		#test task
		self.taskOfferId=newTaskOfferID
		self.providerLogin="MichMichdu54"
		self.done=False
		self.accepted=True

		newTaskID=Task.create(taskOfferId=self.taskOfferId, providerLogin=self.providerLogin, done=self.done, accepted=self.accepted)
		task=Task.get_by_id(newTaskID)
		self.response.write("<p>taskOfferId : "+str(task.taskOfferId) +", providerLogin : "+ task.providerLogin + ", done : "+ str(task.done)+"</p>")
		for tasks in Task.findByTaskOfferId(self.taskOfferId):
			self.response.write("<p>taskOfferId : "+str(tasks.taskOfferId) +", providerLogin : "+ tasks.providerLogin + ", done : "+ str(tasks.done)+"</p>")

app = webapp2.WSGIApplication([('/', MainHandler)], debug=True)