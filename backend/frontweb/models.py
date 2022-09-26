from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )
    bio = models.CharField(max_length=240, blank=True)

    website = models.URLField(blank=True)
    login_username = models.CharField(max_length=255, unique=True, blank=True)
    login_email = models.CharField(max_length=255, unique=True, blank=True)
    login_password = models.CharField(max_length=255, blank=True)

    blogspot_url = models.URLField(blank=True,unique=True,)
    business_url = models.URLField(blank=True,unique=True,)
    postachio_url = models.URLField(blank=True,unique=True,)

    reddit_page = models.URLField(blank=True,unique=True,)
    tumblr_page = models.URLField(blank=True,unique=True,)
    stackoverflow_page = models.URLField(blank=True,unique=True,)
    quora_page = models.URLField(blank=True,unique=True,)

    facebook_profile = models.URLField(blank=True,unique=True,)
    facebook_page = models.URLField(blank=True,unique=True,)

    linkedin_profile = models.URLField(blank=True,unique=True,)
    linkedin_page = models.URLField(blank=True,unique=True,)

    twitter_profile = models.URLField(blank=True,unique=True,)
    twitter_page = models.URLField(blank=True,unique=True,)

    pinterest_profile = models.URLField(blank=True,unique=True,)
    pinterest_page = models.URLField(blank=True,unique=True,)

    instagram_profile = models.URLField(blank=True,unique=True,)
    instagram_page = models.URLField(blank=True,unique=True,)

    def __str__(self):
        return self.user.get_username()

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    subtitle = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    body = models.TextField()
    meta_description = models.CharField(max_length=150, blank=True)
    published = models.BooleanField(default=True)
    author = models.ForeignKey(Profile, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, blank=True)
    category = models.CharField(max_length=255, blank=True)

    meta_title = models.TextField(blank=True, null=True)
    meta_keywords = models.TextField(blank=True, null=True)
    meta_urls = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.title
        
class Service(models.Model):
    title = models.CharField(max_length=255, unique=True)
    subtitle = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    body = models.TextField()
    meta_description = models.CharField(max_length=150, blank=True)
    published = models.BooleanField(default=True)
    author = models.ForeignKey(Profile, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, blank=True)
    category = models.CharField(max_length=255, blank=True)
    meta_title = models.TextField(blank=True, null=True)
    meta_keywords = models.TextField(blank=True, null=True)
    meta_urls = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255, unique=True)
    subtitle = models.CharField(max_length=255, blank=True)
    price = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    body = models.TextField()
    published = models.BooleanField(default=True)
    author = models.ForeignKey(Profile, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, blank=True)
    category = models.CharField(max_length=255, blank=True)

    meta_description = models.CharField(max_length=150, blank=True)
    meta_title = models.TextField(blank=True, null=True)
    meta_keywords = models.TextField(blank=True, null=True)
    meta_urls = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.title

class WebToScrape(models.Model):
    sitename = models.CharField(max_length=255,unique=True,blank=True, null=True)
    siteurl = models.CharField(max_length=255,unique=True)
    category = models.CharField(max_length=255,blank=True, null=True)
    robotstxt = models.CharField(max_length=255,unique=True,blank=True, null=True)
    sitemapxml = models.CharField(max_length=255,unique=True,blank=True, null=True)
    def __str__(self):
        return self.sitename

class DraftPost(models.Model):

    title = models.TextField(blank=True, null=True)
    slug = models.TextField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    keywords = models.TextField(blank=True, null=True)
    images = models.TextField(blank=True, null=True)
    meta_title = models.TextField(blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.TextField(blank=True, null=True)
    meta_urls = models.TextField(blank=True, null=True)
    sitename = models.CharField(max_length=255,blank=True, null=True)
    urlsource = models.CharField(max_length=1000,unique=True)
    published = models.BooleanField(default=True)

    def __str__(self):
            return self.title



class Companie(models.Model):
    name = models.TextField(blank=True, null=True)
    website = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True,unique=True)
    phone = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    logo = models.TextField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    keywords = models.TextField(blank=True, null=True)
    sitename = models.CharField(max_length=255,blank=True, null=True)
    urlsource = models.CharField(max_length=1000,unique=True,blank=True, null=True)

    def __str__(self):
            return self.email
