from handler import Handler
from user import User

import cookie
import hash
import inputValidation
import urllib
import urllib2

URL = 'http://localhost:8080/api/auth'
KEY = 'ead76786f6e85a40fcf143885929d7903a2645e123edcf69117074efbf84eef6'

class ApiTest(Handler):
	def get(self):
			self.render("apiLoginTest.html", auth = False, login = None)

	def post(self):
		login    = self.request.get("login")
		password = self.request.get("password")

		params = dict(login = login,
			password = password,
			key      = KEY)

		url  = URL
		data = urllib.urlencode(params)
		try:
			req  = urllib2.Request(url, data)
			response = urllib2.urlopen(req)
			content  = response.read()
		except urllib2.HTTPError, e:
			response = e.code
			
		self.render("renderRequest.html", content = content )