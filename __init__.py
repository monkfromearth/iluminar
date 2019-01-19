# -*- coding: utf-8 -*-

from multiverse import site
import config.app as APP

def init():
	try:
		from multiverse.libraries.zredis import ZRedis
		cache = ZRedis.connect()
		if cache.get('iLuminar:init') == None or cache.get('iLuminar:init') == '0':
			from models.user import User
			import config.init as INIT
			creation = User.create({
				'firstname':INIT.firstname,
				'lastname':INIT.lastname,
				'email':INIT.email,
				'passwd':INIT.passwd
			})
			if creation['status']: cache.set('iLuminar:init', '1')
	except Exception as e: pass

if __name__ == "__main__":
	# Load configs and Run
	init()
	site.jinja_env.cache = {}
	site.secret_key = APP.SECRET_KEY
	site.jinja_env.auto_reload = True
	site.config['TEMPLATES_AUTO_RELOAD'] = True
	site.run(host=APP.HOST, port=APP.PORT, debug=APP.DEBUG, threaded=APP.THREADED)