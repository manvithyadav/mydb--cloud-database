# Generated by Django 4.2.6 on 2023-11-01 09:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('explorer', '0002_alter_folder_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('upload_time', models.DateTimeField(auto_now_add=True)),
                ('file_type', models.CharField(choices=[('text', 'text'), ('html', 'html'), ('css', 'css'), ('js', 'js'), ('ppt', 'ppt'), ('pdf', 'pdf')], max_length=255)),
                ('folder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='explorer.folder')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
