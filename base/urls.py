from django.urls import path
from .views import upload_file, audio_transcript, transcriptions


urlpatterns = [
    path('', upload_file, name="upload_file"),
    path('transcriptions/<str:aid>', audio_transcript, name="view_transcription"),
    path('transcriptions', transcriptions, name="transcriptions"),
]

