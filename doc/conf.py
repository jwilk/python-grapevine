import sys
import os

extensions = [
    'sphinx.ext.doctest',
]

source_suffix = '.rst'
master_doc = 'index'

html_theme = 'haiku'
pygments_style = 'sphinx'

project = 'grapevine'
copyright = '2007-2015, Jakub Wilk'

def get_version():
    d = {}
    path = os.path.join(
        os.path.dirname(__file__),
        os.pardir,
        'grapevine.py'
    )
    file = open(path)
    try:
        for line in file:
            if line.startswith('__version__ ='):
                exec(line, d)
    finally:
        file.close()
    try:
        return d['__version__']
    except LookupError:
        raise IOError('unexpected end-of-file')

release = version = get_version()

# vim:ts=4 sts=4 sw=4 et
