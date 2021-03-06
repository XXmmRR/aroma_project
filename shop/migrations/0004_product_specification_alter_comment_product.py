# Generated by Django 4.0.2 on 2022-02-27 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Specification',
            field=models.TextField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='shop.product'),
        ),
    ]
