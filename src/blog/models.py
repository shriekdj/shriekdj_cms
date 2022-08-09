from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# choices

class NewsLetter(models.Model):

	class SenderReplyTo(models.TextChoices):
		NEWSLETTER = 'newsletter'
		SUPPORT = 'support'

	class Status(models.TextChoices):
		ACTIVE = 'active'
		ARCHIVED = 'archived'

	class FontCategory(models.TextChoices):
		SERIF = 'serif'
		SANS_SERIF = 'sans_serif'
	
	class TitleAlignment(models.TextChoices):
		CENTER = 'center'
		LEFT = 'left'
	
	id = models.BigAutoField(primary_key=True, null=False)
	# uuid = models.UUIDField(max_length=36, null=False, unique=True)
	name = models.CharField(max_length=191, null=False, unique=True)
	description = models.TextField(max_length=2000, null=True)
	slug = models.SlugField(null=False, unique=True)
	sender_name = models.CharField(max_length=191, null=True)
	sender_email = models.EmailField(max_length=191, null=True)
	sender_reply_to = models.CharField(max_length=191, null=False, choices=SenderReplyTo.choices, default=SenderReplyTo.NEWSLETTER)
	status = models.CharField(max_length=10, null=False, choices=Status.choices, default=Status.ACTIVE)
	visibility = models.CharField(max_length=50, null=False, default="members")
	subscribe_on_signup = models.BooleanField(null=False, default=True)
	sort_order = models.PositiveIntegerField(null=False, default=0)
	show_header_title = models.BooleanField(null=False, default=True)
	title_font_category = models.CharField(max_length=191, null=False, choices =FontCategory.choices, default=FontCategory.SANS_SERIF)
	title_font_category = models.CharField(max_length=191, null=False, choices =TitleAlignment.choices, default=TitleAlignment.CENTER)
	show_feature_image = models.BooleanField(null=False, default=True)
	body_font_category = models.CharField(max_length=191, null=False, choices=FontCategory.choices, default=FontCategory.SANS_SERIF)
	footer_content = models.TextField(max_length=1000000000, null=True)
	show_badge = models.BooleanField(null=False, default=True)
	show_header_name = models.BooleanField(null=False, default=True)
	created_at = models.DateTimeField(null=False)
	updated_at = models.DateTimeField(null=True)

	def __str__(self) -> str:
		return '<Newsletter ' + self.slug + '>' 

class TypeName(models.TextChoices):
	POST = 'post'
	PAGE = 'page'

class Post(models.Model):

	class Status(models.TextChoices):
		PUBLISHED = 'published'
		DRAFT = 'draft'
		SCHEDULED = 'scheduled'
		SENT = 'sent'

	id = models.BigAutoField(primary_key=True, null=False)
	# uuid = models.UUIDField(max_length=36, null=False, unique=True)
	title = models.CharField(max_length=2000, null=False)
	slug = models.SlugField(max_length=191, null=False)
	mobiledoc = models.TextField(max_length=1000000000, null=True)
	html = models.TextField(max_length=1000000000, null=True)
	comment_id = models.CharField(max_length=50, null=True)
	plaintext = models.TextField(max_length=1000000000, null=True)
	feature_image = models.CharField(max_length=2000, null=True)
	featured = models.BooleanField(null=False, default= False)
	type_name = models.CharField(max_length=50, null=False, choices=TypeName.choices, default=TypeName.POST)
	status = models.CharField(max_length=50, null=False, default=Status.DRAFT)

	# future fields
	locale = models.CharField(max_length=6, null=True)
	visibility = models.CharField(max_length=50, null=False, default="public")
	email_recipient_filter = models.TextField(max_length=1000000000, null=False)
	created_at = models.DateTimeField(null=False)

	created_by = models.CharField(max_length=24, null=False)
	updated_at = models.DateTimeField(null=True)
	updated_by = models.CharField(max_length=24, null=True)
	published_at = models.DateTimeField(null=True)
	published_by = models.CharField(max_length=24, null=True)
	custom_excerpt = models.CharField(max_length=2000, null=True)
	codeinjection_head = models.CharField(max_length=65535, null=True)
	codeinjection_foot = models.CharField(max_length=65535, null=True)
	custom_template = models.CharField(max_length=100, null=True)
	canonical_url = models.URLField(max_length=2000, null=True)
	newsletter = models.ForeignKey("NewsLetter", on_delete=models.CASCADE)

class PostMeta(models.Model):
	id = models.BigAutoField(primary_key=True, null=False)
	post = models.OneToOneField(Post, max_length=24, null=False, unique=True, on_delete=models.CASCADE)
	og_image = models.CharField(max_length=2000, null=True)
	og_title = models.CharField(max_length=300, null=True)
	og_description = models.CharField(max_length=500, null=True)
	twitter_image = models.CharField(max_length=2000, null=True)
	twitter_title = models.CharField(max_length=300, null=True)
	twitter_description = models.CharField(max_length=500, null=True)
	meta_title = models.CharField(max_length=500, null=True)
	meta_description = models.CharField(max_length=2000, null=True)
	email_subject = models.CharField(max_length=300, null=True)
	frontmatter = models.TextField(max_length=65535, null=True)
	feature_image_alt = models.CharField(max_length=191, null=True)
	feature_image_caption = models.TextField(max_length=65535, null=True)
	email_only = models.BooleanField(null=False, default=False)

