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
SOCIAL = (('Twitter', 'https://twitter.com/Podcast__init__'),)

DEFAULT_PAGINATION = 10
DEFAULT_CATEGORY = 'Episodes'

THEME = 'pelican-themes/plumage'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
STATIC_PATHS = ['extra', 'images', 'pages']
EXTRA_PATH_METADATA = {'extra/favicon.ico': {'path': 'favicon.ico'}}

TWITTER_USERNAME = 'Podcast__init__'

SITE_THUMBNAIL = '/images/podcast_init_logo.png'
SITESUBTITLE = 'A podcast about Python and the people who make it great'
RIGHT_SIDEBAR = """
<a href="https://itunes.apple.com/us/podcast/podcast.-init/id981834425?mt=2&uo=6&at=&ct=" target="itunes_store" style="display:inline-block;overflow:hidden;background:url(http://linkmaker.itunes.apple.com/images/badges/en-us/badge_itunes-lrg.png) no-repeat;width:165px;height:40px;@media only screen{background-image:url(http://linkmaker.itunes.apple.com/images/badges/en-us/badge_itunes-lrg.svg);}"></a>
<a href="http://www.stitcher.com/s?fid=64838&refid=stpr"><img src="http://cloudfront.assets.stitcher.com/promo.assets/stitcher-banner-120x90.jpg" width="120" height="90" alt="Listen to Stitcher"></a>
"""
