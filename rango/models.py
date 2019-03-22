from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=128, unique=True)
	views = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)
	slug = models.SlugField(unique = True)
	
	def save(self, *args, **kwargs): 
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)

	
	class Meta:
		verbose_name_plural = 'Categories'
	
	
	def __str__(self): # For Python 2, use __unicode__ too
		return self.name
	
class Page(models.Model):
	category = models.ForeignKey(Category)
	title = models.CharField(max_length=128)
	address = models.CharField(max_length=128)
	phone = models.CharField(max_length=128, default = 0)
	slug = models.SlugField(unique = True)
	
	def save(self, *args, **kwargs): 
		self.slug = slugify(self.title)
		super(Page, self).save(*args, **kwargs)
	
	def __str__(self): # For Python 2, use __unicode__ too
		return self.title
		
		
class Review(models.Model):
	page = models.ForeignKey(Page)
	title = models.CharField(max_length=128)
	text = models.CharField(max_length=128)
	rating = models.IntegerField(default = 0)

	def __str__(self): # For Python 2, use __unicode__ too
		return self.title
		
	
class UserProfile(models.Model):
	# This line is required. Links UserProfile to a User model instance. 
	user = models.OneToOneField(User)
	
	# The additional attributes we wish to include.
	website = models.URLField(blank=True)
	picture = models.ImageField(upload_to='profile_images', blank=True)

	# Override the __unicode__() method to return out something meaningful! 
	# Remember if you use Python 2.7.x, define __unicode__ too!
	def __str__(self):
		return self.user.username
