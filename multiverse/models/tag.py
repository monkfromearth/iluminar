from libraries.neumann import DB
from libraries.exception import MVCError
from libraries.repo import Repo

class Tag:

	table = 'tags'

	@staticmethod
	def create(props):
		status = False; content = {}
		try:
			name = props.get('name', '')
			if len(name) == 0:
				raise MVCError('REQUEST:ERROR:EMPTY_INPUT')
			created = Repo.time()
			info = {
				'name':name,
				'created':created
			}
			db = DB.connect()
			rowsInserted = db.insert(Tag.table, info)
			db.end()
			status = rowsInserted == 1
			if status:
				content['code'] = 'PLATFORM:SUCCESS:DB_DATA_CREATED'
				content['info'] = info
			else:
				content['code'] = 'PLATFORM:ERROR:DB_UNKNOWN'
		except MVCError as e: content['code'] = str(e)
		except Exception as e: content['exception'] = MVCError.catch(e)
		return Repo.api('models:tag#create', status, content)

	@staticmethod
	def get(props):
		status = False; content = {}
		try:
			id = props.get('id', '')
			name = props.get('name', '')
			db = DB.connect()
			if len(id) != 0:
				result = db.getOne(Tag.table, ['*'], ('id = %s', [ id ]))
			elif len(name) != 0:
				result = db.getOne(Tag.table, ['*'], ('name = %s', [ name ]))
			else:			
				result = db.getAll(Tag.table, ['*'])
			db.end()
			status = result is not None
			if status:
				content['code'] = 'PLATFORM:SUCCESS:DB_DATA_FOUND'
				content['result'] = DB.tupleToDict(result)
			else:
				content['code'] = 'PLATFORM:ERROR:DB_UNKNOWN'
				content['result'] = []
		except MVCError as e: content['code'] = str(e)
		except Exception as e: content['exception'] = MVCError.catch(e)
		return Repo.api('models:tag#get', status, content)

	@staticmethod
	def exists(props):
		status = False; content = {}
		try:
			id = props.get('id', '')
			if len(id) == 0:
				raise MVCError('REQUEST:ERROR:EMPTY_INPUT')
			db = DB.connect()
			result = db.getAll(Tag.table, ['id'], ('id = %s', [ id ]))
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
		return Repo.api('models:tag#exists', status, content)

	@staticmethod
	def remove(props):
		status = False; content = {}
		try:
			id = props.get('id', '')
			if len(id) == 0:
				raise MVCError('REQUEST:ERROR:EMPTY_INPUT')
			db = DB.connect()
			rowsDeleted = db.delete(Tag.table, ('id = %s', [ id ]))
			db.end()
			status = rowsDeleted == 1
			if status:
				content['code'] = 'PLATFORM:SUCCESS:DB_DATA_DELETED'
			else:
				content['code'] = 'PLATFORM:ERROR:DB_UNKNOWN'
		except MVCError as e: content['code'] = str(e)
		except Exception as e: content['exception'] = MVCError.catch(e)
		return Repo.api('models:tag#remove', status, content)