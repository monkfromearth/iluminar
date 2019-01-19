import config.database as DATABASE
import config.app as APP
from .simplemysql import SimpleMysql
from collections import namedtuple
import random, string, uuid

class DB:

	@staticmethod
	def token(N = APP.TOKEN_LENGTH):
		''' Generates a random base64 string with defined length '''
		return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(N))

	@staticmethod
	def connect():
		if APP.DEBUG:
			return SimpleMysql(
				host = DATABASE.DB_HOST,
				db = DATABASE.DB_NAME,
				user = DATABASE.DB_USER,
				passwd = DATABASE.DB_PASSWORD,
				autocommit = True,
				charset = "utf8mb4"
			)
		else:
			return SimpleMysql(
				host = DATABASE.DB_HOST_PRODUCTION,
				db = DATABASE.DB_NAME_PRODUCTION,
				user = DATABASE.DB_USER_PRODUCTION,
				passwd = DATABASE.DB_PASSWORD_PRODUCTION,
				autocommit = True,
				charset = "utf8mb4"
			)

	@staticmethod
	def utoken(db, table, **kwargs):
		utoken = None
		length = kwargs.get('length', APP.TOKEN_LENGTH)
		column = kwargs.get('column', 'id')
		is_uuid = kwargs.get('uuid', False)
		while True:
			utoken = DB.token(length) if not is_uuid else str(uuid.uuid4())
			if db.getOne(table, [column], ('%s = %s', [column, utoken])) is None: break
		return utoken

	@staticmethod
	def rowsToTuple(cur, result, multiple = True):
		rows = None
		if result:
			Row = namedtuple("Row", [ f[0] for f in cur.description ])
			rows = [Row(*r) for r in result] if multiple else Row(*r)
		return rows

	@staticmethod
	def tupleToDict(tupl, forceList = False):
		def convertTupleToDict(t):
			dic = {}
			for r in list(t._fields):
				dic[r] = getattr(t, r)
			return dic
		if isinstance(tupl, list):
			rows = []
			for ti in tupl: rows += [ convertTupleToDict(ti) ]
			return rows
		else:
			if forceList:
				return [ convertTupleToDict(tupl) ]
			else:
				return convertTupleToDict(tupl)

	@staticmethod
	def query(db, sql):
		cur = db.query(sql)
		return DB.rowsToTuple(cur, cur.fetchall())