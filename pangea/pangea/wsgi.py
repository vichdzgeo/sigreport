"""
WSGI config for pangea project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

#activate_this = '/var/www/cap2/venv/bin/activate_this.py'
#with open(activate_this) as file_:
#    exec(file_.read(), dict(file=activate_this))



def execfile(filename):
    globals = dict( __file__ = filename )
    exec( open(filename).read(), globals )


import os
import sys

PROJECT_DIR="/var/www/cap2"
sys.path.insert(0, os.path.join(PROJECT_DIR, 'pangea'))

activate_this = os.path.join( PROJECT_DIR, 'venv/bin', 'activate_this.py' )
execfile( activate_this )



from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pangea.settings')

application = get_wsgi_application()
