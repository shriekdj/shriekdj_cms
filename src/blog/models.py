import random
from typing import Iterable, Optional
from django.db import models
from django.utils.text import slugify

def random_words():
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz0123456789'.split('')) for _ in range(6))

# Create your models here.
class Post(models.Model):
	title = models.CharField(verbose_name='title', max_length=255, null=False)
	content = models.TextField(verbose_name='content', null=False, blank=True)
	created_on = models.DateTimeField(auto_now=True, auto_created=True, null=False, blank=False)
	published_on = models.DateTimeField(null=True)
	updated_on = models.DateTimeField(null=True)
	slug = models.SlugField(verbose_name='slug', max_length=255, unique=True)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title + random_words())
		super(Post, self).save(*args, **kwargs)

