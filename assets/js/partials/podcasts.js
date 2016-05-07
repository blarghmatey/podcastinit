
var Podcasts = {

  current_epsiode: 0,
  context: {items: []},
  current_page: 0,
  total_pages: 0,
  move_distance: 660,

  fetch: function() {
    var _this = this;
    this.context.items = podcast_episodes;
    this.setup();
    // $.getJSON("", function(json) {
    //   _this.context.items = json.episodes;
    //   _this.setup();
    // });
  },

  findEpsiodeById: function(id) {
    var i;
    var len = (this.context.items.length-1);
    for(i = 0; i <= len; i++) {
      if ( this.context.items[i].episode_id == id ) {
        return this.context.items[i];
      }
    }
    return false;
  },

  // Paging
  setArrows: function() {
    var pages;
    pages = Math.ceil(this.context.items.length / this.move_distance);
    if (this.current_page === 0) {
      $('.podcasts_arrow--prev').addClass('podcasts_arrow--inactive');
      $('.podcasts_arrow--next').removeClass('podcasts_arrow--inactive');
    } else if (this.current_page >= this.total_pages) {
      $('.podcasts_arrow--prev').removeClass('podcasts_arrow--inactive');
      $('.podcasts_arrow--next').addClass('podcasts_arrow--inactive');
    } else {
      $('.podcasts_arrow--prev').removeClass('podcasts_arrow--inactive');
      $('.podcasts_arrow--next').removeClass('podcasts_arrow--inactive');
    }
  },

  moveIt: function() {
    var dis = (this.current_page * this.move_distance);

    if ( (dis + window.innerWidth) > $('.podcasts__slider').width() ) {
      dis = ( $('.podcasts__slider').width() - window.innerWidth) + 82; // Arrows
      console.log('Adjust...', dis);
    }

    dis = -dis;

    console.log(dis)
    
    $('.podcasts__slider').css({
      '-webkit-transform': 'translateX('+dis+'px)',
      '-ms-transform': 'translateX('+dis+')',
      'transform': 'translateX('+dis+'px)'
    });

  },

  setupPaging: function() {
    var _this = this;
    $('.podcasts_arrow').on("click", function(e) {
      e.preventDefault();
      if ( $(this).hasClass('podcasts_arrow--inactive') ) return;
      if ( $(this).hasClass('podcasts_arrow--prev') ) {
        if (_this.current_page === 0) return;
        _this.current_page--;
      } else {
        if (_this.current_page >= _this.total_pages) return;
        _this.current_page++;
      }
      _this.moveIt();
      _this.setArrows();
    });
  },

  setupTemplate: function() {
    var source, template, html, wid;

    source   = $("#entry-template").html();
    template = Handlebars.compile(source);
    html    = template(this.context);
    $('.podcasts__slider').html(html);
    wid = (this.context.items.length * ($('.podcasts__row').width()+22));
    $('.podcasts__slider').css({'width': wid}).show();
    this.move_distance = (($('.podcasts__row').width()+22) * 3);
    this.total_pages = Math.ceil((wid-window.innerWidth) / this.move_distance);
  },

  setupPodcastClicks: function() {
    var _this = this;
    $('.podcasts__row a').on('click', function(e) {
      e.preventDefault();
      // _this.current_podcast = $(this).data('podcast_id');
      // _this.current_epsiode = $(this).data('episode_id');
      // var podcast = _this.findPodcastById(_this.current_podcast);
      // var episode = _this.findEpsiodeById(_this.current_epsiode);
      // window.open('/podcasts/?episode=' + episode.episode_id);
      // $('.podcasts').addClass('podcasts--activate');
      // $('.podcasts').addClass('podcasts--on');
      // $('.podcasts__player iframe').attr('src', 'http://www.podcastone.com/episodewidget?pid=' + episode.episode_id + '&logo=true&autoplay=true');
    });
  },

  toggleOffTextArea: function() {
    $('.podcasts__player__textarea h3').text('');
    $('.podcasts__player__textarea').removeClass('on');
    $('.podcasts__player__textarea__content').text('');
  },

  setup: function() {
    this.setupTemplate();
    //this.setupPodcastClicks();
    this.setupPaging();
    this.setArrows();
  },

  init: function() {
    Podcasts.fetch()
  }

};

$(Podcasts.init);
