# Generated by Django 3.2.18 on 2023-03-01 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0017_post_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
