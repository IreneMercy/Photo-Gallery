from django.db import models

class Images(models.Model):
    image_path = models.ImageField()
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)

class Location(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
