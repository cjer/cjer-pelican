#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'Dan Bareket'
SITENAME = 'cjer'
SITEURL = 'https://cjer.github.io'

PATH = 'content'

STATIC_PATHS = ['extra']
EXTRA_PATH_METADATA = {
    'extra/google7a5dd5ba97352752.html': {'path': 'google7a5dd5ba97352752.html'},
    'extra/README.md': {'path': 'README.md'},
    'extra/BingSiteAuth.xml': {'path': '/BingSiteAuth.xml'},
    'extra/yandex_0535b382efa4270d.html': {'path': '/yandex_0535b382efa4270d.html'}
    }
ARTICLE_EXCLUDES = ['extra']

TIMEZONE = 'Asia/Tel_Aviv'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

OUTPUT_PATH = '../cjer.github.io/'
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = ['.git']

GOOGLE_ANALYTICS = "UA-111620097-1"
DISQUS_SITENAME = "cjer"

# Blogroll
LINKS = (('OpenBus', 'https://github.com/hasadna/open-bus/'),
		)

# Social widget
SOCIAL = (('Social link will come here', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Add plugins for notebook usage
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code', 'liquid_tags.notebook',
           'sitemap',]

NOTEBOOK_DIR = 'notebooks'

# The theme file should be updated so that the base header contains the line:
#
#  {% if EXTRA_HEADER %}
#    {{ EXTRA_HEADER }}
#  {% endif %}
# 
# This header file is automatically generated by the notebook plugin
if not os.path.exists('_nb_header.html'):
    import warnings
    warnings.warn("_nb_header.html not found.  "
                  "Rerun make html to finalize build.")
else:
    EXTRA_HEADER = open('_nb_header.html', encoding='utf-8').read()

THEME = 'theme'

### FOR NEW THEME

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'codehilite'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

IPYNB_EXTEND_STOP_SUMMARY_TAGS = [('h2', None), ('ol', None), ('ul', None)]

SHOW_ARCHIVES = True
SHOW_FEED = True

GOOGLE_ANALYTICS_CODE = 'UA-111620097-1'
GOOGLE_ANALYTICS_DOMAIN = 'cjer.github.io'
