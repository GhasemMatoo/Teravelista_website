# Generated by Django 3.2.8 on 2021-11-17 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_comment_messages'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='Post',
            new_name='Poost',
        ),
    ]