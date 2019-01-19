from flask import request, jsonify, session
import config.app as APP
from Crypto.Hash import MD5, SHA256
import config.codes as CODES
import config.app as APP
import random, string, sys, os, time, requests, validators, user_agents
from dicttoxml import dicttoxml

class Repo:

	@staticmethod
	def hash(data, algo='md5'):
		''' Generates a hash without salt '''
		if algo is 'md5':
			return MD5.new(data).hexdigest()
		elif algo is 'sha256': 
			return SHA256.new(data).hexdigest()

	@staticmethod
	def csrfToken():
		''' Sets a CSRF Token for the current session '''
		csrf_token = session.get('csrf_token')
		if csrf_token is None:
			csrf_token = Repo.hash(os.urandom(32))
			session['csrf_token'] = csrf_token
		return csrf_token

	@staticmethod
	def time():
		''' Returns the UNIX Timestamp as int '''
		return int(time.time())

	@staticmethod
	def api(kind, status, content = {}, **kwargs):
		''' Returns a dict with the kind of API '''
		kind = '%s-%s' % (APP.SITE_NAME.lower(), kind)
		ocode = content.get('code', '')
		if len(ocode) == 0: content['code'] = 'PLATFORM:ERROR:UNKNOWN'
		message = Repo.getMessage(content.get('code'))

		# Checking for internal exceptions
		shared = kwargs.get('shared', False)
		if content.get('exception') is not None:
			del content['exception']
		package = {
			'kind':kind,
			'status':status,
			'message':message,
			'content':content
		}
		format = kwargs.get('format', 'dict')
		if format == 'json':
			return jsonify(package)
		elif format == 'xml':
			return dicttoxml(package, attr_type=False, custom_root='api')
		return package

	@staticmethod
	def output(package, format = 'json'):
		if format == 'xml':
			return dicttoxml(package, attr_type=False, custom_root='api')
		else:
			return jsonify(package)

	@staticmethod
	def request(props):
		''' Makes an external request '''
		status = False; content = {}
		try:
			# Getting inputs
			method = props.get('method', 'GET')
			endpoint = props.get('endpoint', '')
			headers = props.get('headers', {})
			timeout = props.get('timeout', APP.REQUEST_TIMEOUT)
			verify = props.get('verify', APP.REQUEST_VERIFY_SSL)
			
			if len(endpoint) == 0 or not validators.url(endpoint):
				raise ShittyError(CODES.REQUEST['ERROR']['INVALID_ENDPOINT'])

			if method is 'POST':
				data = props.get('data', {})
				r = requests.post(endpoint, data=data, timeout=timeout, headers=headers, verify=verify)
			elif method is 'GET':
				params = props.get('params', {})
				r = requests.get(endpoint, params=params, timeout=timeout, headers=headers, verify=verify)
			
			# Taking that the request was succesful, otherwise an exception would've been raised
			content['result'] = r
			status = True
			content['code'] = 'REQUEST:SUCCESS:CONNECT_SUCCESSFUL'

		except requests.exceptions.Timeout: content['code'] = 'REQUEST:ERROR:NO_CONNECTION'
		except Exception as e: Repo.exception(e)
		return Repo.api('libraries:repo#request', status, content)

	@staticmethod
	def getMessage(ocode = 'PLATFORM:ERROR:UNKNOWN'):
		''' Creates a message from the CODES config file '''
		code = ocode.split(':')
		message = CODES.C.get(code[0], {}).get(code[1], {}).get(code[2], {})
		return message

	@staticmethod
	def getLocationFromIP(ipaddr):
		''' Uses the IPStack API to make request for getting location from IP '''
		status = False; content = {}
		try:
			locationRequest = Repo.request({
				'endpoint':APP.IPSTACK_URL % (ipaddr)
			})
			content = locationRequest['content']
			if locationRequest['status']:	
				data = locationRequest['content']['result'].json()
				status = data['continent_code'] is not None
				if status: content['location'] = data
			del content['result']
		except MVCError as e: content['code'] = str(e)
		except Exception as e: Repo.exception(e)
		return Repo.api('libraries:repo#getLocationFromIP', status, content)