from django.db import models


class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, null=True)
    price = models.IntegerField()
    image = models.ImageField()
    release_date = models.DateField(blank=True, null=True)
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=150)
