# OAuth Configurations

## reCaptcha

RECAPTCHA_SECRET = '6LeX-IoUAAAAAHz34ajghrqpuDAcGzQ4xlEmE0NK'
RECAPTCHA_ENDPOINT = 'https://www.google.com/recaptcha/api/siteverify'

## Google

GOOGLE_CLIENT_ID = '893169002346-in2imf6eavuufa122kftbuunfr2tq6la.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET = 'wmoMZPWdfS8_WWHqhqFsrZSe'
GOOGLE_ENDPOINT = 'https://www.googleapis.com/oauth2/v1/userinfo?alt=json'
GOOGLE_ACCESS_TOKEN_URL = 'https://accounts.google.com/o/oauth2/token'
GOOGLE_AUTHORIZE_URL = 'https://accounts.google.com/o/oauth2/auth'

# Facebook

FACEBOOK_APP_ID = '512057682651293'
FACEBOOK_APP_SECRET = '14a29e68a35abe3ccac2af035ec0ecc1'
FACEBOOK_ENDPOINT = 'https://graph.facebook.com/v3.0/me?fields=id,last_name,first_name,email'
FACEBOOK_ACCESS_TOKEN_URL = 'https://graph.facebook.com/oauth/access_token'
FACEBOOK_AUTHORIZE_URL = 'https://www.facebook.com/dialog/oauth'
FACEBOOK_ENDPOINT_AVATAR = 'https://graph.facebook.com/%s/picture?type=large&redirect=true&width=250&height=250'