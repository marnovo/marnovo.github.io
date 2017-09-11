#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Marcelo Novaes'
SITENAME = 'mnovaes'
SITEURL = 'http://www.mnovaes.com'

# THEME = 'medius'
THEME = 'nest'
# THEME = 'martin-pelican'  # --> broken?

PATH = 'content'

TIMEZONE = 'Europe/Madrid'

DEFAULT_LANG = 'en'

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
          ('Twitter', 'http://www.twitter.com/marnovo'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# TODO: don't keep relative URLs
RELATIVE_URLS = True
