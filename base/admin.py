from django.contrib import admin
from .models import Audio, AudioSegments


class AudioSegmentsInline(admin.StackedInline):
    model = AudioSegments
    extra = 1


class AudioAdmin(admin.ModelAdmin):
    inlines = [AudioSegmentsInline]


# Register your models here.
admin.site.register(Audio, AudioAdmin)
