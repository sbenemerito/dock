from django import forms
from .models import ShortenedURL


class URLForm(forms.ModelForm):
    class Meta:
        model = ShortenedURL
        fields = ['url']
        labels = {'url': 'Your URL here'}

