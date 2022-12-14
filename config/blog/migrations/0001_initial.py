# Generated by Django 4.1 on 2022-08-17 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('created_at', models.DateTimeField(auto_created=True, auto_now=True, verbose_name='created_at')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('content', models.TextField(blank=True, verbose_name='content')),
                ('published_at', models.DateTimeField(null=True, verbose_name='published_at')),
                ('updated_at', models.DateTimeField(null=True, verbose_name='updated_at')),
                ('slug', models.SlugField(default='djangodbmodelsfieldscharfield<django.db.models.fields.BigAutoField>', max_length=255, unique=True, verbose_name='slug')),
            ],
        ),
    ]
