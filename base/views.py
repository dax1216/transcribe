from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from .models import Audio, AudioSegments
from .forms import AudioEntryForm
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import json
from .tasks import transcribe


def upload_file(request):
    if request.method == 'POST':
        image_file = request.FILES['audio_file']

        if settings.USE_S3:
            audio_form = AudioEntryForm(request.POST, request.FILES)

            if audio_form.is_valid():
                audio = audio_form.save()
            else:
                return render(request, 'base/upload.html', { 'form': audio_form })
        else:
            fs = FileSystemStorage()
            filename = fs.save(image_file.name, image_file)
            image_url = fs.url(filename)
            audio = Audio(audio_file=filename, title=request.POST['title'])
            audio.save()

        transcribe.delay(audio.id)

        return redirect('transcriptions')

    context = {
        'form': AudioEntryForm()
    }
    return render(request, 'base/upload.html', context)


def audio_transcript(request, aid=None):
    audio = Audio.objects.get(pk=aid)
    audio_segments = audio.audiosegments_set.all()

    context = {
        'audio': audio,
        'audio_segments': audio_segments
    }

    return render(request, 'base/transcription.html', context)


def transcriptions(request):
    audios = Audio.objects.all().order_by('-created')
    context = {
        'audios': audios
    }

    return render(request, 'base/transcriptions.html', context)

