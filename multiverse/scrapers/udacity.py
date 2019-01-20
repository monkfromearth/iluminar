import requests, json
from bs4 import BeautifulSoup

class Udacity:

	@staticmethod
	def fromCoursePage(link):
		data = {}
		data['content'] = []
		data['instructors'] = []
		data['ratings'] = {}
		
		r = requests.get(link, headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})
		html = r.content
		soup = BeautifulSoup(html, 'html.parser')
		
		data['title'] = soup.findAll('h1')[0].text

		# findingAbout = soup.findAll('p', {'class':'description'})
		# if len(findingAbout) > 0:
		# 	pass
		# elif len(soup.findAll('p', {'class':'summary'})) > 0:
		# 	findingAbout = soup.findAll('p', {'class':'summary'})
		# elif len(soup.findAll('div', {'class':'content'})) > 0:
		# 	findingAbout = soup.findAll('div', {'class':'overlay'})[0].findChildren(('div', {'class':'content'}))[0].findChildren('p')
		# data['about'] = findingAbout[0].text
		
		data['ratings']['rating'] = soup.findAll('span', {'class':'stats__average__rating'})[0].text if len(soup.findAll('span', {'class':'stats__average__rating'})) > 0 else None # Rating
		
		if len(soup.findAll('ir-instructor-cards-in')) > 0:
			for li in soup.findAll('ir-instructor-cards-in')[0].findChildren('li'):
				instructor = {}
				instructor['source'] = None
				instructor['name'] = li.findChildren('h5', {'class':'name'})[0].text
				instructor['position'] = li.findChildren('p', {'class':'title'})[0].text
				data['instructors'].append(instructor)
		elif len(soup.findAll('ir-nd-instructors')) > 0:
			for li in soup.findAll('ir-nd-instructors')[0].findChildren('div', {'class':'card'}):
				instructor = {}
				instructor['source'] = None
				instructor['name'] = li.findChildren('h5', {'class':'name'})[0].text
				instructor['position'] = li.findChildren('p', {'class':'title'})[0].text
				data['instructors'].append(instructor)

		if len(soup.findAll('ir-degree-meta-info')) > 0:
			data['length'] = soup.findAll('ir-degree-meta-info')[1].findChildren('span')[0].text
			data['effort'] = soup.findAll('ir-degree-meta-info')[2].findChildren('span')[0].text
		elif len(soup.findAll('ir-nd-overview')) > 0:
			data['length'] = soup.findAll('ir-nd-overview')[0].findChildren('h5')[0].text
			data['effort'] = soup.findAll('ir-nd-overview')[0].findChildren('p')[0].text
		if len(soup.findAll('ir-ratings-overview')) > 0:
			data['ratings']['total_reviews'] = (soup.findAll('ir-ratings-overview')[0].findChildren('div')[0].findChildren('p')[0].text) # No. of reviews
		elif len(soup.findAll('div', {'class':'stats__container'})) > 0:
			data['ratings']['total_reviews'] = (soup.findAll('div', {'class':'stats__container'})[0].findChildren('p')[0].text.strip('()')) # No. of reviews
		else:
			data['ratings']['total_reviews'] = None
		
		# gettingSyllabus = soup.findAll('ir-term-details', {'class':'pricing-card-content'})
		# if len(gettingSyllabus) > 0:
		# 	gettingSyllabus = gettingSyllabus[0].findChildren('ul', {'class':'card_body'})[0].findChildren('li')
		# 	for m in gettingSyllabus:
		# 		heading = m.findChildren("h5")[0].text
		# 		text = m.findChildren("p")[0].text
		# 		data['content'].append({'heading':heading, 'description':text})
		# else:
		# 	gettingSyllabus = soup.findAll('section', {'class':'degree-syllabus-preview__content--parts'})[0].findChildren('li', {'class':'ng-star-inserted'})
		# 	for m in gettingSyllabus:
		# 		heading = m.findChildren("h4")[0].text
		# 		text = m.findChildren("p")[0].text
		# 		data['content'].append({'heading':heading, 'description':text})
		return data

	@staticmethod
	def fromTrackPage(link):
		data = []
		r = requests.get(link)
		html = r.content
		soup = BeautifulSoup(html, 'html.parser')
		for d in soup.findAll('ir-nanodegree-card-in', {'class':'nanodegree-card__container'}):
			print("Fetching %s ..." % ('https://in.udacity.com' + d.findChildren('div')[0].findChildren('a')[0]['href']))
			data.append(Udacity.fromCoursePage('https://in.udacity.com' + d.findChildren('div')[0].findChildren('a')[0]['href']))
		return data