# App Configurations

SITE_NAME = 'iLUMiNAR'

HOST = '0.0.0.0'

PORT = 2404

ENVIRONMENT = 'local'

DEBUG = True if ENVIRONMENT is 'local' else False

THREADED = True

TOKEN_LENGTH = 16

REQUEST_TIMEOUT = 90 # in seconds

REQUEST_VERIFY_SSL = False

SECRET_KEY = '</M0nkFr0m3@rth></M0nkFr0m3@rth>'

SESSION_DAYS = 31

ACCESS_TOKEN_EXPIRY_SECONDS = 86400