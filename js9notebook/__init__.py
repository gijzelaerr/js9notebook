from os import path
from IPython.core.displaypub import publish_display_data

__version__ = '0.1'

STATIC = path.join(path.dirname(__file__), 'static')


def initialize():
    resources = {
        'application/javascript': ('js9support.js', 'js9.js', 'js9plugins.js'),
        'text/html': ('js9support.css', 'js9.css'),
    }

    for type_, files in resources.items():
        for file_ in files:
            data = open(path.join(STATIC, file_), 'rb').read()
            publish_display_data(data={type_: data})
