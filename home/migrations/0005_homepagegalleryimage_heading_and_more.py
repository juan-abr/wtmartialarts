# Generated by Django 4.1.4 on 2023-01-29 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_homepage_intro_alter_homepage_body_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepagegalleryimage',
            name='heading',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='homepagegalleryimage',
            name='button_url',
            field=models.URLField(blank=True),
        ),
    ]
