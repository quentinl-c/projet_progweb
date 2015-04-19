#!/usr/bin/python

import unittest
import hash
import string

class HashTest(unittest.TestCase):
	def test_correct_password(self):
		name = "Name"
		password = "Password"
		pw_hash = hash.make_pw_hash(name, password)
		self.assertTrue(hash.valid_pw(name, password, pw_hash))

	def test_incorrect_password(self):
		name = "Name"
		password = "Password"
		pw_hash = hash.make_pw_hash(name, password)
		self.assertFalse(hash.valid_pw(name, "Wrong", pw_hash))

	def test_legitimate_value(self):
		val = "over 9000"
		self.assertEqual(hash.read_secure_val(hash.make_secure_val(val)), val)

	def test_illegitimate_value(self):
		val = "over 9000"
		secure_val = hash.make_secure_val(val)
		hacked_val = "Thug Life" + "|" + secure_val.split('|')[1]
		self.assertIsNone(hash.read_secure_val(hacked_val))

	def test_bad_formed_value(self):
		bad_formed_val = "r77n,"
		self.assertIsNone(hash.read_secure_val(bad_formed_val))

if __name__ == '__main__':
	unittest.main()