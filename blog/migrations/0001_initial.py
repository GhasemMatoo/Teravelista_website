# Generated by Django 3.2.8 on 2021-10-14 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=250)),
                ('content', models.TextField()),
                ('counted_views', models.IntegerField(default=0)),
                ('status', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(null=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('published_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
