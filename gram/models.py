from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone

# Create your models here.

class Profile(models.Model):
    pro_photo = models.ImageField(upload_to = 'images/',null=True)
    name = models.CharField(max_length =30,null=True)
    bio = models.TextField(null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile',null=True)

    def __str__(self):
        return self.bio

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

class Image(models.Model):
    name = models.CharField(max_length =30,null=True)
    image = models.ImageField(upload_to = 'images/')
    user = models.ForeignKey(User, null=True)
    profile = models.ForeignKey(Profile, null=True)
    date = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return self.user.username

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    class Meta:
        ordering = ["-id"]

    @classmethod
    def upl(cls):
        uploads = cls.objects.all()
        return uploads

class Comment(models.Model):
    comment = models.CharField(max_length =80,null=True)
    user = models.ForeignKey(User,null=True)
    post = models.ForeignKey(Image,related_name='comments',null=True)

    def __str__(self):
        return self.comment


    def save_comment(self):
        self.save()


    def delete_comment(self):
        self.delete()
