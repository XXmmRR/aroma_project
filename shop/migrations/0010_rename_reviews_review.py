# Generated by Django 4.0.2 on 2022-02-27 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_remove_reviews_star_reviews_rate'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reviews',
            new_name='Review',
        ),
    ]
