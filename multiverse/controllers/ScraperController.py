# -*- coding: utf-8 -*-

from universe import *

from scrapers.coursera import Coursera
from scrapers.udacity import Udacity
from scrapers.udemy import Udemy

from libraries.repo import Repo

def query():
	agent = request.form.get('agent')
	url = request.form.get('url')
	if agent == 'coursera':
		result = Coursera.fromCoursePage(url)
	elif agent == 'udacity':
		result = Udacity.fromCoursePage(url)
	elif agent == 'udemy':
		result = Udemy.fromCoursePage(url)
	return jsonify(result)

def scrapToDatabase():
	from models.tag import Tag
	from models.course import Course 
	from models.cinfo import CInfo
	from urlparse import urlparse
	import json, os, validators

	file = open(os.path.abspath('multiverse/datasets/courses_programming.json'))
	data = file.read().splitlines()[0]
	file.close()

	data = json.loads(data)

	for tag in data.keys():
		getting = Tag.get({ 'name':tag })
		print getting
		if not getting['status']: continue
		id = getting['content']['result']['id']
		for course in data[tag]:
			if not validators.url(course['link']): continue
			else:
				site = urlparse(course['link'])
				print site
				if site.netloc == 'www.udacity.com' or site.netloc == 'udacity.com':
					result = Udacity.fromCoursePage(course['link'])
					creation = Course.create({
						'tag':id,
						'title':course['title'],
						'link':course['link'],
						'created':Repo.time()
					})
					if creation['status']:
						CInfo.create({
							'course':creation['content']['info']['id'],
							'name':'content',
							'content':json.dumps(result['content'])
						})

	return jsonify(data)