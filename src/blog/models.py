from django.db import models

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
	
	id = models.BigAutoField(primary_key=True)
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
	footer_content = models.CharField(max_length=1000000000, null=True)
	show_badge = models.BooleanField(null=False, default=True)
	show_header_name = models.BooleanField(null=False, default=True)
	created_at = models.DateTimeField(null=False)
	updated_at = models.DateTimeField(null=True)
