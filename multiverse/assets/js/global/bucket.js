var Name = "Zathura";

var Codes = {
    'Request':{
        'INPUT_TOO_LONG': "Input too long. Please provide an input of %s or less characters.",
        'EMPTY_INPUT': "Please provide some input to proceed.",
        'INCORRECT_INPUT': "Please provide some valid input.",
        'INCORRECT_CSRF_TOKEN': "Please clear cookies and cache, then try again.",
        'INVALID_CHAR': "Please use valid characters for the input.",
        'INVALID_INPUT': "Please provide some valid input.",
        'INVALID_CAPTCHA': "Please properly fill the reCaptcha.",
        'NO_CONNECTION': "Internet not connected.",
        'INVALID_EMAIL': "Please provide a valid email address.",
        'INVALID_FILETYPE':"Please select a supported media for work."
    },
    'User': {
        'NOT_FOUND': "User not found.",
        'ALREADY_EXISTS': "User with the email already exists.",
        'USERNAME_EXISTS': "Username taken. Please choose another one.",
        'PASSWD_TOO_SHORT': "Please choose a strong password of 8 or more characters.",
        'CONFIRM_PASSWD': "Please confirm the password you entered."
    }
}

var Routes = {
    API: {
        userExists:'/api/user:exists',
        webUserSearch:'/api/web/user:search',
        voteCreate:'/api/vote:create'
    },
    SCRIPTS: {
    }
}

var Content = {
}