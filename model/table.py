#!/bin/env python
#coding = utf-8

import MySQLdb
import MySQLdb.cursors 
import sys

class Table():
	"""docstring for Table"""
	_name = ''
	_primary = ''

	def __init__(self):
		try:
			self.conn=MySQLdb.connect(host="127.0.0.1",user="root",passwd="123456",db="pay",cursorclass=MySQLdb.cursors.DictCursor)
			self.conn.autocommit(False)
		except MySQLdb.Error, e:
			raise Exception(e.args[1], 1)

	def __del__(self):
		self.close()

	def close(self):
		"""Closes this database connection."""
		if getattr(self, "conn", None) is not None:
			self.conn.close()
			self.conn = None

	def commit(sqls):
		self.cursor=self.conn.cursor()
		status = True
		try:
			for sql in sqls:
				self.cursor.execute(sql)
			self.conn.commit()
		except MySQLdb.Error, e:
			self.conn.rollback()
			status = False
		finally:
			self.cursor.close()
		return status

	def get(self, id = 0):
		sql = 'select * from ' + self._name + ' where ' + self._primary + " ='" + str(id) + "'"

		self.cursor=self.conn.cursor()
		try:
			self.cursor.execute(sql)
			rows = self.cursor.fetchone()
			return rows
		except MySQLdb.Error, e:
			raise Exception(e.args[1], 2)
		finally:
			self.cursor.close()
		
	def find(self, where = '', fields = [], order = '', limit = ''):
		if not where:
			where = ' where 1 = 1'
		else:
			where = ' where ' + where
		if fields :
			field = '`' + "`, `".join(fields) + '`'
		else :
			field = "*"
		if not order:
			order = ''
		else:
			order = ' order by ' + order
		if not limit:
			limit = ' limit 200'
		else:
			limit = ' limit ' + limit
		sql = 'select ' + field + ' from ' + self._name + where + order + limit

		self.cursor=self.conn.cursor()
		try:
			self.cursor.execute(sql)
			rows = self.cursor.fetchall()
			return rows
		except MySQLdb.Error, e:
			raise Exception(e.args[1], 2)
		finally:
			self.cursor.close()

	def fetch(self, where = '', fields = [], order = ''):
		if not where:
			where = ' where 1 = 1'
		else:
			where = ' where ' + where
		if fields :
			field = '`' + "`, `".join(fields) + '`'
		else :
			field = "*"
		if not order:
			order = ''
		else:
			order = ' order by ' + order
		sql = 'select ' + field + ' from ' + self._name + where + order

		self.cursor=self.conn.cursor()
		try:
			self.cursor.execute(sql)
			rows = self.cursor.fetchone()
			return rows
		except MySQLdb.Error, e:
			raise Exception(e.args[1], 2)
		finally:
			self.cursor.close()

	def insert(self, data = {}):
		fields = ''
		values = ''
		for key,value in data.items():
			fields = fields + "`" + key + "`, "
			values = values + "'" + value + "', "
		fields = fields[:-2]
		values = values[:-2]
		sql = 'insert into '+ self._name +' (' + fields + ') values (' + values + ')'

		self.cursor=self.conn.cursor()
		try:
			self.cursor.execute(sql)
			self.conn.commit()
			return self.cursor.lastrowid
		except MySQLdb.Error, e:
			raise Exception(e.args[1], 2)
		finally:
			self.cursor.close()

	def update(self, data = {}, where = "", flag = 0):
		fields = ''
		for key,value in data.items():
			fields = fields + "`" + key + "` = '" + value + "', "
		fields = fields[:-2]
		if not where:
			where = ' where 1 = 1'
		else:
			where = ' where ' + where
		if flag == 0:
			limit = ' limit 200'
		else:
			limit = ''
		sql = 'update '+ self._name +' set ' + fields + where + limit

		self.cursor=self.conn.cursor()
		try:
			self.cursor.execute(sql)
			self.conn.commit()
			return self.cursor.rowcount
		except MySQLdb.Error, e:
			raise Exception(e.args[1], 2)
		finally:
			self.cursor.close()

	def save(self, data = {}, id = 0):
		fields = ''
		for key,value in data.items():
			fields = fields + "`" + key + "` = '" + value + "', "
		fields = fields[:-2]
		if id == 0:
			where = ' limit 1'
		else:
			where = ' where ' + self._primary + " ='" + str(id) + "'"
		sql = 'update '+ self._name +' set ' + fields + where

		self.cursor=self.conn.cursor()
		try:
			self.cursor.execute(sql)
			self.conn.commit()
			return self.cursor.rowcount
		except MySQLdb.Error, e:
			raise Exception(e.args[1], 2)
		finally:
			self.cursor.close()

	def delete(self, where = '', flag = 0):
		if not where:
			where = ' where 1 = 1'
		else:
			where = ' where ' + where
		if flag == 0:
			limit = ' limit 200'
		else:
			limit = ''
		sql = 'delete from '+ self._name + where + limit

		self.cursor=self.conn.cursor()
		try:
			self.cursor.execute(sql)
			self.conn.commit()
			return self.cursor.rowcount
		except MySQLdb.Error, e:
			raise Exception(e.args[1], 2)
		finally:
			self.cursor.close()

	def deld(self, id = 0):
		if id == 0:
			where = ' limit 1'
		else:
			where = ' where ' + self._primary + " ='" + str(id) + "'"
		sql = 'delete from '+ self._name + where

		self.cursor=self.conn.cursor()
		try:
			self.cursor.execute(sql)
			self.conn.commit()
			return self.cursor.rowcount
		except MySQLdb.Error, e:
			raise Exception(e.args[1], 2)
		finally:
			self.cursor.close()