# Generated by Django 3.0.3 on 2021-01-11 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_auto_20210104_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='totalComments',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]