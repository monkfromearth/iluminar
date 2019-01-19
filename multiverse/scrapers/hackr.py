from selenium import webdriver
from bs4 import BeautifulSoup
import json


browser = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')

browser.get('https://hackr.io/')

print "Fetching %s" % ('https://hackr.io/')

html = browser.page_source

soup = BeautifulSoup(html, 'html.parser')

container = {}

categories = soup.findAll('a', {'class':'topic-grid-item'})


for a in categories:
	category = a.text.strip().strip('\n')
	container[category] = []
	link = a['href']
	print "Category: %s (%s)" % (category, link)
	browser.get(link)
	html = browser.page_source
	fresh = BeautifulSoup(html, 'html.parser')
	for div in fresh.findAll('div', {'class':'tut-list'}):
		break
		title = div.findAll('span', {'class':'tutorial-title-txt'})[0].text
		link = div.findAll('a', {'class':'js-tut-direct-link'})
		if len(link) > 0:
			link = link[0]['href']
			if len(link) > 0:
				link = link.split('=')[-1]
			else: continue
		else: continue
		print "%s [%s]" % (title, link)
		container[category] += [ {'link':link, 'title':title} ]
	print fresh.findAll('div', {'class':'pagination'})
	for li in fresh.findAll('ul', {'class':'pagination'}):
		 print(li.findChildren('a'))
	print ""

	
file = open('courses_design.json', 'w')
file.write(json.dumps(container))
file.close()