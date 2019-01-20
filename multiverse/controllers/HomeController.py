# -*- coding: utf-8 -*-

# Home Controller

# Renders all the global functions, wrappers and variables
from universe import *

from models.course import Course

def search():
	query = request.args.get('q', '')
	from models.course import Course
	searching = Course.search({
		'query':query
	})
	if not ['searching']:
		abort(500)
	else:
		return render('pages/web/search', query=query, result=searching['content']['result'])

def index():
	''' Renders the index page '''
	return render('pages/guest/index')

def privacy():
	return render('pages/web/privacy')

def tos():
	return render('pages/web/tos')

def test():
	return render('pages/web/test')

def query():
	query = request.args.get('title', '')
	searching = Course.search({
		'query':query,
		'fields':['title']
	})
	print searching['content']['result']
	if not searching['status']:
		return jsonify({})
	else:
		return jsonify(searching['content']['result'])
