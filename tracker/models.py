from django.db import models

class Page(models.Model):
	name = models.CharField(max_length=256)
	session = models.CharField(max_length=256)
	first_visit = models.DateTimeField(auto_now=True)
	visits = models.PositiveIntegerField()


class Session(models.Model):
	ip = models.GenericIPAddressField()
	continent = models.CharField(max_length=20)
	country = models.CharField(max_length=256)
	city = models.CharField(max_length=256)
	os = models.CharField(max_length=256)
	browser = models.CharField(max_length=256)
	session = models.CharField(max_length=256)
	timestamp = models.DateTimeField(auto_now=True)
