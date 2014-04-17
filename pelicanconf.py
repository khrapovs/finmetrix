#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Stanislav Khrapov'
SITENAME = u'Pythonic FinMetrix'
SITEURL = 'http://khrapovs.github.io/finmetrix'

# Times and dates
DEFAULT_DATE_FORMAT = '%b %d, %Y'
TIMEZONE = 'Europe/Moscow'
DEFAULT_LANG = u'en'

# Set the article URL
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Theme and plugins
THEME = '../pelican-themes/gum/'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Title menu options
MENUITEMS = (('About', 'https://sites.google.com/site/khrapovs'),
             ('Contact', 'mailto:khrapovs@gmail.com'))

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),)
GITHUB_URL = 'http://github.com/khrapovs/'

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Delete the output directory, and all of its contents, before generating new files.
#This can be useful in preventing older, unnecessary files from persisting in your output.
DELETE_OUTPUT_DIRECTORY = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
