# Codes for message display and logging

CODES_USER_SUCCESS = {
	'CREATED': "Signed up successfully.",
	'PASSWD_CHANGE': "Password changed successfully.",
	'EMAIL_SENT': "Email sent to you successfully.",
	'VALID_CREDENTIALS': "The credentials you entered are valid.",
	'INFO_ADDED': "The information was added successfully.",
	'INFO_UPDATED': "The information was updated successfully.",
	'UNIQUE_CREDENTIALS': "The credentials you entered are unique."
}

CODES_USER_ERROR = {
	'NOT_FOUND': "User not found.",
	'ALREADY_EXISTS': "User with the email already exists.",
	'INVALID_EMAIL': "Please provide a valid email address.",
	'EMAIL_FAILED': "Couldn't send email to you.",
	'USERNAME_EXISTS': "Username taken. Please choose another one.",
	'PASSWD_TOO_SHORT': "Please choose a strong password of 8 or more characters.",
	'NOT_CREATED': "Unfortunately, couldn't sign you up.",
	'CANT_REMOVE': "Unfortunately, couldn't remove user.",
	'INVALID_CREDENTIALS': "The credentials you entered are invalid."
}

CODES_SESSION_SUCCESS = {
	'SIGNED_IN': "Successfully signed in.",
	'SIGNED_OUT': "Successfully signed out."
}

CODES_SESSION_ERROR = {
	'INCORRECT_CREDENTIALS': "Incorrect email address, username or password.",
	'INCORRECT_PASSWD': "Password is incorrect.",
	'PASSWD_NOT_MATCHED': "Password doesn't match.",
	'INVALID_SESSION':"Couldn't validate the session. Please sign in again to continue.",
	'NOT_SIGNEDIN': "You're not signed in.",
	'COULDNT_SIGNIN': "Sorry, we couldn't sign you in."
}

CODES_REQUEST_SUCCESS = {
	'CONNECT_SUCCESSFUL': "A connection was successfully made."
}

CODES_REQUEST_ERROR = {
	'INPUT_TOO_LONG': "Input too long. Please provide an input of given or less characters.",
	'EMPTY_INPUT': "Please provide some input to proceed.",
	'INCORRECT_INPUT': "Please provide some valid input.",
	'INCORRECT_CSRF_TOKEN': "Please clear cookies and cache, then try again.",
	'INVALID_CHAR': "Please use valid characters for the input.",
	'INVALID_INPUT': "Please provide some valid input.",
	'INVALID_CAPTCHA': "Please properly fill the reCaptcha.",
	'NO_CONNECTION': "Internet not connected.",
	'INVALID_ENDPOINT': "Please provide a valid endpoint",
	'NOT_FOUND':"Not found. Perhaps, it went missing."
}

CODES_PLATFORM_SUCCESS = {
	'DB_DATA_FOUND': "Successfully found data in our database.",
	'DB_DATA_DELETED':"Successfully deleted data in our database.",
	'UNKNOWN':"The process happened successfully.",
	'DB_DATA_CREATED':"Successfully created entry in the database.",
	'DB_DATA_UPDATED':"Successfully updated entry in the database.",
	'MEDIA_UPLOADED':"The media was successfully uploaded.",
	'MEDIA_REMOVED':"The media was successfully removed."
}

CODES_PLATFORM_ERROR = {
	'UNKNOWN':"Oops! Something went wrong.",
	'DB_UNKNOWN': "There was some error with our database.",
	'DB_CANNOT_CONNECT': "Couldn't connect to the database.",
	'FILE_SIZE_BIG': "File is too large.",
	'FILE_ERROR': "There was an error with the file.",
	'DB_DATA_NOT_FOUND': "Couldn't find the data in our database.",
	'API_CLIENT_NOT_FOUND':"Couldn't find the API Client in our database.",
	'API_INVALID_ACCESS_TOKEN':"Please regenerate your access token, as this one is invalid.",
	'MEDIA_NOT_UPLOADED':"Couldn't upload the media.",
	'MEDIA_NOT_REMOVED':"Couldn't remove the media."
}

# Success and Error Codes
C = {
	'USER' : {
		'SUCCESS': CODES_USER_SUCCESS,
		'ERROR': CODES_USER_ERROR
	},
	'SESSION' : {
		'SUCCESS': CODES_SESSION_SUCCESS,
		'ERROR': CODES_SESSION_ERROR
	},
	'REQUEST' : {
		'SUCCESS': CODES_REQUEST_SUCCESS,
		'ERROR': CODES_REQUEST_ERROR
	},
	'PLATFORM' : {
		'SUCCESS': CODES_PLATFORM_SUCCESS,
		'ERROR': CODES_PLATFORM_ERROR
	},
	'HTTP' : {
		'ERROR':{
			'404':"It went missing."
		}
	}
}