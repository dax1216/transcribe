# Generated by Django 4.2 on 2023-06-10 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audio',
            name='audio_link',
        ),
        migrations.AddField(
            model_name='audio',
            name='audio_file',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
