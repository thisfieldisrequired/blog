# Generated by Django 4.2 on 2023-05-22 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tag',
            new_name='tags',
        ),
    ]
