# Generated by Django 4.2.6 on 2023-11-01 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explorer', '0003_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='file',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]