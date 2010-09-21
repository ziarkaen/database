#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       sqlite.py
#       
#       Copyright 2010  <ziarkaen@zeus>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

import sqlite3

class SqliteDatabase():
	def __init__(self, filename):
		self.filename = filename
		self.conn = sqlite3.connect(filename)
		self.tablename = self._GetTableName()
		self.columns = self._GetColumns()
		return
		
	def _GetTableName(self):
		c = self.conn.cursor()
		c.execute("SELECT name FROM sqlite_master WHERE type='table';")
		tablename = c.fetchone()[0]
		return tablename
		
	def _GetColumns(self):
		cur = self.conn.cursor()
		cur.execute("SELECT * FROM " + self.tablename + ";")
		name_list = [t[0] for t in cur.description]
		return name_list


def backend_MatchIdentifier(identifier):
	if identifier.split(".")[-1] == "sqlite":
		return True
	else:
		return False

def backend_OpenIdentifier(identifier):
	return SqliteDatabase(identifier)

if __name__ == '__main__':
	logging.error("sqlite.py started by itself.  Use a frontend.")
	exit("You cannot run this script by itself; use a frontend.")

