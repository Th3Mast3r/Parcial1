# Generated by Django 4.1.1 on 2022-09-21 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_blogs_date_reviews_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='author',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
