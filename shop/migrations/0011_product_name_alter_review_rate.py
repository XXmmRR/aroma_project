# Generated by Django 4.0.2 on 2022-02-27 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_rename_reviews_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='rate',
            field=models.PositiveSmallIntegerField(choices=[(1, '1 - Trash'), (2, '2 - Almost trash'), (3, '3 - Usable'), (4, '4 - Good'), (5, '5 - Excellent')], null=True),
        ),
    ]
