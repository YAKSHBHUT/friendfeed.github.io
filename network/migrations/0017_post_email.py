# Generated by Django 3.0.2 on 2023-02-10 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0016_auto_20201008_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='email',
            field=models.TextField(blank=True, max_length=140),
        ),
    ]
