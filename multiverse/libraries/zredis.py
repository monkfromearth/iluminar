from redis import Redis
import config.database as DATABASE

class ZRedis:

	@staticmethod
	def connect():
		return Redis(
			host = DATABASE.REDIS_HOST,
			port = DATABASE.REDIS_PORT,
		)