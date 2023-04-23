from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)  # Добавляем поле created_date
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='files/', blank=True, null=True)  # Добавляем поле file

    def __str__(self):
        return self.title

class MediaFile(models.Model):
    file = models.ImageField(upload_to='media_files/')
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)