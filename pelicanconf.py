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

CATEGORIES_TO_DISPLAY_ON_HOMEPAGE=('Artz')
DISPLAY_PAGES_ON_MENU=TRUE
MENUITEMS=(('Printz', 'https://www.inprnt.com/gallery/catmeister/'),)

SITEURL = 'https://joshpsawyer.com'
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
RELATIVE_URLS = True
FEED_ALL_RSS = 'feeds/all.rss'

# this can be changed to true at some point
DELETE_OUTPUT_DIRECTORY = False
OUTPUT_RETENTION = [".hg", ".git", ".bzr"]

OUTPUT_PATH = '../joshpsawyer.github.io/'
