$(document).ready(function(){

	$(document).on('show.bs.dropdown', '.post .dropdown', function () {
		var $this = $(this);
		var postId = '#' + $this.closest('.post').attr('id');
		$this.attr('data-post', postId);
		$('body').append($this.css({
			position:'absolute',
			left:$this.offset().left, 
			top:$this.offset().top
		}).detach());
	});

	$('.post .dropdown').on('hidden.bs.dropdown', function () {
		var $this = $(this);
		var postId = $this.attr('data-post');
		$(postId).find('.media-heading').append($this.css({
			position:'', left:'', top:''
		}).detach());
	});


	$(document).on('click', '.post .post-reactions', function(e){
		e.preventDefault();
	});

	var doReactionPopover = function($this, event){
	    if ($this.next('div.popover:visible').length){
	      if (event == 'show') return false;
	      else $this.popover('hide');
	    } else {
	      if (event == 'show') $this.popover('show');
	      else return false;
	    }
	};

    $('.post .post-reactions').popover({
		title:"",
		content:$('.post-reactions-content').html(), 
		html:true, 
		placement:"top",
		trigger:'manual'
    }).focus(function(){
		doReactionPopover($(this), 'show');
	}).blur(function(){
		doReactionPopover($(this), 'hide');
	}).hover(function(){
		if (!$(this).is(':focus')) $(this).focus();
	});

	$(document).on('click', '.post-reactions-icon', function(){
		NProgress.start();

		var reaction = $(this).attr('data-reaction');
		var name = $(this).attr('data-name').toLowerCase();
		var post = $(this).closest('.post').attr('id');

		var postId = '#' + post;
		
		var color = null, initHTML = null, initColor = null;

		var reactionColors = {
			'upvote':'#6699FF',
			'downvote':'#66CC99',
			'love':'#FF6666',
			'angry':'#FF9900',
			'haha':'#ffc815',
			'wow':'#ffc815',
			'sad':'#ffc815'
		}

		var $reactionBtn = $(postId).find('.post-reactions');

		initHTML = $reactionBtn.html();
		initColor = $reactionBtn.css('color');

		$reactionBtn.html('<img src="/assets/images/reactions/' + name + '.24.png" alt="' + name.toTitleCase() + '" class="img" /> ' + name.toTitleCase());
		$reactionBtn.css('color', reactionColors[name]);

		$.post(Routes.API.voteCreate, {
			reaction:reaction,
			post:post,
			csrf_token:csrf_token
		}, function(ajax){
			NProgress.done();
			if (!ajax.status){
				$reactionBtn.html(initHTML);
				$reactionBtn.css('color', initColor);
			}
		}).fail(function(e, s, t){
			NProgress.done();
			$reactionBtn.html(initHTML);
			$reactionBtn.css('color', initColor);
		});

	});

	$(document).on('click', '.post-comments', function(){
		$(this).closest('.post').find('.comment-form').fadeIn();
	});

});