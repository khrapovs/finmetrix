#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Stanislav Khrapov'
SITENAME = u'Pythonic FinMetrix'
SITEURL = 'http://khrapovs.github.io/finmetrix'
GITHUB_URL = 'http://github.com/khrapovs/'

# Times and dates
DEFAULT_DATE_FORMAT = '%b %d, %Y'
TIMEZONE = 'Europe/Moscow'
DEFAULT_LANG = u'en'

# Set the article URL
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Theme and plugins
THEME = '../pelican-themes/gum/'
# Plugins
PLUGIN_PATH = '../pelican-plugins/'
PLUGINS = ['summary', 'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.include_code', 'liquid_tags.notebook',
           'liquid_tags.literal']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Title menu options
MENUITEMS = (('About', 'https://sites.google.com/site/khrapovs'),
             ('Contact', 'mailto:khrapovs@gmail.com'))

# Blogroll
# LINKS =  (('Pelican', 'http://getpelican.com/'),
#           ('Python.org', 'http://python.org/'),
#           ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('LinkedIn', 'http://www.linkedin.com/in/khrapovs'),
		  ('Twitter', 'https://twitter.com/khrapovs'),
          ('Google+', 'https://www.google.com/+StanislavKhrapov'),)
TWITTER_USER = 'khrapovs'
GOOGLE_PLUS_USER = 'StanislavKhrapov'

DEFAULT_PAGINATION = 10

# Delete the output directory, and all of its contents, before generating new files.
# This can be useful in preventing older, unnecessary files from persisting in your output.
DELETE_OUTPUT_DIRECTORY = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# RSS/Atom feeds
FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'