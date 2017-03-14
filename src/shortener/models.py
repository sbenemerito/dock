from django.db import models
from .utils import create_shortcode
from django.core.urlresolvers import reverse


class ShortenedURL(models.Model):
	url = models.URLField()
	shortcode = models.CharField(max_length=15, blank=True)
	created = models.DateTimeField(auto_now=True)
	updated = models.DateTimeField(auto_now_add=True)

	def save(self, *args, **kwargs):
		if self.shortcode is None or self.shortcode == "":
			self.shortcode = create_shortcode(self)
		super(ShortenedURL, self).save(*args, **kwargs)


	def __str__(self):
		return str(self.url)

	def get_short_url(self):
		return reverse('scode', kwargs={'shortcode': self.shortcode})		