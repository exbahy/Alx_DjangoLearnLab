This project implements:
A custom user model in the 'users' app.
Advanced model relationships (ForeignKey, ManyToMany, OneToOne) in the 'relationship_app'.
A basic 'bookshelf' app with custom admin and permissions.
To set up and run:
Navigate to Alx_DjangoLearnLab/advanced_features_and_security.
Activate your virtual environment: .\venv\Scripts\Activate (Windows) or source venv/bin/activate (Linux/macOS).
Apply migrations: python manage.py makemigrations users bookshelf relationship_app then python manage.py migrate.
Create a superuser: python manage.py createsuperuser.
Run the development server: python manage.py runserver.
Access: http://127.0.0.1:8000/admin/ or http://127.0.0.1:8000/relationships/.