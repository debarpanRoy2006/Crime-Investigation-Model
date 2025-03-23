#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

import os
from django.http import HttpResponse
from django.conf import settings
from django.urls import path
from django.core.management import execute_from_command_line
from django.core.wsgi import get_wsgi_application

# Configure Django settings
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
settings.configure(
    DEBUG=True,
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=['*'],
    INSTALLED_APPS=[],
)

# Define the view
def home_view(request):
    with open(os.path.join(BASE_DIR, 'result.html'), 'r') as file:
        return HttpResponse(file.read())

def other_view(request):
    return HttpResponse("Welcome to another route!")

# Define the URL patterns
urlpatterns = [
    path('/', home_view),
    path('other/', other_view),
]

# Create the WSGI application
application = get_wsgi_application()

# Run the development server
if __name__ == "__main__":
    execute_from_command_line(['manage.py', 'runserver'])

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
