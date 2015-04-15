#!/usr/bin/python

from google.appengine.ext import db

class Users(db.Model):
	login = db.StringProperty(required = True)
	password = db.StringProperty(required = True)
	email = db.EmailProperty(required = True)
	lastName = db.StringProperty()
	fistName = db.StringProperty()
	birthDate = db.DateTimeProperty()
	address = db.StringProperty()
	phoneNumber = db.IntegerProperty()
	points = db.IntegerProperty()

	@classmethod
	def create(cls,login,password,email,lastName=None,fistName=None,birthDate=None,address=None,phoneNumber=None):
		#TODO : hash pwd
		newUser = Users(login=login,password=password,email=email,lastName=lastName,firstName=fistName,birthDate=birthDate,address=address,phoneNumber=phoneNumber,points=0)
		print newUser.put() 
		return newUser.key().id()


	@classmethod
	def deleteUser(cls,idf):
		Users.get_by_id(idf).delete()
		
	@classmethod
	def findByLogin(cls,login):
		return db.GqlQuery("SELECT * FROM Users WHERE login = \'%s\'" % login)
