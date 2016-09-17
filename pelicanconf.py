#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Tobias Macey'
SITENAME = 'Podcast.__init__'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Renaissance Dev', 'http://blog.renaissancedev.com'),
         ('Blind, Not Dumb', 'http://www.feoh.org'),
         ('iTunes', 'https://itunes.apple.com/us/podcast/podcast.-init/id981834425'),
         ('Stitcher', 'http://www.stitcher.com/s?fid=64838&refid=stpr'))

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/Podcast__init__'),
          ('Email', 'hosts@podcastinit.com'))

DEFAULT_PAGINATION = 10
DEFAULT_CATEGORY = 'Episodes'

THEME = 'pelican-themes/plumage'
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['share_post']
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
STATIC_PATHS = ['extra', 'images']
EXTRA_PATH_METADATA = {'extra/favicon.ico': {'path': 'favicon.ico'}}

TWITTER_USERNAME = 'Podcast__init__'

SITE_THUMBNAIL = '/images/podcast_init_logo.png'
SITESUBTITLE = 'A podcast about Python and the people who make it great'
RIGHT_SIDEBAR = """
<div class="well">
<!-- Begin MailChimp Signup Form -->
<link href="//cdn-images.mailchimp.com/embedcode/classic-081711.css" rel="stylesheet" type="text/css">
<style type="text/css">
        #mc_embed_signup{clear:left; font:14px Helvetica,Arial,sans-serif; }
        /* Add your own MailChimp form style overrides in your site stylesheet or in this style block.
           We recommend moving this block and the preceding CSS link to the HEAD of your HTML file. */
</style>
<div id="mc_embed_signup">
<form action="//podcastinit.us11.list-manage.com/subscribe/post?u=67a43ab3c498ae52ee22503c0&amp;id=6cd31bc877" method="post" id="mc-embedded-subscribe-form" name="mc-embedded-subscribe-form" class="validate" target="_blank" novalidate>
    <div id="mc_embed_signup_scroll">
        <h4>Keep Up To Date With Podcast.__init__</h4>
<div class="mc-field-group">
        <label for="mce-EMAIL">Email Address  <span class="asterisk">*</span>
</label>
        <input type="email" value="" name="EMAIL" class="required email" id="mce-EMAIL">
</div>
<div class="mc-field-group">
        <label for="mce-FNAME">First Name </label>
        <input type="text" value="" name="FNAME" class="" id="mce-FNAME">
</div>
<div class="mc-field-group">
        <label for="mce-LNAME">Last Name </label>
        <input type="text" value="" name="LNAME" class="" id="mce-LNAME">
</div>
<p>Powered by <a href="http://eepurl.com/bsQ43H" title="MailChimp - email marketing made easy and fun">MailChimp</a></p>
        <div id="mce-responses" class="clear">
                <div class="response" id="mce-error-response" style="display:none"></div>
                <div class="response" id="mce-success-response" style="display:none"></div>
        </div>    <!-- real people should not fill this in and expect good things - do not remove this or risk form bot signups-->
    <div style="position: absolute; left: -5000px;"><input type="text" name="b_67a43ab3c498ae52ee22503c0_6cd31bc877" tabindex="-1" value=""></div>
    <div class="clear"><input type="submit" value="Subscribe" name="subscribe" id="mc-embedded-subscribe" class="button"></div>
    </div>
</form>
</div>
<script type='text/javascript' src='//s3.amazonaws.com/downloads.mailchimp.com/js/mc-validate.js'></script><script type='text/javascript'>(function($) {window.fnames = new Array(); window.ftypes = new Array();fnames[0]='EMAIL';ftypes[0]='email';fnames[1]='FNAME';ftypes[1]='text';fnames[2]='LNAME';ftypes[2]='text';}(jQuery));var $mcj = jQuery.noConflict(true);</script>
<!--End mc_embed_signup-->
</div>
<div class="well">
<h4>Don't Miss an Episode!</h4>
<br/>
<a href="https://itunes.apple.com/us/podcast/podcast.-init/id981834425?mt=2&uo=6&at=&ct=" target="itunes_store" style="display:inline-block;overflow:hidden;background:url(http://linkmaker.itunes.apple.com/images/badges/en-us/badge_itunes-lrg.png) no-repeat;width:165px;height:40px;@media only screen{background-image:url(http://linkmaker.itunes.apple.com/images/badges/en-us/badge_itunes-lrg.svg);}"></a>
<hr/>
<a href="https://goo.gl/app/playmusic?ibi=com.google.PlayMusic&isi=691797987&ius=googleplaymusic&link=https://play.google.com/music/m/I7ogju4xv6adasgqz6545jndgsy?t%3DPodcast.__init___-_Python_and_the_people_who_make_it_great">
<img src="/images/Google_Play_Music_icon.png"/>
</a>
<hr/>
<a href="http://www.stitcher.com/s?fid=64838&refid=stpr"><img src="http://cloudfront.assets.stitcher.com/promo.assets/stitcher-banner-120x90.jpg" width="120" height="90" alt="Listen to Stitcher"></a>
<hr/>
<iframe src="http://tunein.com/embed/follow/p726240/" style="width:64px;height:22px;" scrolling="no" frameborder="no"></iframe>
<hr/>
<p style="margin-top: 8px;"><a href="http://podcastinit.podbean.com/feed/"><img src="/images/feed-icon.png"/></a></p>
</div>
<div class="well">
<h4>Support The Show!</h4>
<hr>
<strong>Donate</strong><br/><br/>
<script data-gratipay-username="Podcast__init__" src="//grtp.co/v1.js"></script>&nbsp&nbsp
<script id='fbsufec'>(function(i){var f,s=document.getElementById(i);f=document.createElement('iframe');f.src='//api.flattr.com/button/view/?uid=podcastinit&url='+encodeURIComponent(document.URL);f.title='Flattr';f.height=62;f.width=55;f.style.borderWidth=0;s.parentNode.insertBefore(f,s);})('fbsufec');</script>
<a href="https://www.patreon.com/podcastinit"><img src="/images/patreon_logo.png" style="vertical-align: inherit; padding: 5px;"/></a>
<form style="display: inline;" action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_top">
<input type="hidden" name="cmd" value="_s-xclick">
<input type="hidden" name="hosted_button_id" value="SFNZEMMKT87PQ">
<input type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif" border="0" name="submit" style="vertical-align: inherit; padding: 22px 5px;" alt="PayPal - The safer, easier way to pay online!">
<img alt="" border="0" src="https://www.paypalobjects.com/en_US/i/scr/pixel.gif" width="1" height="1">
</form>
<br/>
<script src="http://coinwidget.com/widget/coin.js"></script>
<script>
CoinWidgetCom.go({
        wallet_address: "1ML2YBGM1eBcPynEgZERKTzz6R43Lkrjke"
        , currency: "bitcoin"
        , counter: "count"
        , alignment: "bl"
        , qrcode: true
        , auto_show: false
        , lbl_button: "Support the Show"
        , lbl_address: "My Bitcoin Address:"
        , lbl_count: "donations"
        , lbl_amount: "BTC"
});
</script>
<hr>
<strong>Use Our Referral Links</strong><br/><br/>
<div><a href="http://www.kqzyfj.com/fn101r09608OWXUPWYUOQRUQUXWUOQTVPPURVVVPPP" target="_top" onmouseover="window.status='http://www.thriftbooks.com';return true;" onmouseout="window.status=' ';return true;">
<img src="http://www.lduhtrp.net/6f102fz2rxvGOPMHOQMGIJMIMPOMGILNHHMJNNNHHH" alt="" border="0" /></a></div><br/><br/>
<div class="alignleft">
<script type='text/javascript'>
 amzn_assoc_ad_type = 'banner';
 amzn_assoc_tracking_id = 'podcastinit-20';
 amzn_assoc_marketplace = 'amazon';
 amzn_assoc_region = 'US';
 amzn_assoc_placement = 'assoc_banner_placement_default';
 amzn_assoc_linkid = 'FJDEJT2D3JSEKLFR';
 amzn_assoc_campaigns = 'home';
 amzn_assoc_p = '40';
 amzn_assoc_banner_type = 'category';
 amzn_assoc_isresponsive = 'false';
 amzn_assoc_banner_id = '1X2AGSSAVB75EDSQR302';
 amzn_assoc_width = '120';
 amzn_assoc_height = '60';
</script>
<script src='//z-na.amazon-adsystem.com/widgets/q?ServiceVersion=20070822&Operation=GetScript&ID=OneJS&WS=1'></script>
</div><br/>
<p><a href="https://www.linode.com/?r=d6891b90c94beb4a3ff335003610e71cd62ee9c4"><img src="https://www.linode.com/media/images/logos/standard/light/linode-logo_standard_light_small.png"/></a></p><br/>
<a href="http://www.oreilly.com/pub/cpc/258"><img src="http://www.oreilly.com/partner_file/ORM_logo_box75_hex.jpg" /></a><br/>
<hr>
<strong>Get Some Help!</strong><br/>
<ul>
<li><a href="https://hackhands.com/renaissancedev/">Schedule a 1-to-1 Pairing Session</a></li>
<li><a href="http://www.boundlessnotions.com?ref=podcastinit">Get Help On A Project</a></li>
</ul>
</div>
"""
