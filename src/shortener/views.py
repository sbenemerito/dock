from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.db.models import Sum

from .models import ShortenedURL
from analytics.models import LinkClick
from .forms import URLForm
from .utils import create_shortcode


def index(request):
	template = 'shortener/home.html'
	context = {'links': ShortenedURL.objects.all().count(), 'form': URLForm()}
	context.update(LinkClick.objects.aggregate(Sum('count')))

	if request.method == 'POST':
		form = URLForm(data=request.POST)
		if form.is_valid():
			new_url = form.save(commit=False)
			obj, created = ShortenedURL.objects.get_or_create(url=new_url.url)

			template = 'shortener/result.html'
			context.update({'form': form, 'object': obj})
	
	return render(request, template, context)


def redirect_to_link(request, shortcode):
	obj = get_object_or_404(ShortenedURL, shortcode=shortcode)
	LinkClick.objects.create_linkclick(obj)
	return HttpResponseRedirect(obj.url)

	