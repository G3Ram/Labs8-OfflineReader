# Generated by Django 2.1.4 on 2018-12-07 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='html',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='images',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]