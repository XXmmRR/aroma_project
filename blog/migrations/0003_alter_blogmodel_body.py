# Generated by Django 4.0.1 on 2022-02-01 17:51

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
