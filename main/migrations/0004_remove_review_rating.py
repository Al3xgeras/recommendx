# Generated by Django 3.2.9 on 2021-11-10 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_review_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='rating',
        ),
    ]
