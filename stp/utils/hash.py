import random
import string
import hashlib
import hmac

secret = "I have never ridden an elephant"

#Functions to hash passwords
def make_salt():
	return ''.join(random.choice(string.letters) for x in xrange(5))

def make_pw_hash(name, pw, salt=None):
	if not salt:
		salt = make_salt()
	h = hashlib.sha256(name + pw + salt).hexdigest()
	return '%s,%s' % (salt, h)

def valid_pw(name, password, h):
	salt = h.split(',')[0]
	return h == make_pw_hash(name, password, salt)

#Functions to hash cookie contents
def make_secure_val(val):
	return '%s|%s' % (val, hmac.new(secret, val).hexdigest())

def read_secure_val(secure_val):
	val = secure_val.split('|')[0]
	if secure_val == make_secure_val(val):
		return val