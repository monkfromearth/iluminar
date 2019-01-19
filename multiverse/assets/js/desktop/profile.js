$(document).ready(function(){

	$(document).on('click', '#profile-navbar li', function(e){
		$.each($('#profile-navbar li'), function(i, li){
			$(li).removeClass('active');
		})
		$(this).addClass('active');
	});

});