# Generated by Django 3.2.8 on 2021-11-14 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_alter_contact_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(blank=True, default=None, max_length=250, null=True),
        ),
    ]
