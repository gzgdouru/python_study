from django.db import models

# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
