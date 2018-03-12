from django.db import models
from django.contrib.auth.models import User

QUARTER  = (
    ('quarter1', 'quarter1'), ('quarter2', 'quarter2'),
    ('quarter3', 'quarter3'), ('quarter4', 'quarter4')
)

class Profile(models.Model):

    user = models.ForeignKey(User, null=True, blank=True)
    mobile = models.CharField(max_length=15, null=True, blank=True)


class Contact(models.Model):

    name = models.TextField(null=True, blank=True)
    email = models.TextField(null=True, blank=True)
    website = models.TextField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)

class FishDetail(models.Model):

    name = models.TextField(null=True, blank=True)
    # image = models.ImageField(null=True, blank=True)
    image = models.FileField(upload_to="fish", null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name


class FishGraphValue(models.Model):

    fish = models.ForeignKey(FishDetail, null=True, blank=True)
    quarter = models.CharField(max_length=25, null=True, blank=True)
    value = models.FloatField(default=0)
    year = models.IntegerField(default=0)

    def __str__(self):
        return self.fish.name


        # >>> fish.fishgraphvalue_set.all().order_by('id').values_list('quarter', 'year')
