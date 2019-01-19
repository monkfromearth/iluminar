# -*- coding: utf-8 -*-

# Error Controller

# Renders all the global functions, wrappers and variables
from universe import *

def show(code):
	message = Repo.getMessage('HTTP:ERROR:404')
	return render("pages/web/error", code=code, message=message), code