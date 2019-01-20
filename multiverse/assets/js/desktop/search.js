$(document).ready(function(){

	var q = new Bloodhound({
		datumTokenizer: Bloodhound.tokenizers.obj.whitespace('title'),
		queryTokenizer: Bloodhound.tokenizers.whitespace,
		remote: {url:'/ajax/query?title=%QUERY',wildcard:'%QUERY'}
	});

	q.initialize();

	$('#search-bar').typeahead({
		hint:true,
		highlight:true,
		minLength:1
	}, {
		name:'title',
		displayKey:'title',
		source:q.ttAdapter()
	});

	$('.learn-more').click(function(){
		var link = $(this).attr('data-link');
		var partner = $(this).attr('data-partner');
		var title = $(this).attr('data-title');
		$('#learnMoreModal .modal-title').text(title + " [" + partner.toTitleCase() + "]");
		$.post('/scraper/query', {
			csrf_token:$('meta[name=csrf_token]').attr('content'),
			url:link,
			agent:partner
		}, function(ajax){
			console.log(ajax);
			if (typeof ajax.about != 'undefined')
				$('#learnMoreModal .modal-body').html("<p>" + ajax.about + "</p>");
			if (typeof ajax.additional != 'undefined')
				$('#learnMoreModal .modal-body').append("<p>In Association with " + ajax.additional.partner + "</p>");
			if (typeof ajax.content != 'undefined'){
				$.each(ajax.content, function(i, key){
					if (typeof key.heading != 'undefined')
						$('#learnMoreModal .modal-body').append('<b>' + key.heading + '</b>');
					if (typeof key.description != 'undefined')
						$('#learnMoreModal .modal-body').append('<p>' + key.description + '</p>');
				});
			}
			if (typeof ajax.instructors != 'undefined'){
				if (ajax.instructors.length > 0){
					$.each(ajax.instructors, function(i, key){
						if (typeof key.heading != 'undefined')
							$('#learnMoreModal .modal-body').append('<img src="' + key.source + '" class="img img-thumbnail" alt="" /> Taught by <b>' + key.name + '</b>, ' + key.position);
					});
				}
			}
		}).fail(function(e){
			$('#learnMoreModal').modal('hide');
		});
		$('#learnMoreModal .modal-body').html(smallSpinningTemplate);
		$('#learnMoreModal').modal('show');
	});

});
