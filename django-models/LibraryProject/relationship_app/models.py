from django.db import models

# موديل المؤلف
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# موديل الكتاب
# الكتاب له مؤلف واحد فقط (علاقة واحد لكتير - ForeignKey)
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# موديل المكتبة
# المكتبة فيها كتب كتير، والكتاب ممكن يكون في كذا مكتبة (علاقة كتير لكتير - ManyToManyField)
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

# موديل أمين المكتبة
# كل مكتبة ليها أمين واحد بس (علاقة واحد لواحد - OneToOneField)
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name