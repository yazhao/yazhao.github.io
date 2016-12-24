#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#Site 
AUTHOR = 'Alex Zhao'
SITENAME = 'Alex Zhao'
SITEURL = 'http://www.alexzhao.us'
TIMEZONE = 'America/New_York'
THEME = 'void/'
AVATAR = '/theme/images/avatar.jpg'
TITLE = 'Alex Zhao: statistics graduate student at Pennsylvnania State University'
DESCRIPTION = "Alex Zhao is a graduate student in statistics at Penn State, with experience as a data analyst at e-commerce and gaming tech companies working with analytics and big data"

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Static Pages
PAGE_PATHS = ['pages']
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
ABOUT_PAGE_HEADER = 'Stay awhile and listen.'
STATIC_PATHS = ['images', 'notebooks','extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

# DEFAULTS
DEFAULT_LANG = 'en'
DEFAULT_CATEGORY = 'misc'
DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%b %d, %Y'
DEFAULT_PAGINATION = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

NAVIGATION = [
    # You probably want to fill these in so they point to your user pages
    {'site': 'twitter', 'user': 'alexzhao', 'url': 'https://twitter.com/alexzhao'},
    {'site': 'github', 'user': 'yazhao', 'url': 'https://github.com/yazhao'},
    {'site': 'linkedin', 'user': 'yealexzhao', 'url': 'http://linkedin.com/in/yealexzhao'},
]

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = ['./plugins','pelican-plugins']
PLUGINS = ['ipynb.markup','assets', 'pelican_dynamic', 'render_math']


TWITTER_NAME = "alexzhao"
TWITTER_CARDS = True
FACEBOOK_SHARE = True
HACKER_NEWS_SHARE = False

# Other
CACHE_CONTENT = False