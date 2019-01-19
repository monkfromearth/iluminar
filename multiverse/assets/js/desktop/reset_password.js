$(document).ready(function(){

    $('#reset-submit').click(function(e){
        e.preventDefault();
        var passwd = $('#reset-passwd').val();
        var confpasswd = $('#reset-conf_passwd').val();
        var integrity = $('#reset-integrity').val();
        if (passwd.length >= 8 && confpasswd == passwd){
            NProgress.start();
            $.post(location.pathname, {
                'passwd':passwd,
                'format':'web:json',
                'integrity':integrity,
                'csrf_token': $('#reset-token').val(),
            }, function(ajax){
                Repo.notify($('#reset-form'), ajax.message, ajax.content.updated ? 'success' : 'danger');
                if (ajax.status && ajax.content.updated){
                    setTimeout(function(){
                        window.location = ajax.content.redirect;
                    }, 2000);                    
                    return false;
                }
                NProgress.done();
            }).fail(function(object, status, error){
                NProgress.done();
                $('#reset-form').submit();
            });
        } else if (passwd.length < 8){
            Repo.notify($('#reset-form'), Codes.User.PASSWD_TOO_SHORT, 'danger', $('#reset-passwd'));
        } else if (confpasswd != passwd){
            Repo.notify($('#reset-form'), Codes.User.CONFIRM_PASSWD, 'danger', $('#reset-conf_passwd'));
        }
    });

});