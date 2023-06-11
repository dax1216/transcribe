# Generated by Django 4.2 on 2023-06-09 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('audio_link', models.CharField(max_length=255)),
                ('complete_transcript', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('START', 'Starting'), ('IN_PROGRESS', 'Transcribing In Progress'), ('COMPLETED', 'Completed'), ('FAILED', 'Failed')], default='START', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='AudioSegments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('segment', models.TextField()),
                ('audio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.audio')),
            ],
        ),
    ]