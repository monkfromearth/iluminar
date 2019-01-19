$(document).ready(function(){

	var sanitizeName = function($this){
		$this.keyup(function(){
			/* Removes invalid firstname characters */
			var name = $(this).val();
			$(this).val(Validator.name(name));
		});
	}

	sanitizeName($('#signup-firstname'));
	sanitizeName($('#signup-lastname'));


	$('#signup-submit').click(function(e){
		e.preventDefault();

		var firstname = $('#signup-firstname').val();
		var lastname = $('#signup-lastname').val();
		var email = $('#signup-email').val();
		var passwd = $('#signup-passwd').val();

		if (firstname.length != 0 && lastname.length != 0 && email.length != 0 && passwd.length >= 8 && Validator.email(email)){
			$.post(Routes.API.userExists, {
				'email':email,
				'csrf_token': $('#signup-token').val(),
			}, function(ajax){
				if (ajax.status){
					if (ajax.content.email){
						Repo.notify($('#signup-form'), ajax.message, 'danger', $('#signup-email'));
						return false;
					}
				} 
				NProgress.start();
	            $.post(location.pathname, {
	                'email':email,
	                'passwd':passwd,
	                'firstname':firstname,
	                'lastname':lastname,
	                'format':'web:json',
	                'csrf_token': $('#signup-token').val(),
	            }, function(ajax){
	                if (ajax.status){
	                    if (ajax.content.signedin){
	                        window.location = ajax.content.redirect;
	                        return false;
	                    }
	                }
	                Repo.notify($('#signup-form'), ajax.message);
	                NProgress.done();
	            }).fail(function(object, status, error){
	                NProgress.done();
	                $('#signin-form').submit();
	            });
			}).fail(function(object, status, error){
				$('#signup-form').submit();
			});
		} else if (firstname.length == 0 || lastname.length == 0 || email.length == 0 || passwd.length == 0){
			Repo.notify($('#signup-form'), Codes.Request.EMPTY_INPUT);
		} else if (!Validator.email(email)){
			Repo.notify($('#signup-form'), Codes.Request.INVALID_EMAIL, 'danger', $('#signup-email'));
		} else if (passwd.length < 8){
			Repo.notify($('#signup-form'), Codes.User.PASSWD_TOO_SHORT, 'danger', $('#signup-passwd'));
		}
	});

});