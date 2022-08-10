from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(verbose_name='title', max_length=255, null=False)
	content = models.TextField(verbose_name='content', null=False, blank=True)
	created_on = models.DateTimeField(auto_now=True, auto_created=True, null=False, blank=False)
	published_on = models.DateTimeField(null=True)
	updated_on = models.DateTimeField(null=True)


