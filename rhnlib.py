#!/usr/local/bin/python
#-----------------------------------------------------------------------------
#
# Satellite redhat api for python
#
#-----------------------------------------------------------------------------
# Metadata
#-----------------------------------------------------------------------------
__version__ = "0.01"
__release__ = "0"
__revision__ = "01"
__author__ = "Daniel Lawrence <daniel@danielscottlawrence.com>"
__URL__ = "http://danielscottlawrence.com/rhnlib"
#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------
import os
import sys
import getopt
import xmlrpclib
import time
#-----------------------------------------------------------------------------
class Satellite(object):

	#-----------------------------------------------------------------------------
	def __init__(self, server=None):
		self.server		=	"http://%s/rpc/api" % server
		self.user		=	None
		self.password	=	None
		self.key		=	None

	#-----------------------------------------------------------------------------
	def login(self, user, password):
		self.user=user
		self.password=password
		self.connect()

	#-----------------------------------------------------------------------------
	def logout(self):
		self.user=None
		self.password=None
		self.disconnect()

	#-----------------------------------------------------------------------------
	def connect(self):
		self.client = xmlrpclib.Server(self.server)
		self.key = self.client.auth.login(self.user, self.password)
		self.system = self.client.system

	#-----------------------------------------------------------------------------
	def disconnect(self):
		self.client.auth.logout(self.key)

#---------------------------------------------------------------------------------
def test():
	""" Generic test to list all the systems in satellite
	"""

	rhn = Satellite("satellite.yourdoman.com")	
	rhn.login("api-username","password")
	for system in rhn.system.listSystems(rhn.key):
		print system['name']
	rhn.logout()


#---------------------------------------------------------------------------------
if __name__ == '__main__':
	test()

#---------------------------------------------------------------------------------
#EOF
