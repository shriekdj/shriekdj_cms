import random
import this
from typing import Iterable, Optional
from django.db import models
from django.utils.text import slugify

def random_words():
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz0123456789'.split('')) for _ in range(6))

# Create your models here.
class Post(models.Model):
	title = models.CharField(verbose_name='title', max_length=255, null=False)
	content = models.TextField(verbose_name='content', null=False, blank=True)
	created_at = models.DateTimeField(verbose_name='created_at',auto_now=True, auto_created=True, null=False, blank=False)
	published_at = models.DateTimeField(verbose_name='published_at',null=True)
	updated_at = models.DateTimeField(verbose_name='updated_at',null=True)
	slug = models.SlugField(verbose_name='slug', max_length=255, unique=True, default='')

	def save(self, *args, **kwargs):
		if self.slug == '':
			self.slug = slugify(self.title + random_words())
		super(Post, self).save(*args, **kwargs)

