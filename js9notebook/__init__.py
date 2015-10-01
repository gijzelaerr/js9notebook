from os import path

__version__ = '0.1'

STATIC = path.join(path.dirname(__file__), 'static')


def initialize():
    from IPython.core.displaypub import publish_display_data
    js = ('js9support.js', 'js9.js', 'js9plugins.js')
    css = ('js9support.css', 'js9.css')

    for file_ in js:
        data = open(path.join(STATIC, file_), 'rb').read()
        publish_display_data(data={'application/javascript': data})

    for file_ in css:
        data = open(path.join(STATIC, file_), 'r').read()
        data = '<style>' + data + '</style>'
        publish_display_data(data={'text/html': data})
