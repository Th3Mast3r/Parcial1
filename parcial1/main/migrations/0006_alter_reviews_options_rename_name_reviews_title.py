# Generated by Django 4.1.1 on 2022-09-21 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_reviews_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reviews',
            options={'ordering': ['title'], 'verbose_name': 'Review', 'verbose_name_plural': 'Reviews'},
        ),
        migrations.RenameField(
            model_name='reviews',
            old_name='name',
            new_name='title',
        ),
    ]
