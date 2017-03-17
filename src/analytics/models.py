from django.db import models
from shortener.models import ShortenedURL


class LinkClickManager(models.Manager):
	def create_linkclick(self, instance):
		if isinstance(instance, ShortenedURL):
			obj, created = self.get_or_create(short_url=instance)
			obj.count += 1
			obj.save()


class LinkClick(models.Model):
	short_url = models.OneToOneField(ShortenedURL)
	count = models.IntegerField(default = 0)
	created = models.DateTimeField(auto_now=True)
	updated = models.DateTimeField(auto_now_add=True)

	objects = LinkClickManager()

	def __str__(self):
		return str(self.count)
