# -*- coding: utf-8 -*-

from datetime import datetime
from urlparse import urlparse

import re

class Helper:

	@staticmethod
	def getTimestamp(timestamp, format = '%B %d, %Y %I:%M %p'):
		return datetime.fromtimestamp(timestamp).strftime(format)

	@staticmethod
	def numberToHumanFormat(num):
		n = str(num)
		if len(n) <= 3:
			return n
		elif len(n) == 4:
			if n[1] != '0': return '%s.%sK' % (n[0], n[1])
			else: return '%sK' % (n[0])
		elif len(n) == 5:
			if n[2] != '0': return '%s%s.%sK' % (n[0], n[1], n[2])
			else: return '%s%sK' % (n[0], n[1])
		elif len(n) == 6:
			return '%s%s%sK' % (n[0], n[1], n[2])
		elif len(n) == 7:
			if n[1] != '0': return '%s.%sM' % (n[0], n[1])
			else: return '%sM' % (n[0])
		elif len(n) == 8:
			if n[2] != '0': return '%s%s.%sM' % (n[0], n[1], n[2])
			else: return '%s%sM' % (n[0], n[1])
		elif len(n) == 9:
			return '%s%s%sM' % (n[0], n[1], n[2])
		elif len(n) == 10:
			if n[1] != '0': return '%s.%sB' % (n[0], n[1])
			else: return '%sB' % (n[0])
		else:
			return n

	@staticmethod
	def getHyperlinks(text):
		URL_REGEX = r"""(?i)\b((?:https?:(?:/{1,3}|[a-z0-9%])|[a-z0-9.\-]+[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)/)(?:[^\s()<>{}\[\]]+|\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\))+(?:\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’])|(?:(?<!@)[a-z0-9]+(?:[.\-][a-z0-9]+)*[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)\b/?(?!@)))"""
		urls = re.findall(URL_REGEX, text)
		l = []
		for url in urls: 
			l += [ (url, 'http://' + url if len(urlparse(url).scheme) == 0 else url) ]
		return l

	@staticmethod
	def getDomain(link):
		result = urlparse(link)
		if result.netloc == 'udemy.com' or result.netloc == 'www.udemy.com':
			return 'udemy'
		elif result.netloc == 'udacity.com' or result.netloc == 'www.udacity.com':
			return 'udacity'
		elif result.netloc == 'coursera.org' or result.netloc == 'www.coursera.org':
			return 'coursera'