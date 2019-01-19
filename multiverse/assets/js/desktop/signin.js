$(document).ready(function(){

    $('#signin-submit').click(function(e){
        e.preventDefault();

        var email = $('#signin-email').val();
        var passwd = $('#signin-passwd').val();

        if (email.length != 0 && passwd.length >= 8 && Validator.email(email)){
            NProgress.start();
            $.post(location.href, {
                'email':email,
                'passwd':passwd,
                'format':'web:json',
                'csrf_token': $('#signin-token').val(),
            }, function(ajax){
                if (ajax.status){
                    if (ajax.content.signedin){
                        window.location = ajax.content.redirect;
                        return false;
                    }
                }
                Repo.notify($('#signin-form'), ajax.message);
                NProgress.done();
            }).fail(function(object, status, error){
                NProgress.done();
                $('#signin-form').submit();
            });
        } else if (email.length == 0 || passwd.length == 0){
            Repo.notify($('#signin-form'), Codes.Request.EMPTY_INPUT);
        } else if (!Validator.email(email)){
            Repo.notify($('#signin-form'), Codes.Request.INVALID_EMAIL, 'danger', $('#signin-email'));
        } else if (passwd.length < 8){
            Repo.notify($('#signin-form'), Codes.User.PASSWD_TOO_SHORT, 'danger', $('#signin-passwd'));
        }
    });

});