#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       database.py
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

import logging
import os # listdir
import os.path # exists
import sys # path

# globals
backends = {}
backend_name = None
backend_module = None


# logging configuration
LOG_FILENAME = 'database.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)

def ImportBackends():
	sys.path.append(os.path.abspath("backends"))
	library_list = {}
    
    for f in os.listdir(os.path.abspath("backends")):       
        module_name, ext = os.path.splitext(f) # Handles no-extension files, etc.
        if ext == 'py': # Important, ignore .pyc/other files.
			logging.info("Found backend: " + module_name)
            module = __import__(module_name)
            library_list[module_name] = module
    return library_list

def db_Init():
	global backends
	backends = ImportBackends()
	
def db_Open(identifier, backend=None):
	for n, m in backends.iteritems():
		if backend:
			if n == backend and m.backend_MatchIdentifier(identifier):
				backend_name, backend_module = (n, m)
		else:
			if m.backend_MatchIdentifier(identifier):
				backend_name, backend_module = (n, m)
	if not backend_name:
		logging.info("Could not open " + identifier + ": no backend.")
		return None
	else:
		o = backend_module.backend_OpenIdentifier(identifier)
		logging.info("Opened " + identifier + " with backend: " + backend_name)
		return (backend_name, o)
	

    



if __name__ == '__main__':
	logging.error("database.py started by itself.  Use a frontend.")
	exit("You cannot run this script by itself; use a frontend.")

