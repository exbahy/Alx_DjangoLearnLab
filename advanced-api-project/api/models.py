from django.db import models


class Author(models.Model):
    # اسم المؤلف
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    # عنوان الكتاب
    title = models.CharField(max_length=255)
    # سنة النشر (عدد موجب)
    publication_year = models.PositiveIntegerField()
    # علاقة One-to-Many مع المؤلف
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
