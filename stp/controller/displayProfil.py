from handler import Handler
from user import User
from opt import opt
from cookie import read_secure, is_valid_and_secure

class DisplayProfil(Handler):

	def get(self, authorId):
		authorId = int(authorId)
		if is_valid_and_secure(self, "userId"):
			userId = int(read_secure(self, "userId"))
			if userId == authorId:
				self.redirect('/profil')
				return
			author = User.get_by_id(authorId)
			params = dict(authlogin = author.login,
				lastName = opt(author.lastName, "Non renseigne"),
				firstName = opt(author.firstName,"Non renseigne"),
				email = opt(author.email,"Non renseigne"),
				phoneNumber = opt(author.phoneNumber, "Non renseigne"),
				auth = True,
				login = User.get_by_id(userId).login)

			self.render("displayProfil.html", **params)
		else:
			self.redirect('/')