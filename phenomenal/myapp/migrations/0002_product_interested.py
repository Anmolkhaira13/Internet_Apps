# Generated by Django 4.0.dev20210216092534 on 2021-11-15 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='interested',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
