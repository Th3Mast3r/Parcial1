# Generated by Django 4.1.1 on 2022-09-15 16:06

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blogs",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("author", models.CharField(blank=True, max_length=200, null=True)),
                ("name", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "description",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                ("body", ckeditor.fields.RichTextField(blank=True, null=True)),
                ("slug", models.SlugField(blank=True, null=True)),
                ("image", models.ImageField(blank=True, null=True, upload_to="blog")),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "Blog",
                "verbose_name_plural": "Blogs",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("name", models.CharField(max_length=100, verbose_name="Name")),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                ("message", models.TextField(verbose_name="Message")),
            ],
            options={
                "verbose_name": "Contact",
                "verbose_name_plural": "Contacts",
                "ordering": ["timestamp"],
            },
        ),
        migrations.CreateModel(
            name="Reviews",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "description",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                ("body", ckeditor.fields.RichTextField(blank=True, null=True)),
                ("image", models.ImageField(blank=True, null=True, upload_to="review")),
                ("slug", models.SlugField(blank=True, null=True)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "Review",
                "verbose_name_plural": "Reviews",
                "ordering": ["name"],
            },
        ),
    ]
