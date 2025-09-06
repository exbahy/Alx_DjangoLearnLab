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
    
# Imports جديدة هنحتاجها
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# الموديل الجديد لبروفايل اليوزر
class UserProfile(models.Model):
    # هنعرف الأدوار المتاحة كثوابت عشان الكود يبقى أنضف
    ADMIN = 'Admin'
    LIBRARIAN = 'Librarian'
    MEMBER = 'Member'
    
    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (LIBRARIAN, 'Librarian'),
        (MEMBER, 'Member'),
    ]

    # علاقة "واحد لواحد" مع موديل اليوزر الأصلي بتاع جانجو
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # الحقل اللي هنخزن فيه دور اليوزر
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=MEMBER)

    def __str__(self):
        return f'{self.user.username} - {self.role}'

# --- Signals ---
# دي فانكشن هتشتغل تلقائيًا أول ما يوزر جديد يتعمل
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    # لو اليوزر ده لسه معمول جديد (created=True)
    if created:
        UserProfile.objects.create(user=instance)

# دي فانكشن هتشتغل تلقائيًا كل ما اليوزر يتعمله save عشان تحفظ البروفايل معاه
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()