from django.db import models


class Image(models.Model):
    image = models.ImageField(upload_to='images/', null=True)
    image_name = models.CharField(max_length=30)
    description = models.TextField()
    image_location = models.ForeignKey(Location)
    image_category = models.ForeignKey(Category)


class Location(models.Model):
    location = models.CharField()
    time_posted = models.DateTimeField(auto_now_add=True)


class Category(models.Model):
    CATEGORY_CHOICES = (
        ('travel', 'Travel'),
        ('food', 'Food'),
        ('sports', 'Sports'),
        ('landscape', 'Landscape')
    )
    category = models.CharField(max_length=9, choices=CATEGORY_CHOICES, default='food')
