from django.db import models


class Location(models.Model):
    location = models.CharField(max_length=20)
    time_posted = models.DateTimeField(auto_now_add=True)


class Category(models.Model):
    CATEGORY_CHOICES = (
        ('travel', 'Travel'),
        ('food', 'Food'),
        ('sports', 'Sports'),
        ('landscape', 'Landscape')
    )
    category = models.CharField(max_length=9, choices=CATEGORY_CHOICES, default='food')


class Image(models.Model):
    image = models.ImageField(upload_to='images/', null=True)
    image_name = models.CharField(max_length=30)
    description = models.TextField()
    image_location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    image_category = models.ForeignKey(Category, on_delete=models.CASCADE)

