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
FEED_ALL_ATOM = 'rss.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = ()
# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 0

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
    'extra/CNAME': {'path': 'CNAME'},
    'extra/robots.txt': {'path': 'robots.txt'},
}
STATIC_PATHS = [
    'extra/robots.txt',
    'extra/CNAME',
    'img',
]

CONTRIBUTIONS = {
    "Containers": [
        {"name": "cilium", "desc": "Linux-native network security", "url": "https://github.com/cilium/cilium"}],
    "DevOps": [
        {"name": "Hashicorp/Terraform", "desc": "Infraestructure as code", "url": "https://github.com/hashicorp/terraform"},
        {"name": "Hashicorp/Packer", "desc": "Build Automated Machine Images", "url": "https://www.packer.io/"},
        {"name": "Vmware/Govmomi", "desc": "Go Bindings for Vsphere", "url": "https://github.com/vmware/govmomi"},
        ],
    "VoIP": [
        {"name": "Kamailio", "desc": "Core Contributor", "url": "https://www.kamailio.org/w/"},
        {"name": "CGrates", "desc": "Golang Real time billing", "url": "https://github.com/cgrates/cgrates"}],
    "Misc": [
        {"name": "Firefox/servo", "desc": "Web browser Engine", "url": "https://servo.org/"},
        {"name": "Firefox/euclid", "desc": "Rust library for Geometry types", "url": "https://github.com/servo/euclid/"},
        {"name": "Radix", "desc": "Golang Redis client", "url": "https://github.com/mediocregopher/radix.v2"},
        {"name": "Grafana", "desc": "Analytics and monitoring", "url": "https://github.com/grafana/grafana-docker-dev-env/pull/1"}
        ],
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
