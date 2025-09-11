# LibraryProject - ALX Django LearnLab

This project implements:
- Custom User Model in the 'users' app.
- Advanced model relationships (ForeignKey, ManyToMany, OneToOne) in the 'relationship_app'.
- Basic 'bookshelf' app with custom admin and permissions.

To set up and run:
1.  Navigate to `Alx_DjangoLearnLab/django-models/LibraryProject`.
2.  Activate virtual environment: `.\venv\Scripts\Activate` (Windows) or `source venv/bin/activate` (Linux/macOS).
3.  Apply migrations: `python manage.py makemigrations users bookshelf relationship_app` then `python manage.py migrate`.
4.  Create superuser: `python manage.py createsuperuser`.
5.  Run server: `python manage.py runserver`.
6.  Access: `http://127.0.0.1:8000/admin/` or `http://127.0.0.1:8000/relationships/`.