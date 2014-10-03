#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Rishi Baijal'
SITENAME = u'Nilmtk Blog'
#SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Facebook', 'https://www.facebook.com/rishi.baijal?fref=ts'),)

DEFAULT_PAGINATION = 10

PLUGIN_PATH='/Users/rishi/Documents/Master_folder/pelican-plugins'
PLUGINS=['assets', 'liquid_tags']
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
