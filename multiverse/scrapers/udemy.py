import requests, json
from bs4 import BeautifulSoup
from selenium import webdriver

class Udemy:

	@staticmethod
	def fromCoursePage(link):
		data = {}
		data['content'] = []
		data['ratings'] = {}
		#browser = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')

		#browser.get('https://hackr.io/')

		#print "Fetching %s" % ('https://hackr.io/')

		#html = browser.page_source

		r = requests.get(link, headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})
		html = r.content
		soup = BeautifulSoup(html, 'html.parser')
		
		data['title'] = soup.findAll('h1')[0].text.strip("\n").strip() if len(soup.findAll('h1')) > 0 else ''

		data['about'] = soup.findAll('div', {'class':'clp-lead__headline'})[0].text.strip('\n').strip() if len(soup.findAll('div', {'class':'clp-lead__headline'})) > 0 else ''
		
		data['ratings']['rating'] = soup.findAll('div', {'class':'rating'})[0].findChildren('div', {'class':'rate-count'})[0].findChildren('span')[0].findChildren('span')[0].text if len(soup.findAll('div', {'class':'rating'})) > 0 else ''
		
		data['ratings']['total_reviews'] = soup.findAll('div', {'class':'rating'})[0].findChildren('div', {'class':'rate-count'})[0].findChildren('span')[0].findAll(text=True, recursive=False)[1].strip('\n').strip().strip('()').replace(" ratings", "").replace(",", "") if len(soup.findAll('div', {'class':'rating'})) > 0 else ''

		data['length'] = soup.findAll('li', {'class':'incentives__item'})[0].text.strip().strip('\n') if len(soup.findAll('li', {'class':'incentives__item'})) > 0 else ''

		if len(soup.findAll('ul', {'class':'what-you-get__items'})) > 0:
			gettingSyllabus = soup.findAll('ul', {'class':'what-you-get__items'})[0].findChildren('li')
			for m in gettingSyllabus:
				text = m.text
				data['content'].append({'description':text.strip('\n').strip()})
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


#print(Udemy.fromCoursePage('https://www.udemy.com/the-web-developer-bootcamp/'))
#print(Udemy.fromCoursePage('https://www.udemy.com/the-ultimate-mysql-bootcamp-go-from-sql-beginner-to-expert/'))