#!/usr/bin/env python

import handler

class Logout(handler.Handler):
	def get(self):
		self.response.delete_cookie("userId")
		self.redirect('/')
