from handler import Handler
from api import Api
from TaskOffer import TaskOffer
from Task import Task
from opt import opt

import cookie

class DevPanel(Handler):

	def get(self):
		if not(cookie.is_valid_and_secure(self, "devId")) :
			self.redirect('/login')
			return

		devId = cookie.read_secure(self, "devId")
		dev   = Api.get_by_id(int(devId))

		params = dict(login = dev.login,
			email  = dev.email,
			apiKey = dev.api_key)

		self.render("DevPanel.html", auth = True, **params)