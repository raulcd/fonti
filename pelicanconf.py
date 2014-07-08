#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Raúl Cumplido'
SITENAME = u'Raúl Cumplido'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
FEED_DOMAIN = None
FEED_ATOM = None
FEED_RSS = None
TAG_FEED_ATOM = None
TAG_FEED_RSS = None

# Blogroll
"""LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)
"""

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/raulcumplido'),
          ('github', 'http://github.com/raulcd'),)


STATIC_PATHS = ['extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}


TWITTER_USERNAME='raulcd'

DISQUS_SITENAME = 'raulcd'

DEFAULT_PAGINATION = False
AUTHOR_SAVE_AS = False
AUTHORS_SAVE_AS = False
TAG_SAVE_AS = False
TAGS_SAVE_AS = False
CATEGORY_SAVE_AS = False
CATEGORIES_SAVE_AS = False
ARCHIVES_SAVE_AS = False
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
