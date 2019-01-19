var Repo = {}, Validator = {};

$(document).tooltip({ selector: '[data-toggle=tooltip]' });

$(document).popover({ selector: '[data-toggle=popover]' });

$(document).selectpicker();

$(function() {
    $('a.onpage-link').click(function(e) {
      e.preventDefault();
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top-50
        }, 1000);
    });
});

$(function() {
  window.emojiPicker = new EmojiPicker({
    emojiable_selector: '[data-emojiable=true]',
    assetsPath: '../../../assets/vendors/emoji-picker/img',
    popupButtonClasses: 'fa fa-smile-o'
  });
  window.emojiPicker.discover();
});

Repo.readImage = function(input, func) {
  if (input.files && input.files[0]) {
    var reader = new FileReader();
    reader.onload = function(e) {
      func(e.target.result);
    }
    reader.readAsDataURL(input.files[0]);
  }
}

String.prototype.toTitleCase = function () {
    return this.replace(/\w\S*/g, function(txt){return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();});
};

Validator.email = function(email){
    var re = /^(([^<>()\[\]\.,;:\s@\"]+(\.[^<>()\[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i;
    return re.test(email);
}

Validator.name = function(name){
  var re = /[^a-zA-Z\u0080-\uFFFF]/gu;
  return name.replace(re, "");
}

Repo.notify = function($parent, message, category, $target){
    category = typeof category == 'undefined' ? 'danger' : category;
    $parent.children('.alert').remove();
    $parent.append('<div class="visible-none alert alert-' + category + '"><button type="button" class="close btn-sm" data-dismiss="alert" aria-label="close" style="color:#FFF;"><i class="fa fa-fw fa-times"></i></button>' + message + '</div>');
    if (typeof $target != 'undefined')
      $target.parent().addClass('has-' + category);
    $parent.find('.alert').fadeIn();
};

var spinningTemplate = '<div class="container skyscraper vcenter-p"><div class="vcenter-c text-center"><i class="fa fa-spin fa-circle-o-notch fa-fw fa-2x"></i></div></div>';

Repo.render = function(params){
    NProgress.start();
    
    var toLogHistory = typeof params.history == 'undefined' ? true : params.history;
    var postData = typeof params.data == 'undefined' ? {} : params.data;
    var toRedirect = typeof params.redirect == 'undefined' ? true : params.redirect;
    var toRedirectTime = typeof params.redirectTime == 'undefined' ? 0 : params.redirectTime;
    var tblock = typeof params.tblock == 'undefined' ? false : params.tblock;
    var tblockTarget = typeof params.tblockTarget == 'undefined' ? false : params.tblockTarget;
    var spinning = typeof params.spinning == 'undefined' ? true : false;
    var method = typeof params.method == 'undefined' ? 'html' : params.method;

    if (spinning) $('#universe').html(spinningTemplate);
    
    var data = {
      format:'web:json',
      navigator:true,
      csrf_token:params.csrf_token
    };
    data = $.extend(data, postData);

    $.post(params.location, data, function(ajax){
      NProgress.done();
      console.log(ajax);
      if (ajax.status){
        if (toRedirect){
          setTimeout(function(){
             if ($.inArray('redirect', Object.keys(ajax.content)) != -1){
              window.location = ajax.content.redirect;
              return false;
            }
          }, toRedirectTime);
        }
        if (!tblock){
          $('title').text(ajax.content.page.title + " | " + Name);
          $('#header').html(ajax.content.page.header);
          $('#universe').html(ajax.content.page.content);
          $('#footer').html(ajax.content.page.footer);
        } else {
          if (method == 'append')
            $(tblockTarget).append(ajax.content.page[tblock]);
          else
            $(tblockTarget).html(ajax.content.page[tblock]);
        }
        if (toLogHistory)
          history.pushState(null, ajax.content.page.title, params.location);
      }
      $('.selectpicker').selectpicker('refresh');
       window.emojiPicker.discover();
    }).fail(function(e, ex){
        NProgress.done();
        var msg = '';
        if (e.status === 0) msg = 'No Internet Connection.';
        else if (e.status == 404) msg = 'Couldn\'t find the page.';
        else if (e.status == 500) msg = 'We messed up. Internal Server Error.';
        else if (ex === 'parsererror') msg = 'Couldn\'t make sense of the data we recieved.';
        else if (ex === 'timeout') msg = 'We only have so much time. Request timed out.';
        else if (ex === 'abort') msg = 'Abort! Abort! Mission Aborted! Page request aborted!';
        else msg = 'Uncaught Error.' + e.responseText;
        console.err(msg);
    });
}

var __dropdown_data___ = [];
$(document).on('keyup', '.mention', function(){
  $(this).suggest('@', {
    data: function(){
      var name = $(document.activeElement).val().split('@')[1];
      if (name.length <= 1) return __dropdown_data___;
      $.post(Routes.API.webUserSearch, {
            query:name,
            on:'firstname',
            csrf_token:$('meta[name="csrf_token"]').attr('content')
      }, function(ajax){
        if (ajax.status){
          __dropdown_data___ = ajax.content.result;
        }
      });
      return __dropdown_data___;
    },
    map: function(user) {
      return {
        value: user.username,
        text: '<strong>' + user.firstname + ' ' + user.lastname + '</strong> <small>(' + user.username + ')</small>'
      };
    },
    filter: { 
      casesensitive:false,
      limit: 5
    }
  });
});