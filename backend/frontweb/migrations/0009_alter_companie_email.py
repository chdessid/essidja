# Generated by Django 4.1.1 on 2022-09-26 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontweb', '0008_alter_companie_urlsource'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companie',
            name='email',
            field=models.TextField(blank=True, null=True, unique=True),
        ),
    ]
