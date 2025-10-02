# django_blog

Minimal Django blog project scaffold created for Alx_DjangoLearnLab.

Setup

1. Create a virtual environment (recommended):

   python -m venv .venv
   .venv\Scripts\Activate.ps1

2. Install dependencies:

   pip install -r requirements.txt

3. Run migrations and start server:

   python manage.py migrate
   python manage.py runserver

Project layout

- blog/: Django app containing models, templates, and static files.
- django_blog/: project settings and URL configuration.

Next steps: create superuser, add posts via admin or shell.
