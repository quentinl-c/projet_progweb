#!/usr/bin/python

from google.appengine.ext import db

import hash

class User(db.Model):
	login = db.StringProperty(required = True)
	password = db.StringProperty(required = True)
	email = db.EmailProperty(required = True)
	lastName = db.StringProperty()
	firstName = db.StringProperty()
	birthDate = db.DateTimeProperty()
	address = db.StringProperty()
	phoneNumber = db.StringProperty()
	points = db.IntegerProperty()

	@classmethod
	def create(cls, login, password, email, lastName=None, firstName=None, birthDate=None, address=None, phoneNumber=None):
		newUser = User(login=login, password=hash.make_pw_hash(login,password), email=email, lastName=lastName, firstName=firstName, birthDate=birthDate, address=address, phoneNumber=phoneNumber, points=0)
		print newUser.put() 
		return newUser.key().id()

	@classmethod
	def deleteUser(cls, idf):
		User.get_by_id(idf).delete()

	@classmethod
	def findByLogin(cls, login):
		return db.GqlQuery("SELECT * FROM Users WHERE login = \'%s\'" % login)
