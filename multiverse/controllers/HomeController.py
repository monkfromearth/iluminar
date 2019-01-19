# -*- coding: utf-8 -*-

# Home Controller

# Renders all the global functions, wrappers and variables
from universe import *

def index():
	''' Renders the index page '''
	return render('pages/guest/index')

def privacy():
	return render('pages/web/privacy')

def tos():
	return render('pages/web/tos')

def test():
	return render('pages/web/test')
