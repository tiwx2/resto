function get_liked_restaurants(user_id){
	card_template_text = `\n \
          <div class="card mb-4 shadow-sm"> \
            <img class="card-img-top" alt="Thumbnail [100%x225]" src="" data-holder-rendered="true"> \
            <div class="card-body"> \
            <p class="card-title">_title</p>\
              <p class="card-text">_description</p> \
              <div class="d-flex justify-content-between align-items-center"> \
                <div class="btn-group"> \
                  <button type="button" class="btn btn-sm btn-outline-secondary like-btn">Like</button> \
                  <button type="button" class="btn btn-sm btn-outline-secondary dislike-btn">Dislike</button> \
                </div> \
                <small class="text-muted">_distance miles</small> \
              </div> \
            </div> \
          </div> \n`

	function render_card(d){
		var mapObj = {
			_title: d.name,
			_description: d.description,
			_distance: d.distance
		}
		card_template = $('<div class="col-md-4" \>').html(card_template_text.replace(/\_(title|description|distance)/gi, function(matched){
			return mapObj[matched]
		}));
		return card_template.clone();
	}

	function append_restaurants(d){
		$('#restaurants').append(render_card(d));
		console.log('d');
	};

	$.ajax({
		url: "/api/liked/" + user_id,
		type: 'GET',
		success: function(data) {
			console.log(data);
			var arrayLength = data['liked_restaurants'].length
			for (var i = 0; i < arrayLength; i++){
					append_restaurants(data['liked_restaurants'][i]);
			};
		},
		error: function(e) {
			console.log(e);
		}
	});
};

