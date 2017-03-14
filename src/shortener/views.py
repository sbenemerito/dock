from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from .models import ShortenedURL
from .forms import URLForm
from .utils import create_shortcode


def index(request):
	template = 'shortener/home.html'
	context = {}

	if request.method == 'POST':
		form = URLForm(data=request.POST)
		if form.is_valid():
			new_url = form.save(commit=False)
			obj, created = ShortenedURL.objects.get_or_create(url=new_url.url)

			if created:
				print("Created!")
			else:
				print("Exists!")

			template = 'shortener/home2.html'
			context = {'form': form, 'url': new_url.url, 'link': obj.get_short_url }
	else:
		form = URLForm()
		context = {'form': form}
	
	return render(request, template, context)


def redirect_to_link(request, shortcode):
	qs = get_object_or_404(ShortenedURL, shortcode=shortcode)
	return HttpResponseRedirect(qs.url)

	