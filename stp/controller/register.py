import handler

class Register(handler.Handler):

	def get(self):
		self.render("signup.html");

	def post(self):
		self.render("signup.html");
