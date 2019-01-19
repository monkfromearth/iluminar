# -*- coding: utf-8 -*-

from universe import *

from scrapers.coursera import Coursera
from scrapers.udacity import Udacity
from scrapers.udemy import Udemy

def home():
	url =''
	result = []
	if request.method == 'POST':
		agent = request.form.get('agent')
		url = request.form.get('url')
		if agent == 'coursera':
			result = Coursera.fromCoursePage(url)
		elif agent == 'udacity':
			result = Udacity.fromCoursePage(url)
		elif agent == 'udemy':
			result = Udemy.fromCoursePage(url)
	return render('pages/scraper/home', result=result, url=url)

def database_manage():
	pass