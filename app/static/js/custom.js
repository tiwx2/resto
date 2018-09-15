card_template_text = `\n \
      <div class="card mb-4 shadow-sm"> \
        <img class="card-img-top" alt="Thumbnail [100%x225]" src="" data-holder-rendered="true"> \
        <div class="card-body"> \
        <p class="card-title">_title</p>\
          <p class="card-text">_description</p> \
          <div class="d-flex justify-content-between align-items-center"> \
            <div class="btn-group"> \
              _button
            </div> \
            <small class="text-muted">_distance miles</small> \
          </div> \
        </div> \
      </div> \n`

function render_card(d, type){
	var like_button = '<button type="button" id="like-' + d.id + '" data-link="' + d.links.like + '" class="btn btn-sm btn-outline-secondary like-btn action-btn">Like</button>'
    var dislike_button = '<button type="button" id="dislike-' + d.id + '" data-link="' + d.links.dislike + '" class="btn btn-sm btn-outline-secondary dislike-btn action-btn">Dislike</button>'
	var mapObj = {
		_title: d.name,
		_description: d.description,
		_distance: d.distance
	}

	if (type === 'like'){
		mapObj._button = like_button;
	} else {
		mapObj._button = dislike_button;
	}

	card_template = $('<div class="col-md-4" \>').html(card_template_text.replace(/\_(title|description|distance|button)/gi, function(matched){
		return mapObj[matched]
	}));
	return card_template.clone();
}

function append_restaurants(d, type){
	$('#restaurants').append(render_card(d, type));
};

function get_liked_restaurants(user_id){
	$.ajax({
		url: "/api/liked/" + user_id,
		type: 'GET',
		success: function(data) {
			console.log(data);
			var arrayLength = data['liked_restaurants'].length
			for (var i = 0; i < arrayLength; i++){
					append_restaurants(data['liked_restaurants'][i], 'dislike');
			};
			set_click_event();
		},
		error: function(e) {
			console.log(e);
		}
	});
};

function get_notliked_restaurants(user_id){
	$.ajax({
		url: "/api/notliked/" + user_id,
		type: 'GET',
		success: function(data) {
			console.log(data);
			var arrayLength = data['not_liked_restaurants'].length
			for (var i = 0; i < arrayLength; i++){
					append_restaurants(data['not_liked_restaurants'][i], 'like');
			};
			set_click_event();
		},
		error: function(e) {
			console.log(e);
		}
	});
};

function set_click_event(){
  $('.action-btn').click(function (){
    $.ajax({
    url: $(this).data('link'),
    type: 'POST',
      success: function(data) {
        console.log(data["message"]);
        update_page();
      },
      error: function(e) {
        console.log(e);
      }
    });
  });
};