# Generated by Django 3.0.6 on 2020-05-05 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_auto_20200505_1434'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='author',
            name='date_of_death',
        ),
    ]