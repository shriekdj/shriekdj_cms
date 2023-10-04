import random
from django.db import models
from django.utils.text import slugify
from django.conf import settings
from django.utils.translation import gettext_lazy as _

def random_words():
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz0123456789'.split('')) for _ in range(6))

class ReactionChoices(models.IntegerChoices):
	LIKE = 1
	LOVE = 2
	HAHA = 3
	WOW = 4
	SAD = 5
	ANGRY = 6

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
	class PostStatus(models.TextChoices):
		PRIVATE = "PR", _("Private")
		PUBLIC = "PU", _("Public")
		UNLISTED = "UN", _("Unlisted")
		DRAFT = "DR", _("Draft")
		#GRADUATE = "GR", _("Graduate")
	id = models.BigAutoField(primary_key=True)
	title = models.CharField(verbose_name='title', max_length=255, null=False)
	subtitle = models.CharField(max_length=255, blank=True)
	content = models.TextField(verbose_name='content', null=False, blank=True)
	meta_title = models.CharField(verbose_name='meta_title', max_length=255, null=True)
	meta_description = models.CharField(max_length=150, blank=True)
	created_at = models.DateTimeField(verbose_name='created_at',auto_now=True, auto_created=True, null=False, blank=False)
	updated_at = models.DateTimeField(verbose_name='updated_at',null=True)
	published_at = models.DateTimeField(verbose_name='published_at',null=True, blank=True)
	#is_published = models.BooleanField(verbose_name='is_published', default=False)
	slug = models.SlugField(verbose_name='slug', max_length=50, unique=True)
	cover_image = models.ImageField(verbose_name='cover_image', null=True, blank=True)
	language = models.CharField(verbose_name='language', max_length=25, null=False, default='english')
	status = models.CharField(verbose_name='status', max_length=2, choices=PostStatus.choices, default=PostStatus.PRIVATE)	

	author = models.ForeignKey(Profile, on_delete=models.PROTECT, default=None)
	tags = models.ManyToManyField(Tag, blank=True)

	class Meta:
		ordering = ["-published_at"]

class PostComment(models.Model):
	id = models.BigAutoField(primary_key=True)
	content = models.TextField(verbose_name='content', null=False, blank=False)
	created_at = models.DateTimeField(verbose_name='created_at',auto_now=True, auto_created=True, null=False, blank=False)
	post = models.ForeignKey(Post, on_delete=models.PROTECT, default=None)

class PostReaction(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.PROTECT, default=None)
    post = models.ForeignKey(Post, on_delete=models.PROTECT, default=None)
    reaction = models.IntegerField(choices=ReactionChoices.choices)
