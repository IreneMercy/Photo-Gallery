from django.db import models



class Location(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

class Images(models.Model):
    image_path = models.ImageField()
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.description

    def save_images(self):
        self.save()
