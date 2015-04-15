#!/usr/bin/python

from google.appengine.ext import db
import hash

class Admin(db.Model):
	login = db.StringProperty(required = True)
	password = db.StringProperty(required = True)
	
	@classmethod
	def create(cls,login,password):
		newAdmin = Admin(login=login,password=hash.make_pw_hash(login,password))
		newAdmin.put()
		return newAdmin.key().id()
		
	def findAdminByLogin(cls,login):
		return db.GqlQuery("SELECT * FROM Admin WHERE login = \'%s\'" % login)