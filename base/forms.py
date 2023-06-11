from django.forms import ModelForm
from .models import Audio


class AudioEntryForm(ModelForm):
    class Meta:
        model = Audio
        fields = ['audio_file', 'title']


