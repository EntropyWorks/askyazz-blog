#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

DELETE_OUTPUT_DIRECTORY = False
OUTPUT_RETENTION = ( ".git" )

PATH = 'content'
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = u'en'
DEFAULT_DATE_FORMAT = ('%a %d %B %Y')

AUTHOR = u'Yazz D. Atlas'
SITENAME = u'Ask Yazz'

SITEURL = 'http://askyazz.com'
RELATIVE_URLS = False 

ALT_NAME = "#! " + SITENAME

THEME = 'pelican-themes/pelican-mg'

DISQUS_SITENAME = 'askyazz'
TWITTER_USERNAME = 'entropyworks'

SC_PROJECT = '10250176'
SC_SECURITY = 'ffa8fb39'

SITESUBTITLE = "WTF is he working on now..."
DESCRIPTION = "A blog about what I have been working on."

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/entropyworks'),
          ('google-plus-square', 'https://plus.google.com/u/0/b/105194639805607840059/105194639805607840059/posts'),
          ('github', 'https://github.com/entropyworks'),
          ('envelope', 'mailto:entropywork@gmail.com'),)

# Footer
FOOTER = ("&copy; 2015 Yazz D. Atlas. All rights reserved.<br>" +
           "Code snippets in the pages are released under " +
            "<a href=\"http://opensource.org/licenses/MIT\" target=\"_blank\">" +
            "The MIT License</a>, unless otherwise specified.")

TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
DEFAULT_PAGINATION = 10
SHARE = True

# Adding a file for github site
STATIC_PATHS = [
    'extras/CNAME',
    'extras/favicon.ico',
        ]

EXTRA_PATH_METADATA = {
    'extras/CNAME': { 'path': 'CNAME'},
    'extras/favicon.ico': { 'path': 'favicon.ico'},
        }

# 
FAVICON = 'favicon.ico'
FAVICON_TYPE = 'image/x-icon'

#
META_IMAGE = SITEURL + "/static/img/og_logo.jpg"
META_IMAGE_TYPE = "image/jpeg"


PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = [ 'summary', 'tipue_search', 'sitemap']
PYGMENTS_RST_OPTIONS = {'classprefix': 'pgcss', 'linenos': 'table'}

#
DIRECT_TEMPLATES = ('index', 'categories', 'archives', 'search', 'tipue_search')
TIPUE_SEARCH_SAVE_AS = 'tipue_search.json'

SITEMAP = { 'format': 'xml'}


# Could not use this since it broke the search, which I don't really know
# enought to modify for my own needs...
#
ARTICLE_URL = "posts/{date:%Y}/"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{slug}/index.html"
#CATEGORY_URL = "category/{slug}/"
#CATEGORY_SAVE_AS = "category/{slug}/index.html"
#TAG_URL = "tag/{slug}/"
#TAG_SAVE_AS = "tag/{slug}/index.html"
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
