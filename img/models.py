from django.db import models

class Info(models.Model):
	email = models.CharField(max_length=100)
	phone = models.TextField()
	
	def __str__(self):
		return self.email

class Image(models.Model):
	image = models.ImageField(upload_to='images', blank=True)
	name = models.CharField(max_length=100)
	
	def __str__(self):
		return self.name

class About(models.Model):
	description = models.TextField()
	
	def __str__(self):
		return self.description

class About_ru(models.Model):
	description = models.TextField()
	
	def __str__(self):
		return self.description
