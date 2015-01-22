#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Yazz Atlas'
SITENAME = u'Ask Yazz'
SITEURL = 'askyazz.com'
ALT_NAME = "#! " + SITENAME
SITESUBTITLE = "WTF is he working on now..."
DESCRIPTION = "A blog about what I have been working on."

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True

PATH = 'content'
#FILES_TO_COPY = (( 'extras/CNAME', 'CNAME' ),)

STATIC_PATHS = [
    'extras/CNAME',
        ]

EXTRA_PATH_METADATA = {
    'extras/CNAME': { 'path': 'CNAME'},
        }


TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = u'en'

#############
#THEME = 'pelican-themes/pelican-cait'
THEME = 'pelican-themes/pelican-mg'

#DEFAULT_DATE = fs
DEFAULT_DATE_FORMAT = ('%a %d %B %Y')
ARTICLE_URL = "posts/{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%m}/{slug}/index.html"
CATEGORY_URL = "category/{slug}"
CATEGORY_SAVE_AS = "category/{slug}/index.html"
TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"

PYGMENTS_RST_OPTIONS = {'classprefix': 'pgcss', 'linenos': 'table'}
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['neighbors', 'summary', 'tipue_search', 'sitemap']

RELATIVE_URLS = False
DISQUS_SITENAME = 'askyazz'
DEFAULT_PAGINATION = 10
SHARE = True

TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
DIRECT_TEMPLATES = ('index', 'categories', 'archives', 'search', 'tipue_search')
TIPUE_SEARCH_SAVE_AS = 'tipue_search.json'

SITEMAP = { 'format': 'xml'}
DELETE_OUTPUT_DIRECTORY = True
TWITTER_USERNAME = 'entropyworks'

#CUSTOM_MENUITEMS = (
#                    ('Contact', 'contact'),
#                    )
#############


# Feed generation is usually not desired when developing
#FEED = 'feeds/all.atom.xml'
FEED_ALL_ATOM = 'feeds/all.atom.xml'
#CATEGORY_FEED_ATOM = None
#TRANSLATION_FEED_ATOM = None
#AUTHOR_FEED_ATOM = None
#AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/entropyworks'),
          ('google-plus-square', 'https://plus.google.com/u/0/b/105194639805607840059/105194639805607840059/posts'),
          ('github', 'https://github.com/entropyworks'),
          ('envelope', 'mailto:entropywork@gmail.com'),)


FOOTER = ("&copy; 2015 Yazz D. Atlas. All rights reserved.<br>" +
           "Code snippets in the pages are released under " +
            "<a href=\"http://opensource.org/licenses/MIT\" target=\"_blank\">" +
            "The MIT License</a>, unless otherwise specified.")

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
