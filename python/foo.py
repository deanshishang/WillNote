#!/usr/bin/env python
"This is a test module"
import sys
import os

debug = True

class FooClass(object):
	"""
		object
	"""
	version = 0.1

	def __init__(self, nm="John"):
		self.name = nm
		print "Created a class instance for", nm

	def showname(self):
		print "Your name is", self.name
		print "My name is", self.__class__.__name__

	def showver(self):
		print self.version

	def addMe2Me(self, x):
		return x+x

def test():
	foo = FooClass()

	if debug:
		print "ran test()"

if __name__ == '__main__':
	print "test"
	test()
