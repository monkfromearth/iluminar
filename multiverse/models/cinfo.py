from libraries.repo import Repo
from libraries.exception import MVCError
from libraries.neumann import DB

class CInfo:

	table = 'cinfo'

	@staticmethod
	def create(props):
		status = False; content = {}
		try:
			course = props.get('course', '')
			name = props.get('name', '')	
			ccontent = props.get('content', '')
			info = {
				'course':course,
				'name':name,
				'content':ccontent,
				'created':Repo.time()
			}
			db = DB.connect()
			rowsInserted = db.insert(CInfo.table, info)
			db.end()
			status = rowsInserted == 1
			if status:
				content['info'] = info
				content['code'] = 'PLATFORM:SUCCESS:DB_DATA_CREATED'
			else:
				content['code'] = 'PLATFORM:ERROR:DB_UNKNOWN'
		except MVCError as e: content['code'] = str(e)
		except Exception as e: MVCError.catch(e)
		return Repo.api('models:cinfo#create', status, content)

	@staticmethod
	def get(props):
		status = False; content = {}
		try:
			pass		
		except MVCError as e: content['code'] = str(e)
		except Exception as e: content['exception'] = MVCError.catch(e)
		return Repo.api('models:cinfo#get', status, content)

	@staticmethod
	def exists(props):
		status = False; content = {}
		try:
			pass		
		except MVCError as e: content['code'] = str(e)
		except Exception as e: content['exception'] = MVCError.catch(e)
		return Repo.api('models:cinfo#exists', status, content)

	@staticmethod
	def remove(props):
		status = False; content = {}
		try:
			pass		
		except MVCError as e: content['code'] = str(e)
		except Exception as e: content['exception'] = MVCError.catch(e)
		return Repo.api('models:cinfo#remove', status, content)