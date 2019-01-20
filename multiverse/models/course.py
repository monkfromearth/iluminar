from libraries.repo import Repo
from libraries.exception import MVCError
from libraries.neumann import DB

class Course:

	table = 'courses'

	@staticmethod
	def search(props):
		status = False; content = {}
		try:
			query = props.get('query', '')
			fields = props.get('fields', ['*'])
			if len(query) == 0:
				raise MVCError('REQUEST:ERROR:EMPTY_INPUT')
			db = DB.connect()
			result = db.getAll(Course.table, fields, ('LOWER(title) LIKE LOWER(%s)', [ '%' + query + '%' ]))
			db.end()
			status = result is not None
			if status:
				content['code'] = 'PLATFORM:SUCCESS:DB_DATA_FOUND'
				content['result'] = DB.tupleToDict(result)
			else:
				content['code'] = 'PLATFORM:SUCCESS:DB_DATA_NOT_FOUND'
				content['result'] = []
		except MVCError as e:  content['code'] = str(e)
		except Exception as e: MVCError.catch(e)
		return Repo.api('models:courses#search', status, content)

	@staticmethod
	def create(props):
		status = False; content = {}
		try:
			tag = props.get('tag', '')
			title = props.get('title', '')
			link = props.get('link', '')
			created = Repo.time()
			info = {
				'tag':tag,
				'title':title,
				'link':link,
				'created':created
			}
			db = DB.connect()
			rowsInserted = db.insert(Course.table, info)
			db.end()
			status = rowsInserted == 1
			if status:
				content['code'] = 'PLATFORM:SUCCESS:DB_DATA_CREATED'
				info['id'] = db.lastId()
				content['info'] = info
			else:
				content['code'] = 'PLATFORM:ERROR:DB_UNKNOWN'
		except MVCError as e: content['code'] = str(e)
		except Exception as e: content['exception'] = MVCError.catch(e)
		return Repo.api('models:course#create', status, content)

	@staticmethod
	def get(props):
		status = False; content = {}
		try:
			id = props.get('id', '')
			link = props.get('link', '')
			tag = props.get('tag', '')
			if all(len(x) == 0 for x in [ id, link, tag ]):
				raise MVCError('REQUEST:ERROR:EMPTY_INPUT')
			if len(id) != 0:
				result = db.getOne(Course.table, ['*'], ('id = %s', [ id ]))
			elif len(tag) != 0:
				result = db.getAll(Course.table, ['*'], ('tag = %s', [ tag ]))
			elif len(link) != 0:
				result = db.getOne(Course.table, ['*'], ('link = %s', [ link ]))
			else: result = None
			db.end()
			status = result is not None
			if status:
				content['code'] = 'PLATFORM:SUCCESS:DB_DATA_FOUND'
				content['result'] = DB.tupleToDict(result)
			else:
				content['code'] = 'PLATFORM:ERROR:DB_DATA_NOT_FOUND'
				content['result'] = []
		except MVCError as e: content['code'] = str(e)
		except Exception as e: content['exception'] = MVCError.catch(e)
		return Repo.api('models:course#get', status, content)

	@staticmethod
	def exists(props):
		status = False; content = {}
		try:
			id = props.get('id', '')
			link = props.get('link', '')
			tag = props.get('tag', '')
			if all(len(x) == 0 for x in [ id, link, tag ]):
				raise MVCError('REQUEST:ERROR:EMPTY_INPUT')
			if len(id) != 0:
				result = db.getOne(Course.table, ['id'], ('id = %s', [ id ]))
			elif len(tag) != 0:
				result = db.getAll(Course.table, ['id'], ('tag = %s', [ tag ]))
			elif len(link) != 0:
				result = db.getOne(Course.table, ['id'], ('link = %s', [ link ]))
			else: result = None
			db.end()
			status = result is not None
			if status:
				content['code'] = 'PLATFORM:SUCCESS:DB_DATA_FOUND'
				content['result'] = DB.tupleToDict(result)
			else:
				content['code'] = 'PLATFORM:ERROR:DB_DATA_NOT_FOUND'
				content['result'] = []		
		except MVCError as e: content['code'] = str(e)
		except Exception as e: content['exception'] = MVCError.catch(e)
		return Repo.api('models:course#exists', status, content)

	@staticmethod
	def remove(props):
		status = False; content = {}
		try:
			id = props.get('id', '')
			tag = props.get('tag', '')
			title = props.get('title', '')
			link = props.get('link', '')
			if all(len(x) == 0 for x in [ id, tag, title, link ]):
				raise MVCError('REQUEST:ERROR:EMPTY_INPUT')
			created = Repo.time()
			db = DB.connect()
			#if 
			rowsDeleted = db.insert(Course.table, (''))
			db.end()
			status = rowsInserted == 1
			if status:
				content['code'] = 'PLATFORM:SUCCESS:DB_DATA_CREATED'
				content['info'] = info
			else:
				content['code'] = 'PLATFORM:ERROR:DB_UNKNOWN'		
		except MVCError as e: content['code'] = str(e)
		except Exception as e: content['exception'] = MVCError.catch(e)
		return Repo.api('models:course#remove', status, content)