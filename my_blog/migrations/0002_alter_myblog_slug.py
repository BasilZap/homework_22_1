# Generated by Django 4.2.4 on 2023-08-22 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myblog',
            name='slug',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Slug'),
        ),
    ]