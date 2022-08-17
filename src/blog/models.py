import random
from django.db import models
from django.utils.text import slugify
from django.conf import settings

def random_words():
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz0123456789'.split('')) for _ in range(6))

class Profile(models.Model):
	user = models.OneToOneField(
		settings.AUTH_USER_MODEL,
		on_delete=models.PROTECT,
	)
	website = models.URLField(blank=True)
	bio = models.CharField(max_length=240, blank=True)

	def __str__(self):
		return self.user.get_username()

class Tag(models.Model):
	name = models.CharField(max_length=50, unique=True, null=False)
	slug = models.SlugField(verbose_name='slug', max_length=50, unique=True)

	def __str__(self) -> str:
		return self.name


# Create your models here.
class Post(models.Model):
	id = models.BigAutoField(primary_key=True)
	title = models.CharField(verbose_name='title', max_length=255, null=False)
	subtitle = models.CharField(max_length=255, blank=True)
	content = models.TextField(verbose_name='content', null=False, blank=True)
	meta_description = models.CharField(max_length=150, blank=True)
	created_at = models.DateTimeField(verbose_name='created_at',auto_now=True, auto_created=True, null=False, blank=False)
	updated_at = models.DateTimeField(verbose_name='updated_at',null=True)
	published_at = models.DateTimeField(verbose_name='published_at',null=True)
	is_published = models.BooleanField(verbose_name='is_published', default=False)
	slug = models.SlugField(verbose_name='slug', max_length=50, unique=True)

	author = models.ForeignKey(Profile, on_delete=models.PROTECT, default=None)
	tags = models.ManyToManyField(Tag, blank=True)
