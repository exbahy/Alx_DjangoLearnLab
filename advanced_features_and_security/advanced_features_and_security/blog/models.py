from django.db import models
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        permissions = [
            ("can_view_post", "Can view post"),
            ("can_create_post", "Can create new post"),
            ("can_edit_post", "Can edit existing post"),
            ("can_delete_post", "Can delete existing post"),
        ]
