# Generated by Django 4.1.1 on 2022-09-26 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontweb', '0010_draftpost_meta_urls'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='meta_keywords',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='meta_title',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='meta_urls',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('subtitle', models.CharField(blank=True, max_length=255)),
                ('price', models.CharField(blank=True, max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('body', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('publish_date', models.DateTimeField(blank=True, null=True)),
                ('published', models.BooleanField(default=False)),
                ('meta_description', models.CharField(blank=True, max_length=150)),
                ('meta_title', models.TextField(blank=True, null=True)),
                ('meta_keywords', models.TextField(blank=True, null=True)),
                ('meta_urls', models.TextField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='frontweb.profile')),
                ('tags', models.ManyToManyField(blank=True, to='frontweb.tag')),
            ],
            options={
                'ordering': ['-publish_date'],
            },
        ),
    ]
