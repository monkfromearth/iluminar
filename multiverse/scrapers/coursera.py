import requests, json
from bs4 import BeautifulSoup

class Coursera:

	@staticmethod
	def fromCoursePage(link):
		data = {}
		data['content'] = []
		data['ratings'] = {}
		data['skills'] = []
		data['instructors'] = []
		r = requests.get(link, headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})
		html = r.content
		soup = BeautifulSoup(html, 'html.parser')
		instructors = soup.findAll('div', {'class':'Instructors'})[0].findChildren('div')[1]
		ins_img = instructors.findChildren('img')
		ins_h3 = instructors.findChildren('h3')
		ins_e = soup.findAll('div', {'class':'Instructors'})[0].findChildren('div')[1].findChildren('div', recursive=False)
		for i in xrange(len(instructors.findChildren('img'))):
			instructor = {}
			instructor['source'] = ins_img[i]['src']
			instructor['name'] = ins_h3[i].text
			e = ins_e[i]
			l = e.findAll(text=True)
			instructor['position'] = "%s, %s" % (l[2], l[4])
			data['instructors'].append(instructor)
		data['length'] = ''.join(filter(str.isdigit, map(str, soup.findChildren('div', {'class':'ProductGlance'})[0].findChildren('div', recursive=False)[2].findChildren('h4')[0].text.split())))
		#data['effort'] = soup.findChildren('div', {'class':'ProductGlance'})[0].findChildren('div', recursive=False)[2].findChildren('div', recursive=False)[1].findChildren('div', recursive=False)[0].findChildren('div', recursive=False)[0].findChildren('span', recursive=False)[0].findChildren('span', recursive=False)[1].text if len(soup.findChildren('div', {'class':'ProductGlance'})) > 0 else ''
		data['title'] = soup.findAll('h1')[1].text
		data['additional'] = {
			'partner':soup.findAll('div', {'class':'Banner'})[0].findChildren('img')[0]['title']
		}
		data['about'] = soup.findAll('div', {'class':'AboutCourse'})[0].findChildren('div', {'class':'content-inner'})[0].text
		for d in soup.findAll('div', {'class':'CourseRating'}):
			data['ratings']['rating'] = d.findChildren('span')[0].text # Rating
			data['ratings']['total_ratings'] = d.findChildren('div')[1].findChildren('span')[0].text.replace(" ratings", "").replace(",", "") # No. of Ratings
			data['ratings']['total_reviews'] = d.findChildren('div')[2].findChildren('div')[1].findChildren('span')[0].text.replace(" reviews", "").replace(",", "") # No. of reviews
		for m in soup.findAll('div', {'class':'SyllabusModule'}):
			heading = m.findChildren("h2")[0].text
			children = m.findChildren("div")
			text = children[5].text.replace("... Show All", "")
			data['content'].append({'heading':heading, 'description':text})
		return data

	@staticmethod
	def fromSpecialization(link):
		data = []
		r = requests.get(link)
		html = r.content
		soup = BeautifulSoup(html, 'html.parser')
		for d in soup.findAll('div', {'class':'CourseItem'}):
			data.append(Coursera.fromCoursePage('https://coursera.org' + d.findChildren('div')[2].findChildren('a', href=True)[0]['href']))
		return data

#print(CourseraScraper('https://www.coursera.org/learn/fashion-design'))
#print(CourseraScraper('https://www.coursera.org/learn/technical-support-fundamentals'))
#print(Coursera.fromCoursePage('https://www.coursera.org/learn/physiology'))
#print(ScrapFromSpecialization('https://www.coursera.org/specializations/digital-marketing'))