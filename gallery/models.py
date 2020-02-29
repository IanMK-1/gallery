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

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls, id, image):
        cls.objects.filter(id=id).update(image=image)

    @classmethod
    def get_image_by_id(cls, id):
        specific_image = cls.objects.filter(id=id)
        return specific_image

    @classmethod
    def search_image_by_category(cls, image_category):
        search_result = cls.objects.filter(image_category__category=image_category)
        return search_result

    @classmethod
    def filter_by_location(cls, location):
        search_image_by_location = cls.objects.filter(image_location__location=location)
        return search_image_by_location
