# C:\Users\user\Alx_DjangoLearnLab\django-models\LibraryProject\bookshelf\models.py

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    class Meta:
        permissions = [
            ("can_view_book", "Can view book"),
            ("can_create_book", "Can create new book"),
            ("can_edit_book", "Can edit existing book"),
            ("can_delete_book", "Can delete existing book"),
        ]

    def __str__(self):
        return f"{self.title} by {self.author}"