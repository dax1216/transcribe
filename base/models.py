from django.db import models
from django.conf import settings
# Create your models here.


class Audio(models.Model):
    class TranscribeStatus(models.TextChoices):
        START = 'START', 'Starting'
        IN_PROGRESS = 'IN_PROGRESS', 'Transcribing In Progress'
        COMPLETED = 'COMPLETED', 'Completed'
        FAILED = 'FAILED', 'Failed'

    title = models.CharField(max_length=255)
    audio_file = models.FileField(null=True)
    complete_transcript = models.TextField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=TranscribeStatus.choices, default=TranscribeStatus.START)

    def __str__(self):
        return self.title

    def get_full_url(self):
        return f'{settings.MEDIA_URL}{self.audio_file}'


class AudioSegments(models.Model):
    audio = models.ForeignKey(Audio, null=False, on_delete=models.CASCADE)
    segment = models.TextField(null=False, blank=False)
    text = models.TextField(null=True)
