# Generated by Django 3.0.8 on 2021-01-29 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_profile_mobile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['created_on']},
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='date',
            new_name='created_on',
        ),
    ]
