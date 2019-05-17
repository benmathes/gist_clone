from django.db import models

from gist_clone.user.models import User


class File(models.Model):
    name = models.TextField()
    last_modified = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


class FileVersion(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    file = models.ForeignKey(File, on_delete=models.CASCADE, related_name='versions')
    created_by = models.ForeignKey(User, related_name='versions',
                                   null=True, on_delete=models.SET_NULL)
