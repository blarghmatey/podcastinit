#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Tobias Macey and Chris Patti'
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
          {'Email', 'hosts@podcastinit.com'})

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
<h4>Don't Miss an Episode!</h4>
<br/>
<a href="https://itunes.apple.com/us/podcast/podcast.-init/id981834425?mt=2&uo=6&at=&ct=" target="itunes_store" style="display:inline-block;overflow:hidden;background:url(http://linkmaker.itunes.apple.com/images/badges/en-us/badge_itunes-lrg.png) no-repeat;width:165px;height:40px;@media only screen{background-image:url(http://linkmaker.itunes.apple.com/images/badges/en-us/badge_itunes-lrg.svg);}"></a>
<hr/>
<a href="http://www.stitcher.com/s?fid=64838&refid=stpr"><img src="http://cloudfront.assets.stitcher.com/promo.assets/stitcher-banner-120x90.jpg" width="120" height="90" alt="Listen to Stitcher"></a>
<hr/>
<iframe src="http://tunein.com/embed/follow/p726240/" style="width:64px;height:22px;" scrolling="no" frameborder="no"></iframe>
<hr/>
<p style="margin-top: 8px;"><a href="http://podcastinit.podbean.com/feed/"><img src="/images/feed-icon.png"/> Episodes</a></p>
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
<input type="hidden" name="encrypted" value="-----BEGIN PKCS7-----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-----END PKCS7-----
">
<input type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif" border="0" name="submit" style="vertical-align: inherit; padding: 22px 5px;" alt="PayPal - The safer, easier way to pay online!">
<img alt="" border="0" src="https://www.paypalobjects.com/en_US/i/scr/pixel.gif" width="1" height="1">
</form>
<hr>
<strong>Use Our Referral Links</strong><br/>
<ul>
<li><a href="http://www.amazon.com/?tag=podcastinit-20">Amazon.com</a></li>
<li><a href="https://www.digitalocean.com/?refcode=7f4b4767f85b">Digital Ocean</a></li>
<li><a href="http://www.kqzyfj.com/c9102ox52x4KSTPMNOQKMMNPRNLPKMPOOQNMLOQLLL">O'Reilly Media</a></li>
</ul>
<hr>
<strong>Get Some Help!</strong><br/>
<ul>
<li><a href="https://hackhands.com/renaissancedev/">Schedule a 1-to-1 Pairing Session</a></li>
<li><a href="http://www.boundlessnotions.com?ref=podcastinit">Get Help On A Project</a></li>
</ul>
</div>
"""
