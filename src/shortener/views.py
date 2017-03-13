from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from .models import ShortenedURL

# Create your views here.
def index(request):
	return render(request, "shortener/home.html", {})


def redirect_to_link(request, shortcode):
	qs = get_object_or_404(ShortenedURL, shortcode=shortcode)
	return HttpResponseRedirect(qs.url)

	