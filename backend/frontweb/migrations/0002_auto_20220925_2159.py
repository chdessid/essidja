# Generated by Django 3.1.7 on 2022-09-25 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontweb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DraftPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('body', models.TextField()),
                ('keywords', models.TextField()),
                ('images', models.TextField()),
                ('meta_title', models.TextField()),
                ('meta_description', models.TextField()),
                ('meta_keywords', models.TextField()),
                ('sitename', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('urlsource', models.CharField(max_length=1000, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='WebToScrape',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sitename', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('siteurl', models.CharField(max_length=255, unique=True)),
                ('category', models.CharField(blank=True, max_length=255, null=True)),
                ('robotstxt', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('sitemapxml', models.CharField(blank=True, max_length=255, null=True, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='blogspot_url',
            field=models.URLField(blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='business_url',
            field=models.URLField(blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='facebook_page',
            field=models.URLField(blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='facebook_profile',
            field=models.URLField(blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='instagram_page',
            field=models.URLField(blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='instagram_profile',
            field=models.URLField(blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='linkedin_page',
            field=models.URLField(blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='linkedin_profile',
            field=models.URLField(blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='login_email',
            field=models.CharField(blank=True, max_length=255, unique=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='login_password',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='profile',
            name='login_username',
            field=models.CharField(blank=True, max_length=255, unique=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='pinterest_page',
            field=models.URLField(blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='pinterest_profile',
            field=models.URLField(blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='postachio_url',
            field=models.URLField(blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='quora_page',
            field=models.URLField(blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='reddit_page',
            field=models.URLField(blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='stackoverflow_page',
            field=models.URLField(blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='tumblr_page',
            field=models.URLField(blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='twitter_page',
            field=models.URLField(blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='twitter_profile',
            field=models.URLField(blank=True, unique=True),
        ),
    ]
