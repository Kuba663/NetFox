"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask
from flask import render_template
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route('/')
def hello():
    """Renders a sample page."""
    tags.__init__()
    tags.html()
    tags.endhtml()

class tags(object):
    def __init__():
        return "<!DOCTYPE html>"
    def html():
        return "<html>"
    def endhtml():
        return "</html>"
    pass

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '666'))
    except ValueError:
        PORT = 666
    app.run(HOST, PORT)
