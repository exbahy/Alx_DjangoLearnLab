from django.db import models

# Book Model
class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان الكتاب")
    publication_year = models.PositiveIntegerField(verbose_name="سنة النشر")
    author = models.ForeignKey(
        "Author",
        related_name="books",
        on_delete=models.CASCADE,
        verbose_name="المؤلف"
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"


# Author Model
class Author(models.Model):
    name = models.CharField(max_length=255, verbose_name="اسم المؤلف")

    def __str__(self):
        return self.name
