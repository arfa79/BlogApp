import os
import django
from django.conf import settings

# Path to the project's settings module
TEST_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(TEST_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BlogApp.settings")

# Configure Django
django.setup()