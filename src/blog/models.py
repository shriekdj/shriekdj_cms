from typing import Iterable, Optional
from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(verbose_name='title', max_length=255, null=False)
	content = models.TextField(verbose_name='content', null=False, blank=True)
	created_on = models.DateTimeField(auto_now=True, auto_created=True, null=False, blank=False)
	published_on = models.DateTimeField(null=True)
	updated_on = models.DateTimeField(null=True)
	slug = models.SlugField(verbose_name='slug', unique=True)

	def save(self, force_insert: bool = ..., force_update: bool = ..., using: Optional[str] = ..., update_fields: Optional[Iterable[str]] = ...) -> None:
		return super().save(force_insert, force_update, using, update_fields)

