from handler import Handler
from TaskOffer import TaskOffer
from jsonRender import as_dict
from search import search
from api import Api
from user import User
from inputValidation import valid_username, valid_password
from cookie import set_secure

class Auth(Handler):
	def get(self):
		response = {'error' : 'InvalidMethod'}
		self.render_json(response)

	def post(self):
		key = self.request.post("key")
		login = self.request.post("login")
		password = self.request.post("password")

		if key:
			if Api.findByKey(fey):
				if login and password:
					if valid_username(login) and valid_password(password):
						user = User.findByLogin(login)
						if user and hash.valid_pw(user.login, password, user.password):
							set_secure(self, "userId", str(user.key().id()))
							response = {'UserAuth' : True}
						else:
							response = {'UserAuth' : 'Invalid', 'key' : True}
					else:
						response = {'UserAuth' : 'InvalidInput', 'key' : True}
			else :
				response = {'UserAuth' : False, 'key' : False}
		else:
			response = {'UserAuth' : False, 'key' : None}
		self.render_json(response)