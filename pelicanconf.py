from pickle import TRUE


AUTHOR = 'Josh P. Sawyer'
SITENAME = "Josh P. Sawyer's Internet Scrapyard"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'EST'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = '../joshpsawyer-dot-com-theme'

CATEGORIES_TO_DISPLAY_ON_HOMEPAGE=('Portfolio')
DISPLAY_PAGES_ON_MENU=TRUE
MENUITEMS=(('Prints', 'https://www.inprnt.com/gallery/catmeister/'),)