# Generated by Django 2.2.21 on 2021-05-31 00:02

import adm_request.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adm_request', '0002_auto_20210530_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='file',
            field=models.FileField(max_length=300, unique=True, upload_to=adm_request.models.Document.get_file_path),
        ),
    ]
