# Generated by Django 3.0.3 on 2021-01-11 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_comment_totalcomments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='totalComments',
        ),
        migrations.AddField(
            model_name='blog',
            name='totalComments',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]