# Generated by Django 3.0.8 on 2021-01-28 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210122_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Mobile',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
