#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Eloy Coto'
SITENAME = u'A calustra'
SITEURL = 'http://www.acalustra.com'
DEFAULT_DATE_FORMAT = ('%A %d-%m-%Y')


PATH = 'content'

TIMEZONE = 'Europe/Madrid'

DEFAULT_LANG = u'es'
DISQUS_SITENAME = 'acalustra'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = ()
# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 5

PLUGIN_PATHS = ["pelican-plugins/"]
PLUGINS = ['sitemap','related_posts']
THEME = 'theme/blog/'
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
RELATED_POSTS_MAX = 5
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/CNAME': {'path': 'CNAME'},
}
STATIC_PATHS = [
    'extra/robots.txt',
    'img',
]
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
