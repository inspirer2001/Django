# Generated by Django 3.0.8 on 2021-01-29 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_blog_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='author',
        ),
    ]