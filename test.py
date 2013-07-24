#!/bin/env python
#coding = utf-8

import tornado.web
import json
from model.test import Test

class TestHandler(tornado.web.RequestHandler):
	"""docstring for TestHandler"""
	def get(self):
		self.write("this is learsu test")

class TradeHandler(tornado.web.RequestHandler):
	"""docstring for TradeHandler"""
	def get(self):
		self.write("this is learsu trade")
	
class TestGetHandler(tornado.web.RequestHandler):
		"""docstring for TestGetHandler"""
		def get(self, id):
			try:
				id = int(id) 
			except ValueError:
				id = 0
			self.write(str(id))

class TestModHandler(tornado.web.RequestHandler):
	"""docstring for TestModHandler"""
	def get(self, id = 0):
		try:
			id = int(id) 
		except ValueError:
			id = 0

		try:
			test = Test()
			b=test.get(id)
			self.write(str(b)+"<br>")
			self.write(json.dumps(b)+"<br>")

			b = test.find(where = '`id` > 1', fields = ['id', 'name'], order = '`id` desc', limit = '')
			self.write(str(b)+"<br>")
			self.write(json.dumps(b)+"<br>")

			b = test.find(where = '`id` > 1', fields = ['id', 'name'], order = '`id` desc', limit = '10, 4')
			self.write(str(b)+"<br>")
			self.write(json.dumps(b)+"<br>")

			b = test.fetch(where = '`id` > 1', fields = ['id', 'name'], order = '')
			self.write(str(b)+"<br>")
			self.write(json.dumps(b)+"<br>")

			data = {'name': 'python-autocommit', 'pwd': '808080'}
			b = test.insert(data)
			self.write(str(b)+" insert<br>")

			data = {'name': 'python-test', 'pwd': '123456'}
			b = test.update(data)
			self.write(str(b)+" update<br>")

			b = test.update(data, '', 0)
			self.write(str(b)+" update<br>")

			b = test.update(data, '`id` > 2', 1)
			self.write(str(b)+" update<br>")

			b = test.update(data, '`id` > 2')
			self.write(str(b)+" update<br>")

		except Exception, e:
			self.write(str(e)+"<br>")
		
		
			
class GoHandler(tornado.web.RequestHandler):
	"""docstring for GoHandler"""
	def get(self, arg1 = "arg1", arg2 = "arg2", arg3 = "arg3"):
		self.write(arg1 + "--->" + arg2 + "--->" + arg3)
		