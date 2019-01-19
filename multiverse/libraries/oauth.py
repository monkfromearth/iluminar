from repo import Repo
from exception import MVCError
import config.app as APP
import config.codes as CODES
import config.oauth as OAUTH
import requests, json

class Agent:

	@staticmethod
	def verifyCaptcha(data):
		status = False; content = {}
		result = Repo.request({
			'method':'POST',
			'endpoint':OAUTH.RECAPTCHA_ENDPOINT, 
			'data':data
		})
		if not result['status']: 
			content = result['content']
		else:
			r = result['content']['result'].json()
			status = r['success']
			if not status: 
				content['code'] = 'REQUEST:ERROR:INVALID_CAPTCHA'
		return Repo.api('libraries:oauth#verifyCaptcha', status, content)

	@staticmethod
	def parseRequest(result):
		status = False
		content = result['content']
		if result['status']:
			r = result['content']['result']
			status = r.status_code != 401
			if not status:
				content['code'] = 'REQUEST:ERROR:UNAUTHORIZED'
			else:
				content['result'] = r.json()
		return status, content

	@staticmethod
	def getGoogleUser(access_token):
		status = False; content = {}
		result = Repo.request({
			'endpoint':OAUTH.GOOGLE_ENDPOINT,
			'headers':{ 'Authorization': 'OAuth %s' % (access_token) }
		})
		status, content = Agent.parseRequest(result)
		return Repo.api('libraries:oauth#getGoogleUser', status, content)

	@staticmethod
	def getFacebookUser(access_token):
		status = False; content = {}
		result = Repo.request({
			'endpoint':OAUTH.FACEBOOK_ENDPOINT,
			'params':{'access_token':access_token},
		})
		status, content = Agent.parseRequest(result)
		return Repo.api('libraries:oauth#getFacebookUser', status, content)