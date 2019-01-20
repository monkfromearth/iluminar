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

var smallSpinningTemplate = '<div class="container-fluid small-skyscraper vcenter-p"><div class="vcenter-c text-center"><i class="fa fa-spin fa-circle-o-notch fa-fw fa-2x"></i></div></div>';