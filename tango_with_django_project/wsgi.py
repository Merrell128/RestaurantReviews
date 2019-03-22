import os
import sys
# Add your project's directory the PYTHONPATH
path = '/home/charstefanos/.virtualenvs/mysite-virtualenv'
if path not in sys.path:
	sys.path.append(path)

# Move to the project directory
os.chdir(path)

# Tell Django where the settings.py module is located
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
					'tango_with_django_project.settings')
					
# Import your Django project's configuration
import django
django.setup()

# Import the Django WSGI to handle any requests
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
