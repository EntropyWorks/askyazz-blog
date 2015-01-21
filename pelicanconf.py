#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Yazz Atlas'
SITENAME = u'AskYazz'
SITEURL = 'askyazz.com'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

#############
THEME = 'pelican-themes/pelican-cait'
DEFAULT_DATE_FORMAT = ('%a %d %B %Y')
ARTICLE_URL = "posts/{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%m}/{slug}/index.html"
CATEGORY_URL = "category/{slug}"
CATEGORY_SAVE_AS = "category/{slug}/index.html"
TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"

PYGMENTS_RST_OPTIONS = {'classprefix': 'pgcss', 'linenos': 'table'}
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'

PLUGIN_PATH = 'pelican-plugins'
PLUGINS = ['neighbors', 'summary']

RELATIVE_URLS = True
DISQUS_SITENAME = 'askyazz'

#CUSTOM_MENUITEMS = (('Blog', `blog`),
#                     ('Contact', 'contact'),
#                     ('Projects', 'pages/projects'))
#############


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
