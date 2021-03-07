# Generated by Django 3.0.8 on 2021-01-31 14:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0009_blog_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('author', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog_post', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
        migrations.DeleteModel(
            name='UserExtra',
        ),
    ]
