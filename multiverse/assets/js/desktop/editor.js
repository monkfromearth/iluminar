$(document).ready(function(){

	var songPlaceholderImage = '/assets/images/song.128.png';
	var videoPlaceholderImage = '/assets/images/video.128.png';

	var mediaAccepts = {
		'audio':'audio/*',
		'image':'image/*',
		'video':'video/mp4',
	};

	var fetchedFonts = [], initialPostType = 'text';

	var placeholderImage = function(image, file, mime){
		var name = (typeof file != 'undefined') ? (typeof file.files[0] != 'undefined') ? file.files[0].name : mime.toTitleCase() : mime.toTitleCase();
		return '<span class="image-overlay"><img src="' + image + '" class="img img-thumbnail" data-toggle="tooltip" title="' + name + '" data-placement="bottom"><span class="image-describe">' + mime.toUpperCase() + '</span><span class="image-close"><i class="fa fa-fw fa-times"></i></span></span>';
	}

	$(document).on('click', '.editor .mediaUploadButton', function(){
		var mime = $(this).attr('data-kind');
		$(this).tooltip('destroy');
		$('#editorPostMediaType').val(mime);
		$('#editorPostMediaBody').attr('accept', mediaAccepts[mime]);
		$('#editorPostMediaBody').click();
	});

	$(document).on('change', '.editor #editorPostMediaBody:not(.in-canvas)', function(){
		var $this = this, mime = $('#editorPostMediaType').val();
		if ($this.files && typeof $this.files[0] != 'undefined' && $this.files[0].type.split('/')[0] == mime){
			initialPostType = $('#editorPostType').val();	
			$('#editorPostType').val('media');
			if (mime == 'image'){
				Repo.readImage($this, function(image){
					$('.editor #editorPictureGallery').html(placeholderImage(image, $this, 'picture'));
				});
			}
			else if (mime == 'audio')
				$('.editor #editorPictureGallery').html(placeholderImage(songPlaceholderImage, $this, 'song'));
			else if (mime == 'video'){
				$('.editor #editorPictureGallery').html('<span class="image-overlay"><video src="' + URL.createObjectURL($this.files[0]) + '" title="' + $this.files[0].name + '" data-placement="bottom" class="img img-thumbnail" data-toggle="tooltip"></video><span class="image-describe">VIDEO</span><span class="image-close"><i class="fa fa-fw fa-times"></i></span></span>');
			}
			$('.editor #editorPictureGallery').removeClass('hidden');
		} else {
			alert(Codes.Request.INVALID_FILETYPE);
			$('#editorPostType').val(initialPostType);
		}
	});

	$(document).on('click', '.editor .image-close', function(e){
		$(this).parent().remove();
		$('#editorPostType').val(initialPostType);
		$('#editorPostMediaType').val('');
		$('#editorPostMediaBody').val('');
		$('#editorPostMediaBody')[0].files = null;
		$('.editor #editorPictureGallery').addClass('hidden');
	});

	/* Canvas Editor Starts */

	$(document).on('click', '#editorCanvasButton', function(e){
		e.preventDefault();
		$(this).tooltip("destroy");
		initialPostType = $('#editorPostType').val();	
		$('#editorPostType').val('canvas');
		$('#canvasEditor').modal();
	});

	$(document).on('click', '#canvasEditor #canvasEditorCreate', function(){
		if ($('#canvasEditorQuote').val().replace(/\s/g, "").length == 0){
			alert("Please write some text on the canvas.");
			return false;
		}
		if ($('#canvasEditorFontColor').val() == $('#canvasEditorBackgroundColor').val()){
			alert("The font color and the background color are same. The text might not be visible.");
			return false;
		}
		$('#editorPostType').val('canvas');
		$('#canvasEditor').modal('hide');
		$('.editor #editorPictureGallery').html(placeholderImage('assets/images/picture.128.png', undefined, 'canvas'));
		$('.editor #editorPictureGallery').removeClass('hidden');
	});

	$(document).on('click', '#canvasEditor #canvasEditorClose', function(){
		$('#canvasEditor').modal('hide');
		$('.canvas-container').css('background-image', '');
		$('#editorPostMediaBody').removeClass('in-canvas');
		$('#editorPostType').val(initialPostType);
		$('.canvas-container').css('background-image', ''); 
	});

	$(document).on('keyup', '#canvasEditor #canvasEditorQuote', function(){
		var quotes = $(this).val();
		$('#editorCanvasText').val(quotes);
		quotes = quotes.split(' ').join('&nbsp;').split('\n');
		$('.canvas-text').html('');
		$.each(quotes, function(i, quote){
			$('.canvas-text').append('<p class="canvas-break-words">' + quote + '</p>');
		});
	});

	$(document).on('click', '#canvasEditor .canvasEditorTextAlignButton', function(){
		var alignClass = $(this).attr('data-class');
		$(this).parent().children().removeClass('active');
		$(this).addClass('active');
		var alignClassSplit = alignClass.split('-');
		$('#editorCanvasTextAlignment').val(alignClassSplit[alignClassSplit.length - 1]);
		$('.canvas-text').removeClass('canvas-text-align-left canvas-text-align-center canvas-text-align-right').addClass(alignClass);
	});

	$(document).on('click', '#canvasEditor .canvasEditorTextPositionButton', function(){
		var positionClass = $(this).attr('data-class');
		$(this).parent().children().removeClass('active');
		$(this).addClass('active');
		var positionClassSplit = positionClass.split('-');
		$('#editorCanvasTextPosition').val(positionClassSplit[positionClassSplit.length - 1]);
		$('.canvas-text').removeClass('canvas-text-position-top canvas-text-position-middle canvas-text-position-bottom').addClass(positionClass);
	});

	$(document).on('click', '#canvasEditor .canvasEditorFontSizeButton', function(){
		var sizeClass = $(this).attr('data-class');
		$(this).parent().children().removeClass('active');
		$(this).addClass('active');
		var sizeClassSplit = sizeClass.split('-');
		$('#editorCanvasFontSize').val(sizeClassSplit[sizeClassSplit.length - 1]);
		$('.canvas-text').removeClass('canvas-heading1 canvas-heading2 canvas-heading3 canvas-heading4 canvas-heading5 canvas-heading6 canvas-heading7 canvas-heading8 canvas-heading9 canvas-heading10 canvas-heading11 canvas-heading12 canvas-heading13 canvas-heading14 canvas-heading15').addClass(sizeClass);
	});

	$(document).on('change', '#canvasEditor #canvasEditorFontColor', function(){
		var color = $(this).val();
		var bgcolor = $('#canvasEditorBackgroundColor').val();
		if (color == bgcolor) $('#editorCanvasColorAlert').removeClass('hidden');
		else $('#editorCanvasColorAlert').addClass('hidden');
		$('#editorCanvasFontColor').val(color);
		$('.canvas-text').css('color', color);
	});

	$(document).on('change', '#canvasEditor #canvasEditorBackgroundColor', function(){
		var bgcolor = $(this).val();
		var color = $('#canvasEditorFontColor').val();
		if (color == bgcolor) $('#editorCanvasColorAlert').removeClass('hidden');
		else $('#editorCanvasColorAlert').addClass('hidden');
		$('#editorCanvasBackgroundColor').val(bgcolor);
		$('.canvas-container').css('background-color', bgcolor);
	});

	$(document).on('click', '#canvasEditor .canvasEditorImagePositionButton', function(){
		var positionClass = $(this).attr('data-class');
		$(this).parent().children().removeClass('active');
		$(this).addClass('active');
		var positionClassSplit = positionClass.split('-');
		$('#editorCanvasImagePosition').val(positionClassSplit[positionClassSplit.length - 1]);
		$('.canvas-container').removeClass('canvas-image-position-top canvas-image-position-center canvas-image-position-bottom').addClass(positionClass);
	});

	$(document).on('click', '#canvasEditor .canvasEditorImageAlignButton', function(){
		var alignClass = $(this).attr('data-class');
		$(this).parent().children().removeClass('active');
		$(this).addClass('active');
		var alignClassSplit = alignClass.split('-');
		$('#editorCanvasImageAlignment').val(alignClassSplit[alignClassSplit.length - 1]);
		$('.canvas-container').removeClass('canvas-image-align-left canvas-image-align-center canvas-image-align-right').addClass(alignClass);
	});

	$(document).on('click', '#canvasEditor #canvasEditorPictureUpload', function(){
		$(this).addClass('btn-sm');
		$('#editorPostMediaType').val('image');
		$('#editorPostMediaBody').attr('accept', mediaAccepts['image']);
		$('#editorPostMediaBody').click();
		$('#editorPostMediaBody').addClass('in-canvas');
	});

	$(document).on('change', '.editor #editorPostMediaBody.in-canvas', function(){
		var $this = this, mime = $('#editorPostMediaType').val();
		if ($this.files && typeof $this.files[0] != 'undefined' && $this.files[0].type.split('/')[0] == mime){
			$('#editorPostType').val('media');
			Repo.readImage($this, function(image){
				window.canvasImageURL = image;
				$('.canvas-container').css('background-image', 'url(' + image + ')');
				$('.editor #editorPictureGallery').html(placeholderImage(image, $this, 'canvas'));
			});
			$('#editorCanvasPictureTab .form-group').removeClass('hidden');
			$('.editor #editorPictureGallery').removeClass('hidden');
		} else {
			alert(Codes.Request.INVALID_FILETYPE);
			$('#editorPostType').val(initialPostType);
		}
	});

	$(document).on('click', '#canvasEditor .canvasEditorImageFilterButton', function(){
		var filter = $(this).attr('data-filter');
		$(this).parent().children().removeClass('active');
		$(this).addClass('active');
		$('#editorCanvasImageFilter').val($(this).attr('data-original-title').toLowerCase());
		$('.canvas-container').css('background-image', 'linear-gradient(' + filter +', ' + filter + '), url(' + window.canvasImageURL + ')');
	});

	$(document).on('change', '#canvasEditor #canvasEditorFontFamilySelect', function(){
		var font = $('#canvasEditorFontFamilySelect option:selected').val();
		if ($.inArray(font, fetchedFonts) == -1){
			fetchedFonts.push(font);
			$('head').append('<link href="' + 'https://fonts.googleapis.com/css?family=' + font.replace(/\s/, '+') + '" rel="stylesheet" />');
		}
		$(".canvas-text").css("font-family", "'" + font + "', serif");
		$("#editorCanvasFontFamily").val(font);
	});

	/* Canvas Editor Ends */

	$(document).on('click', '.editor #editorPostButton', function(e){
		e.preventDefault();
		
		// Getting Data
		var meta = {};
		$.each([ 'PostContent', 'PostType', 'PostMediaType', 'PostMediaBody', 'CanvasText', 'CanvasTextAlignment', 'CanvasTextPosition', 'CanvasImageAlignment', 'CanvasImagePosition', 'CanvasFontFamily', 'CanvasFontSize', 'CanvasFontColor', 'CanvasBackgroundColor', 'CanvasImageFilter' ], function(i, tag){
				var $this = $('#editor' + tag);
				meta[$this.attr('name')] = $this.val();
		});
		$.each([ 'PostAudience', 'PostCategory', ], function(i, tag){
				meta[$('#editor' + tag).attr('name')] = $('#editor' + tag + ' > option:selected').val();
		});
		console.log(meta);
		
		// Error Checking Mandatory Data
		if (meta['post:audience'].replace(/\s/g, "").length == 0){
			$('#editorAlerts').removeClass('hidden');
			Repo.notify($('#editorAlerts'), "Please select <b>Audience</b> for the post.");
			return false;
		}
		if (meta['post:category'].replace(/\s/g, "").length == 0){
			$('#editorAlerts').removeClass('hidden');
			Repo.notify($('#editorAlerts'), "Please select <b>Category</b> for the post.");
			return false;
		}
		if (meta['post:type'].replace(/\s/g, "").length == 0){
			$('#editorAlerts').removeClass('hidden');
			Repo.notify($('#editorAlerts'), "Please select <b>Post Type</b> for the post.");
			return false;
		}
		if (meta['post:type'] == 'text'){
			if (meta['post:content'].replace(/\s/g, "").length == 0){
				$('#editorAlerts').removeClass('hidden');
				Repo.notify($('#editorAlerts'), "Please write something to post.");
				return false;
			}
		}
		if (meta['post:type'] == 'media'){
			if (meta['post:media:type'].replace(/\s/g, "").length == 0){
				$('#editorAlerts').removeClass('hidden');
				Repo.notify($('#editorAlerts'), "Please select <b>Media Type</b> to proceed.");
				return false;
			}
			if (meta['post:media:body'].replace(/\s/g, "").length == 0){
				$('#editorAlerts').removeClass('hidden');
				Repo.notify($('#editorAlerts'), "Please upload something to post.");
				return false;
			}
		}
		if (meta['post:type'] == 'canvas'){
			var canvasCheck = {
				'canvas:text':"text",
				'canvas:alignment':"text alignment",
				'canvas:position':"text position",
				'canvas:image:alignment':"image alignment",
				'canvas:image:position':"image position",
				'canvas:image:filter':"image filter",
				'canvas:background:color':"background color",
				'canvas:font:color':"font color",
				'canvas:font:size':"font size",
				'canvas:font:family':"font family"
			}
			$.each(Object.keys(canvasCheck), function(i, key){
				if (meta[key].replace(/\s/g, "").length == 0){
					$('#editorAlerts').removeClass('hidden');
					Repo.notify($('#editorAlerts'), "Please select <b>" + canvasCheck[key] + "</b> on the canvas.");
					return false;
				}
			});
		}
		$('#editorf').submit();
		$(this).addClass('disabled').attr('disabled', true);
	});

});