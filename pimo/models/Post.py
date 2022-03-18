from django.db import models


class Post(models.Model):
    title = models.CharField('Title', max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField('Publication date')
    details = models.TextField('Details')
    likes = models.BooleanField('Likes')

    def __str__(self):
        return self.title