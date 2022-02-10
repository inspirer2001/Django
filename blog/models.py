from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
class blog(models.Model):
	title=models.CharField(max_length=100)
	slug=models.SlugField()
	body=models.TextField()
	author=models.OneToOneField(User, on_delete= models.CASCADE,related_name='blog_posts',null=True)
	created_on=models.DateTimeField(auto_now_add=True)
	#thumbnail
	#author
	class Meta:
		ordering=['created_on']
	def __str__(self):
		return self.title
class Profile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	image=models.ImageField(default='default.jpg',upload_to='profile_pics')
	file=models.FileField(default='default.pdf',upload_to='file')
	Mobile=models.CharField(blank=True,max_length=10)
	#thumbnail
	#author
	def __str__(self):
		return f'{self.user.username} Profile'

class news(models.Model):
	title=models.CharField(max_length=1000)
	image=models.ImageField(default='default.jpg',upload_to='profile_pics')
	body=models.TextField()
	created_on=models.DateTimeField(auto_now_add=True)
	#thumbnail
	#author
	class Meta:
		ordering=['created_on']
	def __str__(self):
		return self.title