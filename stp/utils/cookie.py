import webapp2
import hash

def set_secure(handler, name, val):
	cookie_val = hash.make_secure_val(val)
	handler.response.set_cookie(str(name), str(cookie_val))

def is_valid_and_secure(handler, name):
	cookie_val = handler.request.cookies.get(name)
	return bool(cookie_val) and bool(hash.read_secure_val(cookie_val))

def read_secure(handler, cookie_name):
	return hash.read_secure_val(handler.request.cookies.get(cookie_name))