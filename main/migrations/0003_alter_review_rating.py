# Generated by Django 3.2.9 on 2021-11-10 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_review_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
    ]