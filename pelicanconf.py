#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#Site 
AUTHOR = 'Alex Zhao'
SITENAME = 'Alex Zhao'
SITEURL = 'https://www.alex-zhao.com'
TIMEZONE = 'America/New_York'
THEME = 'void/'
LOGO_IMAGE = 'content/images/favicon.jpg'
TITLE = 'Alex Zhao'
DESCRIPTION = "Alex Zhao is a Ph.D. student in Statistics at Penn State, with industry experience in data science and analytics"


ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Static Pages
PAGE_PATHS = ['pages']
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
ABOUT_PAGE_HEADER = ''
STATIC_PATHS = ['images', 'notebooks','extra/CNAME','figure']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

# DEFAULTS
DEFAULT_LANG = 'en'
DEFAULT_CATEGORY = 'misc'
DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%b %d, %Y'
DEFAULT_PAGINATION = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

NAVIGATION = [
    # You probably want to fill these in so they point to your user pages
   	{'site': 'twitter', 'user': 'alexzhao', 'url': 'https://twitter.com/alexzhao'},
    {'site': 'github', 'user': 'yazhao', 'url': 'https://github.com/yazhao'},
    {'site': 'linkedin', 'user': 'yealexzhao', 'url': 'http://linkedin.com/in/yealexzhao'},
]

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['ipynb.markup','assets', 'pelican_dynamic', 'render_math'] #,'rmd_reader'] # taken out


TWITTER_CARDS = True
TWITTER_NAME = "alexzhao"
FACEBOOK_SHARE = True
HACKER_NEWS_SHARE = True

#### Analytics
DOMAIN = "www.alex-zhao.com"

# Other
CACHE_CONTENT = False
IGNORE_FILES = [".ipynb_checkpoints"]  

# RMarkdown
#RMD_READER_RENAME_PLOT = 'directory'
#RMD_READER_KNITR_OPTS_CHUNK = {'fig.path': 'figure/'}
