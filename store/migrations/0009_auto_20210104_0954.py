# Generated by Django 3.0.3 on 2021-01-04 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20210104_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='reply',
            field=models.TextField(),
        ),
    ]
