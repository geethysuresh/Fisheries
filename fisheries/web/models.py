from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

	user = models.ForeignKey(User, null=True, blank=True)
	mobile = models.CharField(max_length=15, null=True, blank=True)


class Contact(models.Model):

	name = models.TextField(null=True, blank=True)
	email = models.TextField(null=True, blank=True)
	website = models.TextField(null=True, blank=True)
	message = models.TextField(null=True, blank=True)