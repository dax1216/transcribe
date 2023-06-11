from time import sleep
from celery import shared_task
from .models import Audio, AudioSegments
from django.conf import settings
import whisper
import json


@shared_task()
def test_req(audio_id):
    audio = Audio.objects.get(pk=audio_id)

    print(audio.__dict__)


@shared_task()
def transcribe(audio_id):
    audio = Audio.objects.get(pk=audio_id)

    try:
        model = whisper.load_model("base.en")

        audio.status = Audio.TranscribeStatus.IN_PROGRESS
        audio.save()

        if settings.USE_S3:
            audio_path = f'{settings.MEDIA_URL}{audio.audio_file}'
        else:
            audio_path = f'{settings.MEDIA_ROOT}/{audio.audio_file}'

        result = model.transcribe(audio_path, fp16=False)

        for item in result["segments"]:
            segment = json.dumps(item, default=str)
            audio_segment = AudioSegments(audio=audio, segment=segment)
            audio_segment.text = item['text']
            audio_segment.save()

        audio.complete_transcript = result["text"]
        audio.status = Audio.TranscribeStatus.COMPLETED
        audio.save()

    except Exception as e:
        audio.status = Audio.TranscribeStatus.FAILED
        audio.save()

