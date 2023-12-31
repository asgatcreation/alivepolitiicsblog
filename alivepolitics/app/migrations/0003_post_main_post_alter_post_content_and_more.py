# Generated by Django 4.2.6 on 2023-10-10 07:14

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0002_tag"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="main_post",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="post",
            name="content",
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name="post",
            name="featured_image",
            field=models.ImageField(upload_to="images"),
        ),
        migrations.AlterField(
            model_name="post",
            name="section",
            field=models.CharField(
                choices=[
                    ("Popular", "Popular"),
                    ("Recent", "Recent"),
                    ("political_Pick", "Political_Pick"),
                    ("Trending", "Trending"),
                    ("Inspiration", "Inspiration"),
                    ("Latest_Posts", "Latest_Posts"),
                ],
                max_length=100,
            ),
        ),
    ]
