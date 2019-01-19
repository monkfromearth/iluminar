$(document).ready(function(){

    $('#reset-submit').click(function(e){
        e.preventDefault();

        var email = $('#reset-email').val();

        if (email.length != 0 && Validator.email(email)){
            $.post(Routes.API.userExists, {
                'email':email,
                'format':'web:json',
                'csrf_token': $('#reset-token').val(),
            }, function(ajax){
                if (ajax.status){
                    if (!ajax.content.email){
                        Repo.notify($('#reset-form'), Codes.User.NOT_FOUND, 'danger', $('#reset-email'));
                        return false;
                    }
                }
                NProgress.start();
                $.post(location.pathname, {
                    'email':email,
                    'format':'web:json',
                    'csrf_token': $('#reset-token').val(),
                }, function(ajax){
                    NProgress.done();
                    Repo.notify($('#reset-form'), ajax.message, ajax.status ? 'success' : 'danger');
                }).fail(function(object, status, error){
                    NProgress.done();
                    $('#reset-form').submit();
                });
            }).fail(function(object, status, error){
                $('#reset-form').submit();
            });
        } else if (email.length == 0){
            Repo.notify($('#reset-form'), Codes.Request.EMPTY_INPUT);
        } else if (!Validator.email(email)){
            Repo.notify($('#reset-form'), Codes.Request.INVALID_EMAIL, 'danger', $('#reset-email'));
        }
    });

});