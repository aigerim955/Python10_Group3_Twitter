from django.db import models
from account.models import User

class Post(models.Model):
    article_title = models.CharField(max_length=120)
    article_text = models.CharField(max_length=300)
    pub_date = models.DateTimeField()
    account = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.article_title

class Comment(models.Model):
    author_name = models.CharField(max_length=120)
    comment_text = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='coments')

    def __str__(self):
        return self.author_name

class PostImage(models.Model):
    product = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='', null=True, blank=True)

