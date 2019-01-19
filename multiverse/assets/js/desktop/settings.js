$(document).ready(function(){

	$(document).on('click', '.panel .panel-btn', function(){
		var open = parseInt($(this).attr('data-open'));
		if (open) $(this).attr('data-open', '0').html('<i class="fa fa-fw fa-plus"></i>').parent().siblings('.panel-body').slideUp();
		else $(this).attr('data-open', '1').html('<i class="fa fa-fw fa-minus"></i>').parent().siblings('.panel-body').slideDown();
	});

});